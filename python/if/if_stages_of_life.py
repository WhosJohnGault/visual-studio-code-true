# Write an if-elif-else chain that determines a person’s
# stage of life Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby
# • If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult
# • If the person is age 65 or older, print a message that the person is an
# elder
age=26
if age>65:
    print("You are nearly dead")
elif age>20:
    print("you are an adult")
elif age>13:
    print("you are angsty")
elif age>4:
    print("you are less annoying and slightly cute now")
elif age>2:
    print("I regret having you still")
else:
    print("I am not sure if you are my child")
