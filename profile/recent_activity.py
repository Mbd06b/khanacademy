import datetime

import util
import models
import templatefilters
from badges import util_badges, models_badges, last_action_cache

# Number of hours until activity is no longer considered "recent" for profiles
HOURS_RECENT_ACTIVITY = 72
# Number of most-recent items shown in recent activity
MOST_RECENT_ITEMS = 12

class RecentActivity:

    def timestamp(self):
        return templatefilters.timesince_ago(self.dt)

    def src_icon(self):
        return self.src_icon_activity

    def description(self):
        return "Activity: " + self.__class__.__name__

    def can_combine_dates(self, dt_a, dt_b):
        return (max(dt_b, dt_a) - min(dt_b, dt_a)) < datetime.timedelta(minutes = 30)

    def combine_with(self, recent_activity):
        return False

class RecentBadgeActivity(RecentActivity):
    def __init__(self, user_badge, badge):
        self.s_type = "Badge"
        self.user_badge = user_badge
        self.badge = badge
        self.src_icon_activity = "/images/generic-badge-icon-inset.png"
        self.dt = user_badge.date

class RecentExerciseActivity(RecentActivity):
    def __init__(self, problem_log):
        self.s_type = "Exercise"
        self.problem_log = problem_log
        self.src_icon_activity = "/images/generic-exercise-icon-inset.png"
        self.dt = problem_log.time_done
        self.c_problems = 1
        self.earned_proficiency = problem_log.earned_proficiency
        self.exercise_display_name = models.Exercise.to_display_name(problem_log.exercise)

    def combine_with(self, recent_activity):
        if self.__class__ == recent_activity.__class__:
            if self.problem_log.exercise == recent_activity.problem_log.exercise:
                if self.can_combine_dates(self.dt, recent_activity.dt):
                    self.dt = recent_activity.dt
                    self.c_problems += 1
                    self.earned_proficiency = self.earned_proficiency or recent_activity.earned_proficiency
                    return True
        return False

class RecentVideoActivity(RecentActivity):
    def __init__(self, video_log):
        self.s_type = "Video"
        self.video_log = video_log
        self.src_icon_activity = "/images/video-camera-icon-inset.png"
        self.dt = video_log.time_watched
        self.seconds_watched = video_log.seconds_watched

    def time_watched(self):
        return util.seconds_to_time_string(self.seconds_watched, False)

    def combine_with(self, recent_activity):
        if self.__class__ == recent_activity.__class__:
            if self.video_log.video_title == recent_activity.video_log.video_title:
                if self.can_combine_dates(self.dt, recent_activity.dt):
                    self.dt = recent_activity.dt
                    self.seconds_watched += recent_activity.seconds_watched
                    return True
        return False

def recent_badge_activity(user, dt_start, dt_end):

    badges_dict = util_badges.all_badges_dict()

    list_badge_activity = []
    user_badges = models_badges.UserBadge.get_for_user_between_dts(user, dt_start, dt_end)

    for user_badge in user_badges:
        badge = badges_dict.get(user_badge.badge_name)
        if badge:
            list_badge_activity.append(RecentBadgeActivity(user_badge, badge))

    return list_badge_activity

def recent_exercise_activity(action_cache, dt_start):

    list_exercise_activity = []

    c_logs = len(action_cache.problem_logs)
    for i in range(c_logs):
        problem_log = action_cache.get_problem_log(c_logs - i - 1)
        if problem_log.time_done > dt_start:
            list_exercise_activity.append(RecentExerciseActivity(problem_log))
        else:
            break

    list_exercise_activity.reverse()
    return list_exercise_activity

def recent_video_activity(action_cache, dt_start):

    list_video_activity = []

    c_logs = len(action_cache.video_logs)
    for i in range(c_logs):
        video_log = action_cache.get_video_log(c_logs - i - 1)
        if video_log.time_watched > dt_start:
            list_video_activity.append(RecentVideoActivity(video_log))
        else:
            break

    list_video_activity.reverse()
    return list_video_activity

def recent_activity_for(user, dt_start, dt_end):

    action_cache = last_action_cache.LastActionCache.get_for_user(user)

    list_recent_activity_types = [
            recent_badge_activity(user, dt_start, dt_end), 
            recent_exercise_activity(action_cache, dt_start), 
            recent_video_activity(action_cache, dt_start),
    ]
    list_recent_activity = [activity for sublist in list_recent_activity_types for activity in sublist]

    return collapse_recent_activity(list_recent_activity)[:MOST_RECENT_ITEMS]

def collapse_recent_activity(list_recent_activity):

    last_recent_activity = None

    for ix in range(len(list_recent_activity)):
        recent_activity = list_recent_activity[ix]
        if last_recent_activity and last_recent_activity.combine_with(recent_activity):
            list_recent_activity[ix] = None
        else:
            last_recent_activity = recent_activity

    return sorted(filter(lambda activity: activity is not None, list_recent_activity), reverse=True, key=lambda activity: activity.dt)

def recent_activity_context(user):
    list_recent_activity = []
    if user:
        dt_end = datetime.datetime.now()
        dt_start = dt_end - datetime.timedelta(hours = HOURS_RECENT_ACTIVITY)
        list_recent_activity = recent_activity_for(user, dt_start, dt_end)
    return { "student": user, "list_recent_activity": list_recent_activity }
