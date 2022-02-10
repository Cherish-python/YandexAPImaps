from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 700, 700)
        self.setWindowTitle('работа с картой')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = MainScreen()
    screen.show()
    sys.exit(app.exec())
