import hashlib
import random
import base64

with open('junk.txt','r') as f:
    val = f.read()
difficulty = int(input("ENTER DIFFICULTY BETWEEN 1-10 : "))   

while True:
    nonce = str(random.randint(0,100000000))
    new = nonce + val
    hsh = hashlib.sha256(base64.b64encode(new.encode('utf-8'))).hexdigest()
    print(hsh)

    if hsh[:2] == '0'*difficulty:
        print('nonce value : ',nonce)
        exit()
