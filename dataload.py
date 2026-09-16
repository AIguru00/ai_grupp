import csv
from pathlib import Path


def load_data(filepath=None):
    """Läser in temperaturdata från en CSV-fil."""
    if filepath is None:
        filepath = Path(__file__).with_name("data.csv")

    data = []

    try:
        with open(filepath, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["temperature_celsius"] = float(row["temperature_celsius"])
                data.append(row)
    except FileNotFoundError:
        print(f"Filen {filepath} hittades inte!")
        return None

    print(f"Laddade {len(data)} rader från {filepath}")
    return data