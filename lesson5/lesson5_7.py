import json

try:
    with open('company_5_7.txt', 'r') as f:
        company_info = {}
        for line in f:
            name_company, form, profit, cost = line.split()
            try:
                profit = int(profit)
                cost = int(cost)
            except ValueError:
                print('Ошибка данных - должны быть числа')
            else:
                proceeds = profit - cost
                company_info[name_company] = proceeds
    print(f': {company_info}')
    profit_making_firm = [value for value in company_info.values() if value > 0]
    average_profit = {"average_profit": round(sum(profit_making_firm) / len(profit_making_firm), 2)}
    print(average_profit)
    data_for_file = [company_info, average_profit]
    with open("my_file.json", "w") as write_f:
        json.dump(data_for_file, write_f, ensure_ascii=False)
        # json.dump(average_profit, write_f)
except IOError:
    print('Ошибка ввода-вывода')

