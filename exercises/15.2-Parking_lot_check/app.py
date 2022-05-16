parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(l):
    state = {'total_slots': 0, 'available_slots': 0, 'occupied_slots': 0}
    for lista in l:
        for element in lista:
            if element != 0:
                state["total_slots"] +=1
            if element == 1:
                state["occupied_slots"] +=1
            if element == 2:
                state["available_slots"] +=1
    return state

print(get_parking_lot(parking_state))




