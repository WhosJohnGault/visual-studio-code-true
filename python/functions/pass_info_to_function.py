#previously in the greeting function, we had a simple program to provide a generic greeting but we can also personalize the greeting 
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " +username.title() + "!")
 #the next line is called a parameter/argument   
greet_user('james')
