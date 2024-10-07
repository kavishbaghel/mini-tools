import basicauth
username = input("Enter the username: ")
password = input("Enter the password: ")
result = basicauth.encode(username, password)
print("Basic Auth string is - ", result)
