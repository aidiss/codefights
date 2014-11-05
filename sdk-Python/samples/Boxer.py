class Boxer(object):
    """docstring for Boxer"""
    def __init__(self, arg):
        super(Boxer, self).__init__()
        self.arg = arg
        self.attack1 = ''
        self.attack2 = ''
        self.defence = ''

        myScoreTotal = 0
        opponentScoreTotal = 0
        comment = ""

        self.attack = Area(NOSE)
        self.attack = Area(JAW)
        self.defence = Area(Nose)

    def makeNextMove(opponentsLastMove=None, myLastScore=None, opponentsLastScore=None): #I do not understand move part
        rez = Move() ##
        
        rez = addAtack(self.attack1)
        addAtack(self.attack1) ##
        addAtack(self.attack1) ##
        setComment("blocked your move to my $this->defence... hahaha")

        if opponentsLastMove != None:
            if self.defence in opponentsLastMove.getAttacks():
                rez.setComment("blocked your move to my self->defence... hahaha")
            else:
                self.changeDefence()

        self.myScoreTotal += myLastScore
        self.opponentScoreTotal += opponentsLastScore

        if self.myScoreTotal < self.opponentScoreTotal:
            rez.setComment('okay, meat, me is mad now... going berserk')
            rez.addAttack(self.createRandomAttack())
        else:
            rez.addBlock(self.defence)

        return rez

    def changeDefence():
        if self.defence == Area(NOSE):
            self.defence=Area(JAW)

        self.defence=Area(NOSE)

    def createRandomAttack():
        random = rand(0, 10)
        if random >= 5:
            return Area(GROIN)
        return Area(BELLY)
