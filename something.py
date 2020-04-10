import random
options = ['камень','ножницы','бумага']
for i in options:
    print(i,end = ' ')
chose = input('. Что выбираем?:').lower()
enemy_chose = random.choice(options)
if enemy_chose == chose:
    print('Противник выбрал', enemy_chose,',ничья')


elif enemy_chose == 'камень' and chose == 'ножницы':
    print('Противник выбрал камень,вы проиграли')


elif enemy_chose == 'камень' and chose == 'бумага':
    print('Противник выбрал камень,вы выиграли')


elif enemy_chose == 'ножницы' and chose == 'камень':
    print('противник выбрал ножницы,вы выиграли')


elif enemy_chose == 'ножницы' and chose == 'бумага':
    print('Противник выбрал ножницы,вы проиграли')


elif enemy_chose == 'бумага' and chose == 'камень':
    print("противник выбрал бумагу,вы проиграли")

elif enemy_chose == 'бумага' and chose == "ножницы":
    print('противник выбрал бумагу,вы выиграли')
