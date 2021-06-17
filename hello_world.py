print("Hello World!")
name = 'Kathryn'
print('Hello,',name)
print('Hello,'+ name)
name = '322'
print('Hello,',name,'!')
# print('Hello,',name+'!') <-- This one gives an error. Probably because name is an integer.
print('Hello,',name+'!')
# Line above runs fine if I make the integer a string.
fav_food1 = 'sushi'
fav_food2 = 'pizza'
print('I love to eat {} and {}.'.format(fav_food1,fav_food2))
print(f'I love to eat {fav_food1} and {fav_food2}.')
k = 'There are an awful lot of cows here.'
print(k.upper())
print(k.count('o'))
