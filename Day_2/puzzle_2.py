
game_pieces = {
    "red": 12,
    "green":13,
    "blue": 14
}

id_sum = 0

f = open("Day_2/day_2_input.txt", "r")
for line in f: 
    line = line[:-1]
    possible = True
    semicolon = line.find(':')
    id = line[5:semicolon]
    game_sets = line[semicolon+2:]
    game_sets = game_sets.replace(';','')
    game_sets = game_sets.replace(',','')
    colors = game_sets.split()
    while len(colors) > 0:
        color = colors.pop()
        count = int(colors.pop())
        if game_pieces[color] < count: possible = False

    if possible: id_sum += int(id)

print(f"The sum of possible game ids is {id_sum}")