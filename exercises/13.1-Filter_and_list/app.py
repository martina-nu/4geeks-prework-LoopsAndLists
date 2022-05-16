
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def my_function(item):
    return item.startswith("R")

resulting_names = list(filter(my_function, all_names))
print(resulting_names)




