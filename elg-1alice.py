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


############MAIN ELGAMAL ENCRYPTION/DECRYPTION SEQUENCE############
######Initialize
#Generate message x
xin=87  #TEMP STEP, REPLACE WITH FUNCTIONALITY

#Generate generator p
p=131 #TEMP STEP, REPLACE WITH FUNCTIONALITY

#Alice randomly choose and validate generator g
g=10 #TEMP STEP, REPLACE WITH FUNCTIONALITY


######ALICE
#Alice choose secret key a
a=3 #TEMP STEP, REPLACE WITH FUNCTIONALITY


#Alice calculate ga=g**a%p to send Alice-->Bob
ga=fastexpo(g,a,p)

#Alice sends to Bob: prime p, generator g, ga
print("Alice sends to Bob: ")
print(p,g,ga)
