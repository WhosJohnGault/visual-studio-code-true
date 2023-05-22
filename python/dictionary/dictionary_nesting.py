#we can create dictionaries for a few aliens and store those dictionaries in a list then loop through the list to print them just like we can expect when the invasion happens

alien_0={'color': 'green', 'points': 5}
alien_1={'color': 'yellow', 'points': 10}
alien_2={'color': 'red', 'points': 15}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)