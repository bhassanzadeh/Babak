# read the file
f = open('caractacus.txt', 'r')
text = f.read()
f.close()
#print(text)

# remove letters
trimmed = ""
droppedLastOne = False
for char in text:
   #new line character
    if char.isalnum():
        if droppedLastOne == False:
            trimmed = trimmed+char
            droppedLastOne = True
        else:
            droppedLastOne = False
    else:
        trimmed=trimmed+char

# save the new file
f = open("trimmed_caractacus.txt","w")
f.write(trimmed)
f.close()