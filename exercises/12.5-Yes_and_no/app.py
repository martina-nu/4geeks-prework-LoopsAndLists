theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def wikiwoko(items):
    if items == 0:
        return "woko"
    elif items == 1:
        return "wiki"

new_list = list(map(wikiwoko, theBools))
print(new_list)

