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
                            "background-color: #f6d2e0")
        
        self.labelinput = QLabel("Input:")
        self.inputfield = QPlainTextEdit()
        self.inputfield.setStyleSheet("background-color: white")

        self.chooseinputfile = QPushButton("Choose file")
        self.labelpath = QLabel("")
        self.chooseinputfile.clicked.connect(self.open)
        self.chooseinputfile.setStyleSheet("background-color: #f8b7cd")
        
        self.labelkey = QLabel("Key:")
        self.inputkey = QPlainTextEdit()
        self.inputkey.setStyleSheet("background-color: white")
        
        self.keyfile = QPushButton("Choose key file")
        self.labelpath = QLabel("")
        self.keyfile.clicked.connect(self.loadkey)
        self.keyfile.setStyleSheet("background-color: #f8b7cd")
        self.keyfile2 = QPushButton("Download key")
        self.keyfile2.clicked.connect(self.savefile)
        self.keyfile2.setStyleSheet("background-color: #f8b7cd")

        
        self.labeloutput = QLabel("Output:")
        self.outputfield = QPlainTextEdit()
        self.outputfield.setReadOnly(True)
        self.outputfield.setStyleSheet("background-color: white")

        self.chooseoutputfile = QPushButton("Download")
        self.chooseoutputfile.clicked.connect(self.savefile)
        self.chooseoutputfile.setStyleSheet("background-color: #f8b7cd")

        #Extrafields
        self.binaryfile = ''
        
        self.label4 = QLabel()
        self.encrypt = QPushButton("Encrypt")
        self.encrypt.clicked.connect(self.encrypt_function)
        self.decrypt = QPushButton("Decrypt")
        self.decrypt.clicked.connect(self.decrypt_function)

        self.encrypt.setStyleSheet("background-color : #67a3d9")
        self.decrypt.setStyleSheet("background-color : #67a3d9")

        widget = QWidget()
        layoutall = QVBoxLayout()
        layoutall.addWidget(self.labelinput)
        layoutall.addWidget(self.inputfield)
        layoutall.addWidget(self.chooseinputfile)
        layoutall.addWidget(self.labelkey)
        layoutall.addWidget(self.inputkey)
        layoutall.addWidget(self.keyfile)
        layoutall.addWidget(self.labelpath)
        layoutall.addWidget(self.keyfile2)
        layoutall.addWidget(self.labeloutput)
        layoutall.addWidget(self.outputfield)
        layoutall.addWidget(self.chooseoutputfile)
        layoutall.addWidget(self.encrypt)
        layoutall.addWidget(self.decrypt)
        
        widget.setLayout(layoutall)
        self.setCentralWidget(widget)


    def loadkey(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Load Key','.', "Text Files (*.txt)")
        content = ''
        # File txt
        if fileName:
            with open(fileName, 'r') as f:
                content = f.read()
                self.inputkey.setText(content)

    def encrypt_function(self):
        key = bytearray(self.inputkey.toPlainText(), "UTF-8")
        rc4 = RC4(key)
        inputtext = bytearray(self.inputfield.toPlainText(), "UTF-8")
        isbinary = False
        instring = []

        if os.path.exists(inputtext):
            isbinary = True
            with open(inputtext, 'rb') as f:
                byte = f.read(1)
                while byte:
                    instring.append(int.from_bytes(byte, "big"))   
                    byte = f.read(1)
                encrypted = rc4.encrypt(inputtext)
                self.binaryfile = encrypted
        else:
            temp = rc4.encrypt(inputtext)
            output = temp.decode()
            
        if isbinary:
            output = 'Berkas telah diencrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def decrypt_function(self):
        key = bytearray(self.inputkey.toPlainText(), "UTF-8")
        rc4 = RC4(key)
        inputtext = bytearray(self.inputfield.toPlainText(), "UTF-8")
        isbinary = False
        instring = []

        if os.path.exists(inputtext):
            isbinary = True
            with open(inputtext, 'rb') as f:
                byte = f.read(1)
                while byte:
                    instring.append(int.from_bytes(byte, "big"))   
                    byte = f.read(1)
                encrypted = rc4.decrypt(inputtext)
                self.binaryfile = encrypted
        else:
            temp = rc4.encrypt(inputtext)
            output = temp.decode()

        if isbinary:
            output = 'Berkas telah didecrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def open(self):
        fileName = ''
        fileName, _ = QFileDialog.getOpenFileName(self, 'File Input')
        content = ''
        if fileName:
            if fileName.endswith('.txt'):
               # File txt
               with open(fileName, 'r', encoding='ISO-8859-1') as f:
                   content = f.read()
                   self.inputfield.setPlainText(content)
            else:
                self.inputfield.setPlainText(fileName)

    def savefile(self):
        # index = self.ciphertype.currentIndex()
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
window.show()

app.exec()
