######Eve ElGamal######
import support
print("------WELCOME EVE: ElGamal Encryption------")

print("Enter N value intercepted from Alice")
n=input()
print("Enter g value intercepted from Alice")
g=input()
print("Enter g^a value intercepted from Alice")
ga=input()
print("Enter g^b value intercepted from Bob")
gb=input()
print("Enter ciphertext message intercepted")
ex=input()
print("Who sent ciphertext message, Alice (1) or Bob (2)")
author=input()

#crack private keys with baby/giant step algo
a=support.bgstep(g,ga,n)
b=support.bgstep(g,gb,n)

#decrypt message with cracked keys
if author==1:
	priv=a
	pub=gb
if author==2:
	priv=b
	pub=ga

xout=support.elgdecrypt( n,pub,priv,ex)
print("Encrypted message: ")
print(xout)
print("Alice's private key a: ")
print(a)
print("Bobs's private key b: ")
print(b)
