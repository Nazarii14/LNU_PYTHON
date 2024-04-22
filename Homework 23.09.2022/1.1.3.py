group = {"Hoshko" : (1, 2, 3, 4, 5),
        "Zhenchenko" : (1, 3, 3, 7, 5),
        "Masnyk" : (1, 12, 3, 0, 5),
        "Protskiv" : (1, 23, 3, 1, 5),
        "Zelenko" : (1, 2, 3, 67, 5),
        "Ishchuk" : (1, 45, 3, 6, 5),
        "Hatala" : (1, 2, 3, 4, 5),
        "Padalka" : (1, 2, 3, 4, 5),
        "Linnik" : (1, 2, 3, 4, 5),
        "Skvarko" : (1, 2, 3, 4, 5)}


def sum_of_even_indexes(group):
    to_return = [sum(i[1::2]) for i in group.values()]
    surnames = [x for x in group.keys()]
    return dict(sorted({surnames[i]:to_return[i] for i in range(len(to_return))}.items(), key=lambda x: -x[1]))

print(sum_of_even_indexes(group))