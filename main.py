import bcrypt
salt = bcrypt.gensalt()
test = bcrypt.hashpw(b"test",salt)
print(test)