############DEFINE SUPPORITNG FUNCTIONS############
import random
import math
from math import ceil, sqrt

#Fast Exponentiation Algorithm
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

#Extended Euclidean Algorithm, return gcd
def xeuclid(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd,x,y

	
#ElGamal encryption function
def elgencrypt(n, pub, priv, xin):
	k=fastexpo(pub, priv, n)
	ex=xin%n*k%n
	return ex

#ElGamal decryption function	
def elgdecrypt(n, pub, priv, ex):
	k=fastexpo(pub,priv,n)
	invk=fastexpo(k,n-2,n)
	xout=ex%n*invk%n
	return xout


#RSA encrytion Function
def rsaencrypt(x,e,n):
	xout=fastexpo(x,e,n)
	return xout

#RSA decryption function
def rsadecrypt(p,q,e,ex):
	n=p*q
	phin=(p-1)*(q-1)
	
	# Calculate d by applying extended euclidean algo to find gcd(phi(N), e) in form 1=y*phi(N)+e*d
	_,_,d=xeuclid(phin,e)
	
	# Translates d value from - to + if applicable, otherwise will yiled same + value
	d=d%phin
	
	# Calculate x=ex^z%N
	ex=fastexpo(ex,d,n)
	
	return ex


#Baby-Step-Giant-Step Algorithm, Solve for x in h=g^x%p
def bgstep(g, h, p):
    
    N = int(ceil(sqrt(p - 1)))
    tbl={fastexpo(g,i,p): i for i in range(N)}
    
    c=fastexpo(g,N*(p-2),p)

    for j in range(N):
        y=(h*fastexpo(c,j,p))%p
        if y in tbl:
            return j*N+tbl[y]

    return None
    

#Miller-Rabin Primality Test
def milrab(d, n):       
    a=2+random.randint(1, n-4); 
    x=fastexpo(a,d,n); 
  
    if (x==1 or x==n-1): 
        return True; 
  
    while (d!=n-1): 
        x=(x*x)%n; 
        d*=2; 
  
        if (x==1): 
            return False; 
        if (x==n-1): 
            return True; 
  
    return False; 

#Leverage Miller-Rabian to determine if number is prime
def isPrime(n,k): 
      
    if (n<=1 or n==4): 
        return False; 
    if (n<=3): 
        return True; 
  
    d=n-1; 
    while (d%2==0): 
        d//=2; 
  
    for i in range(k): 
        if (milrab(d,n)==False): 
            return False; 
  
    return True;
    
    
 #Leverage Miller-Rabian and isPrime to generate a prime number
 #accepts input s for size of number. s=digits, i.e. s=6 = range(100000,999999)
def primegen(s):
	k=4
	p=False
	while not p:
		n=random.randint(10**(s-1),10**s-1)
		p=isPrime(n,k)
	
	return n

#RSA generate e value coprime to phi(n)
def rsakeygen(p,q):
	n=p*q
	phin=(p-1)*(q-1)
	gcd=0
	while gcd!=1:
		etest=random.randint(1,n-1)
		gcd,_,_=xeuclid(phin,etest)
		
	return etest

	
#Generate ElGamal g value
def getprimroot(n):   	
 	a = 2
 	b = (n - 1) // a

 	if n == 2:
 		return 1

 	while(1):
 		testn = random.randint( 2, n-1 )
 		if not (fastexpo(testn, (n-1) // a, n) == 1):
 			if not (fastexpo(testn, (n-1) // b, n) == 1):
 				return testn


#Generate ElGamal private key (a/b value) where q is the mult order of g in Z_N
def privkeygen(n,g):
	for q in range(2,n):
		#g^q mod N = 1
		if fastexpo(g,q,n)==1:
			key=random.randint(1,q)
			break
	return key


#Pollards Rho Algorithm, used to factor p & q values given n (crack RSA encryption)
#from fractions import gcd
def polrho(n):
    x=2; y=2; d=1
    f=lambda x: (x**2+1)%n
    while d==1:
        x=f(x); y=f(f(y))
        d,_,_=xeuclid(abs(x-y),n)
    if d != n: return d
