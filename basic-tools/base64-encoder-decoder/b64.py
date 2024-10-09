import base64
import argparse

# Function to encode string to base64
def encode_b64(string):
    return base64.b64encode(string)

# Function to decode string from base64
def decode_b64(string):
    return base64.b64decode(string)

# Function to read argument from the command line
def read_args():
    parser = argparse.ArgumentParser(prog="python b64.py", 
                                     description="This program encodes a string into base64 and decodes base64 value into string.")
    parser.add_argument("-i", "--input", type=str, help="The input value to be encoded/decoded.")
    parser.add_argument("-a", "--action", type=str, help="The action to be performed.Provide value `encode` for encoding to base64 and `decode` for decoding from base64.")
    return parser.parse_args()

if __name__=="__main__":
    args = read_args()
    data = ""
    if args.action == "encode" or args.action == "decode":
        if args.action == "encode":
            data = encode_b64(args.input)
            print("Base64 encoded value is: " + data)
        else:
            data = decode_b64(args.input)
            print("Original value is: " + data)
    else:
        print("Incorrect option provided. Please provide a correct action - `encode` for encoding to base64 and `decode` for decoding from base64.")



