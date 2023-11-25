import math

#this function run in O(log(n))
#because the number of iterations are halfed each time
def primeFactorize(n):
    primeFactors = []

    # print the number of two which divide n
    # after this, the residual n value will not be even anymore
    while n % 2 == 0:
        primeFactors.append(2)
        n /= 2

    # because n is odd at this point
    # so we can start at 3 and we jump in twos in each iteration
    # because the difference of any two consecutive prime factors must be at least 2
    

    #This is the reason we only iterate to the square root of n (Proof by contradiction)
    #__________________________________________________________________________________
    # Every composite number has at least one prime factor less than or equal to
    # the square root of itself.
    # This property can be proved using a counter statement. Let a and b be two
    # factors of n such that a*b = n. If both are greater than √n, then a.b > √n, * √n,
    # which contradicts the expression “a * b = n”.

    #because of the syntax of the python range function we have to put a (+1)
    #to inclusively loop to the sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , append i and divide n by i
        #(for as long as i divides n without a remainder, add i to the list,
        # and reduce n by a factor or i)
        while n % i == 0:
            primeFactors.append(i)
            n /= i
    
    # edge case where n is a prime number greater than 2
    # (i.e. the number left over is prime itself)
    if n > 2:
        primeFactors.append(n)

    return primeFactors

#set the number to prime factorize
n = 100000000000
factors = primeFactorize(n)
for factor in factors:
    print(int(factor))

