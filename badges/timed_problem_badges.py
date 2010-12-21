from badges import Badge, BadgeContextType, BadgeCategory
from exercise_badges import ExerciseBadge
import logging

# All badges awarded for completing a certain number of correct problems
# within a specific amount of time inherit from TimedProblemBadge
class TimedProblemBadge(ExerciseBadge):

    def is_satisfied_by(self, *args, **kwargs):
        user_exercise = kwargs.get("user_exercise", None)
        action_cache = kwargs.get("action_cache", None)

        logging.critical("A")

        if user_exercise is None or action_cache is None:
            return False
        logging.critical("B")

        c_logs = len(action_cache.problem_logs)
        if c_logs >= self.problems_required:

            time_taken = 0
            time_allotted = self.problems_required * user_exercise.seconds_per_fast_problem
            logging.critical("C:" + str(time_allotted))

            for i in range(self.problems_required):

                problem = action_cache.get_problem_log(c_logs - i - 1)
                time_taken += problem.time_taken

                if time_taken > time_allotted or not problem.correct or problem.exercise != user_exercise.exercise:
                    logging.critical("exiting for exercise: " + problem.exercise + ", taken: " + str(time_taken))
                    return False

            return time_taken <= time_allotted

        return False

    def extended_description(self):
        return "Quickly & correctly answer %s exercise problems in a row (time limit depends on exercise difficulty)" % str(self.problems_required)

class NiceTimedProblemBadge(TimedProblemBadge):

    def __init__(self):
        self.problems_required = 4
        self.description = "Picking Up Steam"
        self.badge_category = BadgeCategory.BRONZE
        self.points = 100
        TimedProblemBadge.__init__(self)

class GreatTimedProblemBadge(TimedProblemBadge):

    def __init__(self):
        self.problems_required = 8
        self.description = "Going Transonic"
        self.badge_category = BadgeCategory.BRONZE
        self.points = 500
        TimedProblemBadge.__init__(self)

class AwesomeTimedProblemBadge(TimedProblemBadge):

    def __init__(self):
        self.problems_required = 16
        self.description = "Going Supersonic"
        self.badge_category = BadgeCategory.SILVER
        self.points = 1000
        TimedProblemBadge.__init__(self)

class RidiculousTimedProblemBadge(TimedProblemBadge):

    def __init__(self):
        self.problems_required = 30
        self.description = "Sub-light Speed"
        self.badge_category = BadgeCategory.GOLD
        self.points = 4000
        TimedProblemBadge.__init__(self)

class LudicrousTimedProblemBadge(TimedProblemBadge):

    def __init__(self):
        self.problems_required = 50
        self.description = "299,792,458 Meters per Second"
        self.badge_category = BadgeCategory.PLATINUM
        self.points = 10000
        TimedProblemBadge.__init__(self)
