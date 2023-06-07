#a function doesn't need to show it's output directly. Sometimes you may want to pass a value through a function then have it return a value. The return statement takes a value from the inside of a function and  sends it back to the line that called the function. 
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)