class ProtocolException(Exception):
	"""docstring for ProtocolException"""
	def __init__(self, message, code=0, previous=None):
		super(ProtocolException, self).__init__()
		self(message, code, previous)

	def _toString():
		return self.code, self.message
					