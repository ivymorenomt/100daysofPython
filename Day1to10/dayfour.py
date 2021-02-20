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


def list_append(arr, val):
    arr.append(val)
    print(f'Append an element at the end: {arr}')
    return arr

def list_extend(arr, val):
    arr.extend(val)
    print(f'Extend the list as one item: {arr}')
    return arr

def list_insert(arr, pos, val):
    arr.insert(pos, val)  # -1 is adding to the second to the last
    print(f'Insert an element at {pos} position: {arr}')
    return arr

def list_pop(arr, val):
    arr.pop(val)
    print(f'Item removed is {val}: {arr}')
    arr.pop()
    print(f'Last item is removed: {arr}')
    return arr

def list_remove(arr,val):
    arr.remove(val)
    print(f'Item is removed: {arr}')
def list_index(arr, val):
    print(f'The index of value {val} is: {arr.index(val)}')

def list_count(arr, val):
    print(f'The number of times {val} has appeared in the list: {arr.count(val)}')

def list_reverse(arr):
    arr.reverse()
    print(f'The list in reverse: {arr}')

def list_sort(arr):
    arr.sort()
    print(f'The list sorted in ascending order: {arr}')

def join_string(arr):
    sentence = ' '.join(arr)
    print(f'Joined string in list: {sentence}')

if __name__ == "__main__":
    first_list = [1, 2, 3, 4, 4, 5]
    words = ['coding', 'is', 'fun']

    list_append(first_list, 5)
    list_extend(first_list, [5, 6, 7, 8])
    list_insert(first_list,1,9)
    list_pop(first_list, 4)
    list_remove(first_list, 5)
    list_index(first_list, 5)
    list_count(first_list, 5)
    list_reverse(first_list)
    list_sort(first_list)
    join_string(words)
    print("\n")
    for_loop()
    while_loop()
    iteration()