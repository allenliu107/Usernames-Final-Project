#Met Criteria: 5.5, 5.6, 5.11, 1.6, 3.18
#This code is for admin who manage the usernames in the data baser who may need to delete things or
#need additional information

import mymodule
import sys

# List of banned usernames
banned_usernames = ["stupid", "mean", "bad"]

# Function to count usernames
def count_usernames(usernames_list):
    count = 0
    # 5.5 You used a for-loop to iterate over a list.
    for name in usernames_list:
        count += 1
    return count

# Function to print all usernames
def print_usernames(usernames_list):
    # 5.6 You used a loop to print or save output iteratively.
    for name in usernames_list:
        print(name)

# Function to remove a username from the list
def remove_username(username_to_delete, usernames_list):
    if username_to_delete in usernames_list:
        # 5.11 You removed an item from a list iteratively (i.e., inside a loop).
        usernames_list.remove(username_to_delete)
        print(f"Username '{username_to_delete}' deleted successfully.")
    else:
        print(f"Error: Username '{username_to_delete}' not found in the list.")
    return usernames_list

if __name__ == "__main__":
    #3.18 You used sys.argv to accept user input at the command line. 
    if len(sys.argv) < 2:
        print("Usage: python script.py <action>")
        sys.exit(1)

    # Get the admin action from the command line
    admin_action_input = sys.argv[1]

    if admin_action_input == "remove_username":
        if len(sys.argv) < 4:
            print("Usage: python script.py remove_username <username_to_delete>")
            sys.exit(1)
        
        # Get the username to delete from the command line
        username_to_delete = sys.argv[2]
        mymodule.usernames = remove_username(username_to_delete, mymodule.usernames)
        #1.6 You can run a Python script from a command line using additional arguments.

    elif admin_action_input == "count_usernames":
        number_of_usernames = count_usernames(mymodule.usernames)
        print(f"Number of usernames: {number_of_usernames}")

    elif admin_action_input == "print_usernames":
        print_usernames(mymodule.usernames)

    else:
        print("Invalid action. Please enter 'remove_username', 'count_usernames', or 'print_usernames'.")
