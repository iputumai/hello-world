import math

"""This program will calculate basal calorie needs and some type of exercise depend on user goals."""


def main():
    user_name = input("What is your name?")
    while True:
        try:
            height = float(input("Enter your height(cm) : "))
            user_weight = float(input("Enter your weight(kilograms) : "))
            user_age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a number!")
    if height > 100:
        ideal_weight = (height - 100) - (0.1 * (height - 100))
        print("Your ideal_weight is: ", ideal_weight, "kg")
    else:
        print("Please enter the height greater than 100")

    # Harrish Benedict Basal Metabolic Rate
    # Litle exercise BMR multiplied by 1.2
    # Light exercise (1-3 days per week) BMR multiplied by 1.375
    # Moderate exercise (3-5 days per week) BMR multiplied by 1.55
    # Active exercise (6-7 days per week) BMR multiplied by 1.725
    # Very active exercise (twice per day) BMR multiplied by 1.9

    male_calorie = ((66.5 + (13.8 * user_weight)) + (5 * height) / (6.8 * user_age)) * 1.55
    female_calorie = ((665.1 + (9.6 * user_weight)) + (1.9 * height) / (4.7 * user_age)) * 1.55

    list_gender = ["male", "female"]
    for i in list_gender:
        print(i)
    gender = str(input("Enter your gender : "))
    list_goals = ["Maintaining Body", "Increasing Weight", "Reducing Weight", "Build Muscle"]
    for goal in list_goals:
        print(goal)
    goals = input("What goals do you want to achieve? ")
    if gender == list_gender[0] or list_gender[1]:
        if goals == list_goals[0]:  # Maintaining Body
            if gender == list_gender[0]:
                calorie_needs_male = print(
                    "The total of basal calorie that you should to take per day: " + str(round(male_calorie, 2)))
                print(calorie_needs_male)
            elif gender == list_gender[1]:
                calorie_needs_female = print(
                    "The total of basal  calorie that you should to take per day: " + str(round(female_calorie,2)))
                print(calorie_needs_female)

            user_information = "\nName: {} \nWeight: {} kg \nHeight: {} cm \nAge: {} \nGender: {} \nGoals: {} \n---".format(
                user_name, user_weight, height, user_age, gender, goals)
            file = open("user_information.txt", "a")
            file.write(user_information)
            file.close()

        elif goals == list_goals[1]:  # Increasing Weight
            first_weight = user_weight
            while True:
                try:
                    weight_increase = float(input("What is the total weight that you want to achieve? "))
                    remaining_weight = print("\nThe total weight that you have to increase is " + str(
                        weight_increase - first_weight) + " kg")
                    break
                except ValueError:
                    print("Please enter a number!")
            if weight_increase >= first_weight:
                print(remaining_weight)
                if gender == list_gender[0]:
                    male_calorie_increase = ((66.5 + (13.8 * weight_increase)) + (5 * height) / (6.8 * user_age)) * 1.55
                    print("The total of basal calorie that you need take per day base on your goal is " + str(
                        round(male_calorie_increase, 2)))
                elif gender == list_gender[1]:
                    female_calorie_increase = ((665.1 + (9.6 * weight_increase)) + (1.9 * height) / (
                                4.7 * user_age)) * 1.55
                    print("The total of basal calorie that you need take per day base on your goal is " + str(
                        round(female_calorie_increase, 2)))

            user_information = "\nName: {} \nWeight: {} kg \nHeight: {} cm \nAge: {} \nGender: {} \nGoals: {} \nWeight goals: {} \n---".format(user_name, user_weight, height, user_age, gender, goals, weight_increase)
            file = open("user_information.txt", "a")
            file.write(user_information)
            file.close()

        elif goals == list_goals[2]:  # Reducing Weight
            first_weight = user_weight
            while True:
                try:
                    weight_reduce = float(input("What is the total weight that you want to achieve? "))
                    remaining_weight = print("\nThe total weight that you have to increase is " + str(
                        first_weight-weight_reduce) + " kg")
                    break
                except ValueError:
                    print("Please enter a number!")
            if weight_reduce <= first_weight:
                print(remaining_weight)
                if gender == list_gender[0]:
                    male_calorie_reduce = ((66.5 + (13.8 * weight_reduce)) + (5 * height) / (6.8 * user_age)) * 1.55
                    print("The total of basal calorie that you need take per day base on your goal is " + str(
                        round(male_calorie_reduce, 2)))
                elif gender == list_gender[1]:
                    female_calorie_reduce = ((665.1 + (9.6 * weight_reduce)) + (1.9 * height) / (4.7 * user_age)) * 1.55
                    print("The total of basal calorie that you need take per day base on your goal is " + str(
                        round(female_calorie_reduce, 2)))

            user_information = "\nName: {} \nWeight: {} kg \nHeight: {} cm \nAge: {} \nGender: {} \nGoals: {} \nWeight goals: {} \n---".format(user_name, user_weight, height, user_age, gender, goals, weight_reduce)
            file = open("user_information.txt", "a")
            file.write(user_information)
            file.close()

        elif goals == list_goals[3]:
            if gender == list_gender[0]:
                calorie_needs_male = print(
                    "The total of basal calorie that you should to take per day: " + str(round(male_calorie, 2)))
                print(calorie_needs_male)
            elif gender == list_gender[1]:
                calorie_needs_female = print(
                    "The total of basal  calorie that you should to take per day: " + str(round(female_calorie,2)))
                print(calorie_needs_female)

            workout_place = ["gym", "home"]
            print(workout_place)

            abs_gym_workout = {
                "abs exercise": ["Sit Up", " Flat Brench Lying Leg Raise", " Jackknife Sit Up, Toe Touchers"]
            }

            arm_gym_workout = {
                "arm exercise": ["Dumbell Curls", "Hammer Curls", "Lying Tricpes Press", "Triceps Pushdown",
                                 "Barbell Curl", "Bench Dips"]
            }

            back_gym_workout = {
                "back exercise": ["Barbell Deadlift", "Wide - grip Pullup", "Standing T - bar Row", "Cable Row",
                                  "Close Grip Pull Down"]
            }

            legs_gym_workout = {
                "legs exercise": ["Barbell Full Squat", "Hack Squats", "Leg Extensions", "Barbell Lunges", "Leg Curl",
                                  "Calf Raises"]
            }

            chest_gym_workout = {
                "chest exercise": ["Barbell Bench Press", "Flat Bench Dumbell Press", "Seated Machine Chest Press",
                                   "Dips For Chest", "Incline Bench Cable Fly", "Peck Deck Machine"]
            }

            abs_home_workout = {
                "abs_home_exercise": ["Sit ups", "Roll ups", "Plank", "Leg Raisers", "Tuck and Crunch",
                                   "V-sit(30 seconds)"]
            }
            arm_home_workout = {
                "arm_home_exercise": ["Push-Ups", "Pull-ups", "Handstands", "Crunches"]
            }
            back_home_workout = {
                "back_home_exercise": ["Squats", "Plank", "Cat", "Stretch", "Superman"]
            }
            legs_home_workout = {
                "legs_home_exercise": ["Squat Jumps", "Side Lunge", "Bulgarian Split Squats", "Reverse Lunge",
                                    "Later Lunge"]
            }
            chest_home_workout = {
                "chest_home_exercise": ["Push - Ups", "Triceps Kickbacks", "Planks Rows", "Dips", "Crunches"]
            }

            user_workout_place = input("Where do you want to do your exercise?")
            muscle_part = ["abs", "arm", "back", "leg", "chest"]
            print(muscle_part)
            if user_workout_place == workout_place[0]:
                muscle_section = input("Which muscle do you want to train? ")
                if muscle_section == "abs":
                    print(list(abs_gym_workout.values()))
                elif muscle_section == "arm":
                    print(list(arm_gym_workout.values()))
                elif muscle_section == "back":
                    print(list(back_gym_workout.values()))
                elif muscle_section == "leg":
                    print(list(legs_gym_workout.values()))
                elif muscle_section == "chest":
                    print(list(chest_gym_workout.values()))
            elif user_workout_place == workout_place[1]:
                muscle_section = input("Which muscle do you want to train? ")
                if muscle_section == "abs":
                    print(list(abs_home_workout.values()))
                elif muscle_section == "arm":
                    print(list(arm_home_workout.values()))
                elif muscle_section == "back":
                    print(list(back_home_workout.values()))
                elif muscle_section == "leg":
                    print(list(legs_home_workout.values()))
                elif muscle_section == "chest":
                    print(list(chest_home_workout.values()))

            user_information = "\nName: {} \nWeight: {} kg \nHeight: {} cm \nAge: {} \nGender: {} \nGoals: {} \nWorkout place: {} \nMuscle exercise: {}\n---".format(user_name, user_weight, height, user_age, gender, goals, user_workout_place, muscle_section)
            file = open("user_information.txt", "a")
            file.write(user_information)
            file.close()

main()




