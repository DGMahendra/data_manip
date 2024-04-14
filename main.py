import json
import pandas as pd
import mysql.connector

# Load JSON data from file
with open('sample_data_for_assignment.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Extract column names and data from JSON
columns = json_data['cols']
data = json_data['data']

# Establish MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mahi@nayak186",
    database="data_manip"
)
cursor = connection.cursor()

# Create table query
create_table_query = f"CREATE TABLE IF NOT EXISTS json_to_sql_table ("
for col in columns:
    create_table_query += f"{col} VARCHAR(255), "
create_table_query = create_table_query[:-2] + ")"
cursor.execute(create_table_query)

# Insert data into MySQL table
for row in data:
    insert_query = f"INSERT INTO json_to_sql_table ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
    cursor.execute(insert_query, row)
connection.commit()

# Unload data from MySQL into pandas DataFrame
select_query = f"SELECT * FROM json_to_sql_table"
cursor.execute(select_query)
df = pd.DataFrame(cursor.fetchall(), columns=columns)

# Change email addresses format
df['email'] = df['email'].apply(lambda x: 'abc@gmail.com' if '@' in x else x)

# Display data
print(df)

# Close connection
cursor.close()
connection.close()
