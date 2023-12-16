#Criteria Complete 3.16, 4.3 4.9
#
#This code imports all the csv containing all of the existing usernames

import pandas as pd

# Replace 'your_csv_file.csv' with the actual path and name of your CSV file
csv_file_path = '/Users/allen/Documents/Python/INST 126/Final Project 2/UserNames.csv'

#4.3 You used an if condition to avoid a potential user error
try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Extract the first column as a Python list
    usernames = df.iloc[:, 0].tolist()

    # Display the list of usernames
    #print("Usernames List:")
    #print(usernames)

#3.16 Handles a missing or incorrect file path, 
    #4.9 You raised an error and provided a helpful error message to the user.
except FileNotFoundError:
    print(f"Error: File not found at the specified path: {csv_file_path}")

except IndexError:
    print("Error: The CSV file is empty or does not have any columns.")

except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")



