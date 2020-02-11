
# RSA-ElGamal Encryption Demonstration

**Overview:** The collection of programs described below intends to function as an elementary implementation of RSA and ElGamal encrypted communication. The goal is to demonstrate the capabilities of Alice and Bob too successfully exchange encrypted communication, as well as the ability for Eve to intercept the protected data and use it to crack the encrypted communication intended for Alice and Bob.
<br><br>
**Program Files:** The following 7 files have been included and are required to run the full implementations:<br>

 - rsaAlice.py: User acts as Alice in an RSA communication<br>
 - rsaBob.py: User acts as Bob in an RSA communication<br>
 - rsaEve.py: User acts as Eve in an RSA communication<br>
 - elgAlice.py: User acts as Alice in an ElGamal communication<br>
 - elgBob.py: User acts as Alice in an ElGamal communication<br> 
 - elgEve.py: User acts as Alice in an ElGamal communication<br>
 - support.py: Contains all of the calculation functions used in the driver programs. Obviously this file must exist in the same directory as the driver files in order for everything to operate properly.<br><br>

**ElGamal Implementation:** Because the ElGamal encryption method relies on establishing a shared secret, Alice and Bob can both play different parts in initiating, sending, and receiving messages. For the purpose of this demonstration, the ElGamal implementation operates with the following rules:<br>

 - Alice is responsible for initializing the communication by
   generating N,g,and g^a values<br>
 - Bob is responsible for responding with a g^b value, which allows
   Alice and Bob to establish their shared secret key k=(g^a)^b<br>
 - At this point, both Alice and Bob are prompted with a choice of
   responsibility for encrypting or decrypting a message. Obviously
   users Alice and Bob must select opposite roles and follow the
   on-screen instructions for the message to properly encrypt and
   decrypt. Eve must also be able to identify who (Alice or Bob) created
   and sent the ciphertext to be able to use the correct combination of
   keys to crack the message.

<br><br>
**RSA Implementation:** For the purpose of this demonstration, the RSA implementation operates with the following rules:<br>
- Alice is responsible for initializing the communication by generating N and e values<br>
- Bob is responsible for encrypting a message with the keys provided by Alice<br>
- Alice is responsible for receiving Bob’s ciphertext and decrypting using the p and q values that were used to generate N in the initialization step.
<br><br>
**Program Operation:** The programs have been developed in Python 2.7 and tested on Ubuntu 16.04. The programs are designed to be run exclusively in the terminal with the following input limitations:<br>
- On-screen instructions have been included in the program to indicate what values to input at a given time. All input is accepted one value at a time (e.g. if prompted for N,g,g^a: inputN, press enter, input g, press enter, input g^a, and press enter). All input values must be integers, including selecting options when prompted on-screen. For example, When cracking ElGamal encrypted message, Eve must identify the source of the cipher text by selecting “Alice (1) or Bob (2). User Eve must input the respective 1 or 2 to make the correct selection.<br>
- The program will crash if non-integer input is entered.<br>
- Certain error messages have been coded to advise the user of invalid input, but the program will still crash and must be restarted. For example, if Bob tries to use RSA to encrypt a message where value x>n, the user will be prompted of the error but the program will still crash.<br>
- Obviously it is the responsibility of the user to accurately communicate and input values when transferring between users.
<br><br>
**ElGamal Encryption Algorithm Abstract:** The following abstract steps are the basis for which the ElGamal implementation has been programmed.  For simplicity, this abstract has Bob encode a message (steps 9-10) and Alice decode the message (steps 11-12). The code implemented allows Alice and Bob to decide at runtime who will be responsible for encoding and decoding the message.<br>
1) Alice: Generate large prime number N to be used as the order of the group<br>
2) Alice: Find generator g for the group Z_N<br>
3) Alice: Choose A in Z_N, and calculate g^A<br>
4) Alice: Send N, g, and g^A to Bob<br>
5) Bob: Receive N, g, and g^A from Alice<br>
6) Bob: Choose B in Z_N, and calculate g^B<br>
7) Bob: Send g^B back to Alice<br>
8) Bob: Calculate k = (g^A)^B (shared secret with Alice)<br>
9) Bob: Encode message x in the form e(x) = x*k<br>
10) Bob: Send g^B and e(x) to Alice<br>
11) Alice: Bob: Calculate k = (g^A)^B (shared secret with Bob)<br>
12) Alice: Calculate inverse of k to decode message e(x) received from Bob to read original message x.<br>
13) Eve: Intercept N, g, g^A, and g^B<br>
14) Eve: Crack private keys A and B<br>
15) Eve: With cracked keys A and B, compute k = (g^A)^B<br>
16) Eve: Calculate inverse of k to decode message e(x) intercepted to read original message x.
<br><br>


**RSA Encryption Algorithm Abstract:** The following abstract steps are the basis for which the RSA implementation has been programmed.<br>
1) Alice generates primes p and  q  and publishes encryption key N,e, where N=p*q<br>
2) Bob encrypts message x  in the form e(x)=x^e%N and sends e(x) to Alice<br>
3) Alice calculates phi(N) = (p-1)*(q-1)<br>
4) Alice calculates d by applying Extended Euclidean Algorithm to find gcd(phi(N), e) in the form 1=y*fi(N)+e*d<br>
5) Alice calculates d=d%fi(N) to find a multiplicative equivalent in the event that d<0 in step 4<br>
6) Alice calculates x=e(x)^d%N to read original message x<br>
7) Eve intercepts N, e, e(x)<br>
8) Eve factors N to determine p and q<br>
9) Eve uses p,q,N,e,e(x) to decode the message following steps 3-6<br>
