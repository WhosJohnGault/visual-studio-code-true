#start with your program from Exercise 4-1
#(page 60) Make a copy of the list of pizzas, and call it friend_pizzas
#Then, do the following:
#• Add a new pizza to the original list
#• Add a different pizza to the list friend_pizzas
#• Prove that you have two separate lists Print the message, My favorite
#pizzas are:, and then use a for loop to print the first list Print the message,
#My friend’s favorite pizzas are:, and then use a for loop to print the second
# list Make sure each new pizza is stored in the appropriate list
my_pizza=['bacon pizza','gabby pizza','meat lovers pizza']
someones_pizza=my_pizza[:]          #using slice will ensure the lists are not 1:1 copies at all points
my_pizza.append('tuna pizza')
someones_pizza.append('salmon pizza')
print(my_pizza)
print(someones_pizza)