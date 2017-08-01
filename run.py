from GameView import GameView
from GameState import GameState
import functions

gamestate = GameState(player=0)
gameview = GameView(gamestate)
enumerations = gameview.enumerate(gamestate)
print len(enumerations)
functions.viewEnumerationNum(enumerations[0])

for i in range(1,4):
	for j in range(6):
		gamestate.cards[i][j]['rank'] = 'unclear'
gamestate.cards[1][0] = {'rank':0, 'color':gamestate.cards[1][0]['color']}
gameview.update(gamestate)
print len(gameview.enumerations)
functions.viewEnumerationNum(gameview.enumerations[0])