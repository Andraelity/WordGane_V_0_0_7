

# this file need to start with the paragraph setted with the number
# fixing the order of the elements.

#
#	
#
#	
#
#	WITH THIS FILE WE NEED TO DEFINE
# 	: COPY THE CHAPTER WITH ALL OF ITS LINES WITH THE NUMBER OF VERSICLE
# 	: ADD A NEWLINE CHARACTER AT THE END OF THE CHAPTER
#	
#
#
#
#







f = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\1_Program_LectureBible.txt", "r+")




# print(f.readline())
print()
print()
print()
print()


listOfVersicles = list()

count = 0

listOfString = list()

for i in f:
	listOfString.append(i)



f.close()




for i in listOfString:

	listOfSimbols = list()

	for j in i:

		if(j == "," or j == "." or j == ";" or j == ":"):

			listTupla = list()

			listTupla.append(j)
			listTupla.append(count)

			listOfSimbols.append(listTupla)

		count += 1

	listOfVersicles.append(listOfSimbols)

	count = 0



for i in listOfVersicles:
	print(i)




print()

print()

elementManipule = "this is a element to manipule"


print(elementManipule.split(" "))

print()

print()





listOfVersicles2 = list()

listNumberOfWords = list()



for i in listOfString:

	listOfWords = i.split(" ")

	listOfWords = listOfWords[1:]

	listOfWords[len(listOfWords) - 1] = listOfWords[len(listOfWords) - 1][: len(listOfWords[len(listOfWords) - 1]) - 1]

	listOfVersicles2.append(listOfWords)

	listNumberOfWords.append(len(listOfWords))




for i in listOfVersicles2:
	print(i)


print()

print()

print()



# for i in listOfVersicles2:
# 	for j in i:
# 		print(j)



fileToWrite = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\words_rawData.txt", "w+")

for i in listOfVersicles2:
	for j in i:
		fileToWrite.write(j + "\n")


fileToWrite.close()




fileNumbers = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\numberOfWordVersicle.txt", "w+")

countWords = 0
for i in listNumberOfWords:
	countWords += i
	fileNumbers.write(str(i) + "\n")


fileNumbers.close()

print(countWords)




# what representation i need to set right now.

