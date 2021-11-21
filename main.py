"""
    User Storage Python Program 
    by OfficialMuffin
"""
from time import sleep

users = []
menu = [
    "List Users",
    "Add User",
    "Delete User",
    "Change User",
    "Sort Users",
    "Find User",
    "Delete List",
    "Save List",
    "Load List"
]

def list_users():
    # Print out users names and the number of users in the list
    if len(users) == 0:
        print("User list is empty. Please add a user from the menu.")
    else:
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
    
def find_user():
    search = str(input("Enter the user you would like to search for: "))
    if search in users:
        print("User exists!")
    else:
        print("User does not exist!")

def del_all():
    if len(users) == 0:
        print("User list is empty. Nothing to delete.")
    else:
        confirm = input("Are you sure you want to clear all? (Y/n): ")
        if confirm == 'Y':
            users.clear()
            print("\nUser list has been cleared!\n")
        elif confirm == 'n':
            main_menu()
            
def save_list():
    filename = str(input("Please enter a filename to save: "))
    if filename == "":
        print("You didnt enter anything, please try again.")
    else: 
        if len(users) == 0:
            print("User list is empty. Unable to save an empty list")
        else:
            filename_with_ext = filename + ".txt"
            file = open(filename_with_ext, 'a')
            for u in users:
                file.write(str(u + '\n'))
            file.close()
            print("File Saved Successfully!")
    
def read_list():
    filename = str(input("Enter the filename of file you wish to open: ")) + ".txt"
    try:
        #file = open(filename, 'r')
        with open(filename, 'r') as file:
            if FileExistsError:
                exists = str(input("File exists. Do you want to append to current list? (Y/n): "))
                if exists == 'Y':
                    # Append to current list
                    """ for users in file:
                        formatted = users.strip('\n')
                        print(formatted)  """
                    file_lines = file.readlines()
                    users.append(file_lines)
                    file.close()

                elif exists == 'n': 
                    # Use the new list in the file
                    file_lines = file.readlines()
                    users.append(file_lines)             
        
    except FileNotFoundError:
        print("File not found. Please try again.")
    
def main_menu():
    # Main menu
    print("Please select from the following items: ")
    for menu_number, enumerated_list in enumerate(menu, start=1):
        print(menu_number, enumerated_list)
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
        find_user()
    elif menu_select == '6':
        save_list()
    elif menu_select == '7':
        read_list()
    elif menu_select == '8':
        del_all()
    else:
        print("Invalid Request!")

if __name__ == "__main__":
    while True:
        main_menu()
        sleep(1)
