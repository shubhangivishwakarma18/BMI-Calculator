import csv
import datetime
import os

CSV_FILE = "bmi_records.csv"


def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Weight (kg)", "Height (m)", "BMI", "Timestamp"])


def save_to_csv(weight, height, bmi):
    initialize_csv()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([weight, height, bmi, timestamp])


def read_from_csv():
    initialize_csv()
    records = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records
