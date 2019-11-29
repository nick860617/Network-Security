# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:39:20 2019

@author: PC01
"""

import prime

class Rabin():
        def __init__(self, p, q):
            self.p = p
            self.q = q
            self.n = self.p*self.q
            
        ## =============== Encryption and Decryption=============== ##      
        def encryption(self, plaintext):
            Ciphertext = pow(self.padding(plaintext), 2, self.n)
            """
            while(self.decryption(Ciphertext)==None):
                self.p = self.prime_number(self.bits, self.iter_time)
                self.q = self.prime_number(self.bits, self.iter_time)
                self.n = self.p*self.q
                Ciphertext = pow(self.padding(plaintext), 2, self.n)
            """
            return Ciphertext
        
        def decryption(self, ciphertext):
            candidates = self.choose(self.sqroot_process(ciphertext))
            
            return candidates

        ## =============== Some method needed ===================== ## 
        def prime_number(self, bits, iter_tim):
            """
            generate a large prime number with given bits. 
            
            Input: 
            (1) bits     -> length of the private key.  
            (2) iter_tim -> parameter for Miller Rabin primality test, larger 
                iteration times brings higher accuracy.

            Output:
                a large prime number
            
            """
            return prime.generate_prime_number(bits, iter_tim)

        def padding(self, plaintext):
            """
            Implement 16-bit repetition padding at the end of plaintext.
            """
            binary_str = bin(plaintext)     
            output = binary_str + binary_str[-16:]      
            return int(output, 2)     
        
        def sqroot_process(self, a):
            """
            find all the candidates of the plaintext
            """
            r, s = 0, 0
            
            # First, find the sqroot
            if ((self.p) % 4) == 3:
                r = prime.sqrt_p_3_mod_4(a, self.p)
            elif ((self.p) % 8) == 5:
                r = prime.sqrt_p_5_mod_8(a, self.p)
 
            if ((self.q) % 4) == 3:
                s = prime.sqrt_p_3_mod_4(a, self.q)
            elif ((self.q) % 8) == 5:
                s = prime.sqrt_p_5_mod_8(a, self.q)
            
            # Second, using Euclid’s algorithm to find integers c,d s.t. cp+dq=1 
            gcd, c, d = prime.egcd(self.p, self.q)
            
            # Third, calculate four candidate plaintext
            x = (r*d*self.q + s*c*self.p) % self.n
            y = (r*d*self.q - s*c*self.p) % self.n
            return [x, self.n-x, y, self.n-y]
  
        def choose(self, candidates):
            for candidate in candidates:
                binary = bin(candidate)
                redundance, plaintext = binary[-16:], binary[:-16]    
                if redundance == plaintext[-16:]:
                    return int(plaintext, 2)