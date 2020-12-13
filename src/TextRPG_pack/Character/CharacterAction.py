import Variables.variable as va

class Character:

    def __init__(self, name, maxHp, atk, defense, luck, level, maxExp, gold):
        self.name = name

        self.maxHp = maxHp
        self.curHp = self.maxHp

        self.atk = atk
        self.defense = defense
        self.luck = luck
        self.level = level

        self.maxExp = maxExp
        self.curExp = maxExp

        self.gold = gold

        self.maxMana = 10
        self.curMana = self.maxMana

        self.mulEmp = 2

    def isDead(self):
        if self.curHp <= 0:
            self.__del__(self.exp, self.gold)

    def __del__(self, dropExp, dropGold):
        print("죽었습니다.")
        print(dropGold, "골드와", dropExp, "경험치를 잃었습니다.")

    def setHp(self, val):
        self.curHp = val
    
    def setMana(self, val):
        self.mana = val
    
    def setExp(self, val):
        self.exp = val

        if self.exp >= self.maxExp:
            self.setLevel(self.maxExp//self.exp, self.maxExp%self.exp)

    def setLevel(self, level, exp):
        self.level += level
        self.exp = exp
        self.maxExp *= self.mulEmp**level
    
    def setGold(self, val):
        self.gold += val
    
    def attack(self, monster):
        monster.curHp -= self.atk
        va.progressText += "플레이어가 공격했습니다!\n"