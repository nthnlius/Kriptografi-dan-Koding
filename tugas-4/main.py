from cProfile import label
import sys
import random
import os.path
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
        self.inputkey = QPlainTextEdit()
        self.inputkey.hide()
        self.inputn = QPlainTextEdit()
        self.inputn.hide()

        self.signing = QPushButton("Sign File")
        self.signing.clicked.connect(self.signing_function)

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

        self.keyfile2 = QPushButton("Choose key file")
        self.keyfile2.clicked.connect(self.open_key)
        self.keyfile2.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        self.inputkey2 = QPlainTextEdit()
        self.inputkey2.hide()
        self.inputn2 = QPlainTextEdit()
        self.inputn2.hide()

        self.verif = QPushButton("Sign File")
        self.verif.clicked.connect(self.verif_function)

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
       
        layout = QVBoxLayout()
        layout.addWidget(self.labeltitle)
        layout.addWidget(self.labelsubtitle)
        layout.addWidget(self.stack)
        
        # self.setCentralWidget(widget)
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
        layout.addWidget(self.inputfield)
        layout.addWidget(self.keyfile)
        layout.addWidget(self.inputkey)
        layout.addWidget(self.inputn)
        layout.addWidget(self.signing)

        self.stacksign.setLayout(layout)

    def layout_verify(self):
        layout = QVBoxLayout()
        layout.addWidget(self.labelinput2)
        layout.addWidget(self.chooseinputfile2)
        layout.addWidget(self.inputdisplay2)
        layout.addWidget(self.inputfield2)
        layout.addWidget(self.verif)
        layout.addWidget(self.verification)

        self.stacksign.setLayout(layout)


    def gen(self):
        self.rsa.genKey()
        self.genkey.setText("Generated!")
        self.genkey.setStyleSheet("background-color: #bfbebe;\n"
                                    "color: black")

    def signing_function(self):
        sign_function(self.inputdisplay.toPlainText(), self.inputkey.toPlainText(), self.inputn.toPlainText())
        self.signing.setText("Signed file downloaded!")
        self.signing.setStyleSheet("background-color: #bfbebe;\n"
                                    "color: black")

    def verif_function(self):
        result = verify_function(self.inputdisplay2.toPlainText(), self.inputkey2.toPlainText(), self.inputn2.toPlainText())
        self.verification.setText(result)
        
    def open_input(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Input')
        content = ''
        self.outputfield.clear()
        if fileName:
            if fileName.endswith('.txt'):
                # File txt
                with open(fileName, 'r', encoding='ISO-8859-1') as f:
                    content = f.read()
                    self.inputfield.setPlainText(fileName)
                    self.inputdisplay.setPlainText(content + "\nFrom: " + fileName)
            else:
                self.inputfield.setPlainText(fileName)
                self.inputdisplay.setPlainText("From: " + fileName)

    def open_key(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Key')
        content = ''
        d = ''
        e =''
        n = ''
        i = 6
        self.outputfield.clear()
        if fileName:
            if fileName.endswith('.pri'):
                f = open(fileName)
                private = json.load(f)
                self.rsa.d = private['d']
                self.rsa.n = private['n']
                f.close()
                self.inputkey.setPlainText(str(self.rsa.d))
                self.inputn.setPlainText(str(self.rsa.n))
            elif fileName.endswith('.pub'):
                f = open(fileName)
                public = json.load(f)
                self.rsa.e = public['e']
                self.rsa.n = public['n']
                f.close()
                self.inputkey.setPlainText(str(self.rsa.e))
                self.inputn.setPlainText(str(self.rsa.n))

app = QApplication(sys.argv)
window = MainWindow()
window.resize(1000,800)
window.show()

app.exec()