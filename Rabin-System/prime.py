# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:41:41 2019

@author: Liou Shing Tzou (108064512)
"""

import random

def Miller_Rabin(N, iter_time):
    """
    Input：
    (1) N          -> number will be tested
    (2) iter_time  -> iteration times 
    
    Output:
        1 -> is a prime
        0 -> not a prime
    """
    s = N-1
    d = 0
    while(d%2 == 0):
        s = s//2
        d += 1
    for trials in range(0, iter_time): 
        a = random.randrange(2, N-1)
        y = pow(a, s, N)
        if y!=1 and y!=N-1:
            i=1
            while(i<=d-1 and y!=N-1):
                y = pow(y, 2, N)
                if y == 1:
                    return 0
                else:
                    i += 1
            if y != N-1:
                return 0
    return 1

def generator(bits):
    cryptogen = random.SystemRandom()
    return cryptogen.randrange(pow(2, bits))

def generate_prime_candidate(bits):
    p = generator(bits)
    
    # Use this method, we could get candiate of prime number quickly, but we 
    # still have to use Miller Rabin test to check if it is a prime.
    p |= (1<<bits - 1) | 1
    
    return p 

def generate_prime_number(bits, iter_time):
    p = 21
    while(not(Miller_Rabin(p, iter_time))):
        p = generate_prime_candidate(bits)
        if not((p-1)%4 == 0):
            continue
    return p

def sqrt_p_3_mod_4(a, p):
    r = pow(a, (p + 1) // 4, p)
    return r

def sqrt_p_5_mod_8(a, p):
    d = pow(a, (p-1)//4, p)
    r =0
    if d == 1:
        r = pow(a, (p+3)//8, p)
    elif d == p - 1:
        r = 2*a*pow(4*a, (p-5)//8, p)%p
    return r

def egcd(a, b):
    """
    Euclid’s algorithm
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = egcd(b % a, a)
        return gcd, x - (b // a) * y, y




