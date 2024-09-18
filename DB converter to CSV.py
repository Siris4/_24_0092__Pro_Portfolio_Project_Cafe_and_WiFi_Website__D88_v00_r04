import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect(
    r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0092__Day88_Pro_Portfolio_Project_Cafe_and_WiFi_Website__240917\NewProject\r00_env_START\r03\pythonProject1\instance\cafes.db')
cursor = conn.cursor()

# List all tables to see the correct table name
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

# Replace 'your_table_name' with the actual table name from the printout
cursor.execute("SELECT * FROM your_table_name")

# Fetch all data
data = cursor.fetchall()

# Get column names
column_names = [description[0] for description in cursor.description]

# Write data to CSV file and save it on the Desktop
with open(r'C:\Users\Siris\Desktop\output_file.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write column headers
    csvwriter.writerow(column_names)

    # Write data
    csvwriter.writerows(data)

# Close the connection
conn.close()
