import time

##############################################################################

def cFloor(x):
    floor = 0
    rc = 0
    #for positive floats
    if x >= 0 :
        while not(x >= floor and x < floor + 1):
            print(floor)
            floor += 1

        rc = floor
    #for negative floats
    else:
        while not(x >= floor - 1 and x < floor):
            print(floor)
            floor -= 1
        
        rc = floor - 1

    return rc

##############################################################################

floatInput = float(input("Enter float: "))

start = time.time()

print("The floor of " + str(floatInput) + " is: " + str(cFloor(floatInput)))

end = time.time()
print("Time Taken: " + str(end - start))