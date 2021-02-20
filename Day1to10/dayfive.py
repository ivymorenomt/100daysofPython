# TODO List Slice

first_list = [1,2,3,4]

print("\n first parameter\n")
print(first_list[1:])
print(first_list[3:])
print(first_list[-1:])
print(first_list[-3:])
print(first_list[:])

print("\n second parameter\n")
print(first_list[:2])
print(first_list[:4])
print(first_list[1:3])
print(first_list[:-1])
print(first_list[1:-1])

print("\n third parameter\n")
print(first_list[1::2])
print(first_list[::2])
print(first_list[1::-1])
print(first_list[:1:-1])
print(first_list[2::-1])

# tricks
string = "this is fun!"
print(string[::-1])

#change values using step
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']

print(numbers)

#Swapping
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]
print(names)