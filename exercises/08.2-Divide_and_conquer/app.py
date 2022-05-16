list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

#Your code here:
#Your code here:
def merge_two_list(list):
    odd = []
    even = []

    for x in list:
        if x % 2 != 0:
            odd.append(x)
        else:
            even.append(x)
    mergeTwoList = []
    mergeTwoList.append(odd)
    mergeTwoList.append(even)
    return mergeTwoList
   


print(merge_two_list(list_of_numbers))
