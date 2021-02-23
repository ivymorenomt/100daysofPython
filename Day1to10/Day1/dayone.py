'''Reading/Writing from/to files.
Reading input from the console.
Split strings
2D array implementation and how to use it.

**Read a file, then split strings and store contents in a 1d array

'''

import os

#Reading/Writing from files
def read_files():
    files = ["accounts.txt", "details.csv", "invite.docx"]
    print("\nLooping thru all the list of files from Files variable and print out directory and filename\n")
    for file in files:
        print(os.path.join("C:\\Users\\marjo\\PycharmProjects\\100daysofcode\\data\\", file))

    entries = os.listdir(getWorkingDirectory())
    print("\nList entries of the current working directory\n")
    for entry in entries:
        print(entry)

    print('\nBelow is a list of files that ends with .txt under this directory:\n')
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            print(os.path.join(os.getcwd(), file))

def getWorkingDirectory():
    print(f"\nThe current working directory is: {os.getcwd()}")
    return os.getcwd()

# Read input from the console
def readIntInput():
    usrInput = int(input("Enter a number: "))
    print(f'Number entered is {usrInput}')

def readStrInput():
    return input("Enter a string to split: ")

# splits string into a list
def split_string(text):
    return text.split()

def read_a_file(file):
    workingDirectory = open(f'C:\\Users\\marjo\\PycharmProjects\\100daysofcode\\data\\{file}')
    text_to_split = workingDirectory.read()
    return split_string(text_to_split)

def string_index(inp, start, stop):
    print(f'The sliced letter within {start} and {stop} is {inp[start:stop]}')
    return inp[start:stop]


if __name__ == "__main__":
    read_files()
    getWorkingDirectory()
    read_a_file("test.txt")
    inp = input("Enter a string for string_index function: ")
    string_index(inp, 2,5)
