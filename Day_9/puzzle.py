import copy
c = copy

sum_of_next_in_sequence = 0

def get_diff(data):
    for i in range(len(data)-1):
        yield data[i+1] - data[i]


f = open("Day_9/input.txt", "r")
for line in f:
    line = line.strip('\n')
    next_val = 0
    line = line.split(' ')
    line = [a.strip() for a in line]
    data = [int(a) for a in line] 
    next_val = data[-1]
    diff = list(get_diff(data))
    next_val += diff[-1]
    print(next_val)
    while diff.count(diff[0]) != len(diff): 
        data = c.deepcopy(diff)
        diff = list(get_diff(data))
        next_val += diff[-1]
    sum_of_next_in_sequence += next_val
        
print(f"The sum of historical next is {sum_of_next_in_sequence}.")

