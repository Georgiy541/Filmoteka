from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QTableWidget, QHBoxLayout


class MainWindowTable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Фильмотека')
        self.setGeometry(500, 200, 500, 400)

        self.add_button = QPushButton('Добавить', self)

        self.films_table = QTableWidget(self)
        self.films_table.setGeometry(0, 30, 500, 370)
        

if __name__ == "__main__":
    App = QApplication([])
    window = MainWindowTable()
    window.show()
    App.exec()