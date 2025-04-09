# Diffie-Hellman Implementation
The Diffie-Hellman key exchange algorithm implemented in python

## Why did you do this?
Currently, my Python Programming II class is doing a lesson in encryption and servers. We were given pre-generated keys and told to use those for the encryption. To extend my project, I made this implementation from scratch to gain an understanding of Diffie-Hellman, prime numbers, and modular arithmetic.

## Potential fixes
There are plenty of things that could be done better, and that I may or may not get to at some point in the future.
- There's a lot of spaghetti code, mostly in the ```encrypt()``` function.
- The whole project is basically concept-dumping, or quickly dropping basic, unoptimized code into a file to represent concepts

## Notes
The method for finding primitive roots becomes INSANELY slow when calculating roots for large numbers. As a note to the user, it's likely better to run this separately and write down the prime number you want to use. Don't run it unless you need to. 
