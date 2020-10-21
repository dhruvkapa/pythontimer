#Timer application
import time
import sys

userInput = input("Do you want to start the timer (Y/N) ")
Timer = True
if userInput.lower() == "y":
    inputMinutes = input("Enter the amount of minutes to set")
    if int(inputMinutes) < 0:
        Timer = False
        print("Sorry you can't set that number, please set a number greater or equal to 0")
        sys.exit()
    inputSeconds = input("Enter the amount of seconds to set")
    if int(inputSeconds) < 0:
        Timer = False
        print("Sorry you can't set that number, please set a number greater or equal to 0")
        sys.exit()
    minutes = int(inputMinutes)
    seconds = int(inputSeconds)


    while Timer == True:

        if seconds < 0:
            minutes -= 1
            seconds = 59
            if minutes < 0:
                Timer = False
        startTime = str(minutes) + ":" + str(seconds)
        if seconds < 10:
            startTime = str(minutes) + ":0" + str(seconds)


        seconds -= 1
        print(startTime)

        time.sleep(1)

