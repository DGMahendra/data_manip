import mysql.connector
import pandas as pd
import numpy as np

def convert_postal_zip_to_int():
    # Establish MySQL connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahi@nayak186",
        database="data_manip"
    )

    # Create cursor
    cursor = connection.cursor()

    # Update postalZip values in the table
    cursor.execute("UPDATE json_to_sql_table SET postalZip = REGEXP_REPLACE(postalZip, '[^0-9]', '')")

    # Commit changes
    connection.commit()

    # Fetch data into pandas dataframe
    cursor.execute("SELECT * FROM json_to_sql_table")
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)

    # Convert postalZip column to numpy integers
    df['postalZip'] = df['postalZip'].astype(np.int64)

    # Close connection
    cursor.close()
    connection.close()

    return df
def convert_phone_to_ascii_from_df(df):
    ascii_chars_list = []
    # Iterate over the phone numbers in the DataFrame
    for phone in df['phone']:
        # Remove non-numeric characters from the phone number
        phone = ''.join(filter(str.isdigit, phone))
        
        ascii_chars = ''
        # Process phone number two digits at a time
        for i in range(0, len(phone), 2):
            two_digits = phone[i:i+2]
            # Convert two digits to ASCII characters
            if len(two_digits) == 2:
                ascii_value = int(two_digits)
                if 65 <= ascii_value <= 99:
                    ascii_chars += chr(ascii_value)
                else:
                    ascii_chars += 'O'  # Replace with 'O' if value is less than 65
            else:
                ascii_chars += 'O'  # Replace with 'O' for odd number of digits
        
        ascii_chars_list.append(ascii_chars)
    
    return ascii_chars_list

# Example usage:
# Assuming df is your DataFrame containing the 'phone' column


# Main function
def main():
    # Convert postalZip values to int and get dataframe
    df = convert_postal_zip_to_int()

    # # Print dataframe
    # print(df)
    # print(type(df['postalZip']))
    ascii_chars_list = convert_phone_to_ascii_from_df(df)
    print(ascii_chars_list)
if __name__ == "__main__":
    main()
