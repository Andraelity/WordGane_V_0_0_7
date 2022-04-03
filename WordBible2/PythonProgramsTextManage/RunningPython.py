variableCodigo = "this is a list of element capable to make me understand how to manage lists"


elementoLista = variableCodigo.split(" ")

for i in elementoLista:
	print(i)

print()
print()
print()
print()

elementoLista = elementoLista[1:]

for i in elementoLista:
	print(i)



codigo = "elemento"

variable = codigo.find(".")

print(variable)



# fileToRead = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\textExcel.csv", "w+")



# fileToRead.write("here,is,this,code\n")
# fileToRead.write("here, is, another, code")

# fileToRead.close()



# fileToRead = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\textExcel.csv", "r+")

# for i in fileToRead:
# 	print(i)

# fileToRead.close()




# what is the next element in the now capable to set a clear reality capable to load the perception i need to define
# a clear motion capable to define a motion, a movement capable to enhance what i could became.





variableCodigo = "bu;;;ona; quee;comovas"

puntoEmprendimiento = variableCodigo.replace(";","")


print(puntoEmprendimiento)


definitionCodigo = "variableLanguage"

puntoEmprendimiento0 = definitionCodigo.replace(";","")

print(puntoEmprendimiento0)



thisIsCode = ";elemento;elemento;"

varThisIsCode = thisIsCode.strip(";")


print(varThisIsCode)





# that code line is just to powerful, is a description capable to set the motion in need to structure.



# learn a clear representations of the qualities.






# approach a clear description of this element

# i need to add to the file a new description, of symbols
# creating a vision loaded with more representation




# what is the vision i need to set
listOfPosition = list()

readFilePositionSymbols = open("D:\\INTERNET\\Wiki-Andresito-16-WORK\\PYTHONNOUNITY\\getPositionSymbols.csv", "r+")


for i in readFilePositionSymbols:
	listOfPosition.append(i)



readFilePositionSymbols.close()


for i in listOfPosition:
	
	for j in range(len(i)):
		
		print(str(j) + "   " + i[j])


	print("salida salida")
	print(len(i))
	print("salida salida")
	print("salida salida")



for i in listOfPosition:
	
	for j in range(len(i)):
		
			
		print(str(j) + "   " + i[j])


	print("salida salida")
	print(len(i))
	print("salida salida")
	print("salida salida")




# WHAT I NEED RIGHT NOW IS TO BE ABLE TO GENEATE THE PERSONALIZATION OF THE CHARACTERS
# DEFINE A EXPRESSION IN THE NOW LOADED WITH MORE UNDERSTANDING



# sense how to interact with the matter
# by enhancing the production of the language



wordPosition = []


for i in range(10):
	if(i % 2 == 0):
		wordPosition.append("hereeee")
	else:
		wordPosition.append("Whyyyyy")


print(wordPosition)

wordPosition.insert(1,"I know")


print()
print()

print(wordPosition)



# DEFINING A WAY TO SET MORE ACTIONS IN MOTION, LEARNING HOW TO DEFINE A CREATION IN THE CURRENT PRESENT TIME
# LOADED WITH PURE DESCRIPTION LOADING A ELEMENT FULL OF QUALITY, A ELEMENT CAPABLE TO DEFINE THE REALITY I NEED TO SET
# A MOTION FULL OF INTERACTION.



# LEARN HOW TO PILOT THE DATA WE ARE EXPERIENCING, LEARNING HOW TO APPROACH MORE BEHAVIORS IN THE CURRENT FIELD OF MOTIONS 


# providing a clear understanding of the whole present time, learning how to achieve more elements in the now
# sense how to believe in the representation of the components, maximize a clear understanding of the now.


# believe in the continual production of the elements sense how to acquire more data, in the current field of motion
# sense how to believe in the personification of the qualities
# by learning how to achieve more definitions.


stringToFix = "believe in the continual production of the elements sense how to acquire more data, in the current field of motion sense how to believe in the personification of the qualities"
stringToFix = "E Dio fece la distesa e separò le acque ch’erano sotto la distesa, dalle acque ch’erano sopra la distesa. E così fu."
stringToFix = "E la terra produsse della verdura, dell’erbe che facevan seme secondo la loro specie, e degli alberi che portavano del frutto avente in sé la propria semenza, secondo la loro specie. E Dio vide che questo era buono."




listaOfWords = stringToFix.split(" ")





countCharactersInString = 0

wordPosition = 0;

listOutPutOfStrings = []


	
listPositionStringEnd = list()

for j in listaOfWords:

	countCharactersInString += len(j)
	countCharactersInString += 1 

	if(countCharactersInString > 110):
		countCharactersInString = 0

		listPositionStringEnd.append(wordPosition)

		countCharactersInString += len(j)
		countCharactersInString += 1 

	wordPosition += 1 

for k in listPositionStringEnd:
	listaOfWords.insert(k, "*")

wordPosition = 0

listOutPutOfStrings.append(listaOfWords)

print(listOutPutOfStrings)

