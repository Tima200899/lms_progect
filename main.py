import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel
)

class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Система управления библиотекой")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel("Добавить книгу:")
        self.layout.addWidget(self.label)

        self.book_input = QLineEdit()
        self.book_input.setPlaceholderText("Введите название книги")
        self.layout.addWidget(self.book_input)

        self.add_button = QPushButton("Добавить книгу")
        self.add_button.clicked.connect(self.add_book)
        self.layout.addWidget(self.add_button)

        self.book_list = QListWidget()
        self.layout.addWidget(self.book_list)

        self.setLayout(self.layout)

    def add_book(self):
        book_title = self.book_input.text()
        if book_title:
            self.book_list.addItem(book_title)
            self.book_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())
