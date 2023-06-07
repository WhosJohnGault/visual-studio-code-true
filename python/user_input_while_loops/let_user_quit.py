prompt= "\nTell me something and I will repeat it back to you."
prompt+="\nEnter 'quit to end the program "
message= " "            #this variable will store the message the user inputs and then compare it to 'quit'
while message!='quit':
    message=input(prompt)
    print(message)