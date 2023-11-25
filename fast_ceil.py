import time
import math

##############################################################################

def cCeil(x):
    return x - (x % 1) + 1

##############################################################################

floatInput = float(input("Enter float: "))

start = time.time()

print("The ceiling of " + str(floatInput) + " is: " + str(math.ceil(floatInput)))

end = time.time()
print("Time Taken: " + str(end - start))