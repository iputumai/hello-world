import tkinter as tk

window = tk.Tk()
window.title("Gym and Food App")
window.configure(bg="red")
window.geometry("800x520")

def fat_to_calories ():
    fatAmount = float(entry1.get())
    calorie_from_fat = fatAmount * 9
     #one gram of fat contain 9 calories
    return calorie_from_fat

def carbohydrate_to_calories():
    carbAmount = float(entry2.get())
    calorie_from_carb = carbAmount * 4
    return calorie_from_carb

def protein_to_calories():
    proteinAmount = float(entry3.get())
    calorie_from_protein = proteinAmount * 9
     #one gram of protein contain 4 calories
    return calorie_from_protein

def main():
    calorie_total = fat_to_calories() + carbohydrate_to_calories() + protein_to_calories()
    total_display = tk.Text(master=window, height=2, width=10)
    total_display.grid(column=1, row=6)
    
    total_display.insert(tk.END, calorie_total)

def maleCalorie():
    height = float(entry4.get())
    weight = float(entry5.get())
    age = float(entry6.get())
    activity_level = float(entry7.get())
    male_calorie = ((66.5 + (13.8 * weight)) + (5 * height) / (6.8 * age)) * activity_level
    return male_calorie

def femaleCalorie():
    height = float(entry4.get())
    weight = float(entry5.get())
    age = float(entry6.get())
    activity_level = float(entry7.get())  
    female_calorie = ((655.1 + (9.6 * weight)) + (1.9 * height) / (4.7 * age)) * activity_level
    return female_calorie


def male_main_calorie():
    male_calorie_total = round(maleCalorie(),2)
    total_calorie = tk.Text(master=window, height=1, width=10)
    total_calorie.grid(column=1, row=15) 
    
    total_calorie.insert(tk.END, male_calorie_total)

def female_main_calorie():
    female_calorie_total = round(femaleCalorie(),2)
    total_calorie = tk.Text(master=window, height=1, width=10)
    total_calorie.grid(column=1, row=18) 
    
    total_calorie.insert(tk.END, female_calorie_total)



#------LABEL-------
# This line of code are responsible for placing the label onto the window using the grid method, and all of this label are putted in the certain row and column to manage the position of each label.
# Grid mathod is a method that is responsible for placing a widgets onto the window
labelTitle1 = tk.Label(text="The Fat, Carbohydrate and Protein Converter", width="35", height="2", bg="yellow", fg="black")
labelTitle1.grid(column=1, row=0)
labelfat = tk.Label(text="Fat amount",width="15", height="1", bg="blue", fg="white")
labelfat.grid(column=0, row=2)
labelcarb = tk.Label(text="Carb amount",width="15", height="1", bg="blue", fg="white")
labelcarb.grid(column=0, row=3)
labelprotein = tk.Label(text="Protein amount",width="15", height="1", bg="blue", fg="white")
labelprotein.grid(column=0, row=4)
labelfat1 = tk.Label(text="gram",width="8", height="1", bg="blue", fg="white")
labelfat1.grid(column=2, row=2)
labelcarb2 = tk.Label(text="gram",width="8", height="1", bg="blue", fg="white")
labelcarb2.grid(column=2, row=3)
labelprotein2 = tk.Label(text="gram",width="8", height="1", bg="blue", fg="white")
labelprotein2.grid(column=2, row=4)


labelspace = tk.Label(text="********************")
labelspace.grid(column=1, row=7)
labelTitle2 = tk.Label(text="Basal Calorie Counter", width="20", height="2", bg="yellow", fg="black")
labelTitle2.grid(column=1, row=8)
labelheight = tk.Label(text="Height",width="15", height="1", bg="blue", fg="white")
labelheight.grid(column=0, row=9)
labelweight = tk.Label(text="Weight",width="15", height="1", bg="blue", fg="white")
labelweight.grid(column=0, row=10)
labelage = tk.Label(text="Age",width="15", height="1", bg="blue", fg="white")
labelage.grid(column=0, row=11)
labelactivity = tk.Label(text="Acitivity Level",width="15", height="1", bg="blue", fg="white")
labelactivity.grid(column=0, row=12)
labelheight2 = tk.Label(text="cm",width="8", height="1", bg="blue", fg="white")
labelheight2.grid(column=2, row=9)
labelweight2 = tk.Label(text="kg",width="8", height="1", bg="blue", fg="white")
labelweight2.grid(column=2, row=10)
labelage2 = tk.Label(text="years",width="8", height="1", bg="blue", fg="white")
labelage2.grid(column=2, row=11)

#According to Harris Benedict Equation

labelActivityLevel1 = tk.Label(text="Litle exercise equals to 1.2", width="40", height="2", bg="green", fg="white")
labelActivityLevel1.grid(column=0, row=14)

labelActivityLevel2 = tk.Label(text="Light exercise (1-3 days per week) equal to 1.375", width="40", height="2", bg="green", fg="white")
labelActivityLevel1.grid(column=0, row=15)

labelActivityLevel3 = tk.Label(text="Moderate exercise (3-5 days per week) equal to 1.55", width="40", height="2", bg="green", fg="white")
labelActivityLevel3.grid(column=0, row=16)

labelActivityLevel4 = tk.Label(text="Active exercise (6-7 days per week) equal to 1.725", width="40", height="2", bg="green", fg="white")
labelActivityLevel4.grid(column=0, row=17)

labelActivityLevel5 = tk.Label(text="Very heavy exercise (twice per day) equal to 1.9", width="40", height="2", bg="green", fg="white")
labelActivityLevel5.grid(column=0, row=18)

#-------ENTRIES-------
entry1 = tk.Entry()
entry1.grid(column=1, row=2)
entry2 = tk.Entry()
entry2.grid(column=1, row=3)
entry3 = tk.Entry()
entry3.grid(column=1, row=4)
entry4 = tk.Entry()
entry4.grid(column=1, row=9)
entry5 = tk.Entry()
entry5.grid(column=1, row=10)
entry6 = tk.Entry()
entry6.grid(column=1, row=11)
entry7 = tk.Entry()
entry7.grid(column=1, row=12)

#------BUTTON------
button1 = tk.Button(text="Calculate Calorie", command=main) # command function give the ability to call any function
button1.grid(column=1, row=5)
button2 = tk.Button(text="Male Calorie", command=male_main_calorie)
button2.grid(column=1, row=14)
button3 = tk.Button(text="Female Calorie", command=female_main_calorie)

button3.grid(column=1, row=17)


window.mainloop()



