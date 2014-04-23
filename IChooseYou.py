import os
import numpy as np
import collections
import operator
import csv

numChosen = 0

overlaps = {}

trainersDir = os.getcwd() + "/results/"
trainerFiles = []
moveNames = []
pokemonNames = []

baseStatsFile = "pokemon_base_stats.txt"
moveScoresFile = "pokemon_moves_scores.txt"
pokemonMovesFile = "pokemon_compatible_moves.txt"
pokemonFullMoveFile = "moves.csv"
pokemonFile = "pokemon.csv"

baseStatsData = np.loadtxt(open(baseStatsFile,"rb"))
pIdStats, baseStats = baseStatsData[0:151,0], baseStatsData[0:151,1]

movesData = np.loadtxt(open(moveScoresFile,"rb"))
# mId, moveScores = movesData[:,0], movesData[:,1]

pokemonMoves = np.loadtxt(open(pokemonMovesFile,"rb"))

# print movesData
# print pokemonMoves



# baseStats = baseStats / np.max(baseStats)

# print baseStats


# baseStatsData = baseStatsData[0:151, :]

# print baseStatsData

# baseStatsData = baseStatsData[np.argsort(baseStatsData[:,1])]
# baseStatsData = baseStatsData[::-1]

# print baseStatsData.shape

# print baseStatsData
# print type(baseStatsData)

for item in os.listdir(trainersDir):
	if not item.startswith('.'):
		trainerFiles.append(item)

# print trainerFiles


for trainer in trainerFiles:
	data = np.loadtxt(open(trainersDir + trainer,"rb"))

	for pId in data:
		if pId not in overlaps:
			overlaps[pId] = 1
		else:
			overlaps[pId] += 1

with open(pokemonFullMoveFile, 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
    	moveNames.append(row[1])

with open(pokemonFile, 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
    	pokemonNames.append(row[1])


# print moveNames
# print pokemonNames


# print overlaps

for key, value in sorted(overlaps.iteritems(), key=operator.itemgetter(1), reverse = True):
	# print key, ':', value
	pass

# print max(overlaps.values())

# print overlaps.keys()[overlaps.values().index(4)]

# print [key for key, value in overlaps.items() if value == 4]

# a = [key for key, value in overlaps.items() if value == 4]

# print a
# print a[0]
# print a[7]

# print pIdStats
# print baseStats

# print baseStats
# print baseStats.shape

def getParty():
	maxOverlaps = max(overlaps.values())

	partyList = np.array([])

	global numChosen
	partyChosen = False

	while (partyList.shape[0] < 6):
		# print "PARTY ITERATION"
		commons = [key for key, value in overlaps.items() if value == maxOverlaps]
		if len(commons) >= (6 - len(partyList)):
			numLeft = 6 - len(partyList)
			best = getBestPokemon(commons, numLeft)
			# partyList.extend(best)

			

		else:
			numLeft = 6 - len(partyList)
			best = getBestPokemon(commons, len(commons))
			# partyList.extend(best)

		if partyList.size == 0:
			partyList = np.array(best)
		else:
			partyList = np.concatenate([partyList, best])

		# print partyList.shape[0]
		# print commons
		# print "overlaps", maxOverlaps
		# print partyList

		maxOverlaps -= 1

		# print len(partyList[0])

	return partyList

def getBestPokemon(commons, num):
	pokemonStatsList = np.array([])
	for pId in commons:
		# if baseStats[pId-1] >= 500 and pId != 151:
		if pId < 144 or pId == 147 or pId == 148 or pId == 149:
		# if pId > 0 and baseStats[pId-1] >= 450 and pId != 151: # THIS
		# if pId > 0 and pId != 151: # AND THIS
			if pokemonStatsList.size == 0:
				pokemonStatsList = np.array([[pId, baseStats[pId-1]]])
			else:
				add = np.array([[pId, baseStats[pId-1]]])
				# pokemonStatsList = np.concatenate([[pokemonStatsList], [pId, baseStats[pId-1]]])
				pokemonStatsList = np.concatenate([pokemonStatsList, add])

	# print pokemonStatsList

	pokemonStatsList = pokemonStatsList[np.argsort(pokemonStatsList[:,1])]
	pokemonStatsList = pokemonStatsList[::-1]

	return pokemonStatsList[0:num]

def getPartyMoves(party):
	allPartyInfo = {}

	for a in party:
		pokemon = a[0]
		# print int(pokemon)
		movesIndexes = np.where(pokemonMoves[:,0] == pokemon)[0]
		# print movesIndexes

		# compatibleMoveScores = np.array([])

		moves = pokemonMoves[movesIndexes,1]
		# print moves

		scores = movesData[moves.astype(int)-1,1]
		# print scores

		pokemonMovesScores = np.concatenate([[moves], [scores]])


		# print "----------"
		# print pokemonMovesScores
		# print pokemonMovesScores.shape
		# print pokemonMovesScores[1,1]

		pokemonMovesScores = np.transpose(pokemonMovesScores)
		# print pokemonMovesScores

		pokemonMovesScores = pokemonMovesScores[np.argsort(pokemonMovesScores[:,1])]
		pokemonMovesScores = pokemonMovesScores[::-1]

		# print pokemonMovesScores

		# print "*****"

		# print pokemonMovesScores[0:4,0]

		global moveNames

		fourMoveNames = []

		for i in range(4):
			fourMoveNames.append(moveNames[pokemonMovesScores[i,0].astype(int)-1])

		allPartyInfo[pokemonNames[int(pokemon-1)]] = fourMoveNames


	return allPartyInfo




fullParty = getParty()

print fullParty

partyMoveSet = getPartyMoves(fullParty)



for i in partyMoveSet:
	print i
	print partyMoveSet[i]

# print np.where(pokemonMoves[:,0] == 6)[0]

# items = overlaps.values()
# items.sort()
# print [value for key, value in items]
