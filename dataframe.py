import mysql.connector
import pandas as pd

def display_data_as_dataframe():
    # Establish MySQL connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahi@nayak186",
        database="data_manip"
    )

    # Select data from MySQL table
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM json_to_sql_table")
    rows = cursor.fetchall()

    # Get column names
    column_names = [desc[0] for desc in cursor.description]

    # Create DataFrame
    df = pd.DataFrame(rows, columns=column_names)

    # Close connection
    cursor.close()
    connection.close()

    return df

# Main function
def main():
    # Display data as DataFrame
    df = display_data_as_dataframe()
    print(df)

if __name__ == "__main__":
    main()
