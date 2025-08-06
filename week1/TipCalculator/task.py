print("Welcome to the tip calculator!")
bill = float(input("What was the total for the bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15, 20?"))
people = int(input("How many people will be splitting the bill?"))
tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
print(f"Each person needs to pay ${billPerPerson}")