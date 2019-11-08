############DEFINE SUPPORITNG FUNCTIONS############

def fastexpo(base,exp,mod):
    b = base
    e = exp
    y = 1
    while e > 0:
        if e % 2 == 0:
            b = (b * b) % mod
            e = e/2
        else:
            y = (b * y) % mod
            e = e - 1
    return y

######ALICE

#Already knew from step 1
a=3
p=131
g=10
ga=83

#Receive from Bob
gb=47
ex=20

#Alice computes gba and comparing gab
gba=fastexpo(gb,a,p)

#Alice computes inverse of gba
invgba=fastexpo(gba,p-2,p)

#Alice decrypts x by computing x=ex*invgba
xout=ex%p*invgba%p
print(xout)

