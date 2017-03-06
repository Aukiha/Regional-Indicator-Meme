#Tkinter GUI coming to theatres near you

word = input()
word = word.lower()
word = list(word)
counter = len(word)
counter2 = len(word)
position = 0
newword = list()
newpos = 0
n = "0"

while 2 == 2:
        
    while counter2 > 0:
        if word[position] == n or "," or ".":
            print("Numbers/Special Characters are not supported.")
            break
        else:
            counter2 = counter2 - 1
            temp = word[position]
            position = position + 1
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

print("".join(word))
