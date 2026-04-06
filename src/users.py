# User Input console
# 1) Fråga efter namn
# 2) Om använder inte skriver något ge ett fel meddelande
# 3) Annars hälsa användaren

users = [] # empty list of users

# TODO
# Add Delete function
# Add Update function

# TODO EXTRA if above is not enough
# Implement age for each user
# Check age of user to see if they are allowed to register
# if below 14 NO REGISTER ALLOWED
# otherwise its okey

def add_user(name):
    
    cleaned = name.strip()
    
    if len(cleaned) == 0:
        return False
    
    if cleaned in users:
        return False
    
    users.append(cleaned)
    return True

def list_users():
    return users

def user_exists(name):    
    cleaned = name.strip()
    return cleaned in users





def collection_of_data():
    print("Hello from Python")

    long_text = """ This is a long text that needs to be printed
    many liner at the same time
    That is cool 
    """

    print(long_text)

    # boolean

    is_a_player = True
    is_he_a_child = False
    print(is_a_player, is_he_a_child)

    # Pythons null
    result = None
    print("Python Null is : ", result)

    # Lists
    number = [1, 2, 3, 4]
    names = ["Meki", "Sara", "Alex"]
    mixed = [1, 2, "Sara", "Alex", 34.6]
    print(number, number[1], names, mixed)

    # Dictionary
    person = {
        "name": "Mekuria",
        "age": "40",
        "is_teacher": False
    }

    key = person.keys()

    for k in key :
        print(k)
        
    value = person.values()

    for v in value :
        print(v)

    # functions
    def greet_name(name):
        print("Hej", name)
        
    greet_name("Mekuria")

    def add(a,b):
        return a + b

    result = add(3,4)
    print(result)

    # if-satser
    age = 20

    if age >= 18:
        print("you are an adult")

    elif age >= 100:
        print("You are too old")
    else:
        print("You are too young")
        
    #range
    for i in range(5):
        print("value", i)
        
    # while-loop
    count = 0

    while count < 3:
        print("count ", count)
        count += 1
        
    # Input from user
    name = input("What is your name? ")

    # Remove white space from strings
    name = name.strip()

    #print(repr(name))

    print("Hello: ", name)
    print(f"Hello again {name}") # formatted string
        
def input_user_info():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    name = input("Provide your name plaease!! ")
    name = name.strip()
    
    return name

def process_user_input(name):
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    if len(name) == 0:
        print("please provide user name")
    else:
        print("Welecome back", name)
        
##### input_name = input_user_info()
####  process_user_input(input_name)

    
