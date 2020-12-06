# 캐릭터 공통 클래스
import Archer



class Player:
    hp = 0
    atk = 0
    defense = 0
    mana = 0
    luk = 0
    exp = 0
    gold = 0
    item = ""
    lvl = 1

    name = ""
    job = ""

    def __init__(self, name, job):
        self.name = name
        self.job = job


    def updateStatus(self, ):


    def __del__(self):
        print("죽었습니다.")

    def attack(self, atk, luk):
        pass

    def defense(self, defense, luk):
        pass

    def skill(self, atk, defense, mana, luk):
        pass

p = Player("지존용사", "도적")



