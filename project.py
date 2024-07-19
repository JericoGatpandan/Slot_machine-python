# 1. Deposit some money
# 2. Determine number of lines to bet on
# 3. Collect the bet amount
# 4. Spin the slot machine
# 5. check if the user won
# 6. give the user their winnings
# 7. Play again
import math

def deposit():
    amount = input("Enter Your Deposit amount: ")
    numAmount = float(amount)

    if  math.isnan(numAmount):
        print("Invalid Deposit amount, try again. ")
    elif numAmount <= 0:
        print("Invalid Deposit amount, try again. ")
    else:
        return numAmount
    

def lines():
    while True:
        lines = input("Enter the line number to bet on (1-3): ")
        numLines = int(lines)

        if  math.isnan(numLines):
            print("Invalid number of lines, try again. ")
        elif numLines > 3:
            print("Invalid number of lines, try again. ")
        elif numLines <= 0:
            print("Invalid number of lines, try again. ")
        else:
            return numLines
        

def bet(balance, lines):
    while True:
        bet = input("total bet per line: ")
        numbet = int(bet)

        if math.isnan(numbet):
            print("Invalid bet, try again. ")
        elif numbet <= 0:
            print("Invalid bet, try again. ")
        elif numbet > balance / lines:
            print("Invalid bet, try again. ")
        else:
            return numbet

