######Eve RSA######
import support

print("------WELCOME EVE: RSA Encryption------")
print("Enter encryption keys intercepted from Alice (N value): ")
n=input()
print("Enter encryption keys intercepted from Alice (e value): ")
e=input()
print("Enter ciphertext intercepted from Bob: ")
ex=input()


#factor n to determine p*q and solve for d
p=support.polrho(n)
print(p,n/p)


x=support.rsadecrypt(p,n/p,e,ex)
print(x)
