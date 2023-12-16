#Completed Criteria 5.15, 5.17, 5.18, 5.19,5.12, 5.13, 5.14
#
#The code will take all of the most important people who have a username in the company and create a 
#additional data through the use of dictionaries and tuples 

# 5.15 You created a dictionary manually.
username_dict = {'booleanBard': 'president', 'webWanderer': 'vice president', 'byteBard': 'treasurer', 'devDreamer': 'Secretary'}

# 5.17 You accessed the keys of a dictionary.
keys = username_dict.keys()

def printVIP():
    updated_dict = {}  # Create a new dictionary to store the updated values
    # 5.18 You iterated through the items of a dictionary to access both keys and values:
    for key, value in username_dict.items():
        #5.19 You updated values in a dictionary programmatically (i.e., using variables/loops, not manually)
        updated_dict[value] = key + " " + "VIP"

    # Print the updated dictionary
    print("Updated dictionary:", updated_dict)

# Call the function to print the updated dictionary
#printVIP()
##########
#5.12 You created a tuple manually.    
#Creating the profile of the president
President_tuple = ('booleanBard', '22', 'president')

# Function that unpacks the tuple
def unpack_president_tuple(president_info):
    username, age, role = president_info
    #5.13 You assigned tuple members to separate variables in one assignment statement.
    return f"Username: {username}, Age: {age}, Role: {role}"
#5.14 You used a tuple to return multiple values from a function.

# Calling the function
president_info_string = unpack_president_tuple(President_tuple)

# Displaying the result
print(president_info_string)