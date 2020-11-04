from functools import reduce
new_list = [x for x in range(100, 1001) if x % 2 == 0]


def multiplication(prev_el, el):
    return prev_el + el


print(reduce(multiplication, new_list))
