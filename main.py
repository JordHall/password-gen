import hashlib
def isEven(num):
    if ((num % 2) == 0):
        return True
    else:
        return False
prompt = input("Enter password: ")
hashedpw = hashlib.sha256(prompt.encode()).hexdigest()
print(hashedpw)
resultpw = ""
index = 0
for char in hashedpw:
    if index == 3:
        resultpw += "_"
    elif index == 6: 
        resultpw += "@"
    elif index == 9:
        resultpw += "/"
    if isEven(index):
        resultpw += char.upper()
    else:
        resultpw += char
    index += 1
print(resultpw)