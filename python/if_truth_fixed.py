cars=['BMW']
for car in cars:
    if car.lower()=='bmw':  #this line fixes the previous error, as it ensures all car names are lower case
        print(car.upper())
    else:
        print("== is case sensitive, make sure to use .lower() before checking")