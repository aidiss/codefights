import sys
from model.Move import Move

class ServerResponse(object):
	move = None
	score1 = None
	score2 = None	

class Protocol(object):
	HANDSHAKE = "I-AM ready";

	REQUEST_HEADER = "";

	YOUR_SCORE = "YOUR-SCORE";
	OPPONENT_SCORE = "OPPONENT-SCORE";
	ENEMY_MOVE = "ENEMY-MOVE";
	MOVE_COMMENT = "COMMENT";


	def __init__(self, inStream, outStream):
		self.outStream = outStream
		self.inStream = inStream

	def handshake(self):
		self.outStream.write(Protocol.HANDSHAKE + "\n")

	def sendRequest(self, move):
		print("sending request")
		self.outStream.write(Protocol.REQUEST_HEADER)
		self.outStream.write(Protocol.serializeMove(move))

	def readResponse(self):
		print("reading response")
		Protocol.parse(self.inStream.readline()) #TODO
		print("response read")

	@staticmethod
	def serializeMove(move):
		rez = ''

		for attack in move.getAttacks():
			rez = rez + 'a' + attack[0]

		for block in move.getBlocks():
			rez = rez + 'b' + block[0]

		if move.getComment() != None:
			rez = rez + 'c' + Protocol.sanitizeComment(move.getComment())

		return rez.lower()

	@staticmethod
	def parseMove(Input):
		sys.stdout.flush()
		if Input == False or Input == None:
			print("Input stream was closed")

		Input = Input.strip()
		rez = Move()

		index = 0

		while index < len(Input):
			Type = Input[index]
			index += 1
			
			#TODO
			if 'a'==Type: 
				rez.addAttack(Protocol.getArea(Input, index)); index += 1 #######?TODO
			
			elif 'b'==Type: 
				rez.addBlock(Protocol.getArea(Input, index)); index += 1 #######?TODO
			
			elif '.'==Type:
				pass

			elif 'c'==Type:
				rez.setComment(Input[index]); index = len(Input) + 1
			
			elif ' '==Type:
				pass
			
			elif r'\t'==Type:
				continue
			
			else:
				print("Unrecognized input:" + Type)
		return rez

	@staticmethod
	def sanitizeComment(comment):
		if (comment == False or comment == None):
			return None

		breaks = ['\t', '\n','\"']

		for Break in breaks:
			result = comment.replace(Break, " ") #TODO

		result = result.strip()

		if len(result) > 150:
			result = result[0:150]

		return result

	@staticmethod
	def parse(line):
		print("parsing line:", line)
		result = ServerResponse()

		words = line.split(' ')
		index = 0

		while index < len(words):
			firstKeywords = words[index]
			index += 1

			if index >= len(words):
				print('Insufficient params in {' + line + '}. Syntax is [YOUR-SCORE area] [OPPONENT-SCORE area] [ENEMY-MOVE move]')

			nextKeyword = words[index]
			index += 1

			if Protocol.YOUR_SCORE == firstKeywords:
				result.score1 = int(nextKeyword)

			elif Protocol.OPPONENT_SCORE == firstKeywords:
				result.score1 = int(nextKeyword)

			elif Protocol.ENEMY_MOVE == firstKeywords:
				result.move = self.parseMove(nextKeyword)

			else:
				print("invalid keyword" + firstKeyword + "Syntax is [YOUR-SCORE area] [OPPONENT-SCORE area] [ENEMY-MOVE move]")
		return result

	@staticmethod
	def getArea(line, index):
		if index >= len(line):
			print("Must also specify attack/defence area!")
		mydict = {
				'n': 'NOSE',
				'j': 'JAW',
				'b': 'BELLY',
				'g': 'GROIN',
				'l': 'LEGS'}

		return mydict[line[index]]
