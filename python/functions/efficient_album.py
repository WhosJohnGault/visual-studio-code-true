# Write a function called make_album() that builds a dictionary
# describing a music album The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information Use the function to make three dictionaries representing different
# albums Print each return value to show that the dictionaries are storing the
# album information correctly
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album If the calling line includes a value for the num-
# ber of tracks, add that value to the album’s dictionary Make at least one new
# function call that includes the number of tracks on an album

#To do:
#Create a while loop so users can input the name of an artist and an album
#while the loop condition is true have a function be called
#prompt the user to enter an artist name and an album 
#prompt the user if they want to enter the number of songs on the album, if they enter 'n' skip
#

prompt="\nPlease enter the name of an artist you enjoy:"
prompt+="\nEnter quit if you don't wish to enter another entry"

prompt2="\nPlease enter the name of an album by" + artist_name + "you enjoy:"
prompt3="If you wish you can enter "
while True:
    def make_album(artist_name,album_name,songs):
    """return a dictionary about an artist and a music album"""
        artistalbum={'artist':artist_name.title(), 'album':album_name.title(),'number of tracks':songs}

        return artistalbum    
