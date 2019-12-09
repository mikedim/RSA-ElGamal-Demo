######Alice RSA######
import support
print("------WELCOME Alice: RSA Encryption------")

#Initialize, generate p*q=N
#paremeter=num of digits
p=support.primegen(4)
q=support.primegen(4)
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
