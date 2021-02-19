#TODO List Methods Continuation

def for_loop():
    print('This function is for For Loops')
    numbers = [4,6,2,9,7,10]
    for num in numbers:
        print(num*num)

    colors = ['purple', 'teal', 'magenta']
    for color in colors:
        print(color)

# if you want to access each item in a list, use for loop

# if you want to take advantage of the index, use while loop

def while_loop():
    print('\nThis function is for While Loops')
    colors = ['purple', 'teal', 'magenta', 'crimson', 'emerald']
    index = 0
    while index < len(colors):
        print(f'{index}: {colors[index]}')
        index +=1

def iteration():
    print('\nThis function is for iteration quiz')
    '''My Code'''
    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
    result = (''.join(sounds)).upper()
    print(result)

    '''Udemy Code'''
    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
    # Define your code below:
    results = ''
    for s in sounds:
        results += s
    results = results.upper()
    print(results)

def list_methods():
    print('\nThis function is for all the list methods\n')
    first_list = [1,2,3,4,4,5]
    first_list.append(5)
    print(f'Append an element at the end: {first_list}')
    first_list.extend([5,6,7,8])
    print(f'Extend the list as one item: {first_list}')
    first_list.insert(1,9) # -1 is adding to the second to the last
    print(f'Insert an element at the second position: {first_list}')
    first_list.pop(2)
    print(f'Item removed is 2: {first_list}')
    first_list.pop()
    print(f'Last item is removed: {first_list}')
    first_list.remove(4)
    print(f'Item is removed: {first_list}')
    print(f'The index of value 4 is: {first_list.index(4)}')
    print(f'The number of times 5 has appeared in the list: {first_list.count(5)}')
    first_list.reverse()
    print(f'The list in reverse: {first_list}')
    first_list.sort()
    print(f'The list sorted in ascending order: {first_list}')
    words = ['coding', 'is','fun']
    sentence = ' '.join(words)
    print(f'Joined list: {sentence}')


if __name__ == "__main__":
    for_loop()
    while_loop()
    iteration()
    list_methods()