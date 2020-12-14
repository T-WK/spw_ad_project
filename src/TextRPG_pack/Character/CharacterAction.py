import Variables.variable as va


class Character:

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
            va.progressText += "죽었습니다.\n"
            va.progressText += str(self.gold*0.5) + "골드와" + str(self.curExp) + "경험치를 잃었습니다."
            self.curExp = 0
            self.gold = self.gold*0.5

    def setHp(self, val):
        self.curHp = val

    def getHp(self):
        return self.curHp

    def setMana(self, val):
        self.curMana = val

    def setExp(self, val):
        self.curExp = val

        if self.curExp >= self.maxExp:
            self.setLevel(self.maxExp // self.curExp, self.maxExp % self.curExp)

    def setLevel(self, level, exp):
        self.level += level
        self.curExp = exp
        self.maxExp *= self.mulEmp ** level

    def setGold(self, val):
        self.gold += val

    def attack(self, monster):
        monster.curHp -= self.atk
        va.progressText += "플레이어가 공격했습니다!\n"

    def Defense(self, monster):
        self.curHp -= monster.atk * (1 - self.defense / 100)
        va.progressText += "플레이어가 방어했습니다!\n"

    def skill_1(self, monster):
        monster.curHp -= self.atk  # 스킬 값 넣어줘야함
        va.progressText += "플레이어가 스킬1을 사용 했습니다!\n"

    def skill_2(self, monster):
        monster.curHp -= self.atk  # 스킬 값 넣어줘야함
        va.progressText += "플레이어가 스킬2를 사용 했습니다!\n"

    def skill_3(self, monster):
        monster.curHp -= self.atk  # 스킬 값 넣어줘야함
        va.progressText += "플레이어가 스킬3를 사용 했습니다!\n"

    def setInt(self):
        self.atk = int(self.atk)
        self.maxHp = int(self.maxHp)
        self.defense = int(self.defense)
        self.maxExp = int(self.maxExp)
