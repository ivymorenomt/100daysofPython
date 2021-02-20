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

## [Day 3](https://github.com/ivymorenomt/100daysofPython/blob/master/Day1to10/daythree.py):

List - it is a collection or grouping of items; also known as Array
Methods:
* Append
* Insert
* Extend
* Reversed() or use slicing which is [::-1] where negative one is the last index
* Sorted

to access items, use array[indexnumber]
to check values in the list, use 'string' in array statement

Dictionary = it has key,value pairs

#### Understanding Data Structures
When to use a list/dictionary?

A list has order(which has index), a dictionary has no order.
A user may have details so use dictionary
List only has single value. It is only an index and some sort of value
Dictionary has a key and a value.

Day three output:
([1, 2, 3, 6, 7, 9])
([9, 7, 6, 3, 2, 1])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
hi my name is marj
Michael
True
List prior to change: ['Hanna', 'Louisa', 'Claudia', 'Angela', 'Geoffrey', 'aparna']
List after all the changes: ['Hannah', 'Louisa', 'Claudia', 'Angela', 'Jeffrey', 'Aparna']
1
2
3
[4, 5, 6, 7, 8]
9

## [Day Four](https://github.com/ivymorenomt/100daysofPython/blob/master/Day1to10/dayfour.py):

#### Add Elements:
* Append - you could only add one element, at the end of the list
* Extend - you could add more items in a list
* Insert - you can insert the item at a given position (index, value)

#### Remove / Clear Elements
* Clear - will remove all items from the list
* Pop - remove the item at the given position in the list and return it; if no index is specified removes and returns last item in teh list
* Remove - removes the first item from the list whose value is x; it throws a valueerror if the item is not found

#### Index, Count, Sort, Reverse and Join
* Index - returns the index of the specified item in the list or start and end
* count - it outputs the number of times x appears in the list
* Reverse - reverse the elements; it does not create a new list but updates this list
* Sort - sorts the elements in place
* Join - convert the two strings and joins them

Day Four Output:

This function is for For Loops
16
36
4
81
49
100
purple
teal
magenta

This function is for While Loops
0: purple
1: teal
2: magenta
3: crimson
4: emerald

This function is for iteration quiz
SUPERCALIFRAGILISTICEXPIALIDOCIOUS
SUPERCALIFRAGILISTICEXPIALIDOCIOUS

This function is for all the list methods

Append an element at the end: [1, 2, 3, 4, 4, 5, 5]
Extend the list as one item: [1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8]
Insert an element at the second position: [1, 9, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8]
Item removed is 2: [1, 9, 3, 4, 4, 5, 5, 5, 6, 7, 8]
Last item is removed: [1, 9, 3, 4, 4, 5, 5, 5, 6, 7]
Item is removed: [1, 9, 3, 4, 5, 5, 5, 6, 7]
The index of value 4 is: 3
The number of times 5 has appeared in the list: 3
The list in reverse: [7, 6, 5, 5, 5, 4, 3, 9, 1]
The list sorted in ascending order: [1, 3, 4, 5, 5, 5, 6, 7, 9]
Joined list: coding is fun

## [Day 5]((https://github.com/ivymorenomt/100daysofPython/blob/master/Day1to10/dayfive.py)):
#### Slicing

Make new lists using slices of the old list

some_list[start:end:step]

First parameter: Start - what index to start slicing from
Second parameter: End - the index to copy up to(exclusive counting)
Third parameter: Step - number to count at a time; same as step with Range; for example, a step of 2 counts every other number

Swapping values
 - shuffling - list of cards
 - sorting - sorting a list in place
 - algorithms
 
 *** Busy writing conference papers.. will continue with List Comprehension/Looping on Day 6.
 
