import os
import time
import random
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)


def bubble(arr, func):
    """
    Bubble Sort Algorithm.
    Time Complexity: O(n^2).
    """

    func(arr)

    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                print(Fore.RED + Style.BRIGHT + f"{arr[j]}")
                print(Fore.CYAN + Style.BRIGHT + f"{arr[j + 1]}")
                print(Fore.YELLOW + f"Swapping {arr[j]} and {arr[j + 1]}...\n")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                func(arr)

    return arr


def quick(arr, func):
    """
    Quick Sort Algorithm.
    Time Complexity: O(n^2).
    """

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    print(Fore.RED + Style.BRIGHT + f"pivot: {pivot}")
    less, greater = [], []

    for number in arr[1:]:
        if number <= pivot:
            less.append(number)
            print(f"Less than {pivot}")
            func(less)
        else:
            greater.append(number)
            print(f"Greater than {pivot}")
            func(greater)

    print()
    start = quick(less, func)
    end = quick(greater, func)

    return start + [pivot] + end