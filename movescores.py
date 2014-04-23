import csv

pokemonMoviesFileName = "moves.csv"
pokemonLevel = 45

writeFile = open("pokemon_moves_scores.txt", "w")

powerWeight = 0.4
ppWeight = 0.2
accuracyWeight = 0.4

with open(pokemonMoviesFileName, 'rb') as f:
	reader = csv.reader(f)
	reader.next()
	print "here"

	count = 0
	pokemonId = 0

	pokemonStats = []

	for row in reader:
		print row

		if int(row[0]) <= 354:
			if row[0] == '':
				moveId = 0
			else:
				moveId = int(row[0])

			if row[2] == '':
				genId = 0
			else:
				genId = int(row[2])

			if row[4] == '':
				power = 0
			else:
				power = int(row[4])

			if row[5] == '':
				pp = 0
			else:
				pp = int(row[5])

			if row[6] == '':
				accuracy = 0
			else:
				accuracy = int(row[6])


			moveScore = int(power*powerWeight + pp*ppWeight + accuracy*accuracyWeight)
			writeFile.write(str(moveId) + "\t" + str(moveScore) + "\n")

