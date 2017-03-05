word = input()
word = word.lower()
word = list(word)
counter = len(word)
position = 0
newword = list()
newpos = 0

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
