#import string for name rules
import string

#character list for rules, variables
letter = string.ascii_letters
number = string.digits

#print(letter) to check if it is working

#initial variable for the program
old_and_young = {}

#loop for user inputs and to break 'yes' and 'no' reentry
while True:
    #2nd loop for another input the answers are 'yes' and 'no'
    while True:
        try:
            #?loop for rules of names
            while True:
                name = input("Please input a name: ")

                if any(char in letter for char in name):
                    break
                else:
                    #error message
                    print("Only letters are allowed.")
                    continue
            
            #?loop for rules of age
            while True:
                age = input("Please input the age: ")
                num_age = int(age)
                if any(char in number for char in age):
                    if num_age < 130 and num_age >= 0:
                            break
                    #error message
                    else:
                        print("Ages between 0 to 130 only.")
                        continue
                #error message
                else:
                     print("Only numbers are allowed.")
                     continue
            
            #an array of the name and age
            old_and_young[name] = {
                "age" : num_age
            }

            print(old_and_young[name])

            #new entries - anoth is short for 'another'
            another_entry = input("Another entry?: ")
            #stop the loop
            break

        except:
            print("There's something wrong...")

    if another_entry == "n":
        print("complete!") #test
        #print the name and age of oldest
        break #stopping the loop

    elif another_entry != "y":
        print("Please only type 'y' or 'n' in the input.")





