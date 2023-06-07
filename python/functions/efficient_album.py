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

def make_album(artist_name, album_name):
    """return a dictionary about an artist and a music album"""
    artistalbum={'artist':artist_name.title(), 'album':album_name.title()}
    artistalbum.update({artist_name,album_name})
    return artistalbum
#these functions will print what we want to show, but we should make this more efficient by using an additional function
musician=make_album(artist_name ='kurt cobain', album_name='bleach')
print(musician)
musician=make_album(artist_name ='lunchmoney lewis', album_name='real thing')
print(musician)