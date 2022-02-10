from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 700, 700)
        self.setWindowTitle('работа с картой')
        self.map_frame = QLabel(self)
        # self.map_frame.setPixmap()  сюда добавишь картинку
        self.map_frame.resize(self.map_frame.pixmap().size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = MainScreen()
    screen.show()
    sys.exit(app.exec())
