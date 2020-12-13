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

    def Dead(self, player):
        va.progressText += self.name + "이(가) 죽었습니다.\n"
        player.curExp += 10
        self.__del__()

    def attack(self):
        va.progressText += self.name + "이(가) 공격했습니다.\n"

    def __del__(self):
        print("처치되었습니다.")
        print(self.dropGold, "골드와", self.dropExp, "경험치를 얻었습니다.")

    def setHp(self, val):
        self.hp = val

    