favorite_languages = {
'jen': 'python',
'sarah goodfellow': 'c',
'edward': 'ruby',
'phil': 'python',
}
#looping through keys is the default behavior when looping through a dictionary
for key,value in favorite_languages.items():
    print(value.title())
# When making use of keys and values in a dictionary it's necessary to use .items() to display both the key value portions,if we want only keys we use .keys(), similarly with values we use .values(). 
#the following output would only print the keys despite us wanting the values
for value in favorite_languages:
    print(value.title())
