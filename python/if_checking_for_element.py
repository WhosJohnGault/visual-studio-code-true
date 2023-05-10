banned_users=['gabby','marie','santiago']
user='berry'
#not in checks to make sure the variable user is not in the list of banned users
if user not in banned_users:
    print(user.title() + ", you can post if you wish")