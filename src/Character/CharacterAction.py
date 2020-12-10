class Character:

    def __init__(self, name, hp, atk, defense, luck, level, exp, maxExp, gold):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.luck = luck
        self.level = level
        self.exp = exp
        self.maxExp = maxExp
        self.gold = gold
        self.mana
        self.mulEmp = 2

    def isDead(self):
        if self.hp <= 0:
            self.__del__(self.dropExp, self.dropGold)

    def __del__(self, dropExp, dropGold):
        print("죽었습니다.")
        print(dropGold, "골드와", dropExp, "경험치를 잃었습니다.")

    def setHp(val):
        self.hp = val
    
    def setMana(val):
        self.mana = val
    
    def setExp(val):
        self.exp = val

        if self.exp >= self.maxExp:
            setLevel(self.maxExp//self.exp, self.maxExp%self.exp)

    def setLevel(level, exp):
        self.level += level
        self.exp = exp
        self.maxExp *= self.mulEmp**level
    
    def setGold(val):
        self.gold += val
    
