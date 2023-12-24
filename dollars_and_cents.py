import random


def four_number():
    row = set()
    while len(row) <= 4:
        if len(row) == 4:
            row = tuple(row)
            break
        else:
            row.add(random.randint(0, 9))
    return row


print('\
------------------ ДОЛЛАРЫ И ЦЕНТЫ ------------------\n\
Правила игры:\n\
Компьютер загадывает комбинацию из четырех неповторяющихся цифр\n\
(комбинация может начинаться с 0). Ваша задача, перебрав аналогичные комбинации\n\
(четырехзначные из неповторяющихся цифр), угадать загаданную компьютером.\n\n\
На каждую Вашу комбинацию компьютер дает следующий ответ:\n\
 - если в Вашей комбинации есть загаданная цифра: 1 cent,\n\
 - если эта цифра стоит на нужном месте: 1 doll.\n\n\
Например:\n\
1730 - комбинация компьютера\n\
----------------------------\n\
0352 - Ваша комбинация\n\
      ответ: 0 doll, 2 cent (есть цифры 0 и 3, но не на своих местах)\n\
0749 - Ваша следующая комбинация\n\
      ответ: 1 doll, 1 cent (цифра 7 стоит на своем месте, цифра 0 присутствует)\n\
2954 - Ваша следующая комбинация\n\
    ответ: 0 doll, 0 cent (таких цифр нет в комбинации компьютера)\n\
1730 - Ваша следующая комбинация\n\
      ответ: 4 doll, 0 cent (все цифры на своих местах - Вы угадали!)\n\
-----------------------------------------------------')

quest = four_number()

print(quest)

ans = None
count = 0
while ans != quest:
    ans = []
    while len(ans) <= 4:
        print('Введите комбинацию из четырех неповторяющихся цифр:')
        combination = list(input())
        ans = [int(i) for i in combination]
        ans_unique_elements = set(ans)
        if (len(ans) != 4) or (len(ans_unique_elements) != 4):
            ans.clear()
            print('четыре неповторяющихся цифры!'.upper())
        else:
            ans = tuple(ans)
            break

    doll = 0
    cent = 0
    count += 1

    for i in ans:
        if (i in quest) and (ans.index(i) == quest.index(i)):
            doll += 1
        elif i in quest:
            cent += 1
    if doll != 4:
        print(f'{doll} doll., {cent} cent')

hidden_comb = ''
for i, v in enumerate(quest):
    hidden_comb += str(v)
    if i != 3:
        hidden_comb += ' '

# print('============================')
print('{:=^28}'.format('='))
print('|{: ^26}|'.format('Hidden combination:'))
print('|{: ^26}|'.format(hidden_comb))
print('|{: ^26}|'.format('4 dollars! You won').upper())
print('|{: ^26}|'.format(f'in {count} steps'))
print('{:=^28}'.format(''))
