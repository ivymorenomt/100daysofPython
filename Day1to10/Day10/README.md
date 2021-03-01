### Day 10

I did most of [21 day data challenge](https://github.com/ivymorenomt/21DaysDataChallenge) code. 
The key takeaway in resolving programming challenges is that, read. Read the problem.
Read it one by one, and visualize how to resolve the issue

Example is the data challenge where: 
Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:

- Total Milk Production
- Total Revenue
- How much revenue did the cow farm make in the year 2020? 

Resolve total milk production first by:

    df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']

Resolve total revenue by:

    df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']

Then finally resolve revenue:

    year_2020 = df['Month'].str.contains('20-')
    tot_2020 = df[year_2020].sum()['Total Revenue']
    
How to come up with these solutions? 
In Total Milk production, think about the formula on how to calculate the total. Obviously, it would be monthly * number of cows
In Total Revenue - it's about the same but use total milk production and the price per pound

the df means Dataframe, I have used pandas library to store the data. 

While doing 100 days of code, i am also doing the 21 day challenge simultaneously so I won't lose my muscle memory on coding/ all the 
important things I have learned in data science/Machine Learning using these libraries.

#### List Comprehension
Syntax
[__ for __ in ___]
a variable, for a variable in range, array, etc

Example:
nums[1,2,3]
[x*10 for x in nums] = for every x in nums, we are going to multiply and put in new list

*** The idea is we take an existing list and output another list with diff values based upon the first list

#### List Comprehension vs Looping
##### For Loop
numbers = [1,2,3,4]
doubled_numbers = []

for num in numbers:
    doubled_number = num*2
    doubled_numbers.append(doubled_number)
print(doubled_numbers) #[2,4,6,8]

##### List Comprehension
numbers = [1,2,3,4]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers) #[2,4,6,8]

List Comprehension with Conditional Logic
numbers = [1,2,3,4,5,6]
evens = [num for num in numbers if num % 2 == 0] 
# take every num, add to a new list, for each num in numbers. If num is divisible by 2 == 0
odds = [num for num in numbers if num % 2 != 0]

[num*2 if num % 2 == 0 else num/2 for num in numbers] # with else statement
# take even number, then multiply by two otherwise divide by two

#Strings
with_vowels = 'This is so much fun!'
''.join(char for char in with_vowels if char not in 'aeiou') #Ths s s mch fn!
 
#### Nested Lists
- complex data structures - matrix
- Games
- Rows and Columns for visualizations, tabulation and grouping data

Accessing Nested Lists

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
How to access 8? = nested_list[-1][-2]
or
nested_list[2][-2]

for l in nested_list: # the first loop will be going thru the top level list [1,2,3]
    for val in l: # 
        print(val)