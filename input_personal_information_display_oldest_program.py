#import string for name rules
import string

#character list for rules, variables
letter = string.ascii_letters
number = string.digits

#print(letter)

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
                
                if any(char in number for char in age):
                    num_age = int(age)
                    if num_age < 130 and num_age >= 0:
                            break
                    else:
                        print("Ages between 0 to 130 only.")
                        continue
                else:
                     print("Only numbers are allowed.")
                     continue
                
        except:
            print("There's something wrong...")


    

    

#an array of the name and age
            
#print the name and age of oldest

#new entries

#stopping the loop






