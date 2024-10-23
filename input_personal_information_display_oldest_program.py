#import string for name rules
import string

#character list for rules, variables
letter = string.ascii_letters
number = string.digits

#print(letter) #to check if it is working

#create a list to handle all
dicts = []

#initial variable for the program
name_and_age = {}


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
                    if num_age < 130 and age != letter and num_age >= 0:
                        break #stop the loop

                    #error message
                    else:
                        print("Ages between 0 to 130 only.")
                        continue
                #error message
                else:
                    print("Only numbers are allowed.")
                    continue
                
            #an array of the name and age
            name_and_age[name] = {
                "name" : name,
                "age" : num_age
            }
            
            print(name_and_age[name])
    
            dicts.append(name_and_age)

            #new entries
            another_entry = input("Another entry?: ")
            break
        except:
            print("There's something wrong...")

    if another_entry == "n":
        print(dicts)
        print("complete!") #test
        break #stopping the loop

    elif another_entry != "y":
        print("Please only type 'y' or 'n' in the input.")
        continue

   
    
        




