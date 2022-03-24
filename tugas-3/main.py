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
    
)

from rsa import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tugas Kecil 3 II4031 Kriptografi dan Koding")
        self.setStyleSheet("font: 10pt Verdana;\n"
                            "background-color: #8ecae6")
        
        self.labeltitle = QLabel("Implementasi Algoritma RSA")
        self.labeltitle.setStyleSheet("font: bold 10pt Verdana")
        self.labelsubtitle = QLabel("By: Nathaniel & Nadya\n")
        self.labelsubtitle.setStyleSheet("font: 10pt Verdana")

        self.labelinput = QLabel("Input:")
        self.chooseinputfile = QPushButton("Choose file")
        self.chooseinputfile.clicked.connect(self.open_input)
        self.chooseinputfile.setStyleSheet("background-color: #023047;\n"
                                            "color: white")
        self.inputfield = QPlainTextEdit()
        self.inputfield.setReadOnly(True)
        self.inputfield.setStyleSheet("background-color: white")
        
        self.label1 = QLabel(" ")
        self.labelkey = QLabel("Key:")
        self.inputkey = QPlainTextEdit()
        self.inputkey.setStyleSheet("background-color: white")
        
        self.keyfile = QPushButton("Choose key file")
        self.keyfile.clicked.connect(self.open_key)
        self.keyfile.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        
        self.label2 = QLabel(" ")
        self.labelgen = QLabel("Do not have key?")
        self.genkey = QPushButton("Generate key first")
        self.genkey.clicked.connect(self.gen)
        self.genkey.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        
        self.label3 = QLabel(" ")
        self.labeloutput = QLabel("Output:")
        self.outputfield = QPlainTextEdit()
        self.outputfield.setReadOnly(True)
        self.outputfield.setStyleSheet("background-color: white")
        self.outputtime = QLabel("")
        self.outputsize = QLabel("")

        self.saveoutput = QPushButton("Download")
        self.saveoutput.clicked.connect(self.savefile)
        self.saveoutput.setStyleSheet("background-color: #023047;\n"
                                            "color: white")
        
        self.encrypt = QPushButton("Encrypt")
        self.encrypt.clicked.connect(self.encrypt_function)
        self.decrypt = QPushButton("Decrypt")
        self.decrypt.clicked.connect(self.decrypt_function)

        self.encrypt.setStyleSheet("background-color : #fb8500")
        self.decrypt.setStyleSheet("background-color : #ffb703")

        widget = QWidget()
        layoutall = QVBoxLayout()
        layoutall.addWidget(self.labeltitle)
        layoutall.addWidget(self.labelinput)
        layoutall.addWidget(self.chooseinputfile)
        layoutall.addWidget(self.inputfield)
        layoutall.addWidget(self.label1)
        layoutall.addWidget(self.labelkey)
        layoutall.addWidget(self.inputkey)
        layoutall.addWidget(self.keyfile)
        layoutall.addWidget(self.label2)
        layoutall.addWidget(self.labelgen)
        layoutall.addWidget(self.genkey)
        layoutall.addWidget(self.label3)
        layoutall.addWidget(self.labeloutput)
        layoutall.addWidget(self.outputfield)
        layoutall.addWidget(self.outputtime)
        layoutall.addWidget(self.outputsize)
        layoutall.addWidget(self.saveoutput)
        layoutall.addWidget(self.encrypt)
        layoutall.addWidget(self.decrypt)
        
        widget.setLayout(layoutall)
        self.setCentralWidget(widget)

    def gen(self):
        rsa = RSA(sympy.randprime(2**63, 2**64-1), sympy.randprime(2**63, 2**64-1))
        rsa.generateE()
        rsa.generateD()
        self.genkey.setText("Generated!")

    def encrypt_function(self):
        instring = []
        inputtext = self.inputfield.toPlainText()

        with open(inputtext, 'rb') as f:
            byte = f.read(1)
            while byte:
                instring.append(int.from_bytes(byte, "big"))   
                byte = f.read(1)
            start_time = time()
            encrypted = RSA.encrypt(instring)
            end_time = time()
            self.outpputtime = "Time taken for encrypting : ", (end_time - start_time), "seconds"
            self.outputfield = encrypted

    def decrypt_function(self):
        instring = []
        inputtext = self.inputfield.toPlainText()

        with open(inputtext, 'rb') as f:
            byte = f.read(1)
            while byte:
                instring.append(int.from_bytes(byte, "big"))   
                byte = f.read(1)
            start_time = time()
            decrypted = RSA.decrypt(instring)
            end_time = time()
            self.outpputtime = "Time taken for decrypting : ", (end_time - start_time), "seconds"
            self.outputfield = decrypted

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
                   self.inputfield.setPlainText(content)
            else:
                self.inputfield.setPlainText(fileName)

    def open_key(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Key')
        content = ''
        self.outputfield.clear()
        if fileName:
            if fileName.endswith('.pri'):
               with open(fileName, 'r', encoding='ISO-8859-1') as f:
                   content = f.read()  
                   RSA.d = content
                   RSA.n = content
            elif fileName.endswith('.pub'):
               with open(fileName, 'r', encoding='ISO-8859-1') as f:
                   content = f.read()
                   RSA.e = content
                   RSA.n = content                

    def savefile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save Output', 'output')
        if(fileName):
            output = self.outputfield
            fname = open(fileName, 'wb')
            fname.write(output)
            fname.close()

app = QApplication(sys.argv)
window = MainWindow()
window.resize(1000,800)
window.show()

app.exec()