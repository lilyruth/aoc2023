import copy
c = copy
total_winnings = 0

hands = []
card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
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
    num_jokers = value.count(1)
    if num_jokers != 5: 
        removing_joker_card_value = c.deepcopy(card_value)
        if 1 in removing_joker_card_value: del removing_joker_card_value[1]
        print('card_value', card_value, 'removing_joker_card_value', removing_joker_card_value)
        subbed_values = list(removing_joker_card_value.values())
        subbed_values.sort()
        subbed_values.reverse()
        max_value = subbed_values[0]
        next_value = ''
        if len(subbed_values) > 1: next_value = subbed_values[1]
        joker_sub_1 = ''
        joker_sub_2 = ''
        for key in removing_joker_card_value: 
            if removing_joker_card_value[key] == max_value: joker_sub_1 = key
            if removing_joker_card_value[key] == next_value: joker_sub_2 = key
        while num_jokers > 0:
            if removing_joker_card_value[joker_sub_1] < 5: removing_joker_card_value[joker_sub_1] += 1
            else: 
                removing_joker_card_value[joker_sub_2] += 1
            num_jokers -= 1
        final_tally = list(removing_joker_card_value.values())
        final_tally.sort()
        final_tally.reverse()
        if final_tally == [1,1,1,1,1]: high_card.append([value, bid])
        elif final_tally == [2,1,1,1]: one_pair.append([value, bid])
        elif final_tally == [2,2,1]: two_pair.append([value, bid])
        elif final_tally == [3,1,1]: three_of_a_kind.append([value, bid])
        elif final_tally == [3,2]: full_house.append([value, bid])
        elif final_tally == [4,1]: four_of_a_kind.append([value, bid])
        elif final_tally == [5]: five_of_a_kind.append([value, bid])
    else: 
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


