# Dictionary is a type of collection like a list
# Alist is a collection of items in a sequence
# A dictionary is different 
# Dictionaries store data in key_vaule pairs 
# You can retrive data quickly by using a unique key
# Instead of retreving it by index (position)

#Example 
# Lists use brackets, dictionaries use braces
vang = {}
"name": "vang" 
"age":17, 
"city": "St Michael"
"pets": 2, 
 "height": 5.8

# Each key must be unique 

# Retreving vaules from a diictionary 

print(vang["age"])

# .get allows you to retreive a vaule without erroring 
# when the key doesn't exist
#The second parameter is what is given if vaule is not found 
print(vang.get("height"))
print(vang.get("Weight", "Not Found"))

# You can add vaules to a dictionary

vang["country"] = "USA"

# You can modify vaules 
vang["age"] = 17

print(vang)

# Remove entries 
vang.pop("pets")

# Iterate through a dictionary using a for loop
for key, vaule in vang.items(): 
 print(key + ": " + str(vaule))

 # Dictionary functions 
  print(vang. keys())     #returns all keys
  print(vang.vaules())   #reurns all vaules 
  print(vang.items())    #returns all pairs 
  print(vang.clear())    #removes all items for the dictionary