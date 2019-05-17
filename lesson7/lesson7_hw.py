import random
import libs.lesson7_hw_lib as cards

kub = []
for i in range(1, 91):
    kub.append(i)

card1 = cards.get_card()
print('\nКарточка 1 игрока:')
for _ in card1:
    print(_)

card2 = cards.get_card()
print('\nКарточка 2 игрока:')
for _ in card2:
    print(_)

print(f'\nБочонки в мешке:\n{kub}')
print('=' * 50)
c1 = 15
c2 = 15
ci = 0
cb = 0
while c1 * c2 > 0:
    q = input('y - Играем дальше > ')
    if q.lower() == 'y':
        ci += 1
    else:
        cb = 1
        break

    el = random.choice(kub)
    print(f'\nХод {ci}')
    print(f'Выпал бочонок: {el}')


    for k in card1:
        for l in range(9):
            if k[l] == el:
                k[l] = '-'
                print('\nСовпадение у 1 игрока!')
                c1 -= 1
    print(f'\nКарточка 1 игрока после выпадения бочонка {el}:')
    for _ in card1:
        print(_)

    for k in card2:
        for l in range(9):
            if k[l] == el:
                k[l] = '-'
                print('\nСовпадение у 2 игрока!')
                c2 -= 1
    print(f'\nКарточка 2 игрока после выпадения бочонка {el}:')
    for _ in card2:
        print(_)

    kub.remove(el)
    print(f'\nОставшиеся бочонки:\n{kub}')
    print('=' * 50)

print(f'\nИгра завершена на {ci} ходу')
if cb == 0:
    if c1 == c2:
        print('Ничья')
    elif c1 == 0:
        print('Выиграл 1 игрок')
    elif c2 == 0:
        print('Выиграл 2 игрок')
else:
    print('Победитель не выявлен')
