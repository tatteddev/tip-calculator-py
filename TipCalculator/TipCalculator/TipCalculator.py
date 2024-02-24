print("Welcome to the tip calculator\n")

total = input("What was the total spent\n")
percent = input("What percent would you like to tip?\n")
people = input("How many people are splitting the check?\n")

percent = float(percent) / 100
tip = (int(total) / int(people)) * percent

print(f"The tip would be ${round(tip, 2)} per person")

