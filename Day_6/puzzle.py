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
time = [int(a) for a in time if a != '']
distance = [int(a) for a in distance if a != '']
races = list(zip(time,distance))
print(races)

for race in races:
    num_ways_to_win = 0
    total_time = race[0]
    record_distance = race[1]
    speed = 0
    time = 0
    while time <= total_time: 
        time += 1
        speed += 1
        distance = (total_time - time) * speed
        if distance > record_distance: num_ways_to_win += 1
    number_of_options_per_race.append(num_ways_to_win)


print(number_of_options_per_race)

margin_of_error = reduce(lambda a,b: a*b, number_of_options_per_race)

print(f"The margin of error is {margin_of_error}")


