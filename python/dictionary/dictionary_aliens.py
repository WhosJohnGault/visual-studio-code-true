alien_0 = {'color' : 'green' , 'points' : 5 }

print(alien_0['color'])
print(alien_0['points'])
#we could make a simple game describing the number of points someone would get
# for shooting aliens
new_points = alien_0['points']
print("you just earned " + str(new_points) + " points!")
#now we can add new key value pairs for the aliens coordinates
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#we can modify our initial dictionary
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}

