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

        self.inputdisplay = QPlainTextEdit()
        self.inputdisplay.setReadOnly(True)
        self.inputdisplay.setStyleSheet("background-color: white")
        self.inputfield = QPlainTextEdit()
        self.inputfield.setReadOnly(True)
        self.inputfield.setStyleSheet("background-color: white")
        
        self.label1 = QLabel(" ")        
        layoutkey = QVBoxLayout()
        self.labelkey = QLabel("e or d:")
        self.inputkey = QPlainTextEdit()
        self.inputkey.setStyleSheet("background-color: white")
        layoutkey.addWidget(self.labelkey)
        layoutkey.addWidget(self.inputkey)

        layoutn = QVBoxLayout()
        self.labeln = QLabel("n:")
        self.inputn = QPlainTextEdit()
        self.inputn.setStyleSheet("background-color: white")
        layoutn.addWidget(self.labeln)
        layoutn.addWidget(self.inputn)

        self.stack1 = QWidget()
        self.stack1.setLayout(layoutkey)
        self.stack2 = QWidget()
        self.stack2.setLayout(layoutn)
        layouth = QHBoxLayout()
        layouth.addWidget(self.stack1)
        layouth.addWidget(self.stack2)

        self.keyfile = QPushButton("Choose key file")
        self.keyfile.clicked.connect(self.open_key)
        self.keyfile.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        
        self.label1 = QLabel(" ")
        self.labelgen = QLabel("Do not have key?")
        self.genkey = QPushButton("Generate key first")
        self.genkey.clicked.connect(self.gen)
        self.genkey.setStyleSheet("background-color: #023047;\n"
                                    "color: white")
        
        self.label2 = QLabel(" ")
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

        self.orioutput = QPlainTextEdit()
        
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
        # layoutall.addWidget(self.inputfield)
        layoutall.addWidget(self.inputdisplay)
        self.stack = QWidget()
        self.stack.setLayout(layouth)
        layoutall.addWidget(self.stack)
        layoutall.addWidget(self.keyfile)
        layoutall.addWidget(self.label1)
        layoutall.addWidget(self.labelgen)
        layoutall.addWidget(self.genkey)
        layoutall.addWidget(self.label2)
        layoutall.addWidget(self.labeloutput)
        layoutall.addWidget(self.outputfield)
        layoutall.addWidget(self.outputtime)
        layoutall.addWidget(self.outputsize)
        layoutall.addWidget(self.saveoutput)
        layoutall.addWidget(self.encrypt)
        layoutall.addWidget(self.decrypt)
        
        widget.setLayout(layoutall)
        self.setCentralWidget(widget)
        self.rsa = RSA()
        
    def gen(self):
        self.rsa = RSA()
        self.genkey.setText("Generated!")

    def encrypt_function(self):
        inputtext = self.inputfield.toPlainText()

        with open(inputtext, 'rb') as f:
            byte = f.read()
        input_size = len(byte)
        start_time = time()
        encrypted = self.rsa.encrypt(byte)
        end_time = time()
        self.outputtime.setText("Time taken for encrypting : " + str(end_time - start_time) + " seconds")
        self.outputsize.setText ("Size of plaintext file: "+ str(input_size * 16) + " bytes")
        nani = ""
        for i in range (len (encrypted)):
            text = hex(encrypted[i])
            if (len(text)< 34):
                text2 = text[0:2]+('0'*(34-len(text)))+text[2:len(text)]
            else :
                text2 = text
            for j in range (1, len(text2)//2):
                euy = text2[j*2 :j*2+2] #euy mengambil tiap bytes dalam text.
                ahh = int(euy, 16) #ahh mengubah euy dari heksadesimal jadi integer
                nani+=(chr(ahh))
        self.outputfield.setPlainText(text2)
        self.orioutput.setPlainText(nani)

    def decrypt_function(self):
        inputtext = self.inputfield.toPlainText()

        with open(inputtext, 'rb') as f:
            byte = f.read()
            input_size = len(byte)
            start_time = time()
            decrypted = self.rsa.decrypt(byte)
            end_time = time()
            self.outputtime.setText("Time taken for decrypting : " + str(end_time - start_time) + " seconds")
            self.outputsize.setText("Size of plaintext file:" + str(input_size / 16) + " bytes")
            self.outputfield.setPlainText(decrypted)

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
                              

    def savefile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save Output', 'output')
        if(fileName):
            output = self.orioutput.toPlainText()
            output2 = bytearray(output, encoding="iso8859")
            fname = open(fileName, 'wb')
            fname.write(output2)
            fname.close()

app = QApplication(sys.argv)
window = MainWindow()
window.resize(1000,800)
window.show()

app.exec()