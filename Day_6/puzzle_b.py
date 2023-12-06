from functools import reduce

number_of_options_per_race = []


f = open("Day_6/input.txt", "r")
input = f.readlines()
time = input[0].split(', ')[0]
time = time[time.index(':')+1:]
distance = input[1].split(', ')[0]
distance = distance[distance.index(':')+1:]
time = time.strip('\n').strip(' ')
distance = distance.strip('\n').strip(' ')
time = time.split(' ')
distance = distance.split(' ')
time = [a for a in time if a != '']
distance = [a for a in distance if a != '']
time = ''.join([a for a in time])
distance = ''.join([a for a in distance])
time = int(time)
record_distance = int(distance)

num_ways_to_win = 0
total_time = time
speed = 0
time = 0
while time <= total_time: 
    time += 1
    speed += 1
    distance = (total_time - time) * speed
    if distance > record_distance: num_ways_to_win += 1

print(num_ways_to_win)

print(f"The margin of error is {num_ways_to_win}")


