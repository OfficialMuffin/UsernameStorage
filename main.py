"""
User Storage Python Program 
by OfficialMuffin
"""
from time import sleep
from os import system, name
import menu

if __name__ == "__main__":
    while True:
        menu.main_menu()
        sleep(3)
        system('cls' if name == 'nt' else 'clear')