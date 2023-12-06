import math
import re 

seeds = []
global conversion
conversion = {}
current_key = ''

lowest_location = math.inf

f = open("Day_5/input.txt", "r")
input = f.readlines()
input = [item.replace('\n', '') for item in input]
input = [item.replace(':', '') for item in input]
input = [item.replace(' map', '') for item in input]
seeds = input[0]
seeds = seeds.split(' ')
seeds = seeds[1:]
seeds = [int(seed) for seed in seeds]
input = input[2:]
input = [item.split(' ') for item in input]
input = [a for a in input if a != ['']]
input.reverse()

while len(input) > 0:
    item = input.pop()
    if re.match('\d', item[0]) is None:
        current_key = item[0]
        conversion[current_key] = []
    else: 
        item = [int(a) for a in item]
        source_start = item[1]
        destination_conversion = item[0] - item[1] 
        source_end = item[1] + item[2]
        conversion[current_key].append([source_start, source_end, destination_conversion]) 
        
        
def seed_to_soil_conversion(seed): 
    soil = 0
    for item in conversion['seed-to-soil']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if seed >= source_start and seed < source_end:
            soil = seed + change
    if soil == 0: soil = seed
    return soil 

def soil_to_fertilizer_conversion(soil):
    fertilizer = 0
    for item in conversion['soil-to-fertilizer']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if soil >= source_start and soil < source_end:
            fertilizer = soil + change
    if fertilizer == 0: fertilizer = soil
    return fertilizer 

def fertilizer_to_water_conversion(fertilizer):
    water = 0
    for item in conversion['fertilizer-to-water']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if fertilizer >= source_start and fertilizer < source_end:
            water = fertilizer + change
    if water == 0: water = fertilizer
    return water 

def water_to_light_conversion(water):
    light = 0
    for item in conversion['water-to-light']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if water >= source_start and water < source_end:
            light = water + change
    if light == 0: light = water
    return light

def light_to_temperature_conversion(light):
    temp = 0
    for item in conversion['light-to-temperature']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if light >= source_start and light < source_end:
            temp = light + change
    if temp == 0: temp = light
    return temp

def temperature_to_humidity_conversion(temp):
    humidity = 0
    for item in conversion['temperature-to-humidity']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if temp >= source_start and temp < source_end:
            humidity = temp + change
    if humidity == 0: humidity = temp
    return humidity

def humidity_to_location_conversion(humidity):
    location = 0
    for item in conversion['humidity-to-location']: 
        source_start = item[0] 
        source_end = item[1]
        change = item[2]
        if humidity >= source_start and humidity < source_end:
            location = humidity + change
    if location == 0: location = humidity
    return location

print(conversion)

for seed in seeds: 
    print('seed', seed)
    soil = seed_to_soil_conversion(seed)
    print('soil', soil)
    fertilizer = soil_to_fertilizer_conversion(soil)
    print('fertilizer', fertilizer)
    water = fertilizer_to_water_conversion(fertilizer)
    print('water', water)
    light = water_to_light_conversion(water)
    print('light', light)
    temp = light_to_temperature_conversion(light)
    print('temp', temp)
    humidity = temperature_to_humidity_conversion(temp)
    print('humidity', humidity)
    location = humidity_to_location_conversion(humidity)
    print('location', location)
    if location < lowest_location: lowest_location = location

print(f"The lowest location is {lowest_location}")


