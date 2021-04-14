# User Storage Python Program by OfficialMuffin

import time

users = ['Alice', 'Bob']

def list_users():
    # Print out users names and the number of users in the list
    for name in users:
        print(f"Name: {name}")
    len_users = str(len(users))
    print("Number of users: " + len_users + "\n")

def add_user():
    # Add user to the list
    new_user = input("Input User: ")
    # Check if the user already exists
    for user in users:
    	if (new_user == user):
    		print("Error: User already exists")
    		return -1
    users.append(new_user)

def delete_user():
    try:
        # Delete user from the list 
        list_users()
        del_user = input("Enter user you want to delete: ")
        users.remove(del_user)
        print("\nSuccess!\n")
    except ValueError:
        print("\nError: User does not exist!\n")

def sort_users():
    # Sort list of users in alphabetical order
    users.sort()

def del_all():
    confirm = input("Are you sure you want to clear all? (Y/n): ")
    if confirm == 'Y':
        users.clear()
        print("\nUser list has been cleared!\n")
    elif confirm == 'n':
        main_menu()

def main_menu():
    # Main menu
    print("Please select from the following items: ")
    print("1. List Users")
    print("2. Add User")
    print("3. Delete User")
    print("4. Sort All")
    print("5. ***DELETE ALL***")
    menu_select = input()

    if menu_select == '1':
        list_users()
    elif menu_select == '2':
        add_user()
    elif menu_select == '3':
        delete_user()
    elif menu_select == '4':
        sort_users()
    elif menu_select == '5':
        del_all()
    else:
        print("Invalid Request!")

if __name__ == "__main__":
    while True:
        main_menu()
        time.sleep(1)
       
