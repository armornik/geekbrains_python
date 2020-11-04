my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[x+1] for x in range(len(my_list) - 1) if my_list[x+1] > my_list[x]]
print(new_list)