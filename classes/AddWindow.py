from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QComboBox


class AddWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Добавить элемент")
        self.setFixedSize(300, 190)
        self.name_label = QLabel("Название", self)
        self.year_label = QLabel("Год выпуска", self)
        self.genre_label = QLabel("Жанр", self)
        self.length_label = QLabel("Длина", self)
        self.add_button = QPushButton("Добавить", self)

        self.name_edit = QLineEdit(self)
        self.year_edit = QLineEdit(self)
        self.genre_box = QComboBox(self)
        self.length_edit = QLineEdit(self)

        self.name_label.move(10, 10)
        self.name_edit.move(90, 10)

        self.year_label.move(10, 40)
        self.year_edit.move(90, 40)

        self.genre_label.move(10, 70)
        self.genre_box.move(90, 70)

        self.length_label.move(10, 100)
        self.length_edit.move(90, 100)

        self.add_button.move(180, 140)
        self.add_button.resize(100, 40)


if __name__ == "__main__":
    App = QApplication([])
    window = AddWindow()
    window.show()
    App.exec()