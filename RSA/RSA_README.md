# RSA


The files included in this project are:
```keygen_rsa.py```  
```encrypt_rsa.py```
```decrypt_rsa.py```
```public_key_rsa.txt```
```private_key_rsa.txt```
```plaintext_rsa.txt```
```cipher_text_rsa.txt```
```deciphered_rsa.txt```
```rsa_runtime.txt```


## File usage:  
```keygen_rsa.py```   is used to generate the public and private keys for encryption and decryption.  
```bash
python3 keygen_rsa.py
```  
The above command allows us to generate public-key in ```public_key_rsa.txt```  and private-key in ```private_key_rsa.txt```
##

```encrypt_rsa.py```  is used to generate the ciphertext using existing plaintext and public-key.  
```bash
python3 encrypt_rsa.py
```  
The above command runs the script which reads from ```plaintext_rsa.txt``` to get input-text and reads the public-key from ```public_key_rsa.txt``` to output the cipher-text to ```cipher_text_rsa.txt```

##
  
```decrypt_rsa.py``` is used to decrypt existing ciphertext using private-key and public-key.
```bash
python3 decrypt_rsa.py
```
The above command runs a script which reads the ciphertext from ```cipher_text_rsa.txt``` and reads the private key from ```private_key_rsa.txt```, the public-key from ```public_key_rsa.txt```to output the deciphered text in ```deciphered_rsa.txt```

##
The file ```rsa_runtime.txt``` stores the running time of the program  ```keygen_rsa.py```, which comes out to be ```1.5s``` on average. 


## File description 
```keygen_rsa.py```  


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

##
```encrypt_rsa.py```
```python
def encrypt():''' encrypts the text using public keys'''
```
##
```decrypt_rsa.py```
```python
def decrypt():''' decrypts the text using private,public keys'''
```  



## License
[MIT](https://choosealicense.com/licenses/mit/)
