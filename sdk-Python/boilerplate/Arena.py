from boilerplate.Commentator import Commentator
from model.GameScoringRules import GameScoringRules

class Arena(object):
	"""docstring for Arena"""
	def __init__(self):
		self.fighters = {}  # TODO: maybe better OrderedDict? 
		self.commentator = Commentator()

	def registerFighter(self, fighter, name):
		self.fighters[name]=fighter
		return self

	def stageFight(self):
		if len(self.fighters) != 2:
			print ("MUST BE TWO FIGHTERS")

		f1name, f2name = None, None

		for f1name in self.fighters: #TODO
			break
		fighter1 = self.fighters.pop(f1name)

		for f2name in self.fighters: 
			break
		fighter2 = self.fighters.pop(f2name)

		self.commentator.setFighterNames(f1name, f2name)

		f1Move = None
		f2Move = None

		score1 = 0
		score2 = 0

		f1Lifepoints = GameScoringRules.LIFEPOINTS #TODO  GameScoringRules.GameScoringRules.LIFEPOINTS?
		f2Lifepoints = GameScoringRules.LIFEPOINTS #TODO

		while (f1Lifepoints > 0 and f2Lifepoints > 0):

			move1 = fighter1.makeNextMove(f2Move, score1, score2)
			if (GameScoringRules.isMoveLegal == False):
				print (f1name, " made an illegal move: ", move1)

			move2 = fighter2.makeNextMove(f1Move, score2, score1)
			if (GameScoringRules.isMoveLegal == False):
				print (f2name, " made an illegal move: ", move2)

			score1 = GameScoringRules.calculateScore(move1.getAttacks(), move2.getBlocks())
			score2 = GameScoringRules.calculateScore(move2.getAttacks(), move1.getBlocks())

			self.commentator.describeRound(move1, move2, score1, score2)
			f1Lifepoints -= score2
			f2Lifepoints -= score1

			f1Move = move1
			f2Move = move2

		self.commentator.gameOver(f1Lifepoints, f2Lifepoints)

	def setCommentator(c):
		self.commentator = c
		return self
