#Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations You’ll have to think of
#someone else to invite
dinner_invite=['gabbi', 'matthew','zack','jessie']
absentee=dinner_invite.pop(0)
dinner_invite.insert(0,'fernando')
#for loops make things look a bit nicer when printing entire lists
print("Hey " + absentee.capitalize() + " could not make it, we need to find a different meal")
for i in dinner_invite:
    print("Hey how do you feel about this? " + i.capitalize())