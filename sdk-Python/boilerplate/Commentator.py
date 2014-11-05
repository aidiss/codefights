from model.GameScoringRules import GameScoringRules

class Commentator(object):

	fighter1 = "Fighter1"
	fighter2 = "Fighter2"

	lp1 = GameScoringRules.LIFEPOINTS
	lp2 = GameScoringRules.LIFEPOINTS
	
	def setFighterNames(self, fighter1name, fighter2name):
		self.fighter1 = fighter1name
		self.fighter2 = fighter2name

	def describeRound(self, move1, move2, score1, score2):
		Commentator.describeMove(self.fighter1, move1, score1, move2) #todo
		Commentator.describeMove(self.fighter2, move2, score2, move1)

		self.lp1 -= score2
		self.lp2 -= score1

		print(self.fighter1, "vs", self.fighter2, ":", self.lp1, "to", self.lp2)

	def gameOver(self, f1Lifepoints, f2Lifepoints):
		print("FIGHT OVER\n")

		if f1Lifepoints > f2Lifepoints:
			print("THE WINNER IS", self.fighter1, "\n")
		elif f2Lifepoints > f1Lifepoints:
			print("THE WINNER IS", self.fighter2, "\n")
		else:
			print("DRAW")

	def describeMove(fighterName, move, score, counterMove):
		print(
			fighterName, 
			Commentator.describeAttacks(move, counterMove, score), 
			Commentator.describeDefences(move),
			Commentator.describeComment(move),
			"\n")

	@staticmethod
	def describeAttacks(move, counterMove, score):
		attacks = move.getAttacks()

		if len(attacks) <= 0:
			return " did NOT attack at all "

		rez = " attacked "

		for attack in attacks:
			rez = rez + attack
			blocked = attack in counterMove.getBlocks() #TODO

			if blocked:
				rez = rez + "(-), "
			else:
				rez = rez + "(+), "

		return str(rez) + " scoring " + str(score)

	@staticmethod
	def describeDefences(move):
		blocks = move.getBlocks()
		if len(blocks) <= 0:
			return "  and was NOT defending at all."

		rez = " while defending "
		for block in blocks:
			rez = rez + block + ", "
			
		return rez

	@staticmethod
	def describeComment(move):
		comment = move.getComment
		if comment or comment == None or len(comment) <= 0:
			return ""

		return "Also said \"", Protocol.sanitizeComment(comment), "\""
