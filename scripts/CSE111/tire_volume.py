# tire_volume.py
# This program calculates the approximate volume of a tire
# and logs the result with the current date into a file.

import math
from datetime import datetime

# Ask the user for tire dimensions
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume
volume = (math.pi * (width ** 2) * aspect_ratio *
         (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the result
print(f"The approximate volume is {volume:.2f} liters")

# Get current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Log the data into volumes.txt
with open("volumes.txt", "at") as file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=file)