

def workout_plan(exercise, reps, day):
    print(f"On {day}, do {reps} {exercise}. Get fit!")

exercise = input("What exercise will you be doing? ").strip().lower()
reps = int(input("How many reps will you do? "))
day = input("What day are you doing it? ").strip().title()

workout_plan(exercise, reps, day)