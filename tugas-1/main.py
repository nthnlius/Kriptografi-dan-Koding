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

from vigenere import *
from playfair import *
from enigma import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tugas Kecil 1 II4031 Kriptografi dan Koding")

        hbox = QHBoxLayout()
        layout = QVBoxLayout()
        
        self.label1 = QLabel("Cipher:")
        self.ciphertype = QComboBox()
        self.ciphertype.addItems(["Vigénere", "Extended Vigénere", "Playfair", "Enigma", "One-time Pad"])


        self.space = QCheckBox("Use space in result")

        
        self.label2 = QLabel("Input:")
        self.inputfield = QPlainTextEdit()

        self.label3 = QLabel("Output:")
        self.outputfield = QPlainTextEdit()
        self.outputfield.setReadOnly(True)


        self.choosefile = QPushButton("Choose file")
        self.labelpath = QLabel("")
        self.choosefile.clicked.connect(self.open)
        self.choosefile2 = QPushButton("Upload")
        self.choosefile2.clicked.connect(self.savefile)
        
        self.label4 = QLabel()
        self.encrypt = QPushButton("Encrypt")
        self.encrypt.clicked.connect(self.encrypt_function)
        self.decrypt = QPushButton("Decrypt")
        self.decrypt.clicked.connect(self.decrypt_function)

        self.encrypt.setStyleSheet("background-color : #98d6ed")
        self.decrypt.setStyleSheet("background-color : #98d6ed")

        # Extra fields
        self.key = QLineEdit()
        self.keyfile = QPushButton("Choose file")
        self.labelpath = QLabel("")
        self.keyfile.clicked.connect(self.open)
        self.keyfile2 = QPushButton("Download")
        self.keyfile2.clicked.connect(self.savefile)
        self.binaryfile = ''

        
        # Buat menu beda sesuai jenis cipher
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.layout1()
        self.layout2()
        self.layout3()
        self.stack = QStackedWidget (self)
        self.stack.addWidget (self.stack1)
        self.stack.addWidget (self.stack2)
        self.stack.addWidget (self.stack3)

        

        self.ciphertype.currentIndexChanged.connect(self.changemenus)

        

        # Masukkan menu ganti cipher
        layout.addWidget(self.space)
        layout.addWidget(self.label2)
        layout.addWidget(self.inputfield)
        layout.addWidget(self.choosefile)
        layout.addWidget(self.labelpath)
        layout.addWidget(self.label3)
        layout.addWidget(self.outputfield)
        layout.addWidget(self.choosefile2)
        layout.addWidget(self.label4)

        widget = QWidget()
        hbox.addLayout(layout)
        hbox.addWidget(self.stack)
        layoutall = QVBoxLayout()
        layoutall.addWidget(self.label1)
        layoutall.addWidget(self.ciphertype)
        layoutall.addLayout(hbox)
        layoutall.addWidget(self.encrypt)
        layoutall.addWidget(self.decrypt)
        widget.setLayout(layoutall)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def layout1(self):
        # Layout 1. Vigenere, Extended, Playfair Cipher
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 32, 0, 0)
        
        labelkey = QLabel("Key:")
        
        layout.addWidget(labelkey)
        layout.addWidget(self.key)
        layout.setAlignment(Qt.AlignTop)
        
        self.stack1.setLayout(layout)

    def layout2(self):
        # Layout 2. Enigma Cipher
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 23, 0, 19)

        labelkey = QLabel("Matriks Kunci:")

        layout.addWidget(labelkey)
        # layout.addWidget(self.matriks)
        layout.setAlignment(Qt.AlignTop)
        
        self.stack2.setLayout(layout)
        

    def layout3(self):
        # # Layout 3. One-time Pad
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 32, 0, 0)

        labelkey = QLabel("Key:")

        layout.addWidget(labelkey)
        layout.addWidget(self.keyfile)
        layout.addWidget(self.keyfile2)
        layout.setAlignment(Qt.AlignTop)
        
        self.stack3.setLayout(layout)
        


    def changemenus(self):
        # Untuk ganti menu saat mengubah jenis cipher
        index = self.ciphertype.currentIndex()
        if index == 3:
            self.stack.setCurrentIndex(1)
        elif index == 4:
            self.stack.setCurrentIndex(2)
        else:
            self.stack.setCurrentIndex(0)


    def encrypt_function(self):
        index = self.ciphertype.currentIndex()
        inputtext = self.inputfield.toPlainText()
        output = ''
        isbinary = False
        
        if index == 0:
            keytext = self.key.text()
            output = vigenere(inputtext, keytext, True)
        
        elif index == 1:
            keytext = self.key.text()
            instring = []

            if os.path.exists(inputtext):
                isbinary = True
                with open(inputtext, 'rb') as f:
                    byte = f.read(1)
                    while byte:
                        instring.append(int.from_bytes(byte, "big"))   
                        byte = f.read(1)
                    encrypted = bytearray(extvigenere(instring, keytext, True))
                    self.binaryfile = encrypted
            else:
                output = extvigenere(inputtext, keytext, True)
        
        elif index == 2:
            keytext = self.key.text()
            output = playfair(inputtext, keytext, True)
        
        elif index == 3:
            output = "Enigma"

        elif index == 4:
            keytext = self.key.text()
            output = otp(inputtext, True)
            
        # Tambah space jika opsi dipilih
        if self.space.isChecked():
            output = ' '.join(output[i:i+5] for i in range(0,len(output),5))
            
        if index == 1 and isbinary:
            output = 'Berkas telah diencrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def decrypt_function(self):
        index = self.ciphertype.currentIndex()
        inputtext = self.inputfield.toPlainText()
        output = ''
        isbinary = False
        
        if index == 0:
            keytext = self.key.text()
            output = vigenere(inputtext, keytext, False)
        
        elif index == 1:
            keytext = self.key.text()
            instring = []
            
            if os.path.exists(inputtext):
                with open(inputtext, 'rb') as f:
                    isbinary = True
                    byte = f.read(1)
                    while byte:
                        instring.append(int.from_bytes(byte, "big"))   
                        byte = f.read(1)
                    encrypted = bytearray(extvigenere(instring, keytext, False))
                    self.binaryfile = encrypted
            else:
                output = extvigenere(inputtext, keytext, False)
        
        elif index == 2:
            keytext = self.key.text()
            output = playfair(inputtext, keytext, False)
        
        elif index == 3:
            output = "Enigma"

        elif index == 4:
            keytext = self.key.text()
            output = otp(inputtext, False)

        if index == 1 and isbinary:
            output = 'Berkas telah didecrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def open(self):
        fileName = ''
        index = self.ciphertype.currentIndex()
        if index != 3:
            fileName, _ = QFileDialog.getOpenFileName(self, 'File Input','.', "Text Files (*.txt)")
        else:
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
        index = self.ciphertype.currentIndex()
        if index == 3 and os.path.exists(self.inputfield.toPlainText()):
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
