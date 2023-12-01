import re 
sum = 0

num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
word_conversion = {}
word_conversion["one"] = 1
word_conversion["two"] = 2
word_conversion["three"] = 3
word_conversion["four"] = 4
word_conversion["five"] = 5
word_conversion["six"] = 6
word_conversion["seven"] = 7
word_conversion["eight"] = 8
word_conversion["nine"] = 9

f = open("Day_1_b/day_1_input.txt", "r")
for line in f: 
    b = len(line)
    if line[b-1] == "\n": line = line[0:b-1]
    print("line", line)
    i_dict = {}
    b = len(line)
    i = 0
    while i < b: 
        if re.match("\d", line[i]): 
            i_dict[i] = line[i]
        slice_3 = line[i:i+3]
        slice_4 = line[i:i+4]
        slice_5 = line[i:i+5]
        if num_words.count(slice_3) > 0: 
            i_dict[i] = word_conversion.get(slice_3)
        if num_words.count(slice_4) > 0: 
            i_dict[i] = word_conversion.get(slice_4)
        if num_words.count(slice_5) > 0: 
            i_dict[i] = word_conversion.get(slice_5)
        i+=1
    indeces = i_dict.keys()
    int_indeces = [int(i) for i in indeces]
    min_i = min(int_indeces)
    max_i = max(int_indeces)
    min_num = i_dict.get(min_i)
    max_num = i_dict.get(max_i)
    combined_num = int(str(min_num) + str(max_num))
    sum += combined_num

print(f"The sum is {sum}")
