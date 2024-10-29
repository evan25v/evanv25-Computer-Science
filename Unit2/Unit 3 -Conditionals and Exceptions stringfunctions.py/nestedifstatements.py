# Nested if statements 
#You are a Prime mem






prime = True
cost = 20
age = 17
consent = False 

if prime: 
    if age >=18: 
        print("You are eligible gor free shipping!")
    else:  
        if consent:    
            print("You are eligible for free shipping!")
        else: 
            print("You are NOT eligible for free shipping!")

elif cost >=25: 
    if age >=18: 
       print("You are eligible for free shipping!")         
    elif consent: 
        print("You are eligible for free shippping!")    
    else: 
        print("You are NOT eligible for free shippping!")

else: 
    print("You are NOT eligible for free shipping!")
