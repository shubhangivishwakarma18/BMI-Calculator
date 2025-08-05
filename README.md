#BMI Calculator
This project is a BMI (Body Mass Index) tracking application built in Python that allows users to calculate, store, and retrieve their BMI data using two storage options:
MySQL Database
CSV File System

Features:
Store BMI Data: Saves the user's weight, height, and BMI into a MySQL database and/or CSV file with a timestamp.
Retrieve Data: Fetches all BMI records for a specific user from the MySQL database.
CSV Management: Creates a CSV file if it doesn't exist and appends new entries to maintain a local log.
Database Connection Handling: Establishes and safely closes MySQL connections using mysql-connector-python.

Technologies Used:
Python
MySQL
CSV module
mysql-connector-python library
