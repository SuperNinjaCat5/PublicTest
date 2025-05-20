import sys
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def question():
    clear_console()
    personame = input("Hi what's your name? \n\n")
    print(f"\nOh, my name is Ben. Nice to meet you {personame}\n")