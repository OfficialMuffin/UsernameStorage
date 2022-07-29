"""
User Storage Python Program
by OfficialMuffin
"""
from time import sleep
from os import system, name
from src import menu
from pyfiglet import Figlet

if __name__ == "__main__":
    print("Welcome to ")
    f = Figlet(font='slant')
    print(f.renderText("UserStore"))
    while True:
        menu.main_menu()
        sleep(3)
        system('cls' if name == 'nt' else 'clear')
