def sum_of_numbers(k):
    return sum([int(i) for i in str(abs(k)) if int(i) in range(10)])

#print(sum_of_numbers(415))


#у списку групи треба виявити скільки голосних є в кожному імені
#визначити імя з найбільшою кількістю голосних
#отримати список імен впорядкований за спаданням

group = {"Hoshko" : "Sofiia",
        "Zhenchenko" : "Sasha",
        "Masnyk" : "Anastasia",
        "Protskiv" : "Nazarii",
        "Zelenko" : "Ira",
        "Ishchuk" : "Andriy",
        "Hatala" : "Olena",
        "Padalka" : "Marichka",
        "Linnik" : "Vlad",
        "Skvarko" : "Andriy"}

def count_vowels(s):
    c = 0
    for i in s:
        if i.lower() in "aoiue":
            c = c+1
    return c


def most_voweled(group):
    num_of_vowels = [count_vowels(i) for i in group.values()]
    return list(group.values())[num_of_vowels.index(max(num_of_vowels))]

def voweled_names_list(group):
    return ([i for i in group.values()])

print(most_voweled(group))
sorted_group = dict(reversed(sorted(group.items(), key=lambda x: count_vowels(x[1]))))
for i in sorted_group.values():
    print(i)