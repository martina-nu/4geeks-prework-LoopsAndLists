all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(lista):
	filtered = list(filter(lambda col: col["sexy"] == True, lista))
	return(filtered)

colores_filtrados = filter_colors(all_colors)

def generate_li(lst):
    name_list = list(map(lambda col: "<li>" + col["label"] + "</li>", lst))
    print(name_list)
    
generate_li(colores_filtrados)
