#starts and end with consonant
def consonant(lst):
    vowels = "aoiue"
    res = []
    for i in lst:
        while i[0].lower() in vowels:
            i = i[1:]
        while i[-1].lower() in vowels:
            i = i[:-1]
        res.append(i)
    res.sort(key=lambda x: -len(x))
    return res

print(consonant([['o', 'w', 'r', 'e', 'I', 'f', 'h', 'o', 'r'], ['e', 'g', 'h', 'd', 'f', 'g', 'h', 'd', 'f', 'g', 'o'],
                 ['f', 'd', 'g', 'h', 'd', 'f', 'g', 'h', 'd'], ['f', 'g', 'h', 'f', 'u']]))
print(consonant(["owreifhor", "eghdfghdfgo", "fdghdfghd", "fghfu"]))



def longest_vowel_consonant_queue(lst):
    vowels = "aoiue"
    res = []
    for i in lst:
        was_vowel = False

        prev_ch = i[0]
        helpstr = ""
        helpstr += prev_ch
        result_lst = []
        for j in range(1, len(i)):
            if prev_ch in vowels:
                was_vowel = True
            else:
                was_vowel = False

            if (i[j] in vowels and not was_vowel) or (i[j] not in vowels and was_vowel):
                helpstr += i[j]
            else:
                result_lst.append(helpstr)
                helpstr = i[j]
            prev_ch = i[j]

            if j == len(i) - 1:
                result_lst.append(helpstr)

        res.append(sorted(result_lst, key=lambda x: -len(x))[0])

    return sorted([list(i) for i in res], key=lambda x: -len(x))

#print(longest_vowel_consonant_queue(["owereifhor", "eghdfghdfgo", "fgutututututututuhfu", "fdghdfghd"]))










# list1 = ["a", "s", "a", "d", "o", "f"]
# list2 = ["h", "d", "g", "s", "t"]
# list3 = ["e", "g", "d", "y", "t", "i", "u"]
# list4 = ["d", "f", "h", "g", "d"]
# list5 = ["a", "f", "a"]
# list6 = ["s", "d", "l", "i", "h", "v", "s", "u", "g", "f", "p"]
# list7 = ["f", "a", "n", "i", "f", "y"]
#
# list_of_lists = [list1, list2, list3, list4, list5, list6, list7]
#
# def Algorithm(list):
#     new_list = []
#     for i in range(len(list)):
#         counter = 0
#
#         if list[i][0].lower() not in "aeiouy" and list[i][-1].lower() not in "aeiouy":
#             new_list.append(list[i])
#
#         for j in range(len(list[i]) - 1):
#             if (list[i][j].lower() not in "aeiouy" and list[i][j+1].lower() in "aeiouy") or (list[i][j].lower() in "aeiouy" and list[i][j+1].lower() not in "aeiouy"):
#                counter += 1
#
#         if len(list[i]) == counter:
#             new_list.append(list[i])
#     return new_list
#
# print(Algorithm(list_of_lists))