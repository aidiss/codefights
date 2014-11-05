import sys
from boilerplate.server.Protocol import Protocol
from boilerplate.server.Protocol import ServerResponse

class ServerMode(object):

	cancelFlag = False

	def __init__(self):
		self.inStream = sys.stdin
		self.outStream = sys.stdout
		print(self.inStream, self.outStream, "defined")
		
	def run(self, fighter): #IFighter
		protocol = Protocol(self.inStream, self.outStream)
		protocol.handshake()

		resp = ServerResponse()

		while self.cancelFlag != True:
			
			move = fighter.makeNextMove(resp.move, resp.score1, resp.score2)
			print('move', move)
			protocol.sendRequest(move)
			resp = protocol.readResponse()
			print('resp', resp)

	def setInputStream(istream):
		self.inStream = istream

	def setOutpupStream(ostream):
		self.outStream = ostream

	def cancel(istream):
		self.cancelFlag = True