from Variables import variable as va

def Turn():
    turn, va.turn = va.turn, not va.turn
    return turn

def isDungeon():
    return va.inDungeon

def changeDungeonVal():
    va.inDungeon = not va.inDungeon