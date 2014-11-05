from model.Area import Area

class Move(object):
	"""docstring for Move"""
	def __init__(self):
		super(Move, self).__init__()
		self.attacks = []
		self.blocks = []
		self.comment = ""

	def getAttacks(self):
		return self.attacks

	def getBlocks(self):
		return self.blocks

	def getComment(self):
		return self.comment

	def setComment(self, comment):
		self.comment = comment

	def addAttack(self, area):
		self.attacks.append(area)

	def addBlock(self, area):
		self.blocks.append(area)


	def _toString(self):
		rez = 'Move '

		for attack in self.attacks:
			rez = rez + ' ATTACK ' + attack

		for block in self.blocks:
			rez = rez + ' BLOCK ' + block

		if comment:
			rez = rez + ' COMMENT ' + self.comment

		return rez
		
	def repr(self):
		return self._toString()
