from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize
import sys
import vlc

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Pyrocinical Soundboard'
        self.left = 10
        self.top = 10
        self.width = 375
        self.height = 290
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.backI = QLabel(self)
        self.backI.setPixmap(QPixmap('resources/back2.jpg'))
        self.backI.setGeometry(0, 0, self.width, self.height)

        a1 = QPushButton('I love fortnite', self)
        a1.resize(110, 30)
        a1.move(10, 10)
        a1.clicked.connect(lambda:self.on_click('resources/iLoveFortnite.mp3'))

        a2 = QPushButton('noob!', self)
        a2.resize(110, 30)
        a2.move(132.5, 10)
        a2.clicked.connect(lambda:self.on_click('resources/noob.mp3'))

        a3 = QPushButton('I hate you', self)
        a3.resize(110, 30)
        a3.move(255, 10)
        a3.clicked.connect(lambda:self.on_click('resources/IHateYou.mp3'))

        a4 = QPushButton('#ads', self)
        a4.resize(110, 30)
        a4.move(10, 70)
        a4.clicked.connect(lambda:self.on_click('resources/hash_ad.mp3'))

        a5 = QPushButton('merch', self)
        a5.resize(110, 30)
        a5.move(132.5, 70)
        a5.clicked.connect(lambda:self.on_click('resources/merch.mp3'))

        a6 = QPushButton('merch2', self)
        a6.resize(110, 30)
        a6.move(255, 70)
        a6.clicked.connect(lambda:self.on_click('resources/merch2.mp3'))

        a7 = QPushButton('communism', self)
        a7.resize(110, 30)
        a7.move(10, 130)
        a7.clicked.connect(lambda:self.on_click('resources/communism.mp3'))

        a8 = QPushButton('text my wife', self)
        a8.resize(110, 30)
        a8.move(132.5, 130)
        a8.clicked.connect(lambda:self.on_click('resources/textingMyWife.mp3'))

        a9 = QPushButton('prison', self)
        a9.resize(110, 30)
        a9.move(255, 130)
        a9.clicked.connect(lambda:self.on_click('resources/prison.mp3'))

        a10 = QPushButton('Oj Simpson', self)
        a10.resize(110, 30)
        a10.move(10, 190)
        a10.clicked.connect(lambda:self.on_click('resources/ojSimpson.mp3'))

        a11 = QPushButton('fortnite', self)
        a11.resize(110, 30)
        a11.move(132.5, 190)
        a11.clicked.connect(lambda:self.on_click('resources/fortnite2.mp3'))

        a12 = QPushButton('epic', self)
        a12.resize(110, 30)
        a12.move(255, 190)
        a12.clicked.connect(lambda:self.on_click('resources/epic.mp3'))

        a13 = QPushButton('no slave', self)
        a13.resize(110, 30)
        a13.move(10, 250)
        a13.clicked.connect(lambda:self.on_click('resources/noSlave.mp3'))

        a14 = QPushButton('women', self)
        a14.resize(110, 30)
        a14.move(132.5, 250)
        a14.clicked.connect(lambda:self.on_click('resources/respectWomen.mp3'))

        a15 = QPushButton('pyrofam', self)
        a15.resize(110, 30)
        a15.move(255, 250)
        a15.clicked.connect(lambda:self.on_click('resources/pyrofam.mp3'))

        self.show()

    @pyqtSlot()
    def on_click(self, path):
        player = vlc.MediaPlayer(path)
        player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
