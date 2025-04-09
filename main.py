import math

''' Old code
def gcd(a, b):
    if (a==0):
        return b
    return gcd(b%a, a)
'''

def phi(n):
    # Initialize the count of coprime numbers to 0
    count=0
    # Iterate from 1 to n-1
    for i in range(1, n):
        # Check if i and n are coprime using gcd
        if math.gcd(i,n)==1:
            count+=1
    return count

def isprime(n):
    if phi(n)==n-1:
        return True
    return False

def relativePrimality(a, b):
    if math.gcd(a,b)==1:
        return True
    return False

def find_order(a, n):
    '''
    The order of (a mod n) is the smallest positive integer k 
    that satisfies (a**k)%n==1, aka (a^k) is congruent 
    to 1 (mod n)
    '''
    if (a==1) & (n==1):
        # 1 is the order of 1
        return 1
    if math.gcd(a,n)!=1:
        raise Exception("A and N should be relatively prime")
    for i in range(1, n):
        if pow(a,i)%n==1:
            return i
    return False

def primitive_roots(n):
    if n==1:
        #0 is the only primative root of 1
        return [0]
    tot=phi(n)
    prim_roots=[]
    for i in range(1,n):
        if math.gcd(i,n)==1:
            order=find_order(i,n)
            if order==tot:
                prim_roots.append(i)
    return prim_roots


def genKeys(g, p, a):
    '''

    Parameters
    ----------
    g : int
        Primitive prime for number generation
    p : int
        Large, agreed-upon prime number
    a : int
        Private key number

    Returns
    -------
    Public-private key pair
    
    '''
    return ((g**a)%p, a)

def padto8(data):
    data=[*data]
    while len(data)<8:
        data.insert(0,"0")
    return ''.join(data)

def encrypt(message:str, key:int):
    key=bin(key)[2:]
    message=[*message]
    binary=None
    encrypted_binary=[]
    
    for i in range(len(message)):
        message[i]=padto8(bin(ord(message[i]))[2:])
        
    print(message)
    
    binary=''.join(message)
    print(binary)
    
    for i in range(len(binary)):
        key_index=i%len(key)
        encrypted_binary.append(int(binary[i])^int(key[key_index]))
    
    for i in range(int(len(binary)/8)):
        real_index=(i*8)
        encrypted_binary.append(binary[real_index:real_index+8])
    print(f"{encrypted_binary=}")
        
    
if __name__ == "__main__":
    keys=genKeys(g=1931, p=2039, a=17)
    encrypt("Hello", keys[0])
    
    print("Primitive roots")
    print(primitive_roots(17))
    

'''
1. Agreement on Public Parameters:
Prime Number (p):
Alice and Bob (the two parties) agree on a large prime number, p. This is a public value, meaning it can be shared openly.
Generator (g):
They also agree on a generator g, which is a primitive root modulo p. This is also a public value. 

2. Private Key Generation:
Alice's Private Key (a): Alice randomly chooses a private number, a, which she keeps secret.
Bob's Private Key (b): Similarly, Bob randomly chooses a private number, b, which he keeps secret. 

3. Public Key Calculation:
Alice's Public Key (A): Alice calculates her public key, A, using the formula: A = g^a mod p.
Bob's Public Key (B): Bob calculates his public key, B, using the formula: B = g^b mod p. 

4. Key Exchange:
Exchange Public Keys: Alice and Bob exchange their public keys (A and B) with each other over an insecure channel. 

5. Shared Secret Key Calculation:
Alice Calculates Shared Key (k):
Alice receives Bob's public key (B). She calculates the shared secret key, k, using the formula: k = B^a mod p.
Bob Calculates Shared Key (k):
Bob receives Alice's public key (A). He calculates the shared secret key, k, using the formula: k = A^b mod p. 

6. Result:
Shared Secret: Both Alice and Bob will arrive at the same shared secret key, k, even though they never directly exchanged their private keys. 
Example (Simplified):
Let's use small numbers for demonstration purposes (in real-world scenarios, p and g would be much larger): 
p = 11: (a prime number)
g = 2: (a generator modulo 11)
Alice's private key (a) = 3
Bob's private key (b) = 5
Alice calculates her public key (A): A = 2^3 mod 11 = 8 mod 11 = 8 
Bob calculates his public key (B): B = 2^5 mod 11 = 32 mod 11 = 10 
Alice and Bob exchange A and B. 
Alice calculates the shared secret key (k): k = 10^3 mod 11 = 1000 mod 11 = 1 
Bob calculates the shared secret key (k): k = 8^5 mod 11 = 32768 mod 11 = 1 
Both Alice and Bob have the same shared secret key (k = 1). 
'''
