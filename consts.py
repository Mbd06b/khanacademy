
# Number of problems required to complete a streak in a normal exercise
REQUIRED_STREAK = 10

# Number of problems required to reach a barrier/milestone in a challenge exercise
CHALLENGE_STREAK_BARRIER = 10

# Number of problems that reward a slowly degrading amount of energy points after the required streak has been reached
# before energy points bottom out for the exercise
DEGRADING_EXERCISES_AFTER_STREAK = 15

# Minimum number of energy points available for a correct problem
EXERCISE_POINTS_BASE = 5

# Minimum number of energy points available for a problem in an unfinished exercise
INCOMPLETE_EXERCISE_POINTS_BASE = 15

# Multiplier for energy points in summative assessment problems
SUMMATIVE_EXERCISE_MULTIPLIER = 1.25

# Multiplier for energy points in suggested exercise problems
SUGGESTED_EXERCISE_MULTIPLIER = 3

# Multiplier for energy points in non-proficient exercise problems
INCOMPLETE_EXERCISE_MULTIPLIER = 5

# Base energy points awarded for watching an entire video
VIDEO_POINTS_BASE = 750

# Maximum time we're willing to report that a user worked on a single problem, in seconds
MAX_WORKING_ON_PROBLEM_SECONDS = 1200

# Required # of saved problems before we run statistics on a particular exercise
REQUIRED_PROBLEMS_FOR_EXERCISE_STATISTICS = 50

# Number of most recent problems we examine when calculating exercise statistics
LATEST_PROBLEMS_FOR_EXERCISE_STATISTICS = 5000

# Speediest exercise percentile to use when calculating "fast" problem times
FASTEST_EXERCISE_PERCENTILE = 0.1

# Minimum seconds we'd ever require for a "fast" problem
MIN_SECONDS_PER_FAST_PROBLEM = 2.0

# Maximum seconds we'd ever allow for a "fast" problem
MAX_SECONDS_PER_FAST_PROBLEM = 30.0
