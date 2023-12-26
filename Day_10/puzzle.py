start_flag = False
pipe_coordinates = []
visited = []
compatible_pipes = {
    '|_north': ['F','7','|','S'],  
    '|_south': ['L', 'J','|','S'],
    'L_north': ['|', 'F', '7','S'],
    'L_east': ['-', 'J', '7','S'],
    'F_south': ['|', 'J','L','S'],
    'F_east': ['-','7','J','S'],
    '7_south': ['L', 'J','|','S'],
    '7_west': ['F', '-','L','S'],
    'J_north': ['F','7','|','S'],
    'J_west': ['F', '-','L','S'],
    '-_east': ['-','7','J','S'],
    '-_west': ['F', '-','L','S'],
    'S_north': ['F','|','7'],
    'S_south': ['|','J','L'],
    'S_east': ['-','7','J'],
    'S_west': ['-','F','L']
}


f = open("Day_10/sample_input.txt", "r")
for line in f:
    line = line.strip('\n')
    x = []
    for char in line: 
        x.append(char)
    pipe_coordinates.append(x)

print(pipe_coordinates) 
start_y = ''
start_x = ''

for y in range(0,len(pipe_coordinates)):
    for x in range(0,len(pipe_coordinates[y])):
        if pipe_coordinates[y][x] == 'S':
            start_y = y
            start_x = x 

print(start_y, start_x)


def get_east(pipe,y,x):
    east = x + 1
    east_pipe = pipe_coordinates[y][east]
    pipe_direction = pipe + '_east'
    if pipe_direction in compatible_pipes and east_pipe in compatible_pipes[pipe_direction] and [y,east] not in visited: 
        new_x = east
        new_y = y
        return [new_y,new_x]
    else: return None


def get_west(pipe,y,x):
    west = x - 1
    west_pipe = pipe_coordinates[y][west]
    pipe_direction = pipe + '_west'
    if pipe_direction in compatible_pipes and west_pipe in compatible_pipes[pipe_direction] and [y,west] not in visited:
        new_x = west 
        new_y = y 
        return [new_y,new_x]
    else: return None


def get_south(pipe,y,x):
    south = y + 1
    south_pipe = pipe_coordinates[south][x]
    pipe_direction = pipe + '_south'
    if pipe_direction in compatible_pipes and  south_pipe in compatible_pipes[pipe_direction] and [south,x] not in visited:
        new_x = x
        new_y = south 
        return [new_y,new_x]
    else: return None


def get_north(pipe,y,x):
    north = y - 1
    north_pipe = pipe_coordinates[north][x]
    pipe_direction = pipe + '_north'
    if pipe_direction in compatible_pipes and  north_pipe in compatible_pipes[pipe_direction] and [north,x] not in visited:
        new_x = x
        new_y = north 
        return [new_y,new_x]
    else: return None


def next_move(y,x):
    pipe = pipe_coordinates[y][x]
    new_x = ''
    new_y = ''

    if y == 0:
        if x == 0:
            new_set_east = get_east(pipe,y,x)
            new_set_south = get_south(pipe,y,x)   
            if new_set_east is not None: 
                return new_set_east 
            else: return new_set_south                    
        elif x == len(pipe_coordinates[y]) - 1:
            new_set_south = get_south(pipe,y,x)
            new_set_west = get_west(pipe,y,x)
            if new_set_south is not None: return new_set_south
            else: return new_set_west 
        else:
            new_set_east = get_east(pipe,y,x)
            new_set_south = get_south(pipe,y,x)
            new_set_west = get_west(pipe,y,x)
            result_list = [new_set_east,new_set_south,new_set_west]
            for item in result_list: 
                if item is not None: return item 
    
    elif y == len(pipe_coordinates) - 1:
        if x == 0:
            new_set_east = get_east(pipe,y,x)
            new_set_north = get_north(pipe,y,x)
            if new_set_east is not None: return new_set_east
            else: return new_set_north 
        elif x == len(pipe_coordinates[y]) - 1:
            new_set_west = get_west(pipe,y,x)
            new_set_north = get_north(pipe,y,x)
            if new_set_west is not None: return new_set_west 
            else: return new_set_north 
        else:
            new_set_east = get_east(pipe,y,x)
            new_set_north = get_north(pipe,y,x)
            new_set_west = get_west(pipe,y,x)
            result_list = [new_set_east,new_set_north,new_set_west]
            for item in result_list: 
                if item is not None: return item
    else: 
        if x == 0:
            new_set_east = get_east(pipe,y,x)
            new_set_north = get_north(pipe,y,x)
            new_set_south = get_south(pipe,y,x)
            result_list = [new_set_east,new_set_north,new_set_south]
            for item in result_list: 
                if item is not None: return item

        elif x == len(pipe_coordinates[y]) - 1:
            new_set_west = get_west(pipe,y,x)
            new_set_north = get_north(pipe,y,x)
            new_set_south = get_south(pipe,y,x)
            result_list = [new_set_west,new_set_north,new_set_south]
            for item in result_list: 
                if item is not None: return item

        else:
            new_set_east = get_east(pipe,y,x)
            new_set_west = get_west(pipe,y,x)
            new_set_north = get_north(pipe,y,x)
            new_set_south = get_south(pipe,y,x)
            result_list = [new_set_east,new_set_west,new_set_north,new_set_south]
            for item in result_list: 
                if item is not None: return item

count = 0
y = start_y
x = start_x 
visited.append([y,x])
new_set = [y,x]
while count < 2: 
    print('y', y, 'x', x, 'pipe', pipe_coordinates[y][x])
    new_set = next_move(y,x)
    y = new_set[0]
    x = new_set[1]
    visited.append([y,x])
    print('y', y, 'x', x, 'pipe', pipe_coordinates[y][x], 'visited', visited)
    count += 1
start_coordinates = visited[0]
visited = visited[1:]
while new_set != start_coordinates:
    #print('y', y, 'x', x, 'pipe', pipe_coordinates[y][x])
    new_set = next_move(y,x)
    y = new_set[0]
    x = new_set[1]
    visited.append([y,x])
    #print('y', y, 'x', x, 'pipe', pipe_coordinates[y][x], 'visited', visited)
    count += 1
print(visited)
print(f"The count is {round(count/2)}")






    