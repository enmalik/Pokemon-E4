import csv
import numpy as np

input_file = 'pokemon_types.csv'

data = np.loadtxt(open(input_file,"rb"),delimiter=",")
pId, types = data[:,0], data[:,1]    

writeFile = open("pokemon_all_types.txt", "w")

# print int(pId[0])

print len(np.where(pId == 1)[0])
# print np.where(pId == 1)[0]


for pokemonId in range(1, 409):
	indexList = np.where(pId == pokemonId)[0]
	# print indexList

	if len(indexList) == 1:
		writeFile.write(str(pokemonId) + "\t" + str(int(types[indexList[0]])) + "\t" + "0" + "\n")
	elif len(indexList) == 2:
		writeFile.write(str(pokemonId) + "\t" + str(int(types[indexList[0]])) + "\t" + str(int(types[indexList[1]])) + "\n")


# with open(input_file, 'rb') as f:
# 	reader = csv.reader(f)
# 	print "here"
# 	primaryType = 0
# 	prevPokemonId = 0

# 	types = []

# 	for row in reader:


	# 	if int(row[0]) > 251:
	# 		break
	# 	print row[0]

	# 	primaryType = int(row[1])
	# 	pokemonId = int(row[0])

	# 	if prevPokemonId != pokemonId:
	# 		writeFile.write(str(pokemonId) + "\t" + str(primaryType) + "\n")

	# 	prevPokemonId = pokemonId
    	
