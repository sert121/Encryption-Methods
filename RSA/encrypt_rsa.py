

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


def encrypt(text,pub_key,n):
    file = open('cipher_text_rsa.txt','w')
    l = [ord(i) for i in text]
    c= []
    for i in l:
        letter = modular_exp(i,pub_key,n)
        c.append(letter)
        file.write(str(letter)+',')
    
    file.close()
    
    return 0 




if __name__ == "__main__":
    
    f = open('public_key_rsa.txt','r')
    pk = f.read()
    pk = pk.split('\n')
    public_key = int(pk[0])
    n = int(pk[1])
    f.close()

    f1 = open('plaintext_rsa.txt','r')
    text = f1.read()
    f1.close()

    encrypt(text,public_key,n)
    print("Done..encrypting")