import mysql.connector
import pandas as pd

def change_email_format():
    # Establish MySQL connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahi@nayak186",
        database="data_manip"
    )

    # Create cursor
    cursor = connection.cursor()

    # Update email addresses in the table
    cursor.execute("UPDATE json_to_sql_table SET email = REPLACE(email, SUBSTRING_INDEX(email, '@', 1), 'abc')")

    # Commit changes
    connection.commit()

    # Fetch data into pandas dataframe
    cursor.execute("SELECT * FROM json_to_sql_table")
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)

    # Close connection
    cursor.close()
    connection.close()

    return df

# Main function
def main():
    # Change email format and get dataframe
    df = change_email_format()

    # Print dataframe
    print(df)

if __name__ == "__main__":
    main()
