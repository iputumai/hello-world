import math

# User profile and goal information

# Calorie needs depend on user goals
def main():
    height = float(input("Enter your height: "))
    user_weight = float(input("Enter your weight(kilograms) : "))
    user_age = int(input("How old are you? "))
    ideal_weight = (height - 100) * (0.1 * (height - 100))
    male_calorie = ((66.5 + 13.8 * user_weight) + (5 * height) / (6.8 * user_age))
    female_calorie = ((665.1 + 9.6 * user_weight) + (1.9 * height) / (4.7 * user_age))
    list_gender = ["male", "female"]
    for i in list_gender:
        print(i)
    gender = str(input("Enter your gender : "))
    list_goals = ["Maintaining Body", "Increasing Weight", "Lossing Weight", "Build Muscle"]
    for goal in list_goals:
        print(goal)
    goals = input("What goals do you want to achieve? ")
    if gender == list_gender[0]:
        if goals == list_goals[0]:
            calorie_needs = print("The amount of calorie that you should to take per day: " + str(male_calorie))
            return calorie_needs
        if goals == list_goals[1]:
            first_weight = user_weight
            weight_increase = float(input("How much weight do you want to achieve ? "))
            remaining_weight = print("\nThe total weight that you have to increase is " + str(weight_increase - first_weight))
            if weight_increase > first_weight:
                print(remaining_weight)
            if weight_increase < first_weight:
                try:
                    weight_increase = float(input("\nPlease use the number of your body weight greater than you have currently, \nEnter the number again:"))
                    remaining_weight = print("\nThe total weight that you have to increase is " + str(weight_increase - first_weight))
                    print(remaining_weight)
                except ZeroDivisionError:
                    print("Nothing can be calculated")
                except ValueError:
                    print("Enter the number please!")
        if goals == list_goals[2]:
            first_weight = user_weight
            weight_losses = float(input("How much weight do you want to achieve? "))
            remaining_weight = print("\nThe total weight that you have to losses is " + str(first_weight - weight_losses))
            if weight_losses < first_weight:
                print(remaining_weight)
            else :
                 try:
                    weight_increase = float(input("\nPlease use the number of your body weight greater than you have currently, \nEnter the number again:"))
                    remaining_weight = print("\nThe total weight that you have to increase is " + str(weight_increase - first_weight))
                    print(remaining_weight)
                 except ZeroDivisionError:
                    print("Nothing can be calculated")
                 except ValueError:
                    print("Enter the number please!")

main()

