#when a function is called python attempts to match each argument in the function call
#with a parameter in the functions definition. We can do this based on the order of the arguments
#provided 

def describe_pet(animal_type, pet_name):
    """Display information about a peter"""
    print("\nI have a "+ animal_type +".")
    print("My " + animal_type +"'s name is " + pet_name.title() +".")
describe_pet('hamster','harry')
#a function can be called as many times as neccecary with the arguments positoned the same way
describe_pet('dog','Eevee')
#we can assign a string to each of the variables we created when we defined the function so we don't need to rely on the correct positioning of arguments in the function call
describe_pet(pet_name='horus',animal_type='hawk')