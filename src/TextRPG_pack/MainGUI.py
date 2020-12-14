# main GUI

from PyQt5.QtCore import Qt

# text
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QLabel

# layout
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout, QVBoxLayout

# layout size
from PyQt5.QtWidgets import QSizePolicy

# widget
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QProgressBar

# button
from PyQt5.QtWidgets import QToolButton

# else
import urllib.request

import System.system as system
from PyQt5.QtGui import *

from Systems import Systems

import Character.CharacterAction as ch
import Monster.MonsterAction as ms
import Monster.MonsterList as ml

import Variables.variable as va


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 40)
        size.setWidth(max(size.width(), size.height()))
        return size


class TextRPG(QWidget):

    sys = Systems()
    chrInfo = ch.Character("용사", 2000, 40, 100, 10, 10, 1, 100, 0)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.messageEdit.setText("플레이어의 직업을 선택해주세요.")
        self.btn1.setText("전사")
        self.btn2.setText("궁수")
        self.btn3.setText("마법사")
        self.showStatusEdit()

    def showStatusEdit(self):
        self.chrInfo.setInt()
        statusText = "레벨 : " + str(self.chrInfo.level) + \
                     "\t최대체력 : " + str(self.chrInfo.maxHp) + \
                     "\t최대마나 : " + str(self.chrInfo.maxMana) + \
                     "\t공격력 : " + str(self.chrInfo.atk) + \
                     "\t방어력 : " + str(self.chrInfo.defense) + \
                     "\t운 : " + str(self.chrInfo.luck) + \
                     "\t골드 : " + str(self.chrInfo.gold)

        self.statusEdit.clear()
        for i in statusText.split("\t"):
            temp = ""
            temp += "<span style=\" font-size:22pt; font-weight:600; color:#000000;\" >"
            temp += i
            temp += "</span>"
            self.statusEdit.append(temp)

    def initUI(self):
        self.playerUI()
        self.monsterUI()
        self.mergeUI()

        hbox = QHBoxLayout()

        vbox1 = QVBoxLayout()
        vbox1.addLayout(self.mergedDisplayUI)

        vbox2 = QVBoxLayout()
        self.progressEdit = QTextEdit()
        self.progressEdit.setReadOnly(True)
        self.messageEdit = QLineEdit()
        self.messageEdit.setReadOnly(True)
        self.statusEdit = QTextEdit()
        self.statusEdit.setReadOnly(True)
        vbox2.addWidget(self.messageEdit)
        vbox2.addWidget(self.progressEdit)
        vbox2.addWidget(self.statusEdit)

        buttonHbox1 = QHBoxLayout()
        buttonHbox2 = QHBoxLayout()
        buttonHbox3 = QHBoxLayout()
        vbox1.addLayout(buttonHbox1)
        vbox1.addLayout(buttonHbox2)
        vbox1.addLayout(buttonHbox3)

        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)

        self.setLayout(hbox)

        buttonHbox1.addWidget(Button("공격", self.buttonEvent))
        buttonHbox1.addWidget(Button("방어", self.buttonEvent))
        buttonHbox1.addWidget(Button("스킬1", self.buttonEvent))
        buttonHbox1.addWidget(Button("스킬2", self.buttonEvent))
        buttonHbox1.addWidget(Button("스킬3", self.buttonEvent))

        buttonHbox2.addWidget(Button("상점", self.buttonEvent))
        buttonHbox2.addWidget(Button("다음 스테이지", self.nextStage))
        buttonHbox2.addWidget(Button("던전나가기", self.buttonEvent))

        self.btn1 = Button("버섯던전", self.buttonEvent)
        buttonHbox3.addWidget(self.btn1)
        self.btn2 = Button("슬라임던전", self.buttonEvent)
        buttonHbox3.addWidget(self.btn2)
        self.btn3 = Button("늑대던전", self.buttonEvent)
        buttonHbox3.addWidget(self.btn3)


    # 왼쪽 상단 GUI

    def playerUI(self):
        playerImg = "Art/모험가.jpeg"

        # player text ui
        self.playerImgUI = QLabel()
        self.playerImgUI.setPixmap(QPixmap(playerImg).scaled(250, 250))

        # player 마나 바 & 체력 & 경험치 바

        self.playerPhysicalBar = QProgressBar(self)
        self.playerManaBar = QProgressBar(self)
        self.playerExpBar = QProgressBar(self)

        self.showPlayerInfo()

        # set position of process bar
        self.playerPhysicalBar.setGeometry(20, 20, 300, 25)
        self.playerManaBar.setGeometry(20, 20, 300, 25)
        self.playerExpBar.setGeometry(20, 20, 300, 25)

        # changing the color of process bar
        self.playerPhysicalBar.setStyleSheet("QProgressBar::chunk "
                                             "{"
                                             "background-color: #FF3000;"
                                             "}")

        self.playerManaBar.setStyleSheet("QProgressBar::chunk "
                                         "{"
                                         "background-color: #0063FF;"
                                         "}")

        self.playerExpBar.setStyleSheet("QProgressBar::chunk "
                                                 "{"
                                                 "background-color: #42FF67;"
                                                 "}")

    def chgPlayerImg(self, job):
        if job == "전사":
            self.playerImg = "Art/전사.png"
        elif job == "궁수":
            self.playerImg = "Art/궁수.png"
        elif job == "마법사":
            self.playerImg = "Art/마법사.png"

        self.playerImgUI.setPixmap(QPixmap(self.playerImg).scaled(250, 250))

    def monsterUI(self):
        self.monsterImg = "Art/투명.png"

        # monster text ui
        self.monsterImgUI = QLabel()
        self.monsterImgUI.setPixmap(QPixmap(self.monsterImg).scaled(250, 250))
        self.monsterImgUI.setGeometry(20, 20, 200, 200)

        # monter 마나 바 & 체력 바
        self.monsterPhysicalBar = QProgressBar(self)

        # set position of process bar
        self.monsterPhysicalBar.setGeometry(20, 20, 300, 25)

        # changing the color of process bar
        self.monsterPhysicalBar.setStyleSheet("QProgressBar::chunk "
                                              "{"
                                              "background-color: #FF3000;"
                                              "}")

    def chgMonsterImg(self, name):
        if self.sys.isDungeon():
            if va.isMonsterDead:
                self.monsterImg = "Art/폭발.jpeg"
            else:
                if name == "주황버섯":
                    self.monsterImg = "Art/주황버섯.png"
                elif name == "파랑버섯":
                    self.monsterImg = "Art/파랑버섯.png"
                elif name == "뿔버섯":
                    self.monsterImg = "Art/뿔버섯.png"
                elif name == "좀비버섯":
                    self.monsterImg = "Art/좀비버섯.png"
                elif name == "변형된 주황버섯":
                    self.monsterImg = "Art/변형된 주황버섯.png"
                elif name == "슬라임":
                    self.monsterImg = "Art/슬라임.png"
                elif name == "레드슬라임":
                    self.monsterImg = "Art/레드슬라임.png"
                elif name == "실버슬라임":
                    self.monsterImg = "Art/실버슬라임.png"
                elif name == "큐브슬라임":
                    self.monsterImg = "Art/큐브슬라임.png"
                elif name == "변형된 슬라임":
                    self.monsterImg = "Art/변형된 슬라임.png"
                elif name == "늑대":
                    self.monsterImg = "Art/늑대.png"
                elif name == "치와와":
                    self.monsterImg = "Art/치와와.png"
                elif name == "케르베로스":
                    self.monsterImg = "Art/케르베로스.png"
                elif name == "고양이":
                    self.monsterImg = "Art/고양이.png"
                elif name == "시바":
                    self.monsterImg = "Art/시바.png"
        else:
            self.monsterImg = "Art/투명.png"

        self.monsterImgUI.setPixmap(QPixmap(self.monsterImg).scaled(250, 250))

    def showMonsterInfo(self):
        hpVal = int((self.monsterInfo.curHp / self.monsterInfo.maxHp) * 100)
        self.monsterPhysicalBar.setValue(hpVal)

    def showPlayerInfo(self):
        hpVal = int((self.chrInfo.curHp / self.chrInfo.maxHp) * 100)
        self.playerPhysicalBar.setValue(hpVal)

        manaVal = int((self.chrInfo.curMana / self.chrInfo.maxMana) * 100)
        self.playerManaBar.setValue(manaVal)

        expVal = int((self.chrInfo.curExp / self.chrInfo.maxExp) * 100)
        self.playerExpBar.setValue(expVal)

    def mergeUI(self):
        # 레이아웃 생성
        self.mergedPlayerUI = QHBoxLayout()
        self.mergePlayerStatusUI = QVBoxLayout()

        self.mergedMonsterUI = QHBoxLayout()
        self.mergeMonsterStatusUI = QVBoxLayout()

        self.mergedDisplayUI = QVBoxLayout()

        # merge player 마나 & 체력 & 경험치 바
        self.mergePlayerStatusUI.addWidget(self.playerPhysicalBar)
        self.mergePlayerStatusUI.addWidget(self.playerManaBar)
        self.mergePlayerStatusUI.addWidget(self.playerExpBar)

        # merge monster 마나 & 체력 & 경험치 바
        self.mergeMonsterStatusUI.addWidget(self.monsterPhysicalBar)

        # merge player layout
        self.mergedPlayerUI.addWidget(self.playerImgUI)
        self.mergedPlayerUI.addLayout(self.mergePlayerStatusUI)

        # merge monster layout
        self.mergedMonsterUI.addLayout(self.mergeMonsterStatusUI)
        self.mergedMonsterUI.addWidget(self.monsterImgUI)

        # merge display ui
        self.mergedDisplayUI.addLayout(self.mergedMonsterUI)
        self.mergedDisplayUI.addLayout(self.mergedPlayerUI)

    # 왼쪽 하단 GUI 버튼 이벤트 들

    def buttonEvent(self):
        sender = self.sender()

        if self.sys.isStart():
            if self.sys.isDungeon():
                if sender.text() == "던전나가기":
                    self.messageEdit.setText("던전에서 나왔습니다.")
                    va.monsterIndex = 0
                    self.sys.changeDungeonVal()
                    self.chgMonsterImg(None)
                    va.progressText = ""
                    self.progressEdit.clear()
                    self.monsterPhysicalBar.setValue(0)
                    return
                if not va.isMonsterDead:
                    if sender.text() == "공격":
                        self.chrInfo.attack(self.monsterInfo)
                        print(self.monsterInfo.maxHp, self.monsterInfo.curHp)
                    elif sender.text() == "방어":
                        print("방어")
                    elif sender.text() == "스킬1":
                        print("스킬1")
                    elif sender.text() == "스킬2":
                        print("스킬2")

                    self.monsterInfo.attack(self.chrInfo)
                    self.isDead()
                    self.isLevelUp()

                    self.showMonsterInfo()
                    self.showPlayerInfo()
                    self.showStatusEdit()
                    self.progressEdit.setText(va.progressText)
                else:
                    return
            else:
                if sender.text() == "상점":
                    print("상점")
                if sender.text() == "버섯던전":
                    va.dungeon = "버섯던전"
                    va.isMonsterDead = False
                    self.messageEdit.setText("버섯던전에 입장하셨습니다.")
                    self.monsterInfo = self.newMonster(va.dungeon, va.monsterIndex)

                    va.progressText += "야생의 " + self.monsterInfo.name + "이(가) 나타났다!\n"
                    self.progressEdit.setText(va.progressText)

                    self.sys.changeDungeonVal()

                    self.chgMonsterImg(self.monsterInfo.name)

                    self.showMonsterInfo()

                if sender.text() == "슬라임던전":
                    va.dungeon = "슬라임던전"
                    va.isMonsterDead = False
                    self.monsterInfo = ms.Monster("슬라임", 1000, 100, 1, 10, 10)
                    self.messageEdit.setText("슬라임던전에 입장하셨습니다.")

                    va.progressText += "야생의 " + self.monsterInfo.name + "이(가) 나타났다!\n"
                    self.progressEdit.setText(va.progressText)

                    self.sys.changeDungeonVal()

                    self.chgMonsterImg(self.monsterInfo.name)

                    self.showMonsterInfo()

                if sender.text() == "늑대던전":
                    va.dungeon = "늑대던전"
                    va.isMonsterDead = False
                    self.monsterInfo = ms.Monster("늑대", 1000, 100, 1, 50, 10)
                    self.messageEdit.setText("늑대던전에 입장하셨습니다.")

                    va.progressText += "야생의 " + self.monsterInfo.name + "이(가) 나타났다!\n"
                    self.progressEdit.setText(va.progressText)

                    self.sys.changeDungeonVal()

                    self.chgMonsterImg(self.monsterInfo.name)

                    self.showMonsterInfo()
        else:
            try:
                if sender.text() == "전사":
                    self.messageEdit.setText("당신의 직업은 전사입니다.")
                    self.chrInfo = ch.Character("전사", 1500, 20, 100, 50, 10, 1, 100, 50)
                    self.showStatusEdit()
                elif sender.text() == "궁수":
                    self.messageEdit.setText("당신의 직업은 궁수입니다.")
                    self.chrInfo = ch.Character("궁수", 1000, 30, 150, 20, 50, 1, 100, 50)
                    self.showStatusEdit()
                elif sender.text() == "마법사":
                    self.messageEdit.setText("당신의 직업은 마법사입니다.")
                    self.chrInfo = ch.Character("전사", 1000, 40, 150, 20, 20, 1, 100, 50)
                    self.showStatusEdit()
                self.chgPlayerImg(sender.text())
                self.sys.changeStartVal()
                self.btn1.setText("버섯던전")
                self.btn2.setText("슬라임던전")
                self.btn3.setText("늑대던전")
            except AttributeError:
                self.messageEdit.setText("직업을 먼저 선택해주세요.")
                return

    def nextStage(self):
        if va.isMonsterDead:
            va.isMonsterDead = False
            va.monsterIndex += 1
            if va.monsterIndex > 4:
                va.monsterIndex = 0
                return
            self.monsterInfo = self.newMonster(va.dungeon, va.monsterIndex)
            self.generateMonster()


    def newMonster(self, dungeon, index):
        if dungeon == "버섯던전":
            keys = list(ml.mushrooms.keys())
            values = list(ml.mushrooms.values())
        elif dungeon == "슬라임던전":
            keys = list(ml.slimes.keys())
            values = list(ml.slimes.values())
        elif dungeon == "늑대던전":
            keys = list(ml.wolves.keys())
            values = list(ml.wolves.values())

        name = keys[index]
        maxHp = values[index][0]
        atk = values[index][1]
        lvl = values[index][2]
        dropExp = values[index][3]
        dropGold = values[index][4]

        monster = ms.Monster(name, maxHp, atk, lvl, dropExp, dropGold)

        return monster

    def generateMonster(self):
        va.progressText = ""
        self.progressEdit.clear()
        va.progressText += "야생의 " + self.monsterInfo.name + "이(가) 나타났다!\n"
        self.progressEdit.setText(va.progressText)
        self.chgMonsterImg(self.monsterInfo.name)

        self.showMonsterInfo()


    def isLevelUp(self):
        if self.chrInfo.curExp >= self.chrInfo.maxExp:
            self.chrInfo.curExp = self.chrInfo.curExp - self.chrInfo.maxExp
            self.chrInfo.maxExp *= 1.5
            self.chrInfo.level += 1

            self.chrInfo.maxHp *= 1.1
            self.chrInfo.defense *= 1.1
            self.chrInfo.atk *= 1.1
            self.chrInfo.maxMana += 2

    def isDead(self):
        if self.monsterInfo.curHp <= 0:
            self.monsterInfo.curHp = 0
            va.isMonsterDead = True
            self.monsterInfo.Dead(self.chrInfo)
            self.chgMonsterImg(None)
            self.showStatusEdit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    rpg = TextRPG()
    rpg.show()
    sys.exit(app.exec_())