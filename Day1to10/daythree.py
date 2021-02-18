def methods():
    basket = [3,6,1,7,2,9]
    sortarray = sorted(basket) #sorted produces a new array
    print(sortarray)
    print(sortarray[::-1]) #this reverses the list
    print(list(range(100)))
    sentence = ' '.join(['hi','my','name','is','marj'])
    print(sentence)

def access_values():
    # Accessing values in a list
    friends = ['Ashley', 'Matt', 'Michael']
    print(friends[2])
    print("Ashley" in friends) # to check if the value is in the list

    # DON'T TOUCH THIS PLEASE!
    people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]
    print(f'List prior to change: {people}')
    # Change "Hanna" to "Hannah"
    people[0] = "Hannah"
    # Change "Geoffrey" to "Jeffrey"
    people[4] = "Jeffrey"
    # Change "aparna" to "Aparna" (capitalize it)
    people[5] = people[5].capitalize()
    print(f'List after all the changes: {people}')

def iterate_list():
    pass

def list_unpack():
    #List Unpacking
    a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
    print(a)
    print(b)
    print(c)
    print(other)
    print(d)


if __name__=="__main__":
    methods()
    access_values()
    list_unpack()