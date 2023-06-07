#continue allows use to continue a while loop without having to execute the entirety of it's code lets demonstrate this using a counting program.
current_number=0
while current_number<10:
    current_number += 1
    if current_number % 2 == 0: #if the current number is even it'll just skip to the next current number without printing
        continue

    print(current_number)