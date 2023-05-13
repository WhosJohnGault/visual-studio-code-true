#using sorted() makes it so lists are sorted in alphabetical order temporarily
people=['Gabbi','Zack','Jessie','James','Matthew','Jonah Hill']
    #reverse=True orders the list in r.alphabetical order
print(sorted(people))   #this temporarily ordered in alphabetical order
print(people)
people.reverse()        #this reversed the original list order
print(people)
print(sorted(people,reverse=True)) #,reverse=true is what makes this work in temp. reverse alph. order
print(people)
