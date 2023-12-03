import re

engine_parts = []   
symbol_coordinates = []
symbols = ['*', '@', '#', '-', '=', '/', '+', '%', '$', '&']
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

def check_for_adjacent_symbols(t,x,y):
    #print(t,x,y)
    add_to_sum_flag = False
    x_min = max(0,x - (t + 1))
    x_max = x
    y_min = max(0,y-1)
    y_max = y+1
    #print('x_min', x_min, 'x_max', x_max, 'y_min', y_min, 'y_max', y_max)
    symbol_flag = False
    for coordinate in symbol_coordinates:
        x_flag = False
        y_flag = False
        coordinate_x = coordinate[0]
        coordinate_y = coordinate[1]
        #print('coordinate_x',coordinate_x,'coordinate_y',coordinate_y)
        if coordinate_x >= x_min and coordinate_x <= x_max: x_flag = True     
        if coordinate_y >= y_min and coordinate_y <= y_max: y_flag = True
        #print('x_flag', x_flag, 'y_flag', y_flag)
        if x_flag == True and y_flag == True: symbol_flag = True
    return symbol_flag        


get_symbol_coordinates()
#print(symbol_coordinates)

def get_number_from_line(line,y):
    r = len(line)
    x = 0
    working_num = ''
    while x < r: 
        a = line[x]
        if len(working_num) > 0 and ((a == '.' or symbols.count(a) > 0) or x == r - 1): 
            t = len(working_num)
            if check_for_adjacent_symbols(t,x,y) == True:
                num = int(working_num)
                engine_parts.append(num)
            working_num = ''
        if re.match("\d",a): working_num += a 
        x += 1


f = open("Day_3/input.txt", "r")
for line in f: 
    get_number_from_line(line,y)
    y+=1

#print(engine_parts)
print(f"The sum of all the part numbers is {sum(engine_parts)}")

