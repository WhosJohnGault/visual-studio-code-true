#tuples are are a type of list that contains values that are considered by
#python to be immutable, they cannot be changed
#instead of enclosing a list with brackets for tuples you enclose the list with 
#paranthesis
dimensions=(200,50)  #this is a tuple
print(dimensions[0])
print(dimensions[1])
dimensions[0]=250     #because tuples are immutable, this line causes an error
print(dimensions[0])