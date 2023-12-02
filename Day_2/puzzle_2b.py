


power_sum = 0

f = open("Day_2/day_2_input.txt", "r")
for line in f: 
    game_pieces = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    line = line[:-1]
    semicolon = line.find(':')
    id = line[5:semicolon]
    game_sets = line[semicolon+2:]
    game_sets = game_sets.replace(';','')
    game_sets = game_sets.replace(',','')
    colors = game_sets.split()
    while len(colors) > 0:
        color = colors.pop()
        count = int(colors.pop())
        if game_pieces[color] < count: game_pieces[color] = count
    print(id, game_pieces)
    power_sum += game_pieces["red"] * game_pieces["green"] * game_pieces["blue"]

print(f"The sum of power of the sets is {power_sum}")