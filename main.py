
from functions import *

print("Welcome to the casino!")
print("Minimum deposit: 10$\n"
          "Maximum deposit: 1000$\n")

legend = input("Do you want to see the rules? y/n ")
if legend == 'y':
    print(legend_3lines)

deposit = float(input("How much money do you want to deposit? $"))
deposit = check_depo(deposit)


while True:
    play = input("Do you want to play? (Press x to leave / Press Enter to join) ")
    if play == 'x':
        break
    spin(deposit)



