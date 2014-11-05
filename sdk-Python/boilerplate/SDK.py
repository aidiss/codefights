from boilerplate.ProtocolException import ProtocolException
from boilerplate.server import Protocol
from boilerplate.server import ServerMode
from boilerplate.Commentator import Commentator
from boilerplate.Human import Human
from boilerplate.Arena import Arena
from model.Move import Move
import random
from random import randint 
#from samples.Boxer import Boxer #TODO
#from samples.Kickboxer import Kickboxer #TODO

from boilerplate.server.ServerMode import ServerMode

NOSE = "NOSE"
GROIN = "GROIN"
BELLY = "BELLY"
JAW = "JAW"

Area = {
NOSE : "NOSE",
GROIN : "GROIN",
BELLY : "BELLY",
JAW : "JAW"}
		

class MyFighter(object):
	"""analize your opponent's last move and make your next move.

	NOTE: rules allow max 3 actions per Move.
	I.e. attack nose (1), attack groin (2) and defend nose (3).
	The areas are Area::NOSE (10pts), Area::JAW (8pts), Area::BELLY (6pts), Area::GROIN(4pts) and Area::LEGS(3 pts)
	
	Args:

	Vars:

	Returns:
		return fighter's next Move
	"""
	#def __init__(self):
	#    super(MyFighter, self).__init__()
	#    self.makeNextMove()

	def makeNextMove(self, opponentsLastMove=None, myLastScore=0, opponentsLastScore=0):
		move = Move()
		move.addAttack('NOSE')
		move.addBlock('GROIN')
		move.addBlock('NOSE')
		return move

FIGHT_HUMAN_SWITCH = "--fight-me"
FIGHT_BOT_SWITCH = "--fight-bot"
RUN_ON_SERVER_SWITCH = "--fight-on-server"


USAGE_INSTRUCTIONS = (
				FIGHT_HUMAN_SWITCH+"\t\truns your bot against you in interactive mode\n"+
				FIGHT_BOT_SWITCH+" boxer\truns your bot against a built-in boxer bot\n"+
				FIGHT_BOT_SWITCH+" kickboxer\truns your bot against a built-in kickboxer bot\n"+
				RUN_ON_SERVER_SWITCH+"\truns your bot in codefights engine environment\n"
				)

class SDK(object):
	"""docstring for SDK"""

	@staticmethod
	def run(argv):
		argv = argv[1:]

		if SDK.isFightHumanMode(argv):
			arena = Arena()
			arena.registerFighter(Human(), "You")
			arena.registerFighter(MyFighter(), "Your bot")
			arena.stageFight()

		elif SDK.isFightBotMode(argv):
			arena = Arena()
			arena.registerFighter(MyFighter(), "Your bot")
			arena.registerFighter(SDK.createBot("boxer"), argv[1])
			arena.stageFight()

		elif SDK.isRunInServerMode(argv):
			serverMode = ServerMode()
			serverMode.run(MyFighter())

		else:
			SDK.printUsageInstructions(argv)

	@staticmethod
	def isRunInServerMode(args):
		return len(args) == 1 and args[0] == RUN_ON_SERVER_SWITCH #TODO

	@staticmethod
	def isFightBotMode(args):
		return len(args) and args[0] == FIGHT_BOT_SWITCH 

	@staticmethod
	def isFightHumanMode(args):
		return len(args) and args[0] == FIGHT_HUMAN_SWITCH

	@staticmethod
	def printUsageInstructions(args):
		if len(args) > 0:
			print("unrecognized option(s): ")

			for arg in args:
				print(arg)
			print("\n")
		print(USAGE_INSTRUCTIONS)

	@staticmethod
	def createBot(args):
		if "boxer" == args:
			return Boxer()
		if "kickboxer" == args:
			return Kickboxer()
		print("unrecognized built-in bot:", args)



class Boxer(object):
	"""docstring for Boxer"""

	myScoreTotal = 0
	opponentScoreTotal = 0
	comment = ""

	def __init__(self):
		super(Boxer, self).__init__()
		self.attack1 = ''
		self.attack2 = ''
		self.defence = ''

		myScoreTotal = 0
		opponentScoreTotal = 0
		comment = ""

		self.attack1 = Area[NOSE]
		self.attack2 = Area[JAW]
		self.defence = Area[NOSE]

	def makeNextMove(self, opponentsLastMove=None, myLastScore=None, opponentsLastScore=None): #I do not understand move part
		move = Move()
		
		move.addAttack(self.attack1)
		move.addAttack(self.attack2) ##
		move.addBlock(self.defence) ##
		#Commentator().setComment("blocked your move to my $this->defence... hahaha")

		if opponentsLastMove != None:
			if self.defence in opponentsLastMove.getAttacks():
				#pass
				move.setComment("blocked your move to my self->defence... hahaha")
			else:
				self.changeDefence()

		self.myScoreTotal += myLastScore #TODO:  type object 'Boxer' has no attribute 'myScoreTotal'
		self.opponentScoreTotal += opponentsLastScore

		if self.myScoreTotal < self.opponentScoreTotal:
			#move.setComment('okay, meat, me is mad now... going berserk')
			move.addAttack(self.createRandomAttack())
		else:
			move.addBlock(self.defence)

		return move

	def changeDefence(self):
		if self.defence == Area[NOSE]:
			self.defence=Area[JAW]

		self.defence=Area[NOSE]

	def createRandomAttack(self):
		random = randint(0, 10)
		if random >= 5:
			return Area[GROIN]
		return Area[BELLY]



from random import randint
class Kickboxer(object):
	attack1 = ''
	attack2 = ''
	attack3 = ''

	opponentName = ''
	comment = ''
	def __init__(self):
		super(KickBoxer, self).__init__()
		attack1 = Area(GROIN)
		attack2 = Area(NOSE)
		defence = Area(NOSE)

	def makeNextMove(opponentsLastMove=None, iLost=None, iScored=None):
		if opponentsLastMove != None:
			if self.defence in opponentsLastMove.getAttacks():
				self.comment = 'haha, blocked your attack to my' + self.defence
			else:
				self.comment = 'ouch'

		self.attack2 = Kickboxer.createRandomArea()

		if opponentsLastMove != None:
			if Kickboxer.attack1 in opponentsLastMove.getBlocks():
				self.attack1 = Kickboxer.createRandomArea()

		move = Move()
		print(move.getAttacks, move.getBlocks)
		move.addAttack(self.attack1)
		move.addAttack(self.attack2)
		move.addBlock(self.defence)
		move.setComment(self.comment)
		print(move.getAttacks, move.getBlocks)
		return move

	@staticmethod
	def createRandomArea():
		random = randint(0, 100)

		if random < 30:
			return Area(NOSE)

		if random < 70:
			return Area(JAW)

		if random < 90:
			return Area(GROIN) # oh yeah

		return Area(LEGS)
