# c7e7_babysitter.py
# Nathan Branson

def toDecimalHours(time):    
    lTime = time.split(":")
    hours = int(lTime[0])
    minutes = int(lTime[1])
    
    minutes = minutes/60
    time = hours + minutes

    return time
    

def main():
    print("This program calculates the total bill for a babysitter.")
    print("Choose the pay rate per hour until 9:00 and the per")
    print("hour after 9:00.  (Start and end times are assumed to")
    print("fall between 1:00 PM and 11:59 PM on the same day.)\n")
    
    start = input("Start time (e.g., 7:30)? ")
    end = input("End time? ")

    payHrDy = float(input("What is the day pay rate per hour? (e.g. $11.50) $"))
    payHrNt = float(input("What is the night pay rate per hour? (e.g. $9.50) $"))

    start = toDecimalHours(start)
    end = toDecimalHours(end)

    dif = end - start

    if end < 12 and start > 1 and end > start:
        if end <= 9:
            pay = payHrDy * dif
        elif start >= 9:
            pay = payHrNt * dif
        elif start < 9 and end >9:
            bHours = (9 - start) * payHrDy
            aHours = (end - 9) * payHrNt
            pay = bHours + aHours

        print("\nThe babysitter's pay should be ${0:.02f}.".format(pay))
    
    else:
        print("I cannot do these times, please try again!")

main()
