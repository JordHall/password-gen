import hashlib
prompt = input("Enter password: ")
hash1 = hashlib.md5(prompt.encode())
hash2 = hashlib.sha1(prompt.encode())
hash3 = hashlib.sha256(prompt.encode())
hashes = {hash1, hash2, hash3}
for item in hashes:
    print(item.hexdigest())