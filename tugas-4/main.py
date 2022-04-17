from cProfile import label
import sys
import random
import os.path
from tabnanny import check
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QPlainTextEdit,
    QFileDialog,
    QStackedWidget,
    QMessageBox,
    
)

from rsa import *
from ds import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tugas Kecil 4 II4031 Kriptografi dan Koding")
        self.setStyleSheet("font: 10pt Verdana;\n"
                            "background-color: #8ecae6")
        
        self.labeltitle = QLabel("Implementasi Program Tanda Tangan Digital")
        self.labeltitle.setStyleSheet("font: bold 10pt Verdana")
        self.labelsubtitle = QLabel("By: Nathaniel & Nadya\n")
        self.labelsubtitle.setStyleSheet("font: 10pt Verdana")

        self.labelfitur = QLabel("Fitur:")
        self.fitur = QComboBox()
        self.fitur.addItems(["Generate Key", "Sign Document", "Verify Document"])
        self.fitur.setStyleSheet("background-color: white")


        #layout generate key
        self.genkey = QPushButton("Generate Key")
        self.genkey.clicked.connect(self.gen)
        self.genkey.setStyleSheet("background-color: #023047;\n"
                                    "color: white")

        #layout sign
        self.labelinput = QLabel("Input:")
        self.chooseinputfile = QPushButton("Choose file")
        self.chooseinputfile.clicked.connect(self.open_input)
        self.chooseinputfile.setStyleSheet("background-color: #023047;\n"
                                            "color: white")

        self.inputdisplay = QPlainTextEdit()
        self.inputdisplay.setReadOnly(True)
        self.inputdisplay.setStyleSheet("background-color: white")
        self.inputfield = QPlainTextEdit()
        self.inputfield.setReadOnly(True)
        self.inputfield.setStyleSheet("background-color: white")

        self.keyfile = QPushButton("Choose key file")
        self.keyfile.clicked.connect(self.open_key)
        self.keyfile.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        self.keydisplay = QPlainTextEdit()
        self.keydisplay.setReadOnly(True)
        self.keydisplay.setStyleSheet("background-color: white")
        self.inputkey = QPlainTextEdit()
        self.inputkey.hide()
        self.inputn = QPlainTextEdit()
        self.inputn.hide()

        self.separate = QCheckBox("Save digital signature in a separate document")
        
        self.signing = QPushButton("Sign File")
        self.signing.clicked.connect(self.signing_function)
        self.signing.setStyleSheet("background-color: #FCE205;\n"
                                    "color: black")

        #layout verify
        self.labelinput2 = QLabel("Input:")
        self.chooseinputfile2 = QPushButton("Choose file")
        self.chooseinputfile2.clicked.connect(self.open_input)
        self.chooseinputfile2.setStyleSheet("background-color: #023047;\n"
                                            "color: white")

        self.inputdisplay2 = QPlainTextEdit()
        self.inputdisplay2.setReadOnly(True)
        self.inputdisplay2.setStyleSheet("background-color: white")
        self.inputfield2 = QPlainTextEdit()
        self.inputfield2.setReadOnly(True)
        self.inputfield2.setStyleSheet("background-color: white")

        self.separate2 = QCheckBox("Digital signature in a separate document")
        self.separate2.clicked.connect(self.check_state)
        self.choosesignfile = QPushButton("Choose signature file")
        self.choosesignfile.setEnabled(False)
        self.choosesignfile.setStyleSheet("background-color: #bfbebe;\n"
                                    "color: black")
        
        self.labelsign = QLabel("Input signature (if separated): ")
        self.inputsign = QPlainTextEdit()
        self.inputsign.setReadOnly(True)
        self.inputsign.setStyleSheet("background-color: white")
        self.signdisplay = QPlainTextEdit()
        self.signdisplay.setReadOnly(True)
        self.signdisplay.setStyleSheet("background-color: white")
        
        self.keyfile2 = QPushButton("Choose key file")
        self.keyfile2.clicked.connect(self.open_key)
        self.keyfile2.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        self.keydisplay2 = QPlainTextEdit()
        self.keydisplay2.setReadOnly(True)
        self.keydisplay2.setStyleSheet("background-color: white")
        self.inputkey2 = QPlainTextEdit()
        self.inputkey2.hide()
        self.inputn2 = QPlainTextEdit()
        self.inputn2.hide()

        self.verif = QPushButton("Verify File")
        self.verif.clicked.connect(self.verif_function)
        self.verif.setStyleSheet("background-color: #FCE205;\n"
                                    "color: black")

        self.verification = QMessageBox()
        self.verification.setWindowTitle("Verification Result")

        #set stack
        self.stackkey = QWidget()
        self.stacksign = QWidget()
        self.stackverify = QWidget()
        self.layout_key()
        self.layout_sign()
        self.layout_verify()
        self.stack = QStackedWidget (self)
        self.stack.addWidget(self.stackkey)
        self.stack.addWidget(self.stacksign)
        self.stack.addWidget(self.stackverify)

        self.fitur.currentIndexChanged.connect(self.changemenus)
       
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.labeltitle)
        layout.addWidget(self.labelsubtitle)
        layout.addWidget(self.labelfitur)
        layout.addWidget(self.fitur)
        layout.addWidget(self.stack)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.rsa = RSA()

    def layout_key(self):
        layout = QVBoxLayout()
        layout.addWidget(self.genkey)

        self.stackkey.setLayout(layout)
        

    def layout_sign(self):
        layout = QVBoxLayout()
        layout.addWidget(self.labelinput)
        layout.addWidget(self.chooseinputfile)
        layout.addWidget(self.inputdisplay)
        layout.addWidget(self.keyfile)
        layout.addWidget(self.inputkey)
        layout.addWidget(self.inputn)
        layout.addWidget(self.keydisplay)
        layout.addWidget(self.separate)
        layout.addWidget(self.signing)

        self.stacksign.setLayout(layout)

    def layout_verify(self):
        layout = QVBoxLayout()
        layout.addWidget(self.labelinput2)
        layout.addWidget(self.chooseinputfile2)
        layout.addWidget(self.inputdisplay2)
        layout.addWidget(self.separate2)
        layout.addWidget(self.labelsign)
        layout.addWidget(self.choosesignfile)
        layout.addWidget(self.signdisplay)
        layout.addWidget(self.keyfile2)
        layout.addWidget(self.inputkey2)
        layout.addWidget(self.inputn2)
        layout.addWidget(self.keydisplay2)
        layout.addWidget(self.verif)

        self.stackverify.setLayout(layout)

    def changemenus(self):
        # Untuk ganti menu fitur
        index = self.fitur.currentIndex()
        if index == 0:
            self.stack.setCurrentIndex(0)
        elif index == 1:
            self.stack.setCurrentIndex(1)
        elif index == 2:
            self.stack.setCurrentIndex(2)
        
        self.genkey.setText("Generate Key")
        self.genkey.setStyleSheet("background-color: #023047;\n"
                                    "color: white")

        self.inputdisplay.clear()
        self.inputkey.clear()
        self.inputn.clear()
        self.keydisplay.clear()
        self.signing.setText("Sign File")
        self.signing.setStyleSheet("background-color: #FCE205;\n"
                                    "color: black")
        self.inputdisplay2.clear()
        self.signdisplay.clear()
        self.inputkey2.clear()
        self.inputn2.clear()
        self.keydisplay2.clear()
        self.verif.setText("Verify File")
        self.verif.setStyleSheet("background-color: #FCE205;\n"
                                    "color: black")

    def check_state(self):
        if self.separate2.isChecked():
            self.choosesignfile.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
            self.choosesignfile.setEnabled(True)
            self.choosesignfile.clicked.connect(self.open_sign)
        else:
            self.choosesignfile.setEnabled(False)
            self.choosesignfile.setStyleSheet("background-color: #bfbebe;\n"
                                    "color: black")

    def gen(self):
        self.rsa.genKey()
        self.genkey.setText("Generated!")
        self.genkey.setStyleSheet("background-color: #bfbebe;\n"
                                    "color: black")

    def signing_function(self):
        sign_function(self.inputfield.toPlainText(), self.inputkey.toPlainText(), self.inputn.toPlainText(), self.separate.isChecked())
        self.signing.setText("Signed file downloaded!")
        self.signing.setStyleSheet("background-color: #bfbebe;\n"
                                    "color: black")

    def verif_function(self):
        if self.separate2.isChecked():
            result = verify_function(self.inputfield2.toPlainText(), self.inputkey2.toPlainText(), self.inputn2.toPlainText(), self.inputsign.toPlainText())
        else:
            result = verify_function(self.inputfield2.toPlainText(), self.inputkey2.toPlainText(), self.inputn2.toPlainText())
        self.verif.setText("Verification done!")
        self.verification.setText(result)
        self.verification.exec_()
        
    def open_input(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Input')
        content = ''
        # self.outputfield.clear()
        if fileName:
            with open(fileName, 'r', encoding='ISO-8859-1') as f:
                content = f.read()
                self.inputfield.setPlainText(fileName)
                self.inputfield2.setPlainText(fileName)
                self.inputdisplay.setPlainText(content + "\nFrom: " + fileName)
                self.inputdisplay2.setPlainText(content + "\nFrom: " + fileName)

    def open_key(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Key')
        content = ''
        d = ''
        e =''
        n = ''
        i = 6
        # self.outputfield.clear()
        if fileName:
            if fileName.endswith('.pri'):
                f = open(fileName)
                private = json.load(f)
                self.rsa.d = private['d']
                self.rsa.n = private['n']
                f.close()
                self.inputkey.setPlainText(str(self.rsa.d))
                self.inputn.setPlainText(str(self.rsa.n))
                self.keydisplay.setPlainText("From: " + fileName)
            elif fileName.endswith('.pub'):
                f = open(fileName)
                public = json.load(f)
                self.rsa.e = public['e']
                self.rsa.n = public['n']
                f.close()
                self.inputkey2.setPlainText(str(self.rsa.e))
                self.inputn2.setPlainText(str(self.rsa.n))
                self.keydisplay2.setPlainText("From: " + fileName)
    
    def open_sign(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Input')
        content = ''
        # self.outputfield.clear()
        if fileName:
            with open(fileName, 'r', encoding='ISO-8859-1') as f:
                content = f.read()
                self.inputsign.setPlainText(fileName)
                self.signdisplay.setPlainText(content + "\nFrom: " + fileName)

app = QApplication(sys.argv)
window = MainWindow()
window.resize(1000,800)
window.show()

app.exec()