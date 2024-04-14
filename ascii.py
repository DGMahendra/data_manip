import pandas as pd
import json

# Function to load JSON data into a DataFrame
def load_json_to_df(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data['data'], columns=data['cols'])
    return df

# Function to convert phone numbers to ASCII characters
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

# Load JSON data into DataFrame
df = load_json_to_df('sample_data_for_assignment.json')

# Apply the function to convert phone numbers to ASCII characters
ascii_chars_list = convert_phone_to_ascii_from_df(df)

# Add the ASCII characters as a new column in the DataFrame
df['ascii_chars'] = ascii_chars_list

# Display the DataFrame
print(df)
