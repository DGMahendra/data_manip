import pandas as pd
import mysql.connector

# Establish MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mahi@nayak186",
    database="data_manip"
)
cursor = connection.cursor()

# Select data from MySQL table
select_query = f"SELECT * FROM json_to_sql_table"
cursor.execute(select_query)
data = cursor.fetchall()

# Extract column names from cursor description
columns = [col[0] for col in cursor.description]

# Create pandas DataFrame
df = pd.DataFrame(data, columns=columns)

# Close connection
cursor.close()
connection.close()

# Display DataFrame
print(df)
