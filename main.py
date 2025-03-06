import sys

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save_informacion)
        self.show()

    def save_informacion(self):
        name = self.ui.nameEdit.text()
        lastName = self.ui.lastNameEdit.text()
        date = self.ui.birthDateEdit.text()
        pesel = self.ui.peselEdit.text()
        street = self.ui.streetEdit.text()
        zipCode = self.ui.zipCodeEdit.text()
        city = self.ui.cityEdit.text()

        informacion = f'{name} | {lastName} | {date} | {pesel} | {street} | {zipCode} | {city}'

        file = open('date.txt', 'a')
        file.write(informacion + '\n')
        file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    sys.exit(app.exec())


