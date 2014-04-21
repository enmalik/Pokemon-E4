import csv

pokemonStatsFileName = "pokemon_stats.csv"
pokemonLevel = 45

writeFile = open("pokemon_base_stats.txt", "w")

with open(pokemonStatsFileName, 'rb') as f:
	reader = csv.reader(f)
	print "here"

	count = 0
	pokemonId = 0

	pokemonStats = []

	for row in reader:
		pokemonId = int(row[0])
		count = int(row[1])
		pokemonStats.append(int(row[2]))

		# print count

		if count == 6:

			print "IN HERE"
			hp = ((int(pokemonStats[0] + 50)*pokemonLevel) / 50) + 5
			attack = ((int(pokemonStats[1])*pokemonLevel) / 50) + 5
			defense = ((int(pokemonStats[2])*pokemonLevel) / 50) + 5
			spAttack = ((int(pokemonStats[3])*pokemonLevel) / 50) + 5
			spDefense = ((int(pokemonStats[4])*pokemonLevel) / 50) + 5
			speed = ((int(pokemonStats[5])*pokemonLevel) / 50) + 5

			baseStat = hp + attack + defense + spAttack + spDefense + speed

			print "resetting count"

			writeFile.write(str(pokemonId) + "\t" + str(baseStat) + "\n")

			pokemonStats = []


		# if prevPokemonId != pokemonId:
		# 	writeFile.write(str(pokemonId) + "\t" + str(primaryType) + "\n")

