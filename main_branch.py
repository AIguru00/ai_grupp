import csv
import random


temperature_celsius = round(random.uniform(-10, 50), 1)

with open("temperature.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["temperature_celsius"])
    writer.writerow([temperature_celsius])