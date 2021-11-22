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

    #relies on the eucledian algorithm , tries to solve the diophantine equation mx + ny = 1
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

def lucas_test(g,p,q):
    power = (p-1)//q
    power = int(power)
    result = modular_exp(g,power,p)
    
    if result !=1:
        print("yeet")
        return True
    else:
        print("no")
        return False
        


def find_primitive_root(q):
    k = random.randrange(q)
    if lucas_test(k,q,2) and lucas_test(k,q,((q-1)//2)):
        return k
    else:
        return find_primitive_root(q)



if __name__ == "__main__":
    while(True):
        p = generate_primes(300,1)
        q = (2*p[0])+1
        if check_prime(q):
            break       
    # we get p and q
    # after gettin p and q we find the primitive root
    primitive_root = find_primitive_root(q)
    # we have found the primitive root

    # now we gotta follow guidelines 
    print(modular_exp(primitive_root,q-1,q))
    g = pow(primitive_root,2)
    a= random.randrange(2,(q-1))
    
    h = modular_exp(g,a,q)
    public_key = [q,g,h]
    secure_key = a

    file = open('public_key_el_gamal.txt','w')
    file.write(str(public_key[0]))
    file.write(',')
    file.write(str(public_key[1]))
    file.write(',')
    file.write(str(public_key[2]))
    file.write(',')
    file.close()

    f = open('private_key_el_gamal.txt','w')
    f.write(str(secure_key))
    f.write(',')
    f.close()


