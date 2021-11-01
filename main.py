from colorama import init, Fore, Back, Style

init()

print(Back.GREEN + "Hi there, welcome to BMI calculation software!")
print(Back.CYAN)
weight = float(input("What's your weight?: "))
height = float(input("And what's your height?: "))
print("")

bmi = float(weight / ((height / 100) ** 2))

print(Back.RESET + "Your current BMI is " + str(bmi))

if bmi <= 16:
    print(Back.RED + "Your current BMI is " + str(bmi))

if 16 <= bmi <= 18.5:
    print(Back.YELLOW + "Insufficient body weight", end='')

if 18.5 <= bmi <= 25:
    print(Back.GREEN + "Your body weight is OK", end='')

if 25 <= bmi <= 30:
    print(Back.YELLOW + "Excess body weight", end='')

if 30 <= bmi <= 35:
    print(Back.RED + "Obesity of the 1 degree", end='')

if 35 <= bmi <= 40:
    print(Back.RED + "Obesity of the 2 degree", end='')

if bmi >= 40:
    print(Back.RED + "Obesity of the 3 degree (morbid)", end='')

print(")", end='')
print(Style.RESET_ALL)
input()
