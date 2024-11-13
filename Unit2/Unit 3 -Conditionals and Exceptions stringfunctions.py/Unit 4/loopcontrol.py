# Loop control statements 
# Allow you to change how loops operate 
# Do things like quit the loop early, skip the current lop, and even do nothing 
# break, continue, pass 

# break
# exits a loop prematurely, before it was supposed to end 

#Example 

bag_of_fruit = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruit: 
    if fruit == "bug":
       print("You ate a " + fruit)
    break       # thebreak statement exits the loop immediately and continues 
else:
    print("You ate a " + fruit)



# Continue
# Skips the current loop
# It does not exit the entire loop, just moveson thenext iteration

#Example
orders = [15, 30, 35, 23, 100, 3, 20, 22]

#Only apply discount for orders above 20 dollars 
# Coupon applying program
for order in orders:
    if order < 20:
      continue     #Skips the rest if the loop iteration and goes to the next iteration
      print("$"str(order) + " discounted 5% to $" + str(order * 0.95))

# Pass 
# Soes nothing
# Usually used as a placholder while writing code
#Text adventure project

if True:
   pass 

def enter_forest():
   pass

def swim_river():
   pass 

def eat_icecream(): 
   pass