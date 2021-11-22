

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



def decrypt(priv_key,text,n2):
    f = open('deciphered_rsa.txt','w')
    p = []
    for i in text:
        letter =  modular_exp(i,priv_key,n2)
        p.append(chr(letter))
    p = ''.join(p)
    f.write(p)
    f.close()

    return 0



if __name__ == "__main__":
    
    f = open('cipher_text_rsa.txt','r')
    text = f.read()
    text2 = text.split(',')
    text2.remove('')
    text2 = [int(i) for i in text2]
    f.close()

    f2 = open('private_key_rsa.txt','r')
    priv = f2.read()
    d = int(priv)

    
    f = open('public_key_rsa.txt','r')
    pk = f.read()
    pk = pk.split('\n')
    public_key = int(pk[0])
    n = int(pk[1])
    f.close()

    decrypt(d,text2,n)

    print("Done..decrypting")