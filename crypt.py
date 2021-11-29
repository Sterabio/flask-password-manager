import rsa
from cryptography.fernet import Fernet
import os.path

def decrypt_data(k,d):
    #print(d)
    prkey = open(k,'rb')
    pkey = prkey.read()
    private_key = rsa.PrivateKey.load_pkcs1(pkey)

    # with open('encrypted_key','rb') as e:
    #     ekey = e.read()
    #print(type(d))

    dpubkey = rsa.decrypt(d,private_key)
    data = bytes.decode(dpubkey)
    return data

    # cipher = Fernet(dpubkey)

    # encrypted_data = open('encrypted_file','rb')
    # edata = encrypted_data.read()


    # decrypted_data = cipher.decrypt(edata)

    # print(decrypted_data.decode())

def encrypt_data(s):
    #data = str.encode(s)
    data = s
    # try:
    pkey = open('.data/publickey.key','rb')
    pkdata = pkey.read()

# load the file
    pubkey = rsa.PublicKey.load_pkcs1(pkdata)

    # encrypt the symmetric key file with the public key
    encrypted_data = rsa.encrypt(data,pubkey)

# with open('encrypted_key','wb') as ekey:
#     ekey.write(encrypted_key)

    return encrypted_data
    # except:
    #     print("no public key")
    #     exit()



def create_keys(path):

    # create the pub & private keys
    (pubkey,privkey)=rsa.newkeys(2048)

    # write the public key to a file
    if not os.path.isfile('.data/publickey.key') and not os.path.isfile(f'{path}/privkey.key'):
        pukey = open('.data/publickey.key','wb')
        pukey.write(pubkey.save_pkcs1('PEM'))
        pukey.close()
    # else:
    #     print("public key already exists")

    # write the private key to a file
    # if not os.path.isfile(f'{path}/privkey.key'):
        prkey = open(f'{path}/privkey.key','wb')
        prkey.write(privkey.save_pkcs1('PEM'))
        prkey.close()
    else:
        print("private key already exists")

# h = encrypt_data("hi")
# #h = h.decode('utf-8').strip()
# h = str(h)
# #h = h.decode()
# print(h)
# print("")
# #print(str(h))

# #create_keys(".data")
# a = decrypt_data("pkt/privkey.key",h)
# print(a)