import hashlib
import argparse

def get_args():
    parser = argparse.ArgumentParser(prog="python hashgen.py", 
                                     description="This program returns hash value for a string using the desired hash function.")
    parser.add_argument("-i", "--input", type=str, help="The input value.")
    parser.add_argument("-f", "--function", type=str, help="The hash function to be used. Allowed values are - md5, sha256, sha384, and sha512.")
    return parser.parse_args()

def generate_hash(hf, string):
    if hf == "md5":
        return hashlib.md5(string.encode('utf-8')).hexdigest()
    elif hf == "sha256":
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
    elif hf == "sha384":
        return hashlib.sha384(string.encode('utf-8')).hexdigest()
    elif hf == "sha512":
        return hashlib.sha512(string.encode('utf-8')).hexdigest()
    else:
        return "Please provide an allowed hash function value from the following - md5, sha256, sha384, and sha512."

