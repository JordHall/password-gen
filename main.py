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
    inputPW = inputPW + applySalt()
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
    updateNotif("Password generated")

## Copy to clipboard ##
def copyClipboard():
    window.clipboard_clear()
    window.clipboard_append(result.get())
    window.update()
    updateNotif("Copied to clipboard")

## Update notification ##
def updateNotif(note):
    print(note)
    notification.set(note)

## Apply salt ##
def applySalt():
    option = defaultOpt.get()
    if (option == defaultOpt):
        return ""
    else:
        return option

## Push notification on option change ##
def optionChanged(*args):
    updateNotif(defaultOpt.get() + " account/salt selected")

## GUI with tkinter ##
window = tk.Tk()
window.title("Password-Gen")
window.geometry("300x280")
window.configure()

# Input/Output Variables #
result = tk.StringVar()
password = tk.StringVar()
notification = tk.StringVar()
defaultOpt = tk.StringVar()
options = ( ## Salt/account options
    "default",
    "google",
    "twitter",
    "facebook",
    "instagram",
    "email",
    "steam"
)
defaultOpt.set(options[0])
defaultOpt.trace("w", optionChanged)

## Widgets ##
promptLabel = tk.Label(window, text="Enter Password:").place(x = 50, y = 40)
userInput = tk.Entry(window, textvariable=password, width=30).place(x = 50, y = 70)
inputBtn = tk.Button(window, text="Generate", command=hashPW).place(x = 50, y = 100)
resultLabel = tk.Label(window, text="Hashed Password:").place(x = 50, y = 140)
entryResult = tk.Entry(window, textvariable=result, width=30).place(x = 50, y = 170)
copyBtn = tk.Button(window, text="Copy", command=copyClipboard).place(x = 50, y = 200)
notifLabel = tk.Label(window, textvariable=notification, fg="red").place(x = 10, y = 250)
optionDrpDwn = tk.OptionMenu(window, defaultOpt, *options).place(x = 200, y = 10)

## Main loop ##
window.mainloop()