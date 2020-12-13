import Variables.variable as va

class Systems:

    def Turn(self):
        turn, va.turn = va.turn, not va.turn
        return turn

    def isDungeon(self):
        return va.inDungeon

    def changeDungeonVal(self):
        va.inDungeon = not va.inDungeon

    def isStart(self):
        return va.isStart

    def changeStartVal(self):
        va.isStart = not va.isStart