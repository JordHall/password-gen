import hashlib

## Returns true if number is even ##
def isEven(num):
    if ((num % 2) == 0):
        return True
    else:
        return False

## Hash input and splice in consistent modifications ##
def hashPW(userInput):
    hashedpw = hashlib.sha256(userInput.encode()).hexdigest()
    resultpw = ""
    index = 0
    for char in hashedpw:
        if index == 3:
            resultpw += "_" # Add 3 symbols ##
        elif index == 6: 
            resultpw += "@"
        elif index == 9:
            resultpw += "/"
        if isEven(index):
            resultpw += char.upper() # Convert some to uppercase #
        else:
            resultpw += char
        index += 1
    print(resultpw)

## Main loop ##
while True:
    prompt = input("Enter password: ")
    hashPW(prompt)