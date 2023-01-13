num1 = 42   # variable declaration, intializing Integer
num2 = 2.3  # float decalration, variable declaration 
boolean = True  # declaration initializing  boolean Data Type 
string = 'Hello World' # declaration string ,initializing  strings  
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # declaration list, initializing list of pizzas
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # declaration dictionaries, initializing of a person info 
fruit = ('blueberry', 'strawberry', 'banana') # declaration tuples, initializing of fruits
print(type(fruit)) # type check,  data type
print(pizza_toppings[1]) # list - access values
pizza_toppings.append('Mushrooms') # list - add values
print(person['name']) # dictionaries - access values
person['name'] = 'George' # dictionaries - add values
person['eye_color'] = 'blue' # dictionaries - change values
print(fruit[2])# tuples - access values

if num1 > 45: # if declaration, num1 initializing
    print("It's greater") 
else:
    print("It's lower") # else - values     

if len(string) < 5: # if initializing 
    print("It's a short word!") 
elif len(string) > 15: # elif 
    print("It's a long word!") 
else: # else    
    print("Just right!")

for x in range(5): # start loop
    print(x)# continues 
for x in range(2,5):# start loop
    print(x)# continues 
for x in range(2,10,3):# start loop     
    print(x)# continues
x = 0 # initializing value, 
while(x < 5): #start  loop
    print(x) # continue
    x += 1# increment

pizza_toppings.pop()# list delete values 
pizza_toppings.pop(1)# list delete values

print(person) # access value of dictionary  
person.pop('eye_color') # delete a value of dictioonary 
print(person) # change value of dictionary

for topping in pizza_toppings: # start for loop
    if topping == 'Pepperoni': # initializing and declaring the value 
        continue # continues    
    print('After 1st if statement')# strings 
    if topping == 'Olives': # change value
        break # stop loop

def print_hello_ten_times(): # function a
    for num in range(10):# 
        print('Hello')# function string value

print_hello_ten_times() # function return value 

def print_hello_x_times(x): # funtion - parameters
    for num in range(x): # start loop
        print('Hello') # stop - string 

print_hello_x_times(4) # function - parameters
def print_hello_x_or_ten_times(x = 10): # function - arguments
    for num in range(x): # start loop       
        print('Hello') # stop loop 

print_hello_x_or_ten_times() # function 
print_hello_x_or_ten_times(4)# function - parameters 


"""
Bonus section  # multiline comment 
"""

# print(num3) ## TypeError: 'tuple' object does not support item assignment
# num3 = 72 ##TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'##IndexError: list index out of range
# print(person['favorite_team']) ##  KeyError: 'favorite_team'
# print(pizza_toppings[7]) ## IndexError: list index out of range
#   print(boolean) ## IndentationError: unexpected indent
# fruit.append('raspberry')  ## IndexError: list index out of range
# fruit.pop(1) ## AttributeError: 'tuple' object has no attribute 'pop'