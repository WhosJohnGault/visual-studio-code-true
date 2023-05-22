#we start with making an empty list for our dictionary to fill later on
aliens=[]

#make 30 aliens some of them even may have happy families
for alien_number in range(30):
    new_alien= {'color':'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

    #showing the first five aliens:
    for alien in aliens[:5]:
        print(alien)
        print("...")
    #showing how many aliens have been generated in total
    print("Total number of aliens: " +str(len(aliens)))
    #despite the fact all of these aliens are the same and lack any sort of meaningful individuality we are somehow expected to believe they are unique individuals. Python does anyway, and we can customize them so thats a plus I guess...
    