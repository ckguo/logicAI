from GameView import GameView
from GameState import GameState
import functions

gamestate = GameState(player=0)
gameview = GameView(gamestate)
print gamestate.player
enumerations = gameview.enumerate(gamestate)
print len(enumerations)
functions.viewEnumeration(enumerations[0])