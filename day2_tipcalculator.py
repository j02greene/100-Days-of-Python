print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

tip_decimal_conversion = tip / 100
total_tip_amt = bill * tip_decimal_conversion
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people
final = format(bill_per_person, ".2f")

print(f"Each person should pay: ${final}")
