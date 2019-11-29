# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:13:16 2019

@author: PC01
"""

import Rabin_Public_Key_Cryptosystem

def DectoHex(num, bits):
    return hex(num).split('x')[-1].zfill(int(bits))

def Simulation1(generator, iter_tim, bits):
    print("<Miller-Rabin>")
    dec_num = generator(bits, iter_tim)
    n_hex = DectoHex(dec_num, bits/8)
    for i in range(0, len(n_hex)):
        if (i+1)%8==0 and not(i==0):
            print (str(n_hex[i])+" ", end='')
        else:
            print (str(n_hex[i]), end='')
    return

def Simulation2():
    print("\n\n<Rabin Encryption>", end='')
    p = (input('p = '))
    q = (input('q = '))
    
    p = int(p.replace(' ', ''), 16)
    q = int(q.replace(' ', ''), 16)
    n = DectoHex(p*q, 64)
    print('')
    print('n = pq = ' + n)
    
    Plaintext = input('Plaintext: ')
    Plaintext = int(Plaintext.replace(' ', ''), 16)
    sys = Rabin_Public_Key_Cryptosystem.Rabin(p=p, q=q)
    Ciphertext = DectoHex(sys.encryption(Plaintext), 64)
    
    print('\nCiphertext = ', end='')
    for i in range(0, len(Ciphertext)): 
        if (i+1)%8==0:
            print(Ciphertext[i] + ' ', end='')
        else:
            print(Ciphertext[i], end='')
    return 

def Simulation3():
    print("\n\n<Rabin Decryption>", end='')
    Ciphertext = input('Ciphertext = ')
    Ciphertext = int(Ciphertext.replace(' ', ''), 16)
    print("\nPrivate Key:")
    p = (input('p = '))
    q = (input('q = '))
    print('')
    p = int(p.replace(' ', ''), 16)
    q = int(q.replace(' ', ''), 16)
    sys = Rabin_Public_Key_Cryptosystem.Rabin(p=p, q=q)
    Plaintext = DectoHex(sys.decryption(Ciphertext), 56)
    print('Plaintext = ', end='')
    for i in range(0, len(Plaintext)): 
        if (i+1)%8==0:
            print(Plaintext[i] + ' ', end='')
        else:
            print(Plaintext[i], end='')
    return
    