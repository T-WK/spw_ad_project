class Monster:
    name = ""
    hp = 1000
    atk = 100
    lvl = 1

    dropExp = 0
    dropGold = 0

    def __init__(self, name, hp, atk, lvl, dropExp, dropGold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.lvl = lvl
        self.dropExp = dropExp
        self.dropGold = dropGold

    def isDead(self):
        if self.hp <= 0:
            self.__del__(self.dropExp, self.dropGold)

    def __del__(self, dropExp, dropGold):
        print("처치되었습니다.")
        print(dropGold, "골드와", dropExp, "경험치를 얻었습니다.")

