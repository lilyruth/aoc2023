points = 0

f = open("Day_4/input.txt", "r")
for line in f: 
    card = 0
    line = line[:-1]
    c = line.index(':')
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
    #print(winning_num_int)
    #print(elf_num_int)
    for num in winning_num_int: 
        if elf_num_int.count(num) > 0: 
            if card == 0: card = 1
            else: card = card * 2
    print(card)
    points += card


print(f"The sum of all the points is {points}")


