import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 700, 700)
        self.setWindowTitle('работа с картой')
        self.map_frame = QLabel(self)
        response = requests.get("http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map")
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(self.map_file)
        self.map_frame.setPixmap(self.pixmap)
        self.map_frame.move(100, 100)
        self.map_frame.resize(500, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = MainScreen()
    screen.show()
    sys.exit(app.exec())
