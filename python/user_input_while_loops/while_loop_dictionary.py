#this program will demonstrate the usage of a while loop to move users from one dictionary to another

#starting with unverified users and an empty list of verified users
unverfied_users=['alice','bob','charles']
confirmed_users=[ ]

#now we verify each user until the list of unconfirmed users is empty
while unverfied_users:
    current_user=unverfied_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    #now we display each user to confirm the program works
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
