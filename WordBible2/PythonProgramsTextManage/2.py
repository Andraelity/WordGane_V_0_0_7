


listOfWords = list()


fileToRead = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\words_rawData.txt", "r+")


for i in fileToRead:
	listOfWords.append(i[:len(i)-1])


fileToRead.close()






# for i in listOfWords:	

# 	if





positionDot = list()
positionComma = list()
positionQuestion = list()
positionColon = list()
positionSemiColon = list()
positionExclamation = list()
positionLeftAppostrophe = list()
positionRigthAppostrophe = list()




countWord = 0

for i in listOfWords:

	if(i.find(".") != -1):
		positionDot.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find(",") != -1):
		positionComma.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find("?") != -1):
		positionQuestion.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find(":") != -1):
		positionColon.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find(";") != -1):
		positionSemiColon.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find("!") != -1):
		positionExclamation.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find("‘") != -1):
		positionLeftAppostrophe.append(countWord)


	countWord += 1




countWord = 0


for i in listOfWords:

	if(i.find("’") != -1):
		positionRigthAppostrophe.append(countWord)


	countWord += 1




stringDot = ""

for i in positionDot:
	stringDot += str(i) + ","


stringComma = ""

for i in positionComma:
	stringComma += str(i) + ","


stringQuestion = ""

for i in positionQuestion:
	stringQuestion += str(i) + ","


stringColon = ""

for i in positionColon:
	stringColon += str(i) + ","


stringSemiColon = ""

for i in positionSemiColon:
	stringSemiColon += str(i) + ","


stringExclamation = ""

for i in positionExclamation:
	stringExclamation += str(i) + ","


stringLeftAppostrophe = ""

for i in positionLeftAppostrophe:
	stringLeftAppostrophe += str(i) + ","


stringRightAppostrophe = ""

for i in positionQuestion:
	stringQuestion += str(i) + ","



print()
print()
print()

print(stringDot)

print()
print()
print()



# for i in positionDot:
# 	print(i)



fileToWriteSymbols = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\getPositionSymbols.csv", "w+")


fileToWriteSymbols.write("stringDot," + stringDot + "\n")
fileToWriteSymbols.write("stringComma," + stringComma + "\n")
fileToWriteSymbols.write("stringQuestion," + stringQuestion + "\n")
fileToWriteSymbols.write("stringColon," + stringColon + "\n")
fileToWriteSymbols.write("stringSemiColon," + stringSemiColon + "\n")
fileToWriteSymbols.write("stringExclamation," + stringExclamation + "\n")
fileToWriteSymbols.write("stringLeftAppostrophe," + stringLeftAppostrophe + "\n")
fileToWriteSymbols.write("stringRightAppostrophe," + stringRightAppostrophe + "\n")


fileToWriteSymbols.close()

