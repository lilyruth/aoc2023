
direction = 0
step_counter = 0
current_step = 'AAA'

nodes = {}

f = open("Day_8/input.txt", "r")
input = f.readlines()
left_right = input[0].strip('\n')
direction_length = len(left_right)
input = input[2:]
for line in input:
    nodes[line[0:3]] = [line[7:10],line[12:15]]

while current_step != 'ZZZ':
    i = ''
    if left_right[direction] == 'L': i = 0
    if left_right[direction] == 'R': i = 1
    current_step = nodes[current_step][i]
    step_counter += 1
    if direction + 1 < direction_length: direction += 1
    else: direction = 0

print(f"It took {step_counter} steps to reach ZZZ.")

