total_winnings = 0

hands = []
card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1
}

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

f = open("Day_7/input.txt", "r")
for line in f:
    card_value = {}
    line = line[:-1]
    line = line.split(' ')
    bid = int(line[1])
    hand = line[0]
    value = [card_rank[a] for a in hand]
    for card in value: 
        if card in card_value: card_value[card] += 1
        else: card_value[card] = 1
    card_values = list(card_value.values())
    card_values.sort()
    card_values.reverse()
    if card_values == [1,1,1,1,1]: high_card.append([value, bid])
    elif card_values == [2,1,1,1]: one_pair.append([value, bid])
    elif card_values == [2,2,1]: two_pair.append([value, bid])
    elif card_values == [3,1,1]: three_of_a_kind.append([value, bid])
    elif card_values == [3,2]: full_house.append([value, bid])
    elif card_values == [4,1]: four_of_a_kind.append([value, bid])
    elif card_values == [5]: five_of_a_kind.append([value, bid])

five_of_a_kind.sort()
five_of_a_kind.reverse()
four_of_a_kind.sort()
four_of_a_kind.reverse()
full_house.sort()
full_house.reverse()
three_of_a_kind.sort()
three_of_a_kind.reverse()
two_pair.sort()
two_pair.reverse()
one_pair.sort()
one_pair.reverse()
high_card.sort()
high_card.reverse()

combined = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + one_pair + high_card
print(combined, len(combined))

rank = len(combined)
for hand in combined: 
    total_winnings += (rank * hand[1])
    rank -= 1


print(f"The total winnings are {total_winnings}")


