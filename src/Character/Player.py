# 캐릭터 공통 클래스

class Player:
    name = ""
    job = ""
    exp = 0
    gold = 0
    item = ""
    lvl = 1

    def __init__(self, name, job, lvl, exp, gold, item):
        self.name = name
        self.job = job
        self.lvl = lvl
        self.exp = exp
        self.gold = gold
        self.item = item

    def __del__(self):
        print("죽었습니다.")

    def attack(self, atk, luk):
        pass

    def defense(self, defense, luk):
        pass

    def skill(self, atk, defense, mana, luk):
        pass

