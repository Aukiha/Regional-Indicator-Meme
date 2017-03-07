from tkinter import *

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
            counter = counter - 1
            word[position] = (" ")
            temp = word[position]
            position = position + 1
        elif word[position] == "1":
            counter = counter - 1
            word[position] = (":one:")
            position = position + 1
        elif word[position] == "2":
            counter = counter - 1
            word[position] = (":two:")
            position = position + 1
        elif word[position] == "3":
            counter = counter - 1
            word[position] = (":three:")
            position = position + 1
        elif word[position] == "4":
            counter = counter - 1
            word[position] = (":four:")
            position = position + 1
        elif word[position] == "5":
            counter = counter - 1
            word[position] = (":five:")
            position = position + 1
        elif word[position] == "6":
            counter = counter - 1
            word[position] = (":six:")
            position = position + 1
        elif word[position] == "7":
            counter = counter - 1
            word[position] = (":seven:")
            position = position + 1
        elif word[position] == "8":
            counter = counter - 1
            word[position] = (":eight:")
            position = position + 1
        elif word[position] == "9":
            counter = counter - 1
            word[position] = (":nine:")
            position = position + 1
        elif word[position] == "0":
            counter = counter - 1
            word[position] = (":zero:")
            position = position + 1
        else:
            counter = counter - 1
            temp = word[position]
            word[position] = (":regional_indicator_" + temp + ": ")
            position = position + 1
    counter =- 1

#Joins together the converted words
    word = "".join(word)
    master.clipboard_clear()
    master.clipboard_append(word)
    messagebox.showinfo("Conversion Complete", "Copied to clipboard")

#Convert to Regional Indicators button
b = Button(master, text="Convert to Regional Indicators", width=30, command=callback)
b.pack()

mainloop()

