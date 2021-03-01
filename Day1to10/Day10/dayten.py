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

name = 'colt'
new_list = [char.upper() for char in name]
print(new_list)

friends = ['ashley', 'matt', 'michael']
new_friend = [friend.capitalize() for friend in friends]
print(new_friend)

print([num*10 for num in range(1,6)])
print([bool(val) for val in [1, [], '']]) #returns true or false

numbers = [1,2,3,4,5]
string_list = [str(num) for num in numbers]
print(string_list)

with_vowels = 'This is so much fun!'
print(''.join(char for char in with_vowels if char not in 'aeiou'))

#Using list comprehensions:
answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
print(answer)
print(answer2)
#Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)

