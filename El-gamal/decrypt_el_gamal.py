
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

def modular_inverse(m,n): # finds the moduloinverse of m modulo n

    #relies on the eucledian algorithm , tries to solve the diophantine equation mx + ny = 1
    # here m is e, and n is phi, as we know ed congruent 1 mod phi, we just need to solve the above diophantine equation such that 
    if m == 0:
        return (n, 0, 1)  # because gcd of zero and and another number is simply the other number

    else:
        gcd, a, b = modular_inverse(n % m, m) # we may switch from m,n to n,m while doing this if m<n,
                                             # and then keep taking the gcd(q,r) where q is the quotient and r is the remainder.

        return (gcd, b - (n//m) * a, a) # after reaching the base case we go back and keep returning to the previous calls 


def decrypt(c1,c2,a,q):
    t3 = []
    for i in range(len(c1)):
        t1 = modular_exp(c1[i],a,q)
        inv = modular_inverse(t1,q)
        ch = inv[1]
        ch = ch+q # tinverse ( we add  incase q is negative)
             
        t3.append(chr((c2[i]*ch)%q))
    
    f = open('decipher_elgamal.txt','w')
    for i in t3:
        f.write(str(i))
    f.close()

    return 0 






if __name__ == "__main__":


    f = open('ciphertext_elgamal.txt','r')
    C = f.read()
    C = C.split('|')

    C1 = C[0].split(',')
    C2 = C[1].split(',')
    C1.remove('')
    C2.remove('')
    C1 = [int(i) for i in C1]
    C2 = [int(i) for i in C2]
    f.close()
    print(C1)

    f = open('private_key_el_gamal.txt','r')
    a = f.read()
    a = a.split(',')
    a_1 = int(a[0])
    f.close()

    f2 = open("public_key_el_gamal.txt",'r')
    text = f2.read()
    text = text.split(',')
    q,g,h = int(text[0]),int(text[1]),int(text[2])
    f2.close()

    decrypt(C1,C2,a_1,q)
