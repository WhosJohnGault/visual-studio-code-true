favorite_languages = {
'jen': 'python',
'sarah goodfellow': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends=['phil', 'sarah']
#looping through keys is the default behavior when looping through a dictionary
for name in favorite_languages.keys():
    print(name.title())

if name in friends:
    print(" Hi " + name.title() + favorite_languages[name].title() + "!")