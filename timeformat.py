def add_time(start, duration, weekday = 0):

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    tick = 0

    x = start.split(":")
    x2 = x[1].split(" ")
    y = duration.split(":")

    durh = y[0]
    durm = y[1]
    starth = x[0]
    startm = x2[0]
    finh = 0

    finm = int(durm) + int(startm)
    finh = int(durh) + int(starth)

    # use a variable called tick to sort AM and PM
    if x2[1] == "PM":
        tick += 1

    # convert everything into minutes then work from there
    
    # sort minutes first as its the easiest 
    if 120>int(finm)>=60:
        finm = int(finm) - 60
        finh += 1
        #if int(starth) == 11   and x2[1] == "PM":
            #tick += 1 #taking care of an edge-case scenario
    elif int(finm)>120:
        print("ERROR: MIN OVER 120")

    # Now the hours
    while int(finh) >= 12:
        finh = int(finh) - 12
        tick += 1
    
    if int(finh) == 0:
        finh = 12 #the test is incredibly petty
    
    if tick % 2 == 0:
            tick2 = "AM"
    else:
            tick2 = "PM"
    
    # Use the tick number to figure out how many days have passed and AM/PM
    days = -(-tick // 2) #can't import libs for test, so no math.ceil(). This works as minus signs makes it round the other way, because reasons.

    if tick < 2:
        days -= 1
        day = ""
    elif x2[1] == "PM" and tick == 2:
        day = " (next day)"
    elif x2[1] == "AM" and tick == 2:
        day = " (next day)"
    else:
        day = f" ({days} days later)"
    
    
    # if the day is given, work it out

    if weekday != 0:
        weekday = weekday.capitalize()
    
    if weekday in week:
         #so that input matches the week list
        x = week.index(weekday)
        days2 = x + days
        while days2 >= 7:
            days2 = days2 - 7
        if days == 0 and tick !=1:
            days2 = ", " + week[days2 - 1]
        elif days == 0 and tick == 1:
            days2 = ", " + week[days2]
        else:
            days2 = ", " + week[days2]
        return str(finh) + ":" + "{:02d}".format(finm) + " " + str(tick2) + days2 + str(day)
    else:
        return str(finh) + ":" + "{:02d}".format(finm) + " " + str(tick2) + str(day)