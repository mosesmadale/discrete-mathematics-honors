import time
import math

##############################################################################

def cCeil(x):
    ceil = 0
    #for positive floats
    if x > 0 :
        while not(x > ceil - 1 and x <= ceil):
            ceil += 1
    #for negative floats
    else:
        while not(x > ceil - 1 and x <= ceil):
            ceil -= 1

    return ceil

##############################################################################

floatInput = float(input("Enter float: "))

start = time.time()

print("The ceiling of " + str(floatInput) + " is: " + str(math.ceil(floatInput)))

end = time.time()
print("Time Taken: " + str(end - start))