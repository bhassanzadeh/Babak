table = []
firstRow = ['Position', 'Club', 'Points']
secondRow = [1, 'Liverpool', 12]
thirdRow = [2, 'Man City', 10]
fourthRow = [3, 'Leicester City', 8]
fifthRow = [4, 'Crystal Palace', 7]

# add the rows to [] one by one
table.append(firstRow)
table.append(secondRow)
table.append(thirdRow)
table.append(fourthRow)
table.append(fifthRow)

# save the file
f = open("epl.txt","w")
for i in table:
    f.write(str(i))
    f.write('\n')
f.close()