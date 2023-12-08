direction = 0
step_counter = 0
current_steps = []

nodes = {}

f = open("Day_8/input.txt", "r")
input = f.readlines()
left_right = input[0].strip('\n')
direction_length = len(left_right)
input = input[2:]
for line in input:
    nodes[line[0:3]] = [line[7:10],line[12:15]]

potential_starting_steps = list(nodes.keys())
current_steps = [a for a in potential_starting_steps if a[2] == 'A']
z_flag = False

def get_step(step):
    i = ''
    if left_right[direction] == 'L': i = 0
    if left_right[direction] == 'R': i = 1
    step = nodes[step][i]
    return step

while z_flag is False:
    current_steps = [get_step(a) for a in current_steps]
    step_counter += 1
    if direction + 1 < direction_length: direction += 1
    else: direction = 0  
    z_flag = True
    #print(current_steps)
    for a in current_steps:
        if a[2] != 'Z': z_flag = False

print(f"It took {step_counter} steps to reach ZZZ.")