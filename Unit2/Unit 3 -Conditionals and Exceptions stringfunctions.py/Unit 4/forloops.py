#For Loops
#This is a big deal
#For Loops allow the programmer to REPEAT, or what we call lOOP

#Write a program thhat prints the numbers one through ten

#for <temp var> in <list>: 
#range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0,10):     #0 is the START vaule, 10 is the STOP vaule
    print(i) 
print("yo") 

top_foods = ["Eggs Benedict", "Fried Chicken", "Mac n Cheese"]
#"Go through every food in top foods"
#Repeats everything in the for loop for each item in the list
#Where food equals the current item 
for food in top_foods:
    print(food)


#PRACTICE: Create a list of groceries- 
#Contains mailk, eggs, bread, butter, apples 
#Ask for user input and an item they purchased 
#If the item was on the list, print ("<item> crossed off the list!")
#You will need a for loop to search for that item
#You will need an if statement in the forloops to check 

groceries =["milk", "egg", "bread", "butter", "apples"]

purchased_item = input("What item did you buy?\n>")

for grocery in groceries:
    if grocery == purchased_item.lower():
        print(grocery + " checked of the list")
        groceries.remove(grocery)

print(groceries) 

#Create a list of five random numbers from 0-100
#Use a for loops to find the sum of those numbers 
