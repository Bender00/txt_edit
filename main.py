from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Створенно вікно самого редактора
        self.setWindowTitle("Редактор кода")
        self.setGeometry(300, 250, 350, 200)

        # Створенно текстове поле 
        self.text_edit = QtWidgets.QTextEdit(self)
        
        # Вказуємо, що найбільшу область буде займати віджет text_edit
        self.setCentralWidget(self.text_edit)

        # Створення меню
        self.createMenuBar()

    def createMenuBar(self):
        # Створення об!єкта яке повністю наслідує QmenuBar
        self.menuBar = QMenuBar(self)

        # Вказуємо, що у вікна буде MenuBar
        self.setMenuBar(self.menuBar)

        # Створення елементів menu
        fileMenu = QMenu("&File", self)
        # Добавляємо пункт 'File' в menu
        self.menuBar.addMenu(fileMenu)

        # Створення підпунктів до 'File'
        # open_file = fileMenu.addMenu("&Open File")
        # save_menu = fileMenu.addMenu("&Save File")
        fileMenu.addAction('Open File', self.action_clicked)
        fileMenu.addAction('Save File', self.action_clicked)

    @QtCore.pyqtSlot() # створення аннотації яка буде обробляти всі кліки по menu
    def action_clicked(self):
        # Через sender можна отримати повну інформацію про об!єкт на який клікнули
        action = self.sender()
        #print("Action: " + action.text())
        if action.text() == "Open File":
            print("Open")
            fname = QFileDialog.getOpenFileName(self)[0]

            #Вилавлюємо помилки
            try:
                f = open(fname, 'r')
                # читаємо файл
                with f:
                    #Кожну строку зберігаємо у data
                    data = f.read()
                    # Кожну строку передаємо у текстове поле редактора кода
                    self.text_edit.setText(data)
                f.close()

            except FileNotFoundError:
                print("No such file")
            
        elif action.text() == "Save File":
            print("Save")
            fname = QFileDialog.getSaveFileName(self)[0]
            #Вилавлюємо помилки
            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No such file")

def application():
    # в app передаємо данні про систему на якій запущена програма
    app = QApplication(sys.argv)

    # Наслідує все із класу Window
    window = Window()

    #корректно закриваємо вікна
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()