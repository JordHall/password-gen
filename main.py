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
    print("Password generated")

def copyClipboard():
    window.clipboard_clear()
    window.clipboard_append(result.get())
    window.update()
    print("Password copied")

## GUI with tkinter ##
window = tk.Tk()
window.title("Password-Gen")
window.geometry("300x280")
window.configure()

# Input/Output Variables #
result = tk.StringVar()
password = tk.StringVar()
# Widgets ##
promptLabel = tk.Label(window, text="Enter Password:").place(x = 50, y = 40)
userInput = tk.Entry(window, textvariable=password, width=30).place(x = 50, y = 70)
inputBtn = tk.Button(window, text="Generate", command=hashPW).place(x = 50, y = 100)
resultLabel = tk.Label(window, text="Hashed Password:").place(x = 50, y = 140)
entryResult = tk.Entry(window, textvariable=result, width=30).place(x = 50, y = 170)
copyBtn = tk.Button(window, text="Copy", command=copyClipboard).place(x = 50, y = 200)

## Main loop ##
window.mainloop()