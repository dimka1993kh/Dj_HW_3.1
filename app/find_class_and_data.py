def find_class_and_data(cell):
    if cell == "":
        cell = "-"
        cell_style = ''

    elif float(cell) < 0:
        cell_style = 'green'
    elif cell == "":
        cell = "-"
        cell_style = ''
    elif 1 > float(cell) >= 0:
        cell_style = 'white'
    elif 2 > float(cell) >= 1:
        cell_style = '#CD5C5C'
    elif 5 > float(cell) >= 2:
        cell_style = '#9B2D30'
    elif float(cell) >= 5:
        cell_style = '900020'
    
    return {
        'cell': cell,
        'style' : cell_style
        }