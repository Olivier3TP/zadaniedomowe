import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox

from layout import Ui_Dialog
from person import Person
from persons import Persons


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.persons = Persons()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem([f'{p.name} {p.lastName}' for p in self.persons.persons])
        self.ui.saveButton.clicked.connect(self.save_informacion)
        self.show()

    def save_informacion(self):
        name = self.ui.nameEdit.text()
        lastName = self.ui.lastNameEdit.text()
        date = self.ui.birthDateEdit.date().toPyDate()
        pesel = self.ui.peselEdit.text()
        street = self.ui.streetEdit.text()
        zipCode = self.ui.zipCodeEdit.text()
        city = self.ui.cityEdit.text()

        # informacion = f'{name} | {lastName} | {date} | {pesel} | {street} | {zipCode} | {city}'
        try:
            self.persons.persons.append(Person(name, lastName, date, pesel, street, zipCode, city))
        except ValueError as e:
            message = QMessageBox()
            message.setText(e.__str__())
            message.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    sys.exit(app.exec())


