## [Day 1](https://github.com/ivymorenomt/100daysofPython/blob/master/Day1to10/dayone.py):

Overall functionality of the code is to read text from a file and converting it to a list
I have also created the following functions:
* Reading from files.
* Reading input from the console.
* Split strings

Output:

Looping thru all the list of files from Files variable and print out directory and filename

C:\Users\marjo\PycharmProjects\100daysofcode\accounts.txt
C:\Users\marjo\PycharmProjects\100daysofcode\details.csv
C:\Users\marjo\PycharmProjects\100daysofcode\invite.docx

The current working directory is: C:\Users\marjo\PycharmProjects\100daysofcode\Day1to10

List entries of the current working directory

dayone.py
daytwo.py
README.md

Below is a list of files that ends with .txt under this directory:


The current working directory is: C:\Users\marjo\PycharmProjects\100daysofcode\Day1to10
Enter a string for string_index function: test
The sliced letter within 2 and 5 is st

## [Day 2](https://github.com/ivymorenomt/100daysofPython/blob/master/Day1to10/daytwo.py):

#### List Slicing

In string slicing, we can do:

string = 'hello'
string[0:2:1] where [start:stop:stepover]

In list, you can do the same. You can also change the element in it as lists are mutable
Strings are immutable:
zoo[0] = 'z' - this is not acceptable


#### Matrix

matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9],
]

These types of arrays or matrix is used in Machine Learning/Computer Vision - it is because images are represented by 1s and 0s.
The representation of 1s and 0s is the pixel of the image being processed.
We can also do heavy calculations using multidimensional arrays/list.

to access:
matrix[0][1] = if you want to access '5'
where [0] is the first array and [1] is the second element in the first array

#### Output of the code:

ï»¿"name,department,birth month"
"James Smith,Accounting,November"
"Erica Banks,IT,March"
21
ï»¿"name,department,birth month"
"James Smith,Accounting,November"
"Erica Banks,IT,March"Mark Ivy,Energy,March

Original List Array: ['notebooks', 'sunglasses', 'toys', 'grapes']

List array on slice: ['notebooks', 'toys']

New List array: ['gum', 'sunglasses', 'toys', 'grapes']

The value in array 1 and element 2 is: 6

The original array value is: [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 150]
After Append: [1, 2, 3, 4, 5, 150]

The original array value is: [1, 2, 3, 4, 5, 150]
After Insert: [1, 2, 3, 4, 500, 5, 150]

The original array value is: [1, 2, 3, 4, 500, 5, 150]
After Removing a value: [2, 3, 4, 500, 5]