import hashlib

def generate_md5_hash(string):
    return hashlib.md5(string)

def get_input():
    i = input("Enter the string: ")
    return i

if __name__=="__main__":
    data = get_input()
    hash_value = generate_md5_hash(data.encode('utf-8'))
    print("MD5 hash for `"+ data + "` is: " + str(hash_value.hexdigest()))