import hashlib

while True:
    string = input("Digite uma string para gerar um hash: ")
    sha1 = hashlib.sha1(string.encode())
    print(f"Hash SHA-1:", sha1.hexdigest())