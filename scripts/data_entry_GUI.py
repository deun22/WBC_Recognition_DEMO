from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout,QMessageBox)

import sys

def runit():
    app = QApplication(sys.argv)
    dialog = data_entry(app)
    run = dialog.exec_()
    return dialog.getinfo(), run

def stop(run):
    sys.exit(run)

class data_entry(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self,app):
        self.app = app
        super(data_entry, self).__init__()

        self.makeform()

        #button_login = QPushButton('Login')
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Laboratory Technician Terminal")

        self.success = False
        print("Data Entry Screen")

    def makeform(self):
        self.formGroupBox = QGroupBox("Enter Specimen Information")
        layout = QFormLayout()
        self.line_edit_firstname = QLineEdit()
        self.line_edit_lastname = QLineEdit()
        self.line_edit_dob = QLineEdit()
        self.line_edit_ssn = QLineEdit()

        layout.addRow(QLabel("First Name:"), self.line_edit_firstname)
        layout.addRow(QLabel("Last Name:"), self.line_edit_lastname)
        layout.addRow(QLabel("DOB:"), self.line_edit_dob)
        layout.addRow(QLabel("SSN:"), self.line_edit_ssn)
        #layout.addRow(QLabel("Country:"), QComboBox())
        #layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)


    def accept(self):
        msg = QMessageBox()
        if self.line_edit_firstname.text() != '' and self.line_edit_lastname.text() != '' and self.line_edit_dob.text() != '' and self.line_edit_ssn.text() != '':
            msg.setText('Success')
            msg.exec_()
            self.app.quit()
            self.success = True
            return self.line_edit_firstname.text(), self.line_edit_lastname.text(), self.line_edit_dob.text(), self.line_edit_ssn.text()

        else:
            msg.setText('Empty Fields')
            msg.exec_()
            self.success = False
    def getinfo(self):
        return self.line_edit_firstname.text(), self.line_edit_lastname.text(), self.line_edit_dob.text(), self.line_edit_ssn.text(), self.success


