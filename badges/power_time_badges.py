import datetime

import util
import logging

from badges import Badge, BadgeContextType, BadgeCategory
from exercise_badges import ExerciseBadge

# All badges awarded for watching a specific amount of playlist time *and* 
# completing a certain number of exercise problems within a set amount of time 
# inherit from PowerTimeBadge
class PowerTimeBadge(Badge):

    def is_satisfied_by(self, *args, **kwargs):
        action_cache = kwargs.get("action_cache", None)

        if action_cache is None:
            return False

        c_problem_logs = len(action_cache.problem_logs)
        c_video_logs = len(action_cache.video_logs)

        if c_video_logs < 1 or c_problem_logs < 1:
            return False

        date_video_end = action_cache.get_video_log(c_video_logs - 1).time_watched
        date_problem_end = action_cache.get_problem_log(c_problem_logs - 1).time_done

        date_end = max(date_video_end, date_problem_end)
        date_start = date_end - datetime.timedelta(seconds = self.seconds_allotted)

        seconds_watched = 0
        for i in range(c_video_logs):
            video_log = action_cache.get_video_log(c_video_logs - i - 1)
            if video_log.time_watched < date_start:
                break
            seconds_watched += video_log.seconds_watched

        if seconds_watched < self.video_seconds_required:
            return False

        problems_correct = 0
        for i in range(c_problem_logs):
            problem_log = action_cache.get_problem_log(c_problem_logs - i - 1)
            if problem_log.time_done < date_start:
                break
            if problem_log.correct:
                problems_correct += 1

        if problems_correct < self.problems_required:
            return False

        return True

    def extended_description(self):
        return "Correctly answer %s problems and watch %s of video in %s" % (self.problems_required, util.seconds_to_time_string(self.video_seconds_required), self.s_time_limit_description)

class PowerFiveMinutesBadge(PowerTimeBadge):

    def __init__(self):
        self.problems_required = 15
        self.video_seconds_required = 60
        self.seconds_allotted = 60 * 5
        self.s_time_limit_description = "five minutes"
        self.description = "Inspired Five Minutes"
        self.badge_category = BadgeCategory.BRONZE
        self.points = 0
        PowerTimeBadge.__init__(self)

class PowerHourBadge(PowerTimeBadge):

    def __init__(self):
        self.problems_required = 90
        self.video_seconds_required = 15 * 60
        self.seconds_allotted = 3600
        self.s_time_limit_description = "one hour"
        self.description = "Power Hour"
        self.badge_category = BadgeCategory.SILVER
        self.points = 0
        PowerTimeBadge.__init__(self)

class DoublePowerHourBadge(PowerTimeBadge):

    def __init__(self):
        self.problems_required = 90 * 2
        self.video_seconds_required = 30 * 60
        self.seconds_allotted = 3600 * 2
        self.s_time_limit_description = "two hours"
        self.description = "Double Power Hour"
        self.badge_category = BadgeCategory.GOLD
        self.points = 0
        PowerTimeBadge.__init__(self)

