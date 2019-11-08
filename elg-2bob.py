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


######BOB



#Recieved from Alice
p=131
g=10
ga=83


#Bob define message to send
xin=87
#Bob choose secret key b
b=5 #TEMP STEP, REPLACE WITH FUNCTIONALITY

#Bob calculate gb=g**b%p AND gab=ga**b%p
gb=fastexpo(g,b,p)
gab=fastexpo(ga,b,p)

#Bob encrypt message x where ex=x*gab
ex=xin%p*gab%p

#Bob sends to Alice: gb, encrypted message ex
print("Bob sends to Alice: ")
print(gb,ex)

print("Bob now knows ga, b, can compute gab")
print("Alice now knows ga, gb, can compute gba")
