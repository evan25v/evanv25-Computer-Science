# Exception Handling
# Write a prograam that asks  for two numbers and adds them

# if = try
# else = except
def divide_two_numbers(): 
    try: 
        x = int(input("Whars the first number?\n>"))
        y = int(input("Whats the second number?\n>"))
        print(x + y)

    except VauleError: 
     print("Invalid entry....") 
     divide_two_nmubers() 

     excpet ZeroDivisionError:
        print("Cannot divide by zero....") 

finally
divide_two_numbers() 
