# El-gamal 

The files included in this project are:  
 ```elgamal_keygen.py```  
```elgamal_encryption.py```  
```elgamal_decryption.py```  
```plain_text_el_gamal.txt```  
```ciphertext_elgamal.txt```  
```decipher_elgamal.txt```   
```elgamal_runtime.txt```  
```private_key_el_gamal.txt```  
```public_key_el_gamal.txt```

## File usage:  
```elgamal_keygen.py```   is used to generate the public and private keys for encryption and decryption.  
```bash
python3 elgamal_keygen.py
```  
The above command allows us to generate public-key in ```public_key_el_gamal.txt```  and private-key in ```private_key_el_gamal.txt```
##

```elgamal_encryption.py```  is used to generate the ciphertext using existing plaintext and public-key.  
```bash
python3 elgamal_encryption.py
```  
The above command runs the script which reads from ```plain_text_el_gamal.txt``` to get input-text and reads the public-key from ```public_key_el_gamal.txt``` to output the cipher-text to ```ciphertext_elgamal.txt```

##
  
```elgamal_decryption.py``` is used to decrypt existing ciphertext using private-key and public-key.
```bash
python3 elgamal_decryption.py
```
The above command runs a script which reads the ciphertext from ```ciphertext_elgamal.txt``` and reads the private key from ```private_key_el_gamal.txt```, the public-key from ```public_key_el_gamal.txt```to output the deciphered text in ```decipher_elgamal.txt```

##
The file ```elgamal_runtime.txt``` stores the running time of the program  ```elgamal_keygen.py```, which comes out to be ```5.5s``` on average. 

## File description 
```elgamal_keygen.py```  


```python
def check_prime(number): ''' checks whether a number is prime or not
by using the miller-rabin optimality test, Is performed multiple times
 because the test isn't foolproof'''
#Sources referred: Wikipedia.org, Brilliant.org
```

```python
def modular_exp(a,n,number): ''' Does exponentiation and 
takes mod at the same time,i.e doesn't compute the 
exponent and operates using modulo at the last stage , instead
it does both at the same moment such that the sqauring happens
 after a mod operation has already occurred. '''
#Sources referred: wikipedia.org
```

```python
def modular_inverse(m,n):'''Calculates the inverse of a number m, given modulo n 
using the extended eucledian algorithm . The extended eucledian algorithm
allows us to find x,y such that mx + ny = 1 where x turns out to be our 
modulo inverse.
 '''
#Sources referred: Wikipedia.org
```

```python
def generate_primes(n,k):''' Generate n bit random numbers, and checks whether 
its prime, if not. it keeps generating until it gets the desired number of 
primes specified by the user
```

```python
def gcd(a,b):''' Finds the gcd of two numbers '''
```

```python
def lucas_test(g,p,q):''' Lucas test allows us to check the validity of
a 'potential' primitive root, it checks with the divisors of a given prime q.
As the q is defined to 2p+1 for our case, we just need to check with the 
divisors 2 and p '''
```

```python
def find_primitive_root(q):''' Finds a primitive root for a give prime q,
in this function we generate a random number in range(q-1) and check its 
validity of being a primitive root using the Lucas test'''
```
##
```elgamal_encryption.py```
```python
def encrypt(pk,text):''' encrypts the text using public keys'''
```
##
```elgamal_decryption.py```
```python
def decrypt(c1,c2,a,q):''' decrypts the text using private,public keys'''
```  
## License
[MIT](https://choosealicense.com/licenses/mit/)
