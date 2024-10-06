from pprint import pprint

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