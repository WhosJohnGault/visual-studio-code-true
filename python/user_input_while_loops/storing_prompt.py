#we can store a prompt in a variable
# then use an input function for that variable
prompt="If you tell us who you are, we can personalize your messages"
prompt += "\nWhat is your first name? "
name=input(prompt)
print("\nHello " + name + "!")