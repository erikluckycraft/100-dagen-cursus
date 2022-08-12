import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

lijst = [rock, paper, scissors]
random = random.randint(0, 2)
optie = int(input("Maak een keus: \n1) Rock\n2) Paper\n3) Scissors\n"))
if optie > 3 or optie < 0:
    print("Geef een geldige invoer.")
    exit()
computer_keus = lijst[random]
gebruiker_keus = lijst[optie -1]

#winnen
print(f"Jij selecteerde {gebruiker_keus}")
print(f"De computer koos {computer_keus}")
if gebruiker_keus == rock and computer_keus == scissors or gebruiker_keus == paper and computer_keus == rock or gebruiker_keus == scissors and computer_keus == paper:
    print("Jij wint!")
#verliezen
elif gebruiker_keus == rock and computer_keus == paper or gebruiker_keus == paper and computer_keus == scissors or gebruiker_keus == scissors and computer_keus == rock:
    print("Jij verliest!")
#gelijkspel
else:
    print("Gelijkspel!")


