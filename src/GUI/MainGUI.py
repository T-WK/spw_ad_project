# main GUI

from PyQt5.QtCore import Qt

# text
from PyQt5.QtWidgets import QLineEdit, QTextEdit

# layout
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout, QVBoxLayout

# layout size
from PyQt5.QtWidgets import QSizePolicy

# widget
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QProgressBar

# button
from PyQt5.QtWidgets import QToolButton

# else
from keypads import attacBtnList, menuBtnList


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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.playerUI()
        self.monsterUI()
        self.mergeUI()

        hbox = QHBoxLayout()

        vbox = QVBoxLayout()
        vbox.addLayout(self.mergedDisplayUI)

        grid = QGridLayout()
        vbox.addLayout(grid)

        hbox.addLayout(vbox)
        hbox.addWidget(QTextEdit())

        self.setLayout(hbox)

        grid.addWidget(Button("공격", self.buttonEvent), 0, 0)
        grid.addWidget(Button("방어", self.buttonEvent), 0, 1)
        grid.addWidget(Button("스킬", self.buttonEvent), 0, 2)

        grid.addWidget(Button("상점", self.buttonEvent), 1, 0)
        grid.addWidget(Button("도망가기", self.buttonEvent), 1, 1)
        grid.addWidget(Button("던전나가기", self.buttonEvent), 1, 2)





    # 왼쪽 상단 GUI

    def playerUI(self):
        # player text ui
        self.playerTextUI = QTextEdit()
        self.playerTextUI.setAcceptRichText(False)

        # player 마나 바 & 체력 & 경험치 바
        self.playerPhysicalBar = QProgressBar(self)
        self.playerManaBar = QProgressBar(self)
        self.playerExperiencevalue = QProgressBar(self)

        # set position of process bar
        self.playerPhysicalBar.setGeometry(20, 20, 300, 25)
        self.playerManaBar.setGeometry(20, 20, 300, 25)
        self.playerExperiencevalue.setGeometry(20, 20, 300, 25)

        # changing the color of process bar
        self.playerPhysicalBar.setStyleSheet("QProgressBar::chunk "
                                             "{"
                                             "background-color: #FF3000;"
                                             "}")

        self.playerManaBar.setStyleSheet("QProgressBar::chunk "
                                         "{"
                                         "background-color: #0063FF;"
                                         "}")

        self.playerExperiencevalue.setStyleSheet("QProgressBar::chunk "
                                                 "{"
                                                 "background-color: #42FF67;"
                                                 "}")

    def monsterUI(self):
        # monster text ui
        self.monsterTextUI = QTextEdit()
        self.monsterTextUI.setAcceptRichText(False)

        # monter 마나 바 & 체력 바
        self.monsterPhysicalBar = QProgressBar(self)
        self.monsterManaBar = QProgressBar(self)

        # set position of process bar
        self.monsterPhysicalBar.setGeometry(20, 20, 300, 25)
        self.monsterManaBar.setGeometry(20, 20, 300, 25)

        # changing the color of process bar
        self.monsterPhysicalBar.setStyleSheet("QProgressBar::chunk "
                                              "{"
                                              "background-color: #42FF67;"
                                              "}")

        self.monsterManaBar.setStyleSheet("QProgressBar::chunk "
                                          "{"
                                          "background-color: #0063FF;"
                                          "}")

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
        self.mergePlayerStatusUI.addWidget(self.playerExperiencevalue)

        # merge monster 마나 & 체력 & 경험치 바
        self.mergeMonsterStatusUI.addWidget(self.monsterPhysicalBar)
        self.mergeMonsterStatusUI.addWidget(self.monsterManaBar)

        # merge player layout
        self.mergedPlayerUI.addWidget(self.playerTextUI)
        self.mergedPlayerUI.addLayout(self.mergePlayerStatusUI)

        # merge monster layout
        self.mergedMonsterUI.addLayout(self.mergeMonsterStatusUI)
        self.mergedMonsterUI.addWidget(self.monsterTextUI)

        # merge display ui
        self.mergedDisplayUI.addLayout(self.mergedMonsterUI)
        self.mergedDisplayUI.addLayout(self.mergedPlayerUI)



    # 왼쪽 하단 GUI



    def buttonEvent(self):
        sender = self.sender()
        if sender.text() == "공격":
            print("공격")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    rpg = TextRPG()
    rpg.show()
    sys.exit(app.exec_())