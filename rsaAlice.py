######Alice RSA######
import support
print("------WELCOME Alice: RSA Encryption------")

#Initialize, generate p*q=N

####V1 IMPLEMENTATION, SEE V2 FOR UPDATES
#paremeter=num of digits
p=support.primegen(16)
q=support.primegen(16)
n=p*q

#select e coprime to phi(n)
e=support.rsakeygen(p,q)

#publish encryption keys (n,e)
print("Enryption keys to send to Bob: ")
print("N="+str(n))
print("e="+str(e))


print("Alice already knows p & q")
print(p,q)

print("Enter ciphertext received from Bob: ")
ex=input()
xout=support.rsadecrypt(p,q,e,ex)
print("decrypted message: ")
print(xout)
