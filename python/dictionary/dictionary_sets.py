dummy_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("the following wastes of time mentioned:")
for languages in set(dummy_languages.values()):
    print(languages.title())