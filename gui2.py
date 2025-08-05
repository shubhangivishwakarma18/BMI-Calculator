import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

import data_storage2


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        self.create_input_fields()
        self.create_buttons()
        self.create_display_section()

    def calculate_bmi(self):
        try:
            user_id = self.id_entry.get()  # Get user ID
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be greater than zero.")

            bmi = weight / (height ** 2)

            # Classify BMI
            category = self.classify_bmi(bmi)

            # Display BMI and category
            self.bmi_label.config(text=f"BMI: {bmi:.2f}")
            self.category_label.config(text=f"Category: {category}")

            # Store data in MySQL
            data_storage2.store_bmi_data(user_id, weight, height, bmi)

            messagebox.showinfo("Success", "BMI calculation completed and data saved successfully.")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def view_historical_data(self):
        try:
            user_id = self.id_entry.get()
            historical_data = data_storage2.retrieve_bmi_data(user_id)

            if historical_data:
                self.show_historical_data(historical_data)
            else:
                messagebox.showinfo("Historical Data", "No historical data available.")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

    def show_historical_data(self, data):
        plt.close()
        # Plot data
        timestamps = [entry[5] for entry in data]
        bmis = [entry[4] for entry in data]
        plt.plot(timestamps, bmis)
        plt.xlabel("Timestamp")
        plt.ylabel("BMI")
        plt.title("BMI History")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    def create_input_fields(self):
        weight_label = tk.Label(self.master, text="Weight (kg):")
        weight_label.grid(row=0, column=0, padx=10, pady=5)

        self.weight_entry = tk.Entry(self.master)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5)

        height_label = tk.Label(self.master, text="Height (m):")
        height_label.grid(row=1, column=0, padx=10, pady=5)

        self.height_entry = tk.Entry(self.master)
        self.height_entry.grid(row=1, column=1, padx=10, pady=5)

        id_label = tk.Label(self.master, text="User ID:")
        id_label.grid(row=2, column=0, padx=10, pady=5)

        self.id_entry = tk.Entry(self.master)
        self.id_entry.grid(row=2, column=1, padx=10, pady=5)

    def create_buttons(self):
        calculate_button = tk.Button(self.master, text="Calculate BMI", command=self.calculate_bmi)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        view_data_button = tk.Button(self.master, text="View Historical Data", command=self.view_historical_data)
        view_data_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_display_section(self):
        self.bmi_label = tk.Label(self.master, text="BMI: ")
        self.bmi_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.category_label = tk.Label(self.master, text="Category: ")
        self.category_label.grid(row=6, column=0, columnspan=2, pady=10)
