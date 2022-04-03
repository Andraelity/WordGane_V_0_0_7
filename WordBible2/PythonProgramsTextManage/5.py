



listOfWords = list()


readFileWords = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\programWordTranslated.txt", "r+")


for i in readFileWords:
	listOfWords.append(i)


readFileWords.close()




listOfPositionSymbols = list()


readFilePositionSymbols = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\getPositionSymbols.csv", "r+")


for i in readFilePositionSymbols:
	listOfPositionSymbols.append(i)


readFilePositionSymbols.close()




listOfPositionNumber = list()


for i in listOfPositionSymbols:

	trimmedString = i.split(",")

	listOfPositionNumber.append(trimmedString)





print()
print()
print()
print()
print()
print()



count = 0

for i in listOfPositionNumber:

	listOfPositionNumber[count] = i[1:len(i) - 1]
	count += 1



for i in listOfPositionNumber:
	print(i)



for i in range(len(listOfWords)):
	print(str(i) + listOfWords[i])


for i in range(len(listOfWords)):
	listOfWords[i] = listOfWords[i][:len(listOfWords[i])-1]

for i in range(len(listOfWords)):
	print(str(i) + listOfWords[i])


for i in listOfPositionNumber:
	print(i)



listOfExclamation = listOfPositionNumber[5]




for i in listOfExclamation:
	print(i)



for i in listOfExclamation:

	wordToFix = listOfWords[int(i)]
	wordToFix += "!"		
	listOfWords[int(i)] = wordToFix
	print(listOfWords[int(i)] + "    " + str(i))



# # learn how to acquire more data in the now, learn how to represent more components


listOfQuestion = listOfPositionNumber[2]


for i in listOfQuestion:
	print(i)


for i in listOfQuestion:

	wordToFix = listOfWords[int(i)]
	wordToFix += "?"		
	listOfWords[int(i)] = wordToFix
	print(listOfWords[int(i)] + "    " + str(i))




listOfDot = listOfPositionNumber[0]


for i in listOfDot:
	print(i)


for i in listOfDot:

	wordToFix = listOfWords[int(i)]
	wordToFix += "."		
	listOfWords[int(i)] = wordToFix
	



listOfComma = listOfPositionNumber[1]


for i in listOfComma:
	print(i)


for i in listOfComma:

	wordToFix = listOfWords[int(i)]
	wordToFix += ","		
	listOfWords[int(i)] = wordToFix




listOfColon = listOfPositionNumber[3]


for i in listOfColon:
	print(i)


for i in listOfColon:

	wordToFix = listOfWords[int(i)]
	wordToFix += ":"		
	listOfWords[int(i)] = wordToFix




listOfSemiColon = listOfPositionNumber[4]


for i in listOfSemiColon:
	print(i)


for i in listOfSemiColon:

	wordToFix = listOfWords[int(i)]
	wordToFix += ";"		
	listOfWords[int(i)] = wordToFix



# wordsProcessed = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\traductionAddedCharacters.txt", "w+")

# for i in listOfWords:
# 	wordsProcessed.write(i)


# wordsProcessed.close()

# # learn how to acquire more data in the now, learn how to represent more components



wordsProcessed = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\traductionAddedCharacters.txt", "w+")

for i in listOfWords:
	wordsProcessed.write(i + "\n")


wordsProcessed.close()
