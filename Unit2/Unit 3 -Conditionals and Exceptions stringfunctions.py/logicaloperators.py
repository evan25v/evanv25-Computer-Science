# logical operators
#Comparison operators  > < == >= <=
#Arithmetic operators + - / * % ** //

def check_eligibilitity(age, exp):
     # You must be at least 18 years old and have 1 year of experience to be eligible 
     if age >= 18 and exp >= 1:
          print("You are eligible for the  competition!")
        
        elif age < 18:
             print("You are notold enough to compete'") 

        elif exp < 1:
            print("You don't have enough eexperince to compete.") 

a =int(input("How old are you?"))
e = int(input("How many yearsof experin=ence do you have?\n>"))

check_eligibility(a, e) 