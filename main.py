import hashlib
import tkinter as tk
import os

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
    resultpw = resultpw[:25]
    print(resultpw)

## GUI with tkinter ##
window = tk.Tk()
window.title = "Password-Gen"
window.geometry("800x400")

promptLabel = tk.Label(window, text="Enter password").place(x = 300, y = 100)
userinput = tk.Entry(window).place(x = 400, y = 100)
button = tk.Button(window, text="Generate").place(x = 400, y = 150)
result = tk.Entry(window).place(x = 350, y = 180)

window.mainloop()