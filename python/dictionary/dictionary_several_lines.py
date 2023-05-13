#we will writer out a dictionary across several lines
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python'
}
#we can use this dictionary by using the given name of the person(Key) who took the poll
#we can see the language they prefer by asking for the value
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +
 ".")