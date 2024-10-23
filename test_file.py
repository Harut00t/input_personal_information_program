# #import string for name rules
# import string

# #character list for rules, variables
# letter = string.ascii_letters
# number = string.digits

# #print(letter) to check if it is working

# #initial variable for the program
# young = {}
# old = {}

# #loop for user inputs and to break 'yes' and 'no' reentry
# while True:
#     #2nd loop for another input the answers are 'yes' and 'no'
#     while True:
#         try:
#             #?loop for rules of names
#             while True:
#                 name = input("Please input a name: ")

#                 if any(char in letter for char in name):
#                     break
#                 else:
#                     #error message
#                     print("Only letters are allowed.")
#                     continue
            
#             #?loop for rules of age
#             while True:
#                 age = input("Please input the age: ")
#                 num_age = int(age)
#                 if any(char in number for char in age):
#                     if num_age < 130 and num_age >= 0:
#                         break
#                     #error message
#                     else:
#                         print("Ages between 0 to 130 only.")
#                         continue
#                 #error message
#                 else:
#                      print("Only numbers are allowed.")
#                      continue
            
#             #an array of the name and age
#             young[name] = {
#                 "name" : name,
#                 "age" : num_age
#             }

#             print(young[name])

#             #new entries - anoth is short for 'another'
#             another_entry = input("Another entry?: ")

#             #print the name and age of oldest
                            
#             #stop the loop
#             break

#         except:
#             print("There's something wrong...")

#     if another_entry == "n":
#         print("complete!") #test
#         break #stopping the loop

#     elif another_entry != "y":
#         print("Please only type 'y' or 'n' in the input.")

# Initialize an empty list to hold dictionaries
dictionaries = []

while True:
    # Create a new dictionary for each iteration
    new_dict = {}
    
    # Get user input for the key-value pairs
    while True:
        key = input("Enter a key (or type 'done' to finish this dictionary): ")
        
        if key.lower() == 'done':
            break  # Exit the inner loop to finish the current dictionary
            
        value = int(input(f"Enter a value for '{key}': "))
        new_dict[key] = value  # Add the key-value pair to the new dictionary

    # Append the new dictionary to the list of dictionaries
    dictionaries.append(new_dict)
    
    # Ask if the user wants to add another dictionary
    another = input("Do you want to add another dictionary? (yes/no): ")
    if another.lower() != 'yes':
        if new_dict[value] > dictionaries(new_dict[value]):
            print(new_dict[key], new_dict[value])
            break  # Exit the outer loop if the user doesn't want to continue
        else:
            print(dictionaries(new_dict[value]))


# Print the list of dictionaries
print("List of Dictionaries:", dictionaries)