

listOfWords = list()

fileToRead = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\words_rawData.txt", "r+")


for i in fileToRead:
	listOfWords.append(i)


fileToRead.close()



listCleanedSymbol = list()

for i in listOfWords:

	wordContainer = i[:len(i)-1]

	wordContainer = wordContainer.replace(".", "")
	wordContainer = wordContainer.replace(",", "")
	wordContainer = wordContainer.replace("?", "")
	wordContainer = wordContainer.replace(":", "")
	wordContainer = wordContainer.replace(";", "")
	wordContainer = wordContainer.replace("!", "")


	listCleanedSymbol.append(wordContainer)



listCleanedApphostrophe = list()

for i in listCleanedSymbol:

	wordContainer = i.strip("‘")
	wordContainer = wordContainer.strip("’")

	listCleanedApphostrophe.append(wordContainer)



for i in listCleanedApphostrophe:
	print(i)


fileToWrite = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\programWordCleaned.txt", "w+")




for i in listCleanedApphostrophe:
	fileToWrite.write(i + "\n")


fileToWrite.close()

# stringDot
# stringComma
# stringQuestion
# stringColon
# stringSemiColon
# stringExclamation
# stringLeftAppostrophe
# stringRightAppostrophe