my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:

new_list = []



for x in my_list:
    if type(x) == dict or type(x) == list:
        new_list.append(x)
    
print(new_list)


