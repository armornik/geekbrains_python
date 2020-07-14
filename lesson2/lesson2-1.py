type_data: tuple = ((1, 2,), [1, 2], 1, "2", True, iter([1, 2]), {'1': 4, '2': 3, }, {1, 2, 3}, print, frozenset('12'),
                    frozenset, b'123', bytearray(b'2'), None,)
for i in type_data:
    print(type(i))
