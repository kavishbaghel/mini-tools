import base64
import argparse

def basicauth_generator(username, password, file):
    creds = f"{username}:{password}"
    basic_auth = "Basic " + base64.b64encode(creds.encode('utf-8')).decode('utf-8')
    with open(file, "w") as f:
        f.write(basic_auth)

def parse_arguments():
    parser = argparse.ArgumentParser(prog="python basicauth.py", 
                                     description="This program takes a username and password as input and generates basic auth header and saves it to the specified file.")
    parser.add_argument("-u", "--username", type=str, help="Username for generating the basic auth file")
    parser.add_argument("-p", "--password", type=str, help="Password for generating the basic auth file")
    parser.add_argument("-f", "--file", type=str, help="File path for storing the basic auth credentials")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    uname = args.username
    passwd = args.password
    file_path = args.file
    try:
        basicauth_generator(uname, passwd, file_path)
    except Exception as e:
        print("The basic auth credentials could not be genrated due to the following error - ", e)
