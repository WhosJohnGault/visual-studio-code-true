#sometimes we don't want to use every part of a function, if we are displaying the full name of a person
#we might not want to display the middle name for instance, so we can format a function in the following way
#to account for this scenario where someone might not want to display their middle name
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    #the defined function has an entry accounting for an empty string for a middle name, so if a middle name is entered when the function is called it will execute the if middle name statement
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)