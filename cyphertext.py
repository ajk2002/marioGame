from fractions import gcd
import random

def iterative_egcd(a,b):
    x,y, u,v = 0,1,1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y
    
   
def modinv(a, m):
    g,x,y = iterative_egcd(a,m)
    if g != 1:
        return None
    else:
        return x%m
def coprimeList(n):
    coprimes = []
    for i in range(1,n):
        if gcd(i,n) == 1:
            coprimes.append(i)
    coprimes.pop(0)
    return coprimes
p = int(input("what's first key: "))
q = int(input("what's second key: "))
mod = p*q
endKey = (p-1)*(q-1)
coprimes = (coprimeList(endKey))
pubExp = random.choice(coprimes)
privExp = modinv(pubExp,endKey)
if pubExp == privExp:
    print("NOOOOOOOOOOOOOOOOOOOOO")
    exit()
print("public: (",pubExp,",",mod,")")
print("private: (",privExp,",",mod,")")   
def encrypt(pubExp):
    global mod
    plaintext = int(input("number: "))
    cyphertext = (plaintext**pubExp % mod)
    print(cyphertext)

def decrypt(privExp):
    global mod
    cyphertext = int(input(" decrypt number: "))
    plaintext = (cyphertext**privExp % mod)
    print(plaintext)
encrypt(pubExp)
decrypt(privExp)


