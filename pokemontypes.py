import csv

input_file = 'pokemon_types.csv'

writeFile = open("pokemon_primary_types.txt", "w")

with open(input_file, 'rb') as f:
	reader = csv.reader(f)
	print "here"
	primaryType = 0
	prevPokemonId = 0

	for row in reader:
		if int(row[0]) > 251:
			break
		print row[0]

		primaryType = int(row[1])
		pokemonId = int(row[0])

		if prevPokemonId != pokemonId:
			writeFile.write(str(pokemonId) + "\t" + str(primaryType) + "\n")

		prevPokemonId = pokemonId
    	
