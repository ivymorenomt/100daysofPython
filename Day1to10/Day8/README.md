Day 8 Random lectures and problem solving in codewars

Algorithm - they process doing something and
Data Structure - algorithms store the data in a data structure

Q3

Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

    '''
    Numerical Score	Letter Grade
    90 <= score <= 100	'A'
    80 <= score < 90	'B'
    70 <= score < 80	'C'
    60 <= score < 70	'D'
    0 <= score < 60	'F'
    '''

Q4

Write reverseList function that simply reverses lists.

- I used the reverse() function at first and it did pass the tests. However, when submitting the code,
it had random tests and it failed the code. So I made use of slicing list[::-1] and this passed the test
Slicing:
[start:end:step] [all elements:all elements: the last index of element]
what it does is it loops all of the elements and since the step is negative, it will return the elements in reverse.

Q5

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
- This question piqued my interest. I didn't know that there is a built-in function bin()
that returns a binary representation of a value.
        
        sum = bin(num1 + num2)[2:]
        
        where [2:] would slice the first 2 values displayed by bin
        
        it would display 0b by default

Q6

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

    Examples:
    Input: [0]
    Output: "even"
    
    Input: [0, 1, 4]
    Output: "odd"
    
    Input: [0, -1, -5]
    Output: "even"
In this case, I have used sum(list) function to get the sum of elements in the list, then used the modulo '%' to get the remainder.
