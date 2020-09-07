import hashlib
import tkinter as tk

## Returns true if number is even ##
def isEven(num):
    if ((num % 2) == 0):
        return True
    else:
        return False

## Hash input and splice in modifications ##
def hashPW():
    inputPW = password.get()
    hashedpw = hashlib.sha256(inputPW.encode()).hexdigest()
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
    resultpw = resultpw[:25]
    result.set(resultpw)

## GUI with tkinter ##
window = tk.Tk()
window.title("Password-Gen")
window.geometry("800x400")

# Input/Output Variables #
result = tk.StringVar()
password = tk.StringVar()
# Widgets ##
promptLabel = tk.Label(window, text="Enter password").place(x = 50, y = 40)
userInput = tk.Entry(window, textvariable=password, width=30).place(x = 50, y = 70)
button = tk.Button(window, text="Generate", command=hashPW).place(x = 50, y = 100)
entryResult = tk.Entry(window, textvariable=result, width=30).place(x = 50, y = 130)

## Main loop ##
window.mainloop()