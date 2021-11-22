import random

def check_prime(number):

    num_of_checks =5
    if number ==2 or number ==3: # if the nnumber is 2 or 3 , the return True
        return True
    if number%2==0 or number == 1 : #: if the number is 1 return false
        return False
    
    x = number-1
    m,n = 0,x 

    while n%2==0: # keep dividing if the number is even 
        n >>=1 
        m = m +1

    def check(a):
        dummy = modular_exp(a, n, number)  # dummy stores
        if dummy == 1:
            # print("test1")
            return False

        for i in range(m):
            # print("test2")
            dummy = modular_exp(a, 2**i * n, number) # miller rabin
            if dummy == x:
                # print(test3)
                return False

        return True

    for _ in range(num_of_checks): # we go through the checks multiple times to because miller rabin doesnt guarantee a primality
        a = random.randrange(2, number-2)
        if check(a):
            return False

    return True

def modular_exp(m, r, num) : 
    result = 1	 # Initialize result 

    m = m % num # modular division
    if (m == 0) : 
        return 0
    while (r > 0) : 
        if ((r & 1) == 1) : #if r is odd
            result = (result * m) % num  # when the power reaches 1 we multiply the product of m we have calculated over the loops
        # r can be even now 
        r = r >> 1	 # ahift r left
        m = (m * m) % num # sqauring the number and then taking the modulo
        
    return result 


def generate_primes(n,k): # n represents the bitlength, k =  number of primes you need
    p = random.getrandbits(n)
    l = []
    while(len(l)!=k):
        if check_prime(p):
            l.append(p)
            p = random.getrandbits(n) # generate a random number of n bits
        else:
            p = random.getrandbits(n)
    return l

def modular_inverse(m,n): # finds the moduloinverse of m modulo n

    #relies on the extended eucledian algorithm , tries to solve the diophantine equation mx + ny = 1
    # here m is e, and n is phi, as we know ed congruent 1 mod phi, we just need to solve the above diophantine equation such that 
    if m == 0:
        return (n, 0, 1)  # because gcd of zero and and another number is simply the other number

    else:
        gcd, a, b = modular_inverse(n % m, m) # we may switch from m,n to n,m while doing this if m<n,
                                             # and then keep taking the gcd(q,r) where q is the quotient and r is the remainder.

        return (gcd, b - (n//m) * a, a) # after reaching the base case we go back and keep returning to the previous calls 

def gcd(a, b):
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if (b == 0):
        return a
    else:
        return gcd(b, a % b) # keep dividing



if __name__ == "__main__":

    j = generate_primes(512,2)
    #j = [5,3]                
    p = abs(j[0])
    q = abs(j[1]) 
    n = p*q
    phi = (p-1)*(q-1)
    val=0

    while(val!=1):
        e = random.randrange(phi)
        val = gcd(phi,e)

    h = modular_inverse(e,phi)
    d = h[1]
    d = d+phi
    assert(e*d%phi)
# ?    print("reached here")
    file = open("public_key_rsa.txt",'w')
    file.write(str(e))
    file.write('\n')
    file.write(str(n))
    file.close()

    file = open("private_key_rsa.txt",'w')
    file.write(str(d))
    file.close()
    
    print("Done..generating keys")