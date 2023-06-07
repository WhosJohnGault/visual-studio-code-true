# Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches Then make an empty list called finished_sandwiches Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches After all the sandwiches have been made, print a
# message listing each sandwich that was made

sandwich_orders=['ruben', 'classic ruben', 'ham', 'turkey', 'club']
finished_sandwiches=[]
#now we will loop the sandwich
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print("\nMaking your " + current_sandwich.title())
    #now we append the finished sandwiches
    finished_sandwiches.append(current_sandwich)
    #once the sandwiches are finished we can print out each entry to confirm te program worked
for finished_sandwich in finished_sandwiches:
    print("\nYour " + finished_sandwich.title() + " sandwich is ready!")
