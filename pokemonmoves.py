import csv

pokemonMovesListFileName = "gen3MovesUpdated.csv"
pokemonLevel = 45

writeFile = open("pokemon_compatible_moves.txt", "w")

powerWeight = 0.5
ppWeight = 0.2
accuracyWeight = 0.3

with open(pokemonMovesListFileName, 'rb') as f:
	reader = csv.reader(f)
	reader.next()
	print "here"

	for row in reader:
		if int(row[0]) <= 354 and int(row[1]) <= 151:
			pokemonId = row[1]
			moveId = row[0]
			writeFile.write(str(pokemonId) + "\t" + str(moveId) + "\n")

