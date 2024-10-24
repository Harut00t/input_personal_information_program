#import string for name rules
import string

#character list for rules, variables
letter = string.ascii_letters

#print(letter) #to check if it is working

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

                if all(char in letter for char in name):
                    break
                else:
                    #error message
                    print("Only letters are allowed.")
                    continue
            
            #?loop for rules of age
            while True:
                age = input("Please input the age: ")
                num_age = int(age)
                
                if age.isdigit():
                    if 0 <= num_age < 130:
                        break #stop the loop

                    #error message
                    else:
                        print("Ages between 0 to 130 only.")
                        continue
                # #error message
                # else:
                #     print("Only numbers are allowed.")
                #     continue
                
            #an array of the name and age
            name_and_age[name] = {
                "name" : name,
                "age" : num_age
            }
            
            print(name_and_age[name])
    
            name_and_age.update(name_and_age)

            #new entries
            another_entry = input("Another entry?: ")
            break
        except:
            print("There's something wrong...")

    if another_entry == "n":
        # for entry in name_and_age.values():
        # print(f"Name: {entry['name']}, Age: {entry['age']}") #a piece of code that prints the name and age
        age_compare = [entry['age'] for entry in name_and_age.values()]
        highest_age = max(age_compare)

        oldest_people = [] #To get the names of the highest age

        for entry in name_and_age.values():
            if entry['age'] == highest_age:
                oldest_people.append(entry['name'])
                
        if len(oldest_people) == 1:
            print(f"the oldest person is {oldest_people[0]}, aged {highest_age}") #oldest person
        else:
            print(f"the oldest person are {', '.join(oldest_people)}, both aged {highest_age}") #oldest people
        break #stopping the loop

    elif another_entry != "y":
        print("Please only type 'y' or 'n' in the input.")
        continue

   
    
        




