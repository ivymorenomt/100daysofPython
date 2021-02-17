#TODO Parse a csv file and write to another csv
#TODO List - do all of the methods associated with List.


def parse_csv():
    file = "test.csv"
    with open(f".\\data\\{file}", mode='r') as my_file:
        print(my_file.read())

def append_csv():
    file = "test.csv"
    with open(f".\\data\\{file}", mode='a') as my_file:
        print(my_file.write("Mark Ivy,Energy,March"))
    parse_csv()

def list_array():
    amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
    print(f'Original List Array: {amazon_cart}')
    print(f'List array on slice: {amazon_cart[0::2]}')

    # strings are immutable, meaning you cannot assign any item to it
    # greet = 'hello'
    # greet[0] = 'x' - this is not acceptable for strings
    # List is mutable

    new_cart = amazon_cart[:] # you're copying entire list, and it is going to equal new_cart
    new_cart[0] = 'gum'
    print(f'New List array: {new_cart}')

def matrix():
    matrix = [
        [1,2,3],
        [2,4,6],
        [7,8,9],
              ]
    print(f"The value in array 1 and element 2 is: {matrix[1][2]}")


def append_list(array):
    print(f'The original array value is: {array}')
    new_list = array.append(150)
    new_list = array
    print(array)
    print(f'After Append: {new_list}')

def insert_list(array):
    print(f'\n The original array value is: {array}')
    new_list = array.insert(4, 500)
    new_list = array
    print(f'After Insert: {new_list}')

def remove_list(array):
    print(f'\n The original array value is: {array}')
    new_list = array.pop()
    new_list = array.pop(0) # removes the index
    new_list = array
    print(f'After Removing a value: {new_list}') # this will remove the end of the list


if __name__ == "__main__":
    parse_csv()
    append_csv()
    list_array()
    matrix()
    basket = [1,2,3,4,5]
    append_list(basket)
    insert_list(basket)
    remove_list(basket)