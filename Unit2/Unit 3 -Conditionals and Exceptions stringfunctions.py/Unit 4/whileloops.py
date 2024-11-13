#There are a couple types of loops in python
# The foor loop lets your iteratea list
# -great for looping a set number of times 
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password.
#You could get it right the first time 
# It could take you a million tires 
# Or  anything in between 

real_pass = "potatos45"
entered_pass = ""

attempts = 0
# A while loop continues looping until the condition is no longer True 
while real_pass != entered_pass:     # Check if the entered password matches the real one 
    # Ask for the password 
    entered_pass = input("Please enter the password\n>")

attempts = attempts + 1 
    #Check if password is correct
if entered_pass == real_pass:
        print("ACCESS GRANTED")
else:
        print("ACCESS DENIED")
        print(str(attempts) + "attempts.")
        print("try again...")

#End password checking 
print("Welcome!")        

#With while loops, you need to becareful for infinite loops
# When you put your computer in rest mode, it has nightmares about infinite loops/joke
# An infinite loop happens when you enter a while loop that can neverbe escaped. 
# example 

#count = 0
#while count < 10:
 #   count += 1
 #   print(count)

#print("All Done") 

# Real World Example:
# Type "exit" to quit 

user_input = ""

while user_input != "exit": 
    user_input = input("Enter something (type 'exit' to quit)")
    print("You entered: " + user_input)

print("All done")


