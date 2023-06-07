def make_album(artist_name, album_name):
    """return a dictionary about an artist and a music album"""
    artistalbum={'artist':artist_name.title(), 'album':album_name.title()}
    return artistalbum
#these functions will print what we want to show, but we should make this more efficient by using an additional function
musician=make_album(artist_name ='kurt cobain', album_name='bleach')
print(musician)
musician=make_album(artist_name ='lunchmoney lewis', album_name='real thing')
print(musician)