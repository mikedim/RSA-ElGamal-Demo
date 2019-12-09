######Alice ElGamal######
import support
print("------WELCOME ALICE: ElGamal Encryption------")
print("Generating keys, this may take a few seconds")
#Generate large prime n
#paremeter=num of digits
n=support.primegen(6)

#Alice randomly choose generator g and secret key a
g=support.getprimroot(n)
a=int(support.privkeygen(n,g))

#Alice calculate ga=g**a%p to send Alice-->Bob
ga=support.fastexpo(g,a,n)

#Alice sends to Bob: prime n, generator g, ga
print("Alice sends to Bob: ")
print("N= " + str(n))
print("g= " + str(g))
print("g^a= " + str(ga))
#print(n,g,ga)

print("Alice keeps private key a: ")
print(a)

print("Enter gb received from Bob: ")
gb=input()

print("Alice: encrypt (1) or decrypt (2) message?")
entry=input()

if entry==1:	
	print("Enter integer to encrypt: ")
	xin=input()
	ex=support.elgencrypt(n,gb,a,xin)
	print("Ciphertext message: ")
	print(ex)
elif entry==2:
	print("Enter ciphertext message: ")
	ex=input()
	xout=support.elgdecrypt(n,gb,a,ex)
	print("Decrypted message: ")
	print(xout)
else:
	print("Input error, try again")
