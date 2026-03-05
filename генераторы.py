l = [0, 1, 2, 3, 4]

"""функция генератор"""

def gen():
    i = 0
    while i < 5:
        yield i
        i += 1

res = gen()
print(l)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))

"""Выражение генератор"""
res = (i for i in l)
print(res)
for i in res:
    print(i, end=" ")
print()
#
# for i in res:
#     print(i, end=" ")
# print()

it = iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
""" Константа - неизменяемая величина характеризуемая именем, 
значением и типом этого значения """

""" Переменная - величина характеризуемая именем, 
значением и типом этого значения """

docs = [
    {'type': 'passport', 'numb': 111, 'name': 'Vasily'},
    {'type': 'passport', 'numb': 222, 'name': 'Mary'},
]

dic = {}
for d in docs:
    dic[d['numb']] = d

dic1 = {d['numb']: d for d in docs}

print(dic)
print(dic1)