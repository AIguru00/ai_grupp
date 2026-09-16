import csv
import random


temperatures_celsius = [
    round(random.uniform(-10, 50), 1)
    for _ in range(10)
]

with open("data.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["temperature_celsius"])
    writer.writerows([[temperature] for temperature in temperatures_celsius])