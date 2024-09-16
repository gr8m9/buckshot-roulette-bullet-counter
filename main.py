import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def show_shells():
    print(style.RED + str(live) + ' live bullets' + style.RESET)
    print(style.GREEN + str(blank) + ' blanks' + style.RESET)
    print(style.WHITE + style.RESET)

print('hello\n(press enter to continue...)')
input()

os.system('cls')

while True:
    print('Input the amount of live and blank shells (e.g., "5 2"):')
    shells = input()
    os.system('cls')
    
    # Input validation for two integer values
    shells1 = shells.split()
    if len(shells1) != 2 or not shells1[0].isdigit() or not shells1[1].isdigit():
        print(style.RED + "Invalid input! Please enter two numbers separated by a space." + style.RESET)
        continue
    
    live = int(shells1[0])
    blank = int(shells1[1])

    while True:
        show_shells()
        print("Which shell was used? (l for live, b for blank, 'end' to finish the round)")
        gone = input().strip().lower()
        
        if gone == 'l':
            if live > 0:
                live -= 1
            else:
                print(style.RED + "No live bullets left!" + style.RESET)
        elif gone == 'b':
            if blank > 0:
                blank -= 1
            else:
                print(style.RED + "No blanks left!" + style.RESET)
        elif gone == 'end':
            os.system('cls')
            break
        else:
            print(style.RED + "Invalid input! Please enter 'l', 'b', or 'end'." + style.RESET)

        os.system('cls')
