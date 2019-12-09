######BOB ElGamal######
import support
print("------WELCOME BOB: ElGamal Encryption------")


print("Enter N value received from Alice")
n=input()
print("Enter g value received from Alice")
g=input()
print("Enter g^a value received from Alice")
ga=input()
print("Generating keys, this may take a few seconds")
#Bob choose secret key b 	
b=support.privkeygen(n,g)

#Bob calculate gb=g**b%p AND gab=ga**b%p
gb=support.fastexpo(g,b,n)


#Bob sends to Alice: gb, encrypted message ex
print("Bob sends gb to Alice: ")
print(gb)
print("Bob keeps private key b: ")
print(b)



print("Bob: encrypt (1) or decrypt (2) message?")
entry=input()

if entry==1:	
	print("Enter integer to encrypt: ")
	xin=input()
	ex=support.elgencrypt(n,ga,b,xin)
	print("Ciphertext message: ")
	print(ex)
elif entry==2:
	print("Enter ciphertext message: ")
	ex=input()
	xout=support.elgdecrypt(n,ga,b,ex)
	print("decrypted message: ")
	print(xout)
else:
	print("Input error, try again")
