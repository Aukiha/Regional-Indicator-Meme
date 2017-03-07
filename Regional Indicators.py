#Just don't use numbers fam

from tkinter import *
master = Tk()

text = Entry(master, width=50)
text.pack()

text.focus_set()

def callback():
    word = text.get()
    word = word.lower()
    word = list(word)
    counter = len(word)
    position = 0


    while counter > 0:
        if word[position] == " ":
            counter = counter - 1
            word[position] = (" ")
            temp = word[position]
            position = position + 1
        else:
            counter = counter - 1
            temp = word[position]
            word[position] = (":regional_indicator_" + temp + ": ")
            position = position + 1
    counter =- 1

    word = "".join(word)
    master.clipboard_append(word)
    messagebox.showinfo("Conversion Complete", "Copied to clipboard")

b = Button(master, text="Convert to Regional Indicators", width=30, command=callback)
b.pack()

mainloop()

