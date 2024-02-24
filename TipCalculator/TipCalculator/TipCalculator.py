print("Welcome to the tip calculator\n")

bill = int(input("What was the total spent\n"))
tip = int(input("What percent would you like to tip?\n"))
people = int(input("How many people are splitting the check?\n"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Every person will pay: ${final_amount}")

