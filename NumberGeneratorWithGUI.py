from tkinter import *

root = Tk()
root.title("RNG with GUI (this is probably a common thing to make)")
root.geometry('400x400')
root.configure(bg="black")

lbl = Label(root, text="Click the button to generate a number", font=("Arial", 14), bg="black", fg="lightblue")
lbl.grid(row=0, column=0, columnspan=2, pady=20)

def clicked(event=None):
    import random
    value = random.randint(1, 1000)
    updateDisplay(value)

def updateDisplay(myString):
    displayVariable.set(myString)

btn1 = Button(
    root, 
    text="Generate Number", 
    font=("Arial", 16), 
    bg="orange", 
    fg="white", 
    width=20, 
    height=2
)
btn1.bind("<Button-1>", clicked)
btn1.grid(row=1, column=0, columnspan=2, pady=20)

displayVariable = StringVar()
displayLabel = Label(
    root, 
    textvariable=displayVariable, 
    font=("Arial", 24, "bold"), 
    bg="black", 
    fg="green"
)
displayLabel.grid(row=2, column=0, columnspan=2, pady=30)

root.mainloop()