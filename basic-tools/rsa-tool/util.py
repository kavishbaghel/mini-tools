import argparse
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

'''
This function generates an rsa private key and public key pair in PEM format for encryption and decryption purposes.

Function Parameters:

             size` - The size of the RSA key. Allowed values - 256, 384, and 512. Default - 256.

            `private_key_path` - The actual path where the private key will be stored after generation. 
                                  If path is not provided the key will be save in the current working directory with the name private.pem.

            `public_key_path` - The actual path where the public key will be stored after generation.
                                If path is not provided the key will be save in the current working directory with the name public.pem.
            
'''
def genrate_rsa_key_pair(size=256, private_key_path="private.pem", public_key_path="public.pem"):
    # Generate the key based on the key size. If provided key size is incorrect then return an error.
    if size == 256 or size == 384 or size == 512:
        private_key = RSA.generate(size*8)
    else:
        raise RuntimeError('The key size provided is not correct. The allowed key sizes are 256, 384, and 512.')
    
    # Create the private key file
    with open(private_key_path, 'wb') as prv:
        prv.write(private_key.export_key())

    # Create the public key using the private key and save it to a file
    with open(public_key_path, "wb") as pub:
        pub.write(private_key.public_key().export_key())

'''

'''
def encrypt_data(public_key_path="public.pem", data=None, hash_algo="SHA256"):
    try:
        with open(public_key_path, "rb") as pub:
            data = pub.read()
        pub_key = RSA.import_key(data)
        if hash_algo == "SHA256" or hash_algo == "SHA384" or hash_algo == "SHA512":
            cipher = PKCS1_OAEP.new(hashAlgo=hash_algo, key=pub_key)
        else:
            raise ValueError("Wrong hash algo provided. Allowed Values - SHA256, SHA384, and SHA512")
        return cipher.encrypt(data)
    except Exception as e:
        print("Following error occured: " + e)

'''
'''
def decrypt_data(private_key_path="private.pem", data=None, hash_algo="SHA256"):
    try:
        with open(private_key_path, "rb") as prv:
            data = prv.read()
        prv_key = RSA.import_key(data)
        if hash_algo == "SHA256" or hash_algo == "SHA384" or hash_algo == "SHA512":
            cipher = PKCS1_OAEP.new(hashAlgo=hash_algo, key=pub_key)
        else:
            raise ValueError("Wrong hash algo provided. Allowed Values - SHA256, SHA384, and SHA512")
        return cipher.decrypt(data)
    except Exception as e:
        print("Following error occured: " + e)