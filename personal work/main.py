#1.1


def func_speed(v0, a, ht):
    T = int(-v0/a)
    speed = [v0 + a*x for x in range(0, T, ht)]
    length = [v0*x + ((a*(x**2))/2)*x for x in range(0, T, ht)]

    print("v(t)         s(t)")
    for i in range(len(speed)):
        print(speed[i], "          ", length[i])

func_speed(3, -1, 1)


#1.2

#1
sl = {"mat1" : 2, "mat2" : 3, "mat4" : 4, "mat5" : 5, "mat6" : 6, "mat7" : 7}

def the_heaviest(lst):
    return list(dict(sorted(lst.items(), key=lambda x: -x[1])))[0]
print(the_heaviest(sl))



#2
lst = [{"mat1" : 2, "mat2" : 3, "mat4" : 4},
       {"mat5" : 5, "mat6" : 6, "mat7" : 7},
       {"mat8" : 8, "mat9" : 9, "mat10" : 10}]

def the_heaviest_per_day(lst):
    return [the_heaviest(x) for x in lst]
print(the_heaviest_per_day(lst))


#3
lst = [{"mat1" : 2, "mat2" : 3, "mat4" : 4},
       {"mat1" : 5, "mat3" : 6, "mat2" : 7},
       {"mat1" : 8, "mat8" : 9, "mat4" : 10}]

def the_heaviest_sum(lst):
    to_return = {}
    for i in lst:
        for j in i.keys():
            if j in to_return.keys():
                to_return[j] += i[j]
            else:
                to_return[j] = i[j]
    return to_return


print(the_heaviest_sum(lst))







