import csv
import sys
import collections

input_file = 'pokemon_types.csv'
effective_pokemon = {}
other_pokemon = {}

with open(input_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	# 2nd column is type id
    	# print isinstance(row[1], str)    	
	    if int(row[1]) in (10, 2, 6, 9): # ice
	    # if int(row[1]) in (3, 14): # fighting
	    # if int(row[1]) in (8, 17): # ghost
	    # if int(row[1]) in (15, 16): # dragon
	    	effective_pokemon[int(row[0])] = 1
	       	print '+1'

# print effective_pokemon


for i in range(1,409):
	other_pokemon[i] = int(-1)
			
# print other_pokemon

for key in effective_pokemon:
    if key in other_pokemon:
        print key
        other_pokemon[key] = 1

# print other_pokemon

all_pokemon = collections.OrderedDict(sorted(other_pokemon.items()))
# for k, v in all_pokemon.iteritems(): 
# 	print k, v

text_file = open("ice_label.txt", "w")
# text_file = open("fighting_label.txt", "w")
# text_file = open("ghost_label.txt", "w")
# text_file = open("dragon_label.txt", "w")

# create the file
for key in all_pokemon:
	text_file.write(str(all_pokemon[key])+ '\n')
text_file.close()