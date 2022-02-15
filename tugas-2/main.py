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

        # hbox = QHBoxLayout()
        # layout = QVBoxLayout()
        
        # self.label1 = QLabel("Cipher:")
        # self.ciphertype = QComboBox()
        # self.ciphertype.addItems(["Vigénere", "Extended Vigénere", "Playfair", "Enigma", "One-time Pad"])
        # self.ciphertype.setStyleSheet("background-color: white")

        # self.space = QCheckBox("Use space in result")

        
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
        # key = bytearray(self.inputkey.toPlainText(), "UTF-8")
        # rc4 = RC4(key)
        self.encrypt = QPushButton("Encrypt")
        self.encrypt.clicked.connect(self.encrypt_function)
        self.decrypt = QPushButton("Decrypt")
        self.decrypt.clicked.connect(self.decrypt_function)

        self.encrypt.setStyleSheet("background-color : #67a3d9")
        self.decrypt.setStyleSheet("background-color : #67a3d9")

        # Extra fields
        # self.rotor1 = QLineEdit()
        # self.rotor2 = QLineEdit()
        # self.rotor3 = QLineEdit()
        # self.rotor1.setStyleSheet("background-color: white")
        # self.rotor2.setStyleSheet("background-color: white")
        # self.rotor3.setStyleSheet("background-color: white")
        # self.displaykey = QPlainTextEdit()
        # self.displaykey.setDisabled(True)
        # self.displaykey.setStyleSheet("background-color: white")


        
        # Buat menu beda sesuai jenis cipher
        # self.stack1 = QWidget()
        # self.stack2 = QWidget()
        # self.stack3 = QWidget()
        # self.layout1()
        # self.layout2()
        # self.layout3()
        # self.stack = QStackedWidget (self)
        # self.stack.addWidget (self.stack1)
        # self.stack.addWidget (self.stack2)
        # self.stack.addWidget (self.stack3)

        

        # self.ciphertype.currentIndexChanged.connect(self.changemenus)

        # layout.addWidget(self.space)
        # layout.addWidget(self.label2)
        # layout.addWidget(self.inputfield)
        # layout.addWidget(self.choosefile)
        # layout.addWidget(self.labelpath)
        # layout.addWidget(self.label3)
        # layout.addWidget(self.outputfield)
        # layout.addWidget(self.choosefile2)
        # layout.addWidget(self.label4)

        widget = QWidget()
        # hbox.addLayout(layout)
        # hbox.addWidget(self.stack)
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
        # layoutall.addWidget(self.ciphertype)
        # layoutall.addLayout(hbox)
        layoutall.addWidget(self.encrypt)
        layoutall.addWidget(self.decrypt)
        
        widget.setLayout(layoutall)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    # def layout1(self):
    #     # Layout 1. Vigenere, Extended, Playfair Cipher
    #     layout = QVBoxLayout()
    #     layout.setContentsMargins(0, 32, 0, 0)
        
    #     labelkey = QLabel("Key:")
        
    #     layout.addWidget(labelkey)
    #     layout.addWidget(self.key)
    #     layout.setAlignment(Qt.AlignTop)
        
    #     self.stack1.setLayout(layout)

    # def layout2(self):
    #     # Layout 2. Enigma Cipher
    #     layout = QVBoxLayout()
    #     layout.setContentsMargins(0, 23, 0, 19)
        

    #     labelkey = QLabel("Rotor Key:")
    #     layout.addWidget(labelkey)

    #     layoutrotor = QHBoxLayout()

    #     rotor1 = QVBoxLayout()
    #     labelrotor1 = QLabel("Slow")
    #     rotor1.addWidget(labelrotor1)
    #     rotor1.addWidget(self.rotor1)

    #     rotor2 = QVBoxLayout()
    #     labelrotor2 = QLabel("Medium")
    #     rotor2.addWidget(labelrotor2)
    #     rotor2.addWidget(self.rotor2)

    #     rotor3 = QVBoxLayout()
    #     labelrotor3 = QLabel("Fast")
    #     rotor3.addWidget(labelrotor3)
    #     rotor3.addWidget(self.rotor3)

    #     layoutrotor.addLayout(rotor1)
    #     layoutrotor.addLayout(rotor2)
    #     layoutrotor.addLayout(rotor3)

    #     layout.addLayout(layoutrotor)
    #     layout.setAlignment(Qt.AlignTop)
        
    #     self.stack2.setLayout(layout)
        

    # def layout3(self):
    #     # # Layout 3. One-time Pad
    #     layout = QVBoxLayout()
    #     layout.setContentsMargins(0, 32, 0, 0)

    #     labelkey = QLabel("Key:")
    #     layout.addWidget(labelkey)
    #     layout.addWidget(self.displaykey)
    #     layout.addWidget(self.keyfile)
    #     layout.addWidget(self.keyfile2)
    #     layout.setAlignment(Qt.AlignTop)
        
    #     self.stack3.setLayout(layout)
        

    def loadkey(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Load Key','.', "Text Files (*.txt)")
        content = ''
        # File txt
        if fileName:
            with open(fileName, 'r') as f:
                content = f.read()
                self.inputkey.setText(content)

    # def changemenus(self):
    #     # Untuk ganti menu saat mengubah jenis cipher
    #     index = self.ciphertype.currentIndex()
    #     if index == 3:
    #         self.stack.setCurrentIndex(1)
    #     elif index == 4:
    #         self.stack.setCurrentIndex(2)
    #     else:
    #         self.stack.setCurrentIndex(0)
        
    #     self.inputfield.clear()
    #     self.outputfield.clear()
    #     self.key.clear()
    #     self.displaykey.clear()


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
            # fileName, _ = QFileDialog.getSaveFileName(self, 'Save Output', 'output')
            # fname = open(fileName, 'wb')
            # fname.write(output)
            # fname.close()
            # self.savefile()
            # output = ''

        
        # elif index == 2:
        #     keytext = self.key.text()
        #     output = playfair(inputtext, keytext, True)
        
        # elif index == 3:
        #     output = enigma(self.rotor3.text(), self.rotor2.text(), self.rotor1.text(), inputtext, True)

        # elif index == 4:
        #     output = otp(inputtext, True, self.displaykey.toPlainText())
        #     with open("keyII4031Kirptografidankodingtapiadatypo.txt", 'r') as f:
        #         content = f.read()
        #         self.displaykey.setPlainText(content)
            
        # Tambah space jika opsi dipilih
        # if self.space.isChecked():
        #     output = ' '.join(output[i:i+5] for i in range(0,len(output),5))
            
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
            # fileName, _ = QFileDialog.getSaveFileName(self, 'Save Output', 'output')
            # fname = open(fileName, 'wb')
            # fname.write(output)
            # fname.close()
            # self.savefile()
            # output = ''

        if isbinary:
            output = 'Berkas telah didecrypt. Silakan unduh dengan tombol "Download"'

        self.outputfield.setPlainText(output)

    def open(self):
        fileName = ''
        # index = self.ciphertype.currentIndex()
        # if index != 3:
        #     fileName, _ = QFileDialog.getOpenFileName(self, 'File Input','.', "Text Files (*.txt)")
        # else:
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
