number_of_goods: int = int(input('Введите количество товаров: '))
list_of_goods = []
for i in range(number_of_goods):
    product_characteristics: list = input(f'Введите характеристику {i + 1} товара (название-цена-кол-во-ед): ').split()
    product_characteristics: list = [product_characteristics[0], int(product_characteristics[1]), int(
        product_characteristics[2]), product_characteristics[3]]
    # print((product_characteristics))
    list_of_goods.append((i + 1, {'название': product_characteristics[0], 'цена': product_characteristics[1],
                                  'количество': product_characteristics[2], 'eд': product_characteristics[3]}))
print(f'Структура данных "Товары": {list_of_goods}')
received_analytics = {'название': [], 'цена': [], 'количество': [], 'ед': [], }
for i in range(number_of_goods):
    received_analytics['название'] += [list_of_goods[i][1]['название']]
    received_analytics['цена'] += [list_of_goods[i][1]['цена']]
    received_analytics['количество'] += [list_of_goods[i][1]['количество']]
    # print(list_of_goods[i][1]['eд'])
    # print(received_analytics['ед'])
    if list_of_goods[i][1]['eд'] not in received_analytics['ед']:
        received_analytics['ед'] += [list_of_goods[i][1]['eд']]
print('Аналитика данных:')
# print(received_analytics)
for i in received_analytics:
    print(received_analytics[i])
