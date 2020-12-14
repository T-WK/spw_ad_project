import Variables.variable as va

class Character:

    isDefense = False

    def __init__(self, name, maxHp, maxMana, atk, defense, luck, level, maxExp, gold):
        self.name = name

        self.maxHp = maxHp
        self.curHp = self.maxHp

        self.atk = atk
        self.defense = defense
        self.luck = luck
        self.level = level

        self.maxExp = maxExp
        self.curExp = 0

        self.gold = gold

        self.maxMana = maxMana
        self.curMana = self.maxMana

        self.mulEmp = 2


    def isDead(self):
        if self.curHp <= 0:
            self.__del__()

    def __del__(self):
        print("죽었습니다.")
        print(self.gold, "골드와", self.curExp, "경험치를 잃었습니다.")

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
        va.progressText += "플레이어가 " + str(monster.name) + \
                           "에게 " + str(self.atk) + "의 데미지를 주었습니다.\n"

    def Dead(self):
        va.progressText += "플레이어가 죽었습니다.\n"
        self.gold /= 2
        self.curExp = 0

    def defense(self, monster):
        self.isDefense = True
        self.cuHp -= monster.atk * (1 - self.defense / 100)
        va.progressText += "플레이어가 방어했습니다!\n"

    def skill_1(self, monster):
        monster.curHp -= self.atk
        va.progressText += "플레이어가 스킬1을 사용해 " + str(monster.name) + \
                           "에게 " + str(self.atk) + "의 데미지를 주었습니다.\n"

    def skill_2(self, monster):
        monster.curHp -= self.atk
        va.progressText += "플레이어가 스킬2를 사용해 " + str(monster.name) + \
                           "에게 " + str(self.atk) + "의 데미지를 주었습니다.\n"

    def skill_3(self, monster):
        monster.curHp -= self.atk
        va.progressText += "플레이어가 스킬3을 사용해 " + str(monster.name) + \
                           "에게 " + str(self.atk) + "의 데미지를 주었습니다.\n"

    def setInt(self):
        self.atk = int(self.atk)
        self.maxHp = int(self.maxHp)
        self.defense = int(self.defense)
        self.maxExp = int(self.maxExp)