import numpy as np

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
step_counts = []

for step in current_steps:
    step_counter = 0
    current_step = step
    #print(current_step)
    while current_step[2] != 'Z':
        i = ''
        if left_right[direction] == 'L': i = 0
        if left_right[direction] == 'R': i = 1
        current_step = nodes[current_step][i]
        #print(current_step)
        step_counter += 1
        if direction + 1 < direction_length: direction += 1
        else: direction = 0
    step_counts.append(step_counter)

#print(step_counts)
reduced_counts = np.lcm.reduce(step_counts)
print(f"It took {reduced_counts} steps to reach ZZZ.")