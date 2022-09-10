import random as rand
import math
def isMillerRabinPassed(n):
    if(n < 3):
        return False

    s = n-1
    r = 0
    while s % 2 == 0:
        s //= 2
        r += 1

    for _ in range(5):
        if(n < 3):
            return False

        a = rand.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

#prime number
def primeNumber():
    candidate = rand.getrandbits(8)
    prime = isMillerRabinPassed(candidate)
    while not prime:
        candidate = rand.getrandbits(8)
        prime = isMillerRabinPassed(candidate)

    return candidate

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def primosEntreSi(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m      

def cript(string, e, n):
    criptString = ""
    for word in string:        
        asciiValue = ord(word)
        valueInt = pow(asciiValue, e, n)
        criptWord = chr(valueInt)
        criptString = criptString + criptWord
        
    return criptString

def decript(criptWord, privateKey, publicKey):
    decriptString = ""
    for word in criptWord:        
        asciiValue = ord(word)
        decriptWord = chr(pow(asciiValue ,privateKey, publicKey))
        decriptString = decriptString + decriptWord 
   
    return decriptString

print("Aluno: Alessandra de Souza Guedes - 081180001")
print("Aluno: Guilherme Sant'anna        - 081180012")
print("Aluno: Lucas Araujo Russo         - 081180021")
print("")

p = primeNumber()
q = primeNumber()
n = p*q
print("P: ", p)
print("Q: ", q)
print("N: ", n)

tn = (p-1)*(q-1)
print("T: ", tn)

e = primeNumber()
while (e > tn and tn%e == 0):
    e = primeNumber()
    
print("E: ", e)

d = 2
while(True):
    if((e*d)%tn == 1):
        break    
    d += 1

print("D: ", d)
print()

string2Cript = input("Escreva a msg: ")
criptString = cript(string2Cript, e, n)
print("Cripty string: ", criptString)

print("Decripty string: ", decript(criptString, d, n))

