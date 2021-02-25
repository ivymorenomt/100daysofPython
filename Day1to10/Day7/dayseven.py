#Random edabit issues
def animals(chickens, cows, pigs):
    chickens = chickens * 2
    cows = cows * 4
    pigs = pigs * 4
    print(chickens + cows + pigs)
    return chickens + cows + pigs

animals(5,2,8)

def get_middle(string):
        if len(string) % 2 == 0:
           print(string[len(string) // 2 - 1] + string[len(string) // 2])
        else:
           print(string[len(string) // 2])

get_middle("A")

def bool_to_word(bool):
    if bool:
        print('Yes')
    else:
        print('No')

bool_to_word(True)
