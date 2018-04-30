def get_day():

    days = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }



    while True:
        day = input("Day? (0-6) ")
        try:
            day = int(day)
        except:
            print ("could not convert to an integer")
            continue
        if day < 0 or day > 6:
            print("Input should be between 0 and 6.")
            day = input("Day? (0-6) ")
        else:  
            break
    print ("You've selected %s. End of loop 1." % days[day])

    exit = False
    while not exit:
        day = input("Beginning loop 2. Day? (0-6) ")
        try:
            day = int(day)
        except:
            print ("could not convert to an integer")
            continue
        if day == 0 or day == 6:
            print("Stay in bed.")   
        else:  
            print("Go to work, homie.")
        
        while True:
            goAgain = input("Want to play again? y/n ")
            if goAgain.upper() == 'Y':
                break
            elif goAgain.upper() == 'N':
                exit = True
                break
            else:
                print("Invalid input.")