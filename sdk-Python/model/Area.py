'''
What you can attack or block.

author Aidis Stukas
'''

class Area(object):
	"""docstring for Area"""
	NOSE="NOSE"
	JAW= "JAW"
	GROIN= "GROIN"
	BELLY= "BELLY"
	LEGS= "LEGS"
	def __init__(self, arg):
		super(Area, self).__init__()
		if arg == "NOSE": return NOSE
		