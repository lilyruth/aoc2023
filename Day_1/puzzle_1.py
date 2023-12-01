import re 
sum = 0

f = open("Day_1/day_1_input.txt", "r")
for line in f: 
    nums = []
    for a in line:
        if a != "\n" : 
            if re.match("\d", a): nums.append(a)

    first_num = nums[0]
    last_num = nums.pop()
    combined_num = int(first_num + last_num)
    sum += combined_num

print(f"The sum is {sum}")