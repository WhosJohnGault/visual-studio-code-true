#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
their_food=my_foods[:]
print(my_foods)
print(their_food)
not_this=their_food.pop(1)
print(not_this)
this='falafel'
print(their_food)
their_food.append(not_this)
print(their_food)




