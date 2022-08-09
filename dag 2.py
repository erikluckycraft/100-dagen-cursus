#Excercise 1 - Data Types
two_digit_number = input("Type a two digit number: ")

getal1 = int(two_digit_number[0])
getal2 = int(two_digit_number[1])

#Exercise 2 - BMI
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight = int(weight)
height = float(height)

bmi = weight / (height * height)

print(int(bmi))

#Exercise 3 - Life in Weeks
age = input("What is your current age?")

totaal_maanden = 1080
totaal_weken = 4680
totaal_dagen = 32850

age_int = int(age)

maanden_over = totaal_maanden - (12*age_int)
weken_over = totaal_weken - (52*age_int)
dagen_over = totaal_dagen - (365*age_int)

print(f"You have {dagen_over} days, {weken_over} weeks, and {maanden_over} months left.")


#Final Exercise - Tip Calculator

print(getal1 + getal2)
print("Welkom bij fooi berekenen.")
rekening = float(input("Wat was de totale rekening: "))
percentage = int(input("Hoeveel procent fooi wil je geven: "))
mensen = int(input("Tussen hoeveel mensen wil je rekening splitsen: "))

percentage += 100

formule = rekening / 100 * percentage / mensen
formule_float = "{:.2f}".format(formule)

print(f"De totale rekening is ${formule_float}")
