#this is a more complicated program involving modifying aliens values 
alien_0= {'x_position': 0, 'y_position':25, 'speed':'medium'}
print("Original x-position "+ str(alien_0['x_position']))

#now we move the alien to the right
#determine how far the alien based on its current speed.
if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment=1
else: 
    # This must be a fast alien.
    x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position'] =alien_0['x_position'] + x_increment

print("New x-position: " +str(alien_0['x_position']))