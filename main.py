# My AI Study Planner
# A beginner-friendly Python project

print("=" * 40)
print("       MY AI STUDY PLANNER")
print("=" * 40)

# Get the student's name
name = input("Enter your name: ").strip()

while not name:
    name = input("Name cannot be empty. Enter your name: ").strip()

# Get the student's AI learning goal
goal = input("What is your AI learning goal? ").strip()

while not goal:
    goal = input("Goal cannot be empty. Enter your goal: ").strip()

# Get the number of study days per week
while True:
    try:
        study_days = int(input("Study days per week (1-7): "))

        if 1 <= study_days <= 7:
            break

        print("Please enter a number from 1 to 7.")

    except ValueError:
        print("Please enter a valid whole number.")

# Get daily study hours
while True:
    try:
        daily_hours = float(input("Daily study hours (greater than 0): "))

        if 0 < daily_hours <= 24:
            break

        print("Enter hours greater than 0 and no more than 24.")

    except ValueError:
        print("Please enter a valid number, such as 1 or 1.5.")

# Calculate total weekly study hours
weekly_hours = study_days * daily_hours

# Create a personalized study plan
plan = f"""
========================================
        MY AI STUDY PLANNER
========================================

Student Name: {name}
AI Learning Goal: {goal}

STUDY SCHEDULE
--------------
Study Days Per Week: {study_days}
Daily Study Hours: {daily_hours:g}
Total Weekly Study Hours: {weekly_hours:g}

PERSONALIZED STUDY PLAN
-----------------------
1. Learn AI concepts and basic terminology.
2. Study Python fundamentals and practice coding.
3. Explore AI topics related to your learning goal.
4. Complete small exercises and practical projects.
5. Review your notes and track your progress.

WEEKLY ROUTINE
--------------
Study for {daily_hours:g} hour(s) on each of your
{study_days} study day(s) every week.

Remember to take breaks, practice regularly,
and review what you learn.

Good luck, {name}! Keep learning and improving!

========================================
"""

# Display the plan
print(plan)

# Save the plan to a text file
try:
    with open("study_plan.txt", "w", encoding="utf-8") as file:
        file.write(plan)

    print("Your study plan was saved to study_plan.txt")

except OSError:
    print("Error: Could not save the study plan.")
