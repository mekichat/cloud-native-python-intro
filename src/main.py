from users import add_user, list_users, user_exists

# User Input console
# 1) Fråga efter namn
# 2) Om använder inte skriver något ge ett fel meddelande
# 3) Annars hälsa användaren


def show_menu():
    print("\n ---- User console---")
    print("1) Add user")
    print("2) List users")
    print("3) Search for users")
    print("4) Exit")
    
  
def handle_add_user():
    name = input("Enter your username: ")
    success = add_user(name)
    
    if success:
        print(f"user {name.strip()} saved")
        
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
         

def main():
    
    while True:
        show_menu()
        
        choice = input("Chose an option (1-4): ")
        #choice = int(choice)
        if choice == "1":
            handle_add_user()
        elif choice == "2":
            handle_list_users()
        elif choice == "3":
            handle_search_user()
        elif choice == "4":
            print("Exiting program bye")
            break
        else:
            print("Invalid choice, try again")
            
if __name__ == "__main__": # run main() program if the main() function is within the main.py file
   main()
            
