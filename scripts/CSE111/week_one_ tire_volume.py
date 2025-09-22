# CSE 111 - W01 Project: Tire Volume
# This program calculates the approximate volume of a tire
# based on its width, aspect ratio, and wheel diameter.
# It saves the results in a log file (volumes.txt).
# Enhancement: asks the user if they want to buy tires and stores phone number.

import math
from datetime import datetime

# Get user input
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute the volume
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display result
print(f"The approximate volume is {volume:.2f} liters")

# Get current date
current_date_and_time = datetime.now()
current_date = f"{current_date_and_time:%Y-%m-%d}"

# Ask user if they want to buy tires
buy_choice = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
phone_number = ""
if buy_choice == "yes":
    phone_number = input("Please enter your phone number: ")

# Save to volumes.txt
with open("volumes.txt", "at") as volumes_file:
    if phone_number:
        print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}", file=volumes_file)
    else:
        print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)