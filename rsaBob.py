######Bob RSA######
import support
print("------WELCOME BOB: RSA Encryption------")

print("Enter N value received from Alice")
n=input()
print("Enter e value received from Alice")
e=input()

print("Enter integer to encrypt: ")
xin=input()
if xin>=n:
	print("Invalid input, message x must be an integer less than n")
else:
	#encrypt message
	ex=support.rsaencrypt(xin,e,n)

	print("Ciphertext to send to Alice ")
	print(ex)
