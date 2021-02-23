# TODO for Loops
#
letters = ["a", "b", "c"]
# #this will print the index and the letter
for letter in enumerate(letters):
    print(letter)

people = [
    ["Homer", 36],
    ["Marge", 34],
    ["Bart", 9],
    ["Lisa", 7],
    ["Maggie", 1],
]
print('Below is using index:\n')
for p in people:
    print(p[0], "is", p[1], "years old.")

print('\nBelow uses multiple variables\n')
for name, age in people:
    print(name, "is", age, "years old.")

# 1. Make a program that lists the countries in the set
clist = ['Canada','USA','Mexico','Australia']
for c in clist:
    print(c)

# 2. Create a loop that counts from 0 to 100
for n in range(1,101):
    print(n)

# 3. Make a multiplication table using a loop
for i in range(1,10):
    print('i = ', i, ':')
    for j in range(1,10):
        print('{:2d}'.format(i*j), end=" ")
    print()
# 5. Create a loop that counts all even numbers to 10
for i in range(1,11):
    if i % 2 == 0:
        print(i)
# 6. Create a loop that sums the numbers from 100 to 200
for x in range (100, 201):
    print(x+x)
