#2 functions 
print("Hello, World!")
input("Please enter your username\n>")  # \n is called an escape character 
# \n startsa new line (Linebreak)
#input is never required  

# variables 
#Syntax
# <name> = <vaule>
x = 5

# Snake naming convention - all lowercase, underscore for your spaces
# CONSICE: Short and descriptive
username = "osowski"        #Define string
fav_animal = "Calugo"       #Defone string
total_poptarts = 12         #Define interger (whole number)
percent_complete = 23.52    #Define
is_cool = True              #Define
first_letter = 'c'          #Define Character (single symobol)

total_poptarts = 8          #Reassign 


# Arithmetic Operators 
 # + - *  /  ** %  //
print(4 + 4)
print("4" +  "4")
print()
print("cat" + "dog")
print("cat" * 3)
print("cat" + 3)           #ERROR: Cannot use + for string and int 

#Make some working programs 
#1. add two numbers usig input 
x = int("What is x?\n>"))       # input() always returns a string
y = intput("What is y?\n>")            
y =int(y)
print(x + y) 

# 2. Conversions celcius to farenheight 
temp_celcius = input("What is the tempreture in Celcius\n>?")
temp_celcius = int     #convert to integer 
print(temp_celcius + " degrees C equals " + temp_farenheight + " degress F")



#Some coversion functions
str()
int()
float()  


#The stuff that goes between the parenthesis is called PARAMETERS 
#Parameters are the variables that the function needs to run 


# Functions 
# Functions are a lot like variables 
# They have names 
# They can be recalled from memory by calling their name
# Store information
# Variables store vaules, functions store code 
def potato():            #def keyword + name + () + : 
    print("potato")      #Lines indented underneath are "inside"  the function 

# functions are not ran when they are undefined 
# they must be called by their name to run 
potato()    #Every function call needs open and closed parenthesis 
            # even if it has no parameters 

def jump(how_high) 
    print(" You jumped " + str(how_high) + " inches! ")

    jump(14) 






































    def make_a_word(a, b, c, d, e, f, g, h, i, j, k)
    print(a + b + c + d + e + f + g + h + i + j + k)

    make_a_word("Z", "a", "b", "c", "k", "O", "s", "o", "w", "s", "k",)


#Functions can have many lines 
def top_ten_games():
print("1. Elden Ring")
print("2. Shadow  of the Colossus")
print("3. Minecraft")
print("4. Diablo 3")
print("5.  Gran Turismo 7")
print("6. Overwatch")
print("7. Ratchet & Clank: Up Your Aresenal")
print("8. World of Exile")
print("10. Enter the Gungeon")

#scope: Global and Local Variables!!
#Scope refers to the context in which the variable was defined
#GLOBAL- defined at no indentation level
#LOCAL- defined inside of a function 

#Global variables can be used anywhere 
todd = "cool guy"        #Global variable- define in a function 

#Local variables exist in the scope they were defined 
smith = 'not cool guy'        #Local variable 




#Return functions 
#Functions can also return vaules 
#The vaule that is returned is sent back to where the function was called 
#This is very similar to how a variable works 
#The function does its work and returns an asnwer back 



# When you call a variable in a function 
# It searches local variables first, then global variables 

#aaaaaiaf you want to reassign a global variable inside of a function 

   