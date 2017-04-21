
from tkinter import *
from tkinter import messagebox

#Initilizes Tkinter window
master = Tk()

#Entry box
text = Entry(master, width=50)
text.pack()

text.focus_set()

#Main word conversion function
def callback():
    word = text.get()
    word = word.lower()
    word = list(word)
    counter = len(word)
    position = 0

#Checks what each value in the entry is, then converts accordingly
    while counter > 0:
        if word[position] == " ":
            counter -= 1
            word[position] = (" ")
            temp = word[position]
            position += 1
        elif word[position] == "b":
            counter -= 1
            word[position] = (":b: ")
            position += 1
        elif word[position] == "1":
            counter -= 1
            word[position] = (":one: ")
            position += 1
        elif word[position] == "2":
            counter -= 1
            word[position] = (":two: ")
            position += 1
        elif word[position] == "3":
            counter -= 1
            word[position] = (":three: ")
            position += 1
        elif word[position] == "4":
            counter -= 1
            word[position] = (":four: ")
            position += 1
        elif word[position] == "5":
            counter -= 1
            word[position] = (":five: ")
            position += 1
        elif word[position] == "6":
            counter -= 1
            word[position] = (":six: ")
            position += 1
        elif word[position] == "7":
            counter -= 1
            word[position] = (":seven: ")
            position += 1
        elif word[position] == "8":
            counter -= 1
            word[position] = (":eight: ")
            position += 1
        elif word[position] == "9":
            counter -= 1
            word[position] = (":nine: ")
            position += 1
        elif word[position] == "0":
            counter -= 1
            word[position] = (":zero: ")
            position += 1
        elif word[position] == ";":
            counter -= 1
            word[position] = (";")
            position += 1
        elif word[position] == ",":
            counter -= 1
            word[position] = (",")
            position += 1
        elif word[position] == ".":
            counter -= 1
            word[position] = (".")
            position += 1
        elif word[position] == "?":
            counter -= 1
            word[position] == ("?")
            position += 1
        elif word[position] == "!":
            counter -= 1
            word[position] == ("!")
            position += 1
        elif word[position] == "-":
            counter -= 1
            word[position] == ("-")
            position += 1
        elif word[position] == "$":
            counter -= 1
            word[position] == ("-")
            position += 1
        elif word[position] == "&":
            counter -= 1
            word[position] == ("&")
            position += 1
        else:
            counter -= 1
            temp = word[position]
            word[position] = (":regional_indicator_" + temp + ": ")
            position += 1
    counter =- 1

#Joins together the converted words
    word = "".join(word)
    master.clipboard_clear()
    master.clipboard_append(word)
    messagebox.showinfo("Conversion Complete", "Copied to clipboard")

l = Label(master, text="Enter text, hit convert, and enjoy your meme")
l.pack()

d = Label(master, text="Discord has a 2,000 character limit, so keep it short.")
d.pack()

#Convert to Regional Indicators button
b = Button(master, text="Convert to Regional Indicators", width=30, command=callback)
b.pack()

mainloop()
