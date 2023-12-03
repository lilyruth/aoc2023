import re

engine_parts = []   
symbol_coordinates = []
gears = {}
gear_ratios = []
symbols = ['*']
y = 0

def get_symbol_coordinates(): 
    y = 0
    f = open("Day_3/input.txt", "r")
    for line in f:
        r = len(line)
        x = 0
        while x < r:  
            if symbols.count(line[x]) > 0: symbol_coordinates.append([x,y])
            x+=1
        y+=1

def check_for_gears(t,x,y,working_num):
    x_min = max(0,x - (t + 1))
    x_max = x
    y_min = max(0,y-1)
    y_max = y+1
    #print('x_min', x_min, 'x_max', x_max, 'y_min', y_min, 'y_max', y_max)
    for coordinate in symbol_coordinates:
        x_flag = False
        y_flag = False
        coordinate_x = coordinate[0]
        coordinate_y = coordinate[1]
        if coordinate_x >= x_min and coordinate_x <= x_max: x_flag = True     
        if coordinate_y >= y_min and coordinate_y <= y_max: y_flag = True
        if x_flag == True and y_flag == True: 
            flattened_coordinate = str(coordinate[0]) + '_' + str(coordinate[1])
            if flattened_coordinate in gears:
                gears[flattened_coordinate].append(int(working_num))
            else:
                gears[flattened_coordinate] = [int(working_num)]


get_symbol_coordinates()

def get_number_from_line(line,y):
    r = len(line)
    x = 0
    working_num = ''
    while x < r: 
        a = line[x]
        if len(working_num) > 0 and ((a == '.' or symbols.count(a) > 0) or x == r - 1): 
            t = len(working_num)
            check_for_gears(t,x,y,working_num)
            working_num = ''
        if re.match("\d",a): working_num += a 
        x += 1


f = open("Day_3/input.txt", "r")
for line in f: 
    get_number_from_line(line,y)
    y+=1

gear_values = gears.values()
for gear_set in gear_values:
    if len(gear_set) == 2:
        gear_ratios.append(gear_set[0] * gear_set[1])

#print(gear_ratios)
print(f"The sum of the gear ratios is {sum(gear_ratios)}")


