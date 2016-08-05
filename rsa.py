#Generating two random numbers
import random
a=7111411111711232535883104105108112973277117114971536356363563967039560953609357630497576304987652454264624624642
#0810532741011011181051161049732771171121129710897
b=8105327410110111810511610497327711711211297108977364363563463463635653456246464261234635753757624652452464742643734586489468469856846979468
#a=9
#b=23
#print('The two random numbers are')
p=random.randrange(a, b)
##print p
q=random.randrange(a, b)
##print q
#Finding two prime numbers using Fermat's prime checker
def modex(x,y,N):     # x power y mod N
    if (y == 0):
        return 1
    z = modex(x, y/2,N) # this creates
    if (y%2 == 0):      # for even numbers
        return z*z%N
    else:
        return x*z*z%N    #for odd numbers
def findPrim(n):
    p=n
    while (True):
        if (modex(2,n-1,n) == 1):# uses the Fermat theorem
            return n
            break
        else:
            n += 1
            continue
#print('The values of p and q are')
p=findPrim(p);
q=findPrim(q);
#p=11
#q=13
#print p;
#print q;
#Finding the value of the modulus 'n'
n=p*q
##print ('The modulus is n=%ld') %n
#Finding the totient
totient=(p-1)*(q-1)
##print ('The totient is %ld') %totient
#Computation of the Encryption key
e=random.randrange(2, totient)
e=2

def findGCD(k,l):
while (l!= 0):
(k, l) = (l, k % l)
return k


def findPublicKey(rand):
while(findGCD(rand,totient)!=1):
rand+=1
rand=e
key=0
while True:
#pubKey=findPublicKey(random.randrange(2, totient))!=0
key=random.randrange(2, totient)
while(findGCD(key,totient)!=1):
key+=1
if(key<totient):
break

e=key
#print 'public key is %d'%e


##print 'random %d, totient %d) for which the GCD is 1  is answer
%d'%(rand,totient,e)
#e = 7
def xgcd_new(e,totient):
if(totient == 0):
return [1,0,a]
t = xgcd_new(totient, e%totient)
return [t[1], t[0]-e/totient*t[1], t[2]]
def xgcd(e,totient):
    s=totient
    #dupkey=e
    prevx, x = 1, 0; prevy, y = 0, 1
    while totient:
        q = e/totient
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        e, totient = totient, e%totient
    if(e==1):
        if(prevx<0):
            prevx=s+prevx
            ##print 'Decryption key d=%ld'%prevx
            return prevx
            #return prevx,prevy,e

        else:
            ##print 'Decryption key d=%ld'%prevx
            return prevx
            #return prevx,prevy,e

#d= xgcd(e,totient)
xgcd_out = xgcd_new(e,totient)
d = xgcd_out[0]
if (d < 0):
d = totient + d
#d = 103
#print 'Decryption key d=%ld'%d
# Text to number conversion
# use ord() to convert a character to its ASCII code
# use ` ` to convert a number to a string
def messToNum(m):
    s = ''
    for k in range(0,len(m)):

        s = s+`ord(m[k])`
    return int(s)
M = messToNum('Group 5:Shilpa Murali Jeevitha Muppala prarthana
varadaraj rajitha reddy jabha')
#M=66
#print 'given message is Group 5:Shilpa Murali Jeevitha Muppala
prarthana varadaraj rajitha reddy jabha'
print 'asci value of given message is %d' % M
#Encrypting the Message
def Encrypt(x,y,N):     # x power y mod N
    if (y == 0):
        return 1
    z = modex(x, y/2,N) # this creates
    if (y%2 == 0):      # for even numbers
        return z*z%N
    else:
        return x*z*z%N
E=Encrypt(M,e,n);
#print'Encrypted Message is %ld'%E
#Decrypting the message
def Decrypt(x,y,N):     # x power y mod N
    if (y == 0):
        return 1
    z = modex(x, y/2,N) # this creates
    if (y%2 == 0):      # for even numbers
        return z*z%N
    else:
        return x*z*z%N
D=Decrypt(E,d,n);
#print'Decrypted Message is %ld'%D
#Converting the decrypted message to Original text
def numToMess(D):
    s = str(D)
    k= 0
    text = ''
    while (k < len(s)-1):
        if (s[k] == '1'):
            text=text+chr(int(s[k:k+3]))
            k = k+3
        else:
            text=text+chr(int(s[k:k+2]))
            k = k+2
    return text
O= numToMess(D);
print('The original text after decryption is %s')%O
