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

from stream import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tugas Kecil 2 II4031 Kriptografi dan Koding")
        self.setStyleSheet("font: 10pt Verdana;\n"
                            "background-color: #8ecae6")
        
        self.labeltitle = QLabel("My Own Stream Cipher")
        self.labeltitle.setStyleSheet("font: bold 12pt Verdana")
        self.labelsubtitle = QLabel("By: Nathaniel & Nadya\n")
        self.labelsubtitle.setStyleSheet("font: 12pt Verdana")

        self.labelinput = QLabel("Input:")
        self.inputfield = QPlainTextEdit()
        self.inputfield.setStyleSheet("background-color: white")

        self.chooseinputfile = QPushButton("Choose file")
        self.chooseinputfile.clicked.connect(self.open)
        self.chooseinputfile.setStyleSheet("background-color: #023047;\n"
                                            "color: white")
        
        self.labelkey = QLabel("Key:")
        self.inputkey = QPlainTextEdit()
        self.inputkey.setStyleSheet("background-color: white")
        
        self.keyfile = QPushButton("Download key")
        self.keyfile.clicked.connect(self.savefile)
        self.keyfile.setStyleSheet("background-color: #023047;\n"
                                    "color: white")

        
        self.labeloutput = QLabel("Output:")
        self.outputfield = QPlainTextEdit()
        self.outputfield.setReadOnly(True)
        self.outputfield.setStyleSheet("background-color: white")

        self.chooseoutputfile = QPushButton("Download")
        self.chooseoutputfile.clicked.connect(self.savefile)
        self.chooseoutputfile.setStyleSheet("background-color: #023047;\n"
                                            "color: white")

        #Extrafields
        self.binaryfile = ''
        
        self.label4 = QLabel()
        self.encrypt = QPushButton("Encrypt")
        self.encrypt.clicked.connect(self.encrypt_function)
        self.decrypt = QPushButton("Decrypt")
        self.decrypt.clicked.connect(self.decrypt_function)

        self.encrypt.setStyleSheet("background-color : #fb8500")
        self.decrypt.setStyleSheet("background-color : #ffb703")

        widget = QWidget()
        layoutall = QVBoxLayout()
        layoutall.addWidget(self.labeltitle)
        layoutall.addWidget(self.labelsubtitle)
        layoutall.addWidget(self.labelinput)
        layoutall.addWidget(self.inputfield)
        layoutall.addWidget(self.chooseinputfile)
        layoutall.addWidget(self.labelkey)
        layoutall.addWidget(self.inputkey)
        layoutall.addWidget(self.keyfile)
        layoutall.addWidget(self.labeloutput)
        layoutall.addWidget(self.outputfield)
        layoutall.addWidget(self.chooseoutputfile)
        layoutall.addWidget(self.encrypt)
        layoutall.addWidget(self.decrypt)
        
        widget.setLayout(layoutall)
        self.setCentralWidget(widget)

    def encrypt_function(self):
        key = bytearray(self.inputkey.toPlainText(), "UTF-8")
        rc4 = RC4(key)
        inputtext = self.inputfield.toPlainText()
        isbinary = False
        instring = []

        if os.path.exists(inputtext):
            isbinary = True
            with open(inputtext, 'rb') as f:
                byte = f.read(1)
                while byte:
                    instring.append(int.from_bytes(byte, "big"))   
                    byte = f.read(1)
                encrypted = rc4.encrypt(instring)
                self.binaryfile = encrypted
        else:
            encryptedtext = bytearray(self.inputfield.toPlainText(), "ANSI")
            temp = rc4.encrypt(encryptedtext)
            output = temp.decode("ANSI")
            
        if isbinary:
            output = 'Berkas telah diencrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def decrypt_function(self):
        key = bytearray(self.inputkey.toPlainText(), "UTF-8")
        rc4 = RC4(key)
        inputtext = self.inputfield.toPlainText()
        isbinary = False
        instring = []

        if os.path.exists(inputtext):
            isbinary = True
            with open(inputtext, 'rb') as f:
                byte = f.read(1)
                while byte:
                    instring.append(int.from_bytes(byte, "big"))   
                    byte = f.read(1)
                encrypted = rc4.decrypt(instring)
                self.binaryfile = encrypted
        else:
            tobedecrypted = bytearray(inputtext, "ANSI")
            temp = rc4.encrypt(tobedecrypted)
            output = temp.decode("ANSI")

        if isbinary:
            output = 'Berkas telah didecrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def open(self):
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

    def savefile(self):
        if os.path.exists(self.inputfield.toPlainText()):
            fileName, _ = QFileDialog.getSaveFileName(self, 'Save Output', 'output')
            if(fileName):
                output = self.binaryfile
                fname = open(fileName, 'wb')
                fname.write(output)
                fname.close()
        else:
            fileName, _ = QFileDialog.getSaveFileName(self, 'Save Output', 'output.txt')
            if(fileName):
                output = self.outputfield.toPlainText()
                fname = open(fileName, 'w')
                fname.write(output)
                fname.close()

app = QApplication(sys.argv)
window = MainWindow()
window.resize(800,800)
window.show()

app.exec()
