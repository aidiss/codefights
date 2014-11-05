from random import randint
class KickBoxer(object):
    """docstring for KickBoxer"""
    def __init__(self, arg):
        super(KickBoxer, self).__init__()
        self.arg = arg
    
        attack1 = ''
        attack2 = ''
        attack3 = ''

        opponentName = ''
        comment = ''

        attack1 = Area(GROIN)
        attack2 = Area(NOSE)
        defence = Area(NOSE)

    def makeNextMove(opponentsLastMove=None, iLost=None, iScored=None):
        if opponentsLastMove != None:
            if defence in opponentsLastMove:
                comment('haha, blocked your attack to my $this->defence')
            else:
                comment('ouch')


        if opponentsLastMove != None:
            if (in_array(self = attack1, opponentsLastMove = getBlocks())):
                self.attack1 = self.createRandomArea();

        move = Move(); # neaiskus
        move.addAttack(self = attack1)
        move.addAttack(self = attack2)
        move.addBlock(self = defence)
        move.setComment(self = comment)

        return move

    def createRandomArea():
        import random
        random = randint(0, 100)

        if (random<30):
            return Area(NOSE)

        if (random<70):
            return Area(JAW)

        if (random<90):
            return Area(GROIN)

        return Area(LEGS)
