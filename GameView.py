from copy import deepcopy
from GameState import GameState
from functions import *
# contains:
# a GameState
# 4 enumerations

class GameView:
    def __init__(self, gamestate):
    	self.gamestate = gamestate
    	self.enumerations = None
    	self.next_history = 0

    def enumerate(self, gamestate):
    	cards = [[None]*6, [None]*6, [None]*6, [None]*6]
    	for j in range(6):
			rank = gamestate.cards[gamestate.player][j]['rank']
			color = gamestate.cards[gamestate.player][j]['color']
			cards[gamestate.player][j] = 12*color + rank
    	mystack = [[cards,0]] #4x6
    	enumerations = []
    	while len(mystack) > 0:
    		config = mystack.pop()
    		if self.check_conflicts(config):
    			continue
    		if config[1] == 24:
    			enumerations.append(config[0])
    		expansions = self.expand(gamestate, config)
    		mystack.extend(expansions)
    	return enumerations

    def check_conflicts(self, config):
    	for i in range(4):
    		prev = 0
    		for j in range(6):
    			if config[0][i][j] == None:
    				continue
    			if config[0][i][j]%12 < prev:
    				return True
    			prev = config[0][i][j]%12
    	return False

    def expand(self, gamestate, config):
    	rank = config[1]
    	color = int(rank/12)
    	for i in range(4):
    		for j in range(6):
    			if config[0][i][j] == rank:
    				new_config = deepcopy(config)
    				new_config[1] = rank + 1
    				return [new_config]
    	results = []
    	for i in range(4):
    		for j in range(6):
    			if config[0][i][j] != None:
    				continue
    			if gamestate.cards[i][j]['color'] != color:
    				continue
    			new_config = deepcopy(config)
    			new_config[0][i][j] = rank
    			new_config[1] = rank + 1
    			results.append(new_config)
    			break
    	return results

    def update(self, new_game_state):
    	if self.enumerations == None:
    		self.enumerations = self.enumerate(new_game_state)
    	pop_indices = []
    	for ind in range(len(self.enumerations)):
    		config = self.enumerations[ind]
    		break_flag = False
    		for i in range(4):
    			if break_flag == True:
    				break
    			for j in range(6):
    				if new_game_state.cards[i][j]['rank'] != 'unclear':
    					num = cardToNum(new_game_state.cards[i][j])
    					if config[i][j] != num:
    						pop_indices.append(ind)
    						break_flag = True
    						break
    	print len(pop_indices)
    	if len(pop_indices) > 0:	
	    	new_enumerations = []
	    	pop_ind = 0
	    	for ind in range(len(self.enumerations)):
	    		next_pop = pop_indices[pop_ind]
	    		if ind == next_pop:
	    			pop_ind += 1
	    			if pop_ind >= len(pop_indices):
	    				new_enumerations.extend(self.enumerations[ind+1:])
	    				break
	    			continue
	    		new_enumerations.append(self.enumerations[ind])
	    	self.enumerations = new_enumerations

    	# for i in range(self.next_history, len(new_game_state.history)):
    	# 	action = new_game_state.history[i]
    	# 	if action.action_type == 'guess':
    	# 		if 


    def guess_card_ratio(self, which_player, which_card, guess):
    	pass

    def guess_card_num_configs(self, which_player, which_card, guess):
    	pass