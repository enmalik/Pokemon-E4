import os
import numpy as np
import collections
import operator

numChosen = 0

overlaps = {}
trainersDir = os.getcwd() + "/resultsANN/"
trainerFiles = []

baseStatsFile = "pokemon_base_stats.txt"

baseStatsData = np.loadtxt(open(baseStatsFile,"rb"))
pIdStats, baseStats = baseStatsData[0:151,0], baseStatsData[0:151,1]

print np.max(baseStats)


# baseStats = baseStats / np.max(baseStats)

print baseStats
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
		print "PARTY ITERATION"
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

		print partyList.shape[0]

		maxOverlaps -= 1

		# print len(partyList[0])

	return partyList

def getBestPokemon(commons, num):
	pokemonStatsList = np.array([])
	for pId in commons:
		if pId < 144:
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

print getParty()


# items = overlaps.values()
# items.sort()
# print [value for key, value in items]
