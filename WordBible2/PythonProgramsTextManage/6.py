

listOneLanguage = list()

readFileOneLanguage = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\words_rawData.txt", "r+")

for i in readFileOneLanguage:
	listOneLanguage.append(i[:len(i)-1])

readFileOneLanguage.close()



listTwoLanguage = list()

readFileTwoLanguage = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\traductionAddedCharacters.txt", "r+")

for i in readFileTwoLanguage:
	listTwoLanguage.append(i[:len(i)-1])

readFileTwoLanguage.close()



listPositionVersicle = list()

readPositionVersicle = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\numberOfWordVersicle.txt", "r+")

for i in readPositionVersicle:
	listPositionVersicle.append(i[:len(i)-1])

readPositionVersicle.close()




# countNumberOfCharacters = 0

# for i in listOneLanguage:
# 	for j in i:
# 		countNumberOfCharacters += 1 




listOfStringOneLanguage = list()

countPositionInFileWord = 0

for i in listPositionVersicle:


	appendWordsInString = list()

	for j in range(int(i)):
	
		appendWordsInString.append(listOneLanguage[j + countPositionInFileWord])


	listOfStringOneLanguage.append(appendWordsInString)

	countPositionInFileWord += int(i)




# for i in listOfStringOneLanguage:
# 	print(i)
# 	print()


print()

countCharactersInString = 0

wordPosition = 0;

listOutPutOfStrings = []


for i in listOfStringOneLanguage:
	
	listPositionStringEnd = list()

	for j in i:

		countCharactersInString += len(j)
		countCharactersInString += 1 

		print(countCharactersInString)

		if(countCharactersInString > 110):

			countCharactersInString = 0
			listPositionStringEnd.append(wordPosition)

			countCharactersInString += len(j)
			countCharactersInString += 1 

		wordPosition += 1 


	listManagement = list()
	listManagement = i	

	for k in listPositionStringEnd:
		listManagement.insert(k, "*")


	wordPosition = 0
	countCharactersInString = 0
	print(listManagement)

	listOutPutOfStrings.append(listManagement)

	print()






listOfSizeStringOneLanguage = list()


for i in listOutPutOfStrings:

	listOfSizeStringOneLanguage.append(len(i))
	

writeFileLengtStringOneLanguage = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\outputWordUnityOneLanguageSizesWords.txt", "w+")


for i in listOfSizeStringOneLanguage:

	writeFileLengtStringOneLanguage.write(str(i) + "\n")


writeFileLengtStringOneLanguage.close()


writeFileWordOneLanguage =  open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\outputWordUnityOneLanguage.txt", "w+")


for i in listOutPutOfStrings:	

	for j in i:

		writeFileWordOneLanguage.write(j + "\n")

writeFileWordOneLanguage.close()




############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
###########################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################





listOfStringTwoLanguage = list()

countPositionInFileWord = 0

for i in listPositionVersicle:


	appendWordsInString = list()

	for j in range(int(i)):
	
		appendWordsInString.append(listTwoLanguage[j + countPositionInFileWord])


	listOfStringTwoLanguage.append(appendWordsInString)

	countPositionInFileWord += int(i)




# for i in listOfStringOneLanguage:
# 	print(i)
# 	print()


print()

countCharactersInString = 0

wordPosition = 0;

listOutPutOfStrings = []


for i in listOfStringTwoLanguage:
	
	listPositionStringEnd = list()

	for j in i:

		countCharactersInString += len(j)
		countCharactersInString += 1 

		print(countCharactersInString)

		if(countCharactersInString > 110):

			countCharactersInString = 0
			listPositionStringEnd.append(wordPosition)

			countCharactersInString += len(j)
			countCharactersInString += 1 

		wordPosition += 1 


	listManagement = list()
	listManagement = i	

	for k in listPositionStringEnd:
		listManagement.insert(k, "*")


	wordPosition = 0
	countCharactersInString = 0
	print(listManagement)

	listOutPutOfStrings.append(listManagement)

	print()






listOfSizeStringTwoLanguage = list()


for i in listOutPutOfStrings:

	listOfSizeStringTwoLanguage.append(len(i))
	

writeFileLengtStringTwoLanguage = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\outputWordUnityTwoLanguageSizesWords.txt", "w+")


for i in listOfSizeStringTwoLanguage:

	writeFileLengtStringTwoLanguage.write(str(i) + "\n")


writeFileLengtStringTwoLanguage.close()



writeFileWordTwoLanguage =  open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\outputWordUnityTwoLanguage.txt", "w+")


for i in listOutPutOfStrings:	

	for j in i:

		writeFileWordTwoLanguage.write(j + "\n")

writeFileWordTwoLanguage.close()







































