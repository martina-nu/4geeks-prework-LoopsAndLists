#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:


def add_num():
    for x in range(10):
        num = random.randint(1,100)
        my_list.append(num)
    return my_list
    

print(add_num())


