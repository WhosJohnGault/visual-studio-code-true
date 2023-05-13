#this program points out why someone would want to becareful with elif statements
pizza_topping=['pepperoni','bacon','ham','onion']
if 'pepperoni' in pizza_topping:
    print("Adding "+'pepperoni'.title())
elif 'bacon' in pizza_topping:  #this code will not execute because the code above it will execute first
    print("Adding "+'bacon'.title())    
elif 'ham' in pizza_topping:
    print("Adding "+'ham'.title())
print("Thanks for making your pizza!")
