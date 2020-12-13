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
    chrInfo = ch.Character("용사", 2000, 100, 10, 10, 1, 100, 0)
    monsterInfo = ms.Monster("슬라임", 1000, 100, 1, 10, 10)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.messageEdit.setText("플레이어의 직업을 선택해주세요.")
        self.btn1.setText("전사")
        self.btn2.setText("궁수")
        self.btn3.setText("마법사")
        self.showStatusEdit()

    def showStatusEdit(self):
        statusText = "레벨 : " + str(self.chrInfo.level) + \
                     "\t최대체력 : " + str(self.chrInfo.maxHp) + \
                     "\t최대마나 : " + str(self.chrInfo.maxMana) + \
                     "\t공격력 : " + str(self.chrInfo.atk) + \
                     "\t방어력 : " + str(self.chrInfo.defense) + \
                     "\t운 : " + str(self.chrInfo.luck)

        self.statusEdit.clear()
        for i in statusText.split("\t"):
            temp = ""
            temp += "<span style=\" font-size:25pt; font-weight:600; color:#000000;\" >"
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
        buttonHbox2.addWidget(Button("도망가기", self.buttonEvent))
        buttonHbox2.addWidget(Button("던전나가기", self.buttonEvent))

        self.btn1 = Button("고블린던전", self.buttonEvent)
        buttonHbox3.addWidget(self.btn1)
        self.btn2 = Button("슬라임던전", self.buttonEvent)
        buttonHbox3.addWidget(self.btn2)
        self.btn3 = Button("늑대던전", self.buttonEvent)
        buttonHbox3.addWidget(self.btn3)


    # 왼쪽 상단 GUI

    def playerUI(self):
        playerImg = "../Art/모험가.jpeg"

        # player text ui
        self.playerImgUI = QLabel()
        self.playerImgUI.setPixmap(QPixmap(playerImg).scaled(250, 250))

        # player 마나 바 & 체력 & 경험치 바

        self.playerPhysicalBar = QProgressBar(self)
        self.playerManaBar = QProgressBar(self)
        self.playerExpBar = QProgressBar(self)

        hpVal = int((self.chrInfo.curHp / self.chrInfo.maxHp) * 100)
        self.playerPhysicalBar.setValue(hpVal)

        manaVal = int((self.chrInfo.curMana / self.chrInfo.maxMana) * 100)
        self.playerManaBar.setValue(manaVal)

        expVal = int((self.chrInfo.maxExp / self.chrInfo.curExp) * 100)
        self.playerExpBar.setValue(expVal)

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
            self.playerImg = "../Art/전사.png"
        elif job == "궁수":
            self.playerImg = "../Art/궁수.png"
        elif job == "마법사":
            self.playerImg = "../Art/마법사.png"

        self.playerImgUI.setPixmap(QPixmap(self.playerImg).scaled(250, 250))

    def monsterUI(self):
        self.monsterImg = "../Art/white.jpg"

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

    def chgMonsterImg(self):
        if self.sys.isDungeon():
            self.monsterImg = "../Art/슬라임.png"
        else:
            self.monsterImg = "../Art/white.jpg"

        self.monsterImgUI.setPixmap(QPixmap(self.monsterImg).scaled(250, 250))

    def showMonsterInfo(self):
        hpVal = int((self.monsterInfo.curHp / self.monsterInfo.maxHp) * 100)
        self.monsterPhysicalBar.setValue(hpVal)

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
                if sender.text() == "공격":
                    self.chrInfo.attack(self.monsterInfo)

                if sender.text() == "방어":
                    print("방어")
                
                if sender.text() == "스킬1":
                    print("스킬1")
                
                if sender.text() == "스킬2":
                    print("스킬2")

                if sender.text() == "도망가기":
                    print("도망가기")
                    self.sys.changeDungeonVal()
                if sender.text() == "던전나가기":
                    self.messageEdit.setText("던전에서 나왔습니다.")
                    
                    self.sys.changeDungeonVal()
                    self.chgMonsterImg()
                    self.monsterPhysicalBar.setValue(0)
                self.monsterInfo.attack()
                self.progressEdit.setText(va.progressText)
                self.monsterInfo.Dead()
                self.showMonsterInfo()
            else:
                if sender.text() == "상점":
                    print("상점")
            
                if sender.text() == "고블린던전":
                    self.messageEdit.setText("고블린던전에 입장하셨습니다.")

                    self.sys.changeDungeonVal()

                    self.chgMonsterImg()

                    self.showMonsterInfo()
            
                if sender.text() == "슬라임던전":
                    self.messageEdit.setText("슬라임던전에 입장하셨습니다.")

                    va.progressText += "야생의 " + self.monsterInfo.name + "이 나타났다!\n"
                    self.progressEdit.setText(va.progressText)

                    self.sys.changeDungeonVal()

                    self.chgMonsterImg()

                    self.showMonsterInfo()
            
                if sender.text() == "늑대던전":
                    self.messageEdit.setText("늑대던전에 입장하셨습니다.")
                
                    self.sys.changeDungeonVal()

                    self.chgMonsterImg()

                    self.showMonsterInfo()
        else:
            if sender.text() == "전사":
                self.messageEdit.setText("당신의 직업은 전사입니다.")
                self.chrInfo.maxHp = 1500
                self.chrInfo.maxMana = 20
                self.chrInfo.atk = 100
                self.chrInfo.defense = 50
                self.chrInfo.luck = 10
                self.showStatusEdit()
            elif sender.text() == "궁수":
                self.messageEdit.setText("당신의 직업은 궁수입니다.")
                self.chrInfo.maxHp = 1000
                self.chrInfo.maxMana = 30
                self.chrInfo.atk = 150
                self.chrInfo.defense = 20
                self.chrInfo.luck = 50
                self.showStatusEdit()
            elif sender.text() == "마법사":
                self.messageEdit.setText("당신의 직업은 마법사입니다.")
                self.chrInfo.maxHp = 1000
                self.chrInfo.maxMana = 40
                self.chrInfo.atk = 150
                self.chrInfo.defense = 20
                self.chrInfo.luck = 20
                self.showStatusEdit()
            self.chgPlayerImg(sender.text())
            self.sys.changeStartVal()
            self.btn1.setText("고블린던전")
            self.btn2.setText("슬라임던전")
            self.btn3.setText("늑대던전")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    rpg = TextRPG()
    rpg.show()
    sys.exit(app.exec_())