arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdd(items):
    total = 0
    for x in items:
        if x%2 != 0:
            total+= x
    print (total)


sumOdd(arr)


