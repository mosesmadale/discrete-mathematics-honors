#Proposition:
#The square of any odd integer can be written in the form
#8m + 1 for some m ∈ Z.


#take an integer input
integerInput = int(input("Enter any integer: "))

#checks if the integer is even
if integerInput % 2:
    #then integer is odd
    #squaring the odd integer
    n = integerInput ** 2
    #then we attempt to put it in the form of 8m + 1
    n -= 1
    if not n % 8:
        #this number can be put in the form of 8m + 1
        print("TRUE: {}² = {} = 8•{} + 1".format(integerInput, integerInput ** 2, n//8))
    else:
        #this code will never get executed if the proposition is true
        print("∃ an odd number such that its square doesn't take the form 8m + 1, for some m ∈ Z")

else:
    print("Integer entered is not odd")
