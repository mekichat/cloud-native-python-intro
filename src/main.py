from users import add_user, list_users, user_exists, delete_user, update_user

# User Input console
# 1) Fråga efter namn
# 2) Om använder inte skriver något ge ett fel meddelande
# 3) Annars hälsa användaren

# TO DO
# Add Delete to menu
# Add Update functionto menu


def show_menu():
    print("\n ---- User console---")
    print("1) Add user")
    print("2) List users")
    print("3) Search for users")
    print("4) Delete user")
    print("5) Update user")
    print("6) Exit")
    
# TO DO
# Add Delete handler
# Add Update handler
    
  
def handle_add_user():
    name = input("Enter your username: ")
    age = input("Enter your agee: ")
    success = add_user(name, age)
    
    if success:
        print(f"user {name.strip()} with age {age.strip()} has saved to the user list")
        
    else:
        print("""could not save user
              name may already be in use or empty""")
    
def handle_list_users():
    all_users = list_users()
    if len(all_users) == 0:
        print("There are no users yet")
    else:
        print("\n registered users")
        
        for i, name in enumerate(all_users, start=1):
            print(f"{i}, {name}")

def handle_search_user():
    name = input("Enter username to search for: ")
    if user_exists(name):
        print(f"Yes, user {name.strip()} exists")
    else:
        print(f"No, user {name.strip()} does not exist")
        
def handle_delete_user():
    name = input("Enter username to be deleted: ")
    success = delete_user(name)
    
    if success:
        print(f"user {name.strip()} has been deleted")
        
    else:
        text = """could not find the
        user name from the existing user list"""
        print(text)
        
def handle_update_user():
    old_name = input("Enter existing username: ")
    new_name = input("Enter new username that needs to be updated: ")
    success, message = update_user(new_name, old_name)
    
    if success:
        print(f"user {old_name.strip()} is replaced by {new_name.strip()} user name")
        
    else: 
        if message == "user not found":
             print(f"User {old_name} does not exist")
        elif message == "new name can not be empty":
            print("New username can not be empty")
        elif message == "existing name can not be empty":
            print("Existing username can not be empty")
        elif message == "name already taken":
             print(f"User {new_name} already exists")           
     
    
         

def main():
    
    while True:
        show_menu()
        
        choice = input("Chose an option (1-6): ")
        #choice = int(choice)
        if choice == "1":
            handle_add_user()
        elif choice == "2":
            handle_list_users()
        elif choice == "3":
            handle_search_user()
        elif choice == "4":
            handle_delete_user()
        elif choice == "5":
            handle_update_user()
        elif choice == "6":
            print("Exiting program bye")
            break
        else:
            print("Invalid choice, try again")
            
if __name__ == "__main__": # run main() program if the main() function is within the main.py file
   main()
            
