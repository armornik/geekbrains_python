def summ_max(var_1: int, var_2: int, var_3: int):
    my_array = [var_1, var_2, var_3]
    var_min = min(my_array)
    my_array.remove(var_min)
    summ_max = sum(my_array)
    return print(summ_max)


summ_max(10, 5, 5,)
summ_max(5, 45, 49)
