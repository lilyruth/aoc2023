
num_matches_per_card = {}
copies = {}

f = open("Day_4/input.txt", "r")
for line in f: 
    matches = 0
    card = 0
    line = line[:-1]
    c = line.index(':')
    d = line.index('d')
    card_number = line[d+2:c]
    card_number = card_number.replace(' ','')
    line = line[c+1:]
    line = line.split('|')
    winning_numbers = line[0]
    winning_numbers = winning_numbers.strip()
    elf_numbers = line[1]
    elf_numbers = elf_numbers.strip()
    winning_numbers = winning_numbers.split(' ')
    winning_numbers = [a for a in winning_numbers if a != '']
    elf_numbers = elf_numbers.split(' ')
    elf_numbers = [a for a in elf_numbers if a != '']
    winning_num_int = [int(a) for a in winning_numbers]
    elf_num_int = [int(a) for a in elf_numbers]
    for num in winning_num_int: 
        if elf_num_int.count(num) > 0: 
            matches += 1
    num_matches_per_card[card_number] = matches

card_number = num_matches_per_card.keys()
for card in card_number: 
    copies[int(card)] = 1

for card in card_number:
    matches = num_matches_per_card[card]
    if matches > 0:
        addons = copies[int(card)]
        count = 1
        while count <= matches:
            copies[int(card) + count] = copies[int(card) + count] + addons
            count += 1
            print(copies)




print(f"The total number of cards is {sum(copies.values())}")


