prompt= "\nTell me something and I will repeat it back to you."
prompt+="\nEnter 'quit to end the program "
#we name a flag in this case active and set it
active= True #setting this to true makes it so the program is in an active state
while active:
    message=input(prompt)

    if message=='quit':
        active= False

    else:
        print(message)