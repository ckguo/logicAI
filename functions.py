import sys

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"

def viewEnumerationNum(enum):
	# enum is a 4x6 array of integers (0-23)
	print('\tCard 1\tCard 2\tCard 3\tCard 4\tCard 5\tCard 6')
	for i in range(4):
		sys.stdout.write(RESET)
		sys.stdout.write('Plyr {}:\t'.format(i))
		for j in range(6):
			num = enum[i][j]
			color = RED if num < 12 else BLUE
			sys.stdout.write(color)
			sys.stdout.write((str) (num % 12) + '\t')
		sys.stdout.write('\n')
	sys.stdout.write(RESET)

def viewEnumerationCard(enum):
	# enum is a 4x6 array of Card objects:
	#	- 'rank' is either an int (0-11) or 'Unclear'
	#	- 'color' is an int (0-1)
	print('\tCard 1\tCard 2\tCard 3\tCard 4\tCard 5\tCard 6')
	for i in range(4):
		sys.stdout.write(RESET)
		sys.stdout.write('Plyr {}:\t'.format(i))
		for j in range(6):
			rank = enum[i][j]['rank']
			num = (str) (rank % 12) if isinstance(rank, int) else '?'
			color = RED if enum[i][j]['color'] == 0 else BLUE
			sys.stdout.write(color)
			sys.stdout.write(num + '\t')
		sys.stdout.write('\n')
	sys.stdout.write(RESET)


def cardToNum(card):
	# card is a dictionary of 'rank' (0-11) and 'color' (0-1)
	return card['rank'] + 12 * card['color']

def numToCard(num):
	# num is an integer (0-23)
	color = 0 if num < 12 else 1
	rank = num % 12
	return {'rank': rank, 'color': color}

def printCard(card):
	# card is a dictionary of 'rank' (0-11) and 'color' (0-1)
	return 'Rank: {}, Color: {}'.format(card['rank'], card['color'])

def numToPrint(num):
	return printCard(numToCard(num))

"""
config = [[{'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 1}, {'rank': 3, 'color': 1}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 0}],
		[{'rank': 'Unclear', 'color': 1}, {'rank': 4, 'color': 1}, {'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 1}],
		[{'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 0}],
		[{'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 0}, {'rank': 'Unclear', 'color': 1}, {'rank': 'Unclear', 'color': 0}]]

viewEnumerationCard(config)

arr = []
for i in range(4):
	subarr = []
	for j in range(6):
		subarr.append(j + 6 * i)
	arr.append(subarr)

viewEnumerationNum(arr)
"""

