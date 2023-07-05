import random

symbols = ['7' , 'A' , 'B' , 'C' , 'D' ,'E']
legend_3lines = ("7 = x10 \n"
                 "A = x5  \n"
                 "B = x3 \n"
                 "C = x2.5  \n"
                 "D = x2 \n"
                 "E = x1  \n")

def check_depo(num):
    if num < 10:
        print("Please deposit more money! The minimum deposit amount is 10 $")
        num = int(input("How much money do you want to deposit? $"))
        check(num)
    elif num > 1000:
        print("The maximum deposit amount is 1000$")
        num = 1000
        check(num)
    return num

def check_bet(num , dep):
    if num > dep:
        print("You don't have enough money!")
        num = int(input("How much money do you want to bet? $"))
        check_bet(num , dep)
    return num

def spin(deposit):
        bet = float(input("How much do you want to bet? $"))
        bet = check_bet(bet , deposit)
        deposit -= bet


        l0c0 = random.choice(symbols)
        l0c1 = random.choice(symbols)
        l0c2 = random.choice(symbols)
        l1c0 = random.choice(symbols)
        l1c1 = random.choice(symbols)
        l1c2 = random.choice(symbols)
        l2c0 = random.choice(symbols)
        l2c1 = random.choice(symbols)
        l2c2 = random.choice(symbols)
        print("|" + l0c0 + "|" + l0c1 + "|" + l0c2 + "|")
        print("|" + l1c0 + "|" + l1c1 + "|" + l1c2 + "|")
        print("|" + l2c0 + "|" + l2c1 + "|" + l2c2 + "|")

        win = 0

        if l0c0 == l0c1 == l0c2:
            if l0c0 == "7":
                win+=10
            elif l0c0 == "A":
                win += 5
            elif l0c0 == "B":
                win += 3
            elif l0c0 == "C":
                win += 2.5
            elif l0c0 == "D":
                win += 2
            else:
                win += 1

        if l1c0 == l1c1 == l1c2:
            if l1c0 == "7":
                win += 10
            elif l1c0 == "A":
                win +=  5
            elif l1c0 == "B":
                win +=  3
            elif l1c0 == "C":
                win +=  2.5
            elif l1c0 == "D":
                win += 2
            else:
                win += 1

        if l2c0 == l2c1 == l2c2:
            if l2c0 == "7":
                win += 10
            elif l2c0 == "A":
                win += 5
            elif l2c0 == "B":
                win += 3
            elif l2c0 == "C":
                win += 2.5
            elif l2c0 == "D":
                win += 2
            else:
                win += 1

        win *= bet
        if win != 0:
            print("Congratulations , you have won " + str(win) +"$")
        else:
            print("I'm sorry ! You have lost " + str(bet) + "$")
        deposit += win
        print("You have " + str(deposit) + "$ left")

        again = input("Play again? y/n ")
        if again == "y":
            spin(deposit)

