
#you can set a default argument when you define a function
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
#you don't need to use the default value, you can still define a pet type such as a hamster if its neccecary
describe_pet(pet_name='harry', animal_type='hamster')
