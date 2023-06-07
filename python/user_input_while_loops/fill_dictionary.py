responses={}

#setting a flag to indicate the poll is active
poll_active = True

while poll_active:
    #prompt for user name and input
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    #next we store the response in a dictionary
    responses[name] = response

    #find out if any others are interested in taking the poll
    repeat=input("Would you like anyone else to respond (yes/no) ")
    if repeat=='no':
        poll_active = False
    #polling is complete. Show the results.
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")
