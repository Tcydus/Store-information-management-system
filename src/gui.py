from PyQt5.QtWidgets import QDialog, QListWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, QInputDialog, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
import sys

db_list = ((1, "water", 7),
           (2, "coke", 15)
          )

class ScanWindow(QWidget):
    def __init__(self):

        # You can use "super().__init__()" instead
        super(ScanWindow, self).__init__()
        
        self.list = QListWidget() # Create scan list

        self.total = QLabel("-") # Create total money label
        self.total.setStyleSheet("background-color: lightgreen")
        
        vbox = QVBoxLayout() # Group widget in vertical box layout

        vbox.addWidget(self.total)

        for text, func in (("Add", self.add),
                           ("Edit", self.edit),
                           ("Remove", self.remove),
                           ("Return", self.returnToMain)
                           ):

            buttons = QPushButton(text)
            buttons.clicked.connect(func)

            vbox.addWidget(buttons)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

        self.setWindowTitle("กับข้าวมาแล้วค๊าบบ")
        self.setWindowIcon(QIcon(".icon\\icon.png"))
        self.show()

    def add(self):
        ''' This function use for add item to cart list by manual '''

        row = self.list.currentRow()
        title = "Add item"
        message = "Enter QR CODE"
        
        string, ok = QInputDialog.getText(self, title, message)

        if ok and string is not None and not string.isspace():
            self.list.insertItem(row, string)


    def edit(self):
        ''' This function use for edit item by manual '''

        print("Edit")

    def remove(self):
        ''' This function use for remove item by manual '''

        print("Remove")

    def returnToMain(self):

        print("Return")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("Scan")
        self.button1.clicked.connect(self.scanClick)
        self.setCentralWidget(self.button1)
        self.show()
    def scanClick(self):
        self.new_window = ScanWindow()
        self.new_window.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    scan_window = Main()
    sys.exit(app.exec())

        

        