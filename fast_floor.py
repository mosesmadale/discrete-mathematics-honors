import time

##############################################################################

def cFloor(x):
    return x - (x % 1)

##############################################################################

floatInput = float(input("Enter float: "))

start = time.time()

print("The floor of " + str(floatInput) + " is: " + str(cFloor(floatInput)))

end = time.time()
print("Time Taken: " + str(end - start))