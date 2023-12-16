#Criteria Complete: 3.17, 3.13, 5.1, 3.21, 3.29

#This files asks the user for the username and saves down the username to the existing csv(datafile)

#3.19 You read in user input from a file to use in your program. 
#^The user inputs username which gets saved in the csv file which is then used as a username that is taken
#and where a user won't be able to input again

#3.17 imported module you created yourself!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import mymodule
import admincontrols
import csv

# 3.13 You use string methods to convert a string to uppercase or lowercase.
def case_change(input_string):
    """Change the case of each character in the input string using str.translate."""
    # Create a translation table that swaps the case of each character
    translation_table = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    # Use str.translate() to apply the translation table
    return input_string.translate(translation_table)

class Main:
    # Infinite loop to repeatedly ask the user for a new username
    #5.1 You used a while-loop to iterate continuously until a condition is reached. 
    while True:
        # Prompt the user to enter a new username or 'stop' to exit
        new_username = input("Enter a new username (or 'stop' to exit): ")
 
        # Check if the user entered 'stop' to exit the loop
        if new_username.lower() == 'stop':
            # Inform the user that they are exiting, then break out of the loop
            print("Exiting. Goodbye!")
            break

        # Check if the entered username is not already in the list
        if new_username not in mymodule.usernames:
            # Add the new username to the list
            mymodule.usernames.append(new_username)
            #Append data to the CSV file
            #3.21 You appended the results of a program to a file.
            with open(mymodule.csv_file_path, 'a', newline = '') as csvfile:
                csv_writer = csv.writer(csvfile)

                for row in mymodule.usernames:
                    csv_writer.writerow(row)

            # Inform the user that the username was added successfully, then break out of the loop
            print(f"Username '{new_username}' added successfully.")
            break
        elif new_username in admincontrols.AdminControls.banned_usernames:
            print("Sorry, the username is not allowed.")
        else:
            # Inform the user that the entered username already exists, prompt them to try a different one
            print(f"Username '{new_username}' already exists. Try a different one such as " + case_change(new_username))







