from boilerplate.server.Protocol import Protocol
from model.GameScoringRules import GameScoringRules
import sys


class Human(object):
	"""docstring for Human"""
	consoleOut = None
	consoleIn = None

	def __init__(self):
		pass
		#self.consoleOut = open("php://stdout", "w")
		#self.consoleOut
		#self.consoleIn = open("php://stdin", "r")
		#self.consoleIn
	
	def makeNextMove(self, oppMove=None, iScored=0, oppScored=0):
		Human.printInstructions(Human)
		while True:
			try:
				something = input('Type your moves here:\n')
				return Human.parseInput(something)
			except Exception as e:
				#catch (ProtocolException $ipe): print("Human error: ".$ipe->getMessage())
				#catch raise SystemExit
				print("some kind of error", e)
				break

	def printInstructions(self):
		print("Make your move by (A)ttacking and (B)locking (N)ose, (J)aw, (B)elly, (G)roin, (L)egs")
		print("  (for example, BN BB AN)")
		print(": ")

	@staticmethod
	def parseInput(Input):
		Input = Input.replace(" ", "")
		Input = Input.lower()
		if Input[0] == "q": #Why Human is not needed?
			print("Exiting")

		move = Protocol.parseMove(Input)
		if GameScoringRules.isMoveLegal(move) == False:
			print("CAN MAKE MAX 3 THINGS")

		return move

	@staticmethod
	def startsWith(self, haystack, needle):
		length = len(needle)
		return(haystack[0:] == needle)