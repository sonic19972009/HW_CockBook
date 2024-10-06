from pprint import pprint
from glob import glob

cook_book = {}
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    for x in file:
        x = x.strip()
        if x.isdigit():
            continue
        elif x and '|' not in x:
            cook_book[x] = []
            food = x
        elif x and '|' in x:
            a, b, c = x.split(" | ")
            cook_book.get(food).append(dict(ingredient_name=a, quantity=int(b), measure=c))

pprint(cook_book)


def get_shop_list_by_foods(food_list, person_count):
    shop_list = {}
    for food in food_list:
        if food in cook_book:
            for ingredient in cook_book[food]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                        (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')
    return shop_list


pprint(get_shop_list_by_foods(['Фахитос', 'Омлет'], 2))

file_names = []

for i in glob('task3\\*.txt'):
    file_names.append(i)

file_contents = []

for filename in file_names:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_contents.append((filename, len(lines), lines))

file_contents.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_info in file_contents:
        file_name, num_lines, lines = file_info
        result_file.write(f"{file_name}\n")
        result_file.write(f"{num_lines}\n")
        for line in lines:
            result_file.write(line)
        result_file.write('\n')
