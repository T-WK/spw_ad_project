import Variables.variable as va

class Monster:
    name = ""
    hp = 1000
    atk = 100
    lvl = 1

    dropExp = 0
    dropGold = 0

    def __init__(self, name, maxHp, atk, lvl, dropExp, dropGold):
        self.name = name
        self.maxHp = maxHp
        self.curHp = self.maxHp
        self.atk = atk
        self.lvl = lvl
        self.dropExp = dropExp
        self.dropGold = dropGold

    def Dead(self):
        if self.curHp <= 0:
            self.curHp = 0
            self.__del__(self.dropExp, self.dropGold)

    def attack(self):
        va.progressText += self.name + "이(가) 공격했습니다.\n"


    def __del__(self, dropExp, dropGold):
        print("처치되었습니다.")
        print(dropGold, "골드와", dropExp, "경험치를 얻었습니다.")

    def setHp(self, val):
        self.hp = val

    