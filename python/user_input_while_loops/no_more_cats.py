#previously if we used remove we could only remove a single instance of something using the remove function
#while loops allow us to use the remove function to remove all instance of a thing.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)