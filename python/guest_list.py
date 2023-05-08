#If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner Then use your list to print a message to each person, inviting
#them to dinner

dinner_invite=['gabbi', 'matthew','zack','jessie']
guest1=dinner_invite[0]
for i in dinner_invite:
    print("\nHi! I would like to invite you to dinner " + i.capitalize(),end=".")
