import random


def get_card():
    base_list = []
    for i in range(1, 91):
        base_list.append(i)
    card = [[], [], []]
    p = [_ for _ in range(9)]
    for _ in card:
        for i in range(9):
            elem = random.choice(base_list)
            _.append(elem)
            base_list.remove(elem)
        _.sort()
    for _ in card:
        ind = random.sample(p, 4)
        for i in range(9):
            if i in ind:
                _[i] = ' '
    base_list = []
    return card
