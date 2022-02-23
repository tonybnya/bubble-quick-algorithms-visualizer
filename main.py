import os
import time
import random
import sys
from sort import bubble, quick
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)


def visualize(arr):
    """
    Function to visualize each swap in the execution of the Bubble Sort Algo.
    """

    # To clear the screen so that the output always be on a single line.
    # os.system('clear')
    print(Style.BRIGHT + f"{arr}")

    # This for loop is to handle the speed of the swap.
    # Test another range to change the speed.
    for _ in range(15000000):
        pass


def main():
    if len(sys.argv) != 3:
        with open('usage.txt') as f:
            print(f.read())

        time.sleep(2)
        sys.exit(1)


    option = sys.argv[1]
    length = int(sys.argv[2])

    arr = []
    for i in range(length):
        arr.append(random.choice(range(1, 100)))

    if option == '-b':
        print('\n===== * BUBBLE SORT * =====\n')
        print(Fore.GREEN + f"Unsorted Array: {arr}\n")
        print(Fore.BLUE + Style.BRIGHT + f"\nSorted Array: {bubble(arr, visualize)}")
        print('\n===========================')
    elif option == '-q':
        print('\n===== * QUICK SORT * =====\n')
        print(Fore.GREEN + f"Unsorted Array: {arr}\n")
        print(Fore.BLUE + Style.BRIGHT + f"Sorted Array: {quick(arr, visualize)}")
        print('\n==========================')
    else:
        print('Unknown option')
        time.sleep(2)
        sys.exit(1)


if __name__ == "__main__":
    main()