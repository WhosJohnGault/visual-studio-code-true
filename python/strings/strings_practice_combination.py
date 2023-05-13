#strings can be combined in interesting ways, strings for things such as names can be stored
#as seperate variables and then combined when needed in the case of names its often preferable to
# in the lower case
firstname="john"
lastname="doe"
# the + sign can be used to combine strings
fullname=firstname + " " + lastname

print(fullname.title())
print("hello" + " " + fullname.title() +"!")
#again we can store the previous line in the variable called "message"
message="hello" + " " + fullname.title() +"!"
print(message)
