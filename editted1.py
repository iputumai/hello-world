import math

# User profile and goal information

# Calorie needs depend on user goals
def main():
    file = open("userinformation.txt", "w") # create the text file and "w" to write the data on the file
    user_name = input("What is your name?")
    file.write(user_name) #this is how to save the data that have been inputed by the user
    #This is the solution if the user enter the word
    while True:
        try:
            height = float(input("Enter your height(cm) : "))
            user_weight = float(input("Enter your weight(kilograms) : "))
            user_age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a number!") 
    if height <= 0 and user_weight <= 0 and user_age <= 0:
        print("Please enter a number greater than zero!")
    if height > 100 :
        ideal_weight = (height - 100) - (0.1 * (height - 100))
        print("Your ideal_weight is: " , ideal_weight, "kg")
    else:
        print("Please enter the height greater than 100")
    male_calorie = ((66.5 + (13.8 * user_weight)) + (5 * height) / (6.8 * user_age)) * 1.55 #user with normal activity multiply by 1.55
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
        if goals == list_goals[0]: #Maintaining Body
            calorie_needs = print("The amount of calorie that you should to take per day: " + str(round(male_calorie, 2)) + " kg")
            if gender == list_gender[0]:
                print(calorie_needs)
            elif gender == list_gender[1]:
                calorie_needs = print("The amount of calorie that you should to take per day: " + str(female_calorie) + " kg")
                print(calorie_needs)
        if goals == list_goals[1]: #Increasing Weight
            first_weight = user_weight
            weight_increase = float(input("What is your weight goals? "))
            remaining_weight = print("\nThe total weight that you have to increase is " + str(weight_increase - first_weight) + " kg")
            if weight_increase >= first_weight:
                print(remaining_weight)
                if gender == list_gender[0]:
                    male_calorie_increase = ((66.5 + (13.8 * weight_increase)) + (5 * height) / (6.8 * user_age)) * 1.55
                    print("The total calorie that you need take per day base on your goal is " + str(round(male_calorie_increase, 2)))
                elif gender == list_gender[1]:
                    female_calorie_increase = ((665.1 + (9.6 * weight_increase)) + (1.9 * height) / (4.7 * user_age)) * 1.55
                    print("The total calorie that you need take per day base on your goal is " + str(round(female_calorie_increase, 2)))
        if goals == list_goals[2]: #Reducing Weight
            first_weight = user_weight
            weight_reduce = float(input("How much weight do you want to achieve? "))
            remaining_weight = print("\nThe total weight that you have to losses is " + str(first_weight - weight_losses) + " kg")
            if weight_reduce <= first_weight:
                print(remaining_weight)
                if gender == list_gender[0]:
                    male_calorie_reduce = ((66.5 + (13.8 * weight_reduce)) + (5 * height) / (6.8 * user_age)) * 1.55
                    print("The total calorie that you need take per day base on your goal is " + str(round(male_calorie_reduce, 2)))
                elif gender == list_gender[1]:
                    female_calorie_reduce = ((665.1 + (9.6 * weight_reduce)) + (1.9 * height) / (4.7 * user_age)) * 1.55
                    print("The total calorie that you need take per day base on your goal is " + str(round(female_calorie_reduce, 2)))

    file.close() #important to close the file
            
main()



