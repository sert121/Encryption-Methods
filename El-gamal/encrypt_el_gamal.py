import random

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


def encrypt(PK,text="thisisadummymessage"):

    q,g,h = PK[0],PK[1],PK[2]
    r = random.randrange(2,q-1)
    mess = text
    mess = [ord(i) for i in mess]
    C1_list = []
    C2_list = []
    for i in mess:
        C1 = modular_exp(g,r,q)
    #t2 = modular_exp(c2,1,q)*modular_exp((1/t1),1,q)  
        C2 = modular_exp(h,r,q)*modular_exp(i,1,q) # encyrpting the letter
        C1_list.append(C1)
        C2_list.append(C2)      
    C=[C1_list,C2_list]
    
    f = open("ciphertext_elgamal.txt",'w')
    for i in C1_list:
        f.write(str(i)+',')
    f.write('|')
    for i in C2_list:
        f.write(str(i)+',')
    f.writelines('|')
        
    return 0 








if __name__ == "__main__":
    
    f = open("public_key_el_gamal.txt",'r')
    text = f.read()
    text = text.split(',')
    q,g,h = int(text[0]),int(text[1]),int(text[2])
    pubkey = [q,g,h]

    f.close()
    f = open('plain_text_el_gamal.txt','r')
    plaintext = f.read()

    encrypt(pubkey,plaintext)
    print("Done")





