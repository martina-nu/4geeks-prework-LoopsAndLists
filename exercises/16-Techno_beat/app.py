
def lyrics_generator(lista):
    one_counter = 0
    new_lista= []
    
    for x in lista:
        
        if x == 1:
            one_counter += 1
            new_lista.append("Drop the base ")
        elif x == 0:
             one_counter  = 0
             new_lista.append("Boom ")
        if one_counter == 3:
            new_lista.append("!!!Break the base!!! ")
            one_counter  = 0
            
    song ="".join([str(item) for item in new_lista])
    return song
    
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))