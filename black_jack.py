import random


def give_card(hand):
    index = random.choice(card_numbers)     # Выбираем случайный номер карты
    card = card_deck.pop(index)				  # По выбранному номеру выбираем карту
    card_numbers.remove(index)              # Удаляем из колоды выбранную карту
    hand.append(card)
    count = sum([card[1] for card in hand])
    return count


def show_cards(hand, points):
    who = ''
    if hand == my_hand:
        who = 'Мои'
    elif hand == comp_hand:
        who = 'Его'
    print(who, 'карты:', end=' ')
    for card in hand[1:]:
        print('[{}]'.format(card[0]), end=' ')
    print('\b. Очки: {}'.format(points))


def check_point(player, computer):
    if computer > player:
        print('Я проиграл!')
    elif computer < player:
        print('Я победил!')
    else:

        print('Ничья...')


card_deck = {
    # пики
    1: ('\u2660_A', 11), 2: ('\u2660_J', 10), 3: ('\u2660_Q', 10), 4: ('\u2660_K', 10),
    5: ('\u2660_2', 2), 6: ('\u2660_3', 3), 7: ('\u2660_4', 4), 8: ('\u2660_5', 5), 9: ('\u2660_6', 6),
    10: ('\u2660_7', 7), 11: ('\u2660_8', 8), 12: ('\u2660_9', 9), 13: ('\u2660_10', 10),

    # трефы
    14: ('\u2663_A', 11), 15: ('\u2663_J', 10), 16: ('\u2663_Q', 10), 17: ('\u2663_K', 10),
    18: ('\u2663_2', 2), 19: ('\u2663_3', 3), 20: ('\u2663_4', 4), 21: ('\u2663_5', 5), 22: ('\u2663_6', 6),
    23: ('\u2663_7', 7), 24: ('\u2663_8', 8), 25: ('\u2663_9', 9), 26: ('\u2663_10', 10),

    # червы
    27: ('\u2665_A', 11), 28: ('\u2665_J', 10), 29: ('\u2665_Q', 10), 30: ('\u2665_K', 10),
    31: ('\u2665_2', 2), 32: ('\u2665_3', 3), 33: ('\u2665_4', 4), 34: ('\u2665_5', 5), 35: ('\u2665_6', 6),
    36: ('\u2665_7', 7), 37: ('\u2665_8', 8), 38: ('\u2665_9', 9), 39: ('\u2665_10', 10),

    # бубны
    40: ('\u2666_A', 11), 41: ('\u2666_J', 10), 42: ('\u2666_Q', 10), 43: ('\u2666_K', 10),
    44: ('\u2666_2', 2), 45: ('\u2666_3', 3), 46: ('\u2666_4', 4), 47: ('\u2666_5', 5), 48: ('\u2666_6', 6),
    49: ('\u2666_7', 7), 50: ('\u2666_8', 8), 51: ('\u2666_9', 9), 52: ('\u2666_10', 10),
}

card_numbers = list(range(1, len(card_deck) + 1))
my_hand = [('none', 0)]     # Список карт игрока
comp_hand = [('none', 0)]   # Список карт компьютера

# Первая сдача карт:
my_points = give_card(my_hand)
show_cards(my_hand, my_points)
comp_points = give_card(comp_hand)


# Сдача карт игроку:
stop = False
while True:
    print('--------------------------')
    answer = input('Ещё карту? (y/n): ')
    if answer == 'y':
        my_points = give_card(my_hand)
        show_cards(my_hand, my_points)
        if my_points == 21:
            break
        if my_points > 21:
            print('Перебор. Я проиграл!')
            stop = True
            break
    elif answer == 'n':
        break
    else:
        print('Не понял...')


# Сдача карт компьютеру:
while not stop:
    if comp_points <= 19:
        comp_points = give_card(comp_hand)
    elif 20 <= comp_points <= 21:
        show_cards(comp_hand, comp_points)
        check_point(my_points, comp_points)
        stop = True
    elif comp_points > 21:
        show_cards(comp_hand, comp_points)
        print('У него перебор. Я победил!')
        stop = True
