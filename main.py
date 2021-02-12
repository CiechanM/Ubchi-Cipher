from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import  *
import tkinter
from tkinter import filedialog
import time
import string
import random
import traceback, sys, os
string.ascii_letters = 'abcdefghijklmnoprstuwxyz'



class Okno(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Okno, self).__init__(*args, *kwargs)
        self.setWindowTitle("UBCHI CODE")

        #tytul aplikacji gora srodek
        titleText = QLabel()
        titleText.setText("UBCHIPTOR")
        titleText.setAlignment(Qt.AlignCenter)
        titleText.setFont(QFont('Courier New',40 ))
        titleText.setStyleSheet("QLabel {color: #1B2A41} ")

        # tekst uwaga na zlodzieje
        warningText = QLabel()
        warningText.setText("Stay safe using Internet")
        warningText.setAlignment(Qt.AlignCenter)
        warningText.setFont(QFont('Courier New', 15))
        warningText.setStyleSheet("QLabel {color: #1B2A41} ")

        #tekst wstaw wiadomosc tutaj
        self.subtitleText = QLabel()
        self.subtitleText.setText("Enter your message and key")
        self.subtitleText.setAlignment(Qt.AlignCenter)
        self.subtitleText.setFont(QFont('Courier New',20))
        self.subtitleText.setStyleSheet("QLabel {color: #1B2A41} ")

        #pole wyswietlajace tekst zaszyfrowany
        self.encryptedText = QLabel()
        self.encryptedText.setWordWrap(True)
        self.encryptedText.setText(" ")
        self.encryptedText.setAlignment(Qt.AlignCenter)
        self.encryptedText.setFont(QFont('Courier New', 20))
        self.encryptedText.setStyleSheet("QLabel {color: #1B2A41} ")

        #pole wyswietlajace tekst zdeszyfrowany
        self.decryptedText = QLabel()
        self.decryptedText.setText(" ")
        self.decryptedText.setWordWrap(True)
        self.decryptedText.setAlignment(Qt.AlignCenter)
        self.decryptedText.setFont(QFont('Courier New', 20))
        self.decryptedText.setStyleSheet("QLabel {color : #000000}")

        #pole wstaw wiadomosc
        self.messageField = QLineEdit()
        self.messageField.setPlaceholderText("*Write a message here*")
        self.messageField.setFont(QFont('Courier New', 11))
        self.messageField.setStyleSheet("QLineEdit {color: #000000}")

        #pole wstaw klucz
        self.keyField = QLineEdit()
        self.keyField.setPlaceholderText("*Enter key here*")
        self.keyField.setFont(QFont('Courier New', 11))
        self.keyField.setStyleSheet("QLineEdit {color: #1B2A41}")

        #pola obok siebie
        textFieldsLayout = QHBoxLayout()
        textFieldsLayout.addWidget(self.messageField)
        textFieldsLayout.addWidget(self.keyField)
        textFieldsLayoutWidget = QWidget()
        textFieldsLayoutWidget.setLayout(textFieldsLayout)

        #przyciski wczytywania
        self.messageFromFileButton = QFileDialog()
        self.keyFromFileButton = QFileDialog()

        messageFileButton = QPushButton()
        messageFileButton.setText("Get message from file")
        messageFileButton.setFont(QFont('Courier New', 12))
        messageFileButton.setStyleSheet("QPushButton {background : #1B2A41}")
        messageFileButton.setStyleSheet("QPushButton {color: #1B2A41}")
        messageFileButton.clicked.connect(self.messageFileClicked)

        keyFileButton = QPushButton()
        keyFileButton.setText("Get key from file")
        keyFileButton.setFont(QFont('Courier New', 12))
        keyFileButton.setStyleSheet("QPushButton {background : #1B2A41}") #poprawic
        keyFileButton.setStyleSheet("QPushButton {color: #1B2A41}")
        keyFileButton.clicked.connect(self.keyFileClicked)

        self.saveButton = QPushButton()
        self.saveButton.setText("Save pair to file")
        self.saveButton.setFont(QFont('Courier New', 12))
        self.saveButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.saveButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.saveButton.clicked.connect(self.saveClicked)
        self.saveButton.setEnabled(False)

        self.infoButton = QPushButton()
        self.infoButton.setText("Info")
        self.infoButton.setFont(QFont('Courier New', 12))
        self.infoButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.infoButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.infoButton.clicked.connect(self.infoClicked)

        buttonsFileLayout = QHBoxLayout()
        buttonsFileLayout.addWidget(messageFileButton)
        buttonsFileLayout.addWidget(keyFileButton)
        buttonsFileLayoutWidget = QWidget()
        buttonsFileLayoutWidget.setLayout(buttonsFileLayout)

        #przyciski
        encryptButton = QPushButton()
        encryptButton.setText("ENCRYPT")
        encryptButton.setFont(QFont('Courier New',12))
        encryptButton.setStyleSheet("QPushButton {background : #1B2A41}")
        encryptButton.setStyleSheet("QPushButton {color : #1B2A41}")
        encryptButton.clicked.connect(self.encryptClicked)

        decryptButton = QPushButton()
        decryptButton.setText("DECRYPT")
        decryptButton.setFont(QFont('Courier New', 12))
        decryptButton.setStyleSheet("QPushButton {background : #1B2A41}")
        decryptButton.setStyleSheet("QPushButton {color : #1B2A41}")
        decryptButton.clicked.connect(self.decryptClicked)

        buttonsLayout = QHBoxLayout()
        buttonsLayout.addWidget(encryptButton)
        buttonsLayout.addWidget(decryptButton)
        buttonsLayoutWidget = QWidget()
        buttonsLayoutWidget.setLayout(buttonsLayout)

        infoButtonsLayout = QHBoxLayout()
        infoButtonsLayout.addWidget(self.saveButton)
        infoButtonsLayout.addWidget(self.infoButton)
        infoButtonsLayoutWidget = QWidget()
        infoButtonsLayoutWidget.setLayout(infoButtonsLayout)


        self.saveMessageButton = QPushButton()
        self.saveMessageButton.setText("Save message to file")
        self.saveMessageButton.setFont(QFont('Courier New', 12))
        self.saveMessageButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.saveMessageButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.saveMessageButton.clicked.connect(self.saveMessageClicked)
        #self.saveButton.setEnabled(False)

        self.saveKeyButton = QPushButton()
        self.saveKeyButton.setText("Save key to file")
        self.saveKeyButton.setFont(QFont('Courier New', 12))
        self.saveKeyButton.setStyleSheet("QPushButton {background : #1B2A41}")
        self.saveKeyButton.setStyleSheet("QPushButton {color : #1B2A41}")
        self.saveKeyButton.clicked.connect(self.saveKeyClicked)
        #self.saveKeyButton.setEnabled(False)

        saveButtonsLayout = QHBoxLayout()
        saveButtonsLayout.addWidget(self.saveMessageButton)
        saveButtonsLayout.addWidget(self.saveKeyButton)
        saveButtonsLayoutWidget = QWidget()
        saveButtonsLayoutWidget.setLayout(saveButtonsLayout)

        instructionText = QLabel()
        instructionText.setText("Choose generator and power")
        instructionText.setAlignment(Qt.AlignCenter)
        instructionText.setFont(QFont('Courier New', 10))
        instructionText.setStyleSheet("QLabel {color: #1B2A41} ")

        self.comboBox = QComboBox(self)
       # self.comboBox.setGeometry(200, 150, 150, 30)
        generators = ["ANSI C", "MIN STD", "RANDU", "Fortran", "NAG", "APPLE"]
        self.comboBox.setEditable(True)
        self.comboBox.addItems(generators)
        self.comboBox.activated.connect(self.do_something)
        edit = self.comboBox.lineEdit()
        edit.setAlignment(Qt.AlignRight)


        self.power = QComboBox(self)
       #self.power.setGeometry(200, 150, 150, 30)
        potega = ["1", "2", "3"]
        self.power.setEditable(True)
        self.power.addItems(potega)
        self.power.activated.connect(self.do_something)
        editPower = self.power.lineEdit()
        editPower.setAlignment(Qt.AlignRight)


            #wstawianie przygotowanych pol do programu
        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titleText)
        mainMenu.addWidget(warningText)
        mainMenu.addWidget(self.subtitleText)
        mainMenu.addWidget(self.encryptedText)
        mainMenu.addWidget(self.decryptedText)

        mainMenu.addWidget(textFieldsLayoutWidget)
        mainMenu.addWidget(buttonsLayoutWidget)

        mainMenu.addWidget(buttonsFileLayoutWidget)
        mainMenu.addWidget(saveButtonsLayoutWidget)
        mainMenu.addWidget(infoButtonsLayoutWidget)


        mainMenu.addWidget(instructionText)

        mainMenu.addWidget(self.comboBox)
        mainMenu.addWidget(self.power)



        mainMenuWidget = QWidget()
        mainMenuWidget.setLayout(mainMenu)

        self.setCentralWidget(mainMenuWidget)



    def do_something(self):
        # printing something
        print(str(self.comboBox.currentText()))
        print(str(self.power.currentText()))

    def encryptClicked(self):
        key = self.keyField.text()
        encrypted = self.encrypt(key)
        self.subtitleText.setText("ENCRYPTED")
        self.encryptedText.setText(encrypted)
        self.decryptedText.setText("")
        self.saveButton.setEnabled(True)

    def decryptClicked(self):
        key = self.keyField.text()
        decrypted = self.decrypt(key)
        self.subtitleText.setText("DECRYPTED")
        self.decryptedText.setText(decrypted)
        self.saveButton.setEnabled(True)


    def messageFileClicked(self):
        self.keyFromFileButton.hide()
        self.messageFromFileButton.show()

        if self.messageFromFileButton.exec():
            files = self.messageFromFileButton.selectedFiles()
            r = open(files[0], 'r')
            with r:
                data = r.read()
                self.messageField.setText(data)

    def keyFileClicked(self):
        self.messageFromFileButton.hide()
        self.keyFromFileButton.show()
        if self.keyFromFileButton.exec():
            files = self.keyFromFileButton.selectedFiles()
            r = open(files[0],'r')
            with r:
                data = r.read()
                self.keyField.setText(data)

    def saveClicked(self):
        f = open("result.txt", "w")
        f.write(self.encryptedText.text())
        f.write("\n" + self.keyField.text())
        f.close()

    def saveMessageClicked(self):
        f = open("message.txt", "w")
        f.write(self.encryptedText.text())
        f.close()

    def saveKeyClicked(self):
        f = open("key.txt", "w")
        f.write(self.keyField.text())
        f.close()

    def infoClicked(self):
        info = QMessageBox()
        info.setWindowTitle("Info")
        info.setStyleSheet("QMessageBox {background-color : #CCC9DC}")
        f = open("info.txt", "r")
        data = f.read()
        info.setText(data)
        info.setFont(QFont('Courier New', 11))
        info.exec_()

    def keySequence(self,key):
        sequence = []
        for pos, ch in enumerate(key):
            lastletters = key[:pos]
            newnumber = 1
            for prevPos, prevCh in enumerate(lastletters):
                if prevCh > ch:
                    sequence[prevPos] += 1
                else:
                    newnumber += 1
            sequence.append(newnumber)
        return sequence

    def textInMatrix(self, string, key):
        lista1 = []
        lista2 = []
        ile = 0

        for x in string:
            lista1.append(x)
            ile = ile + 1
            if (ile % len(key) == 0):
                lista2.append(lista1.copy())
                lista1.clear()
                ile = 0
        if (ile % len(key) != 0):
            for y in range(0, len(key) - ile):
                lista1.append(' ')
            lista2.append(lista1.copy())
        return lista2

    def textFromMatrix(self, list, sekwencja, key, ileZnakowDodatkowych):
        finalMatrix = []
        column = []  # empty list

        for x in range(1, len(sekwencja) + 1):
            index = sekwencja.index(x)
            for row in list:  # dodawanie kolumny
                if row[index] != ' ':  # kropka na spacje
                    column.append(row[index])
                if len(column) == len(key):
                    finalMatrix.append(column.copy())
                    column.clear()
        for i in range(ileZnakowDodatkowych):  # dodawanie kolumny
            literka = random.choice(string.ascii_letters)
            column.append(literka)
            if len(column) == len(key):
                finalMatrix.append(column.copy())
                column.clear()
        if (len(column) > 0):
            for j in range(len(key) - len(column)):
                column.append(' ')
            finalMatrix.append(column.copy())

        return finalMatrix

    def splitMatrix(self, list, sekwencja):
        string = ''
        ile = 0
        for x in range(1, len(sekwencja) + 1):
            index = sekwencja.index(x)
            for row in list:  # dodawanie kolumny
                if row[index] != ' ':
                    string += row[index]
                    ile = ile + 1

                if ile == 5:
                    ile = 0
                    string += " "
        return string

    def textIntoColumns(self, stringTmp, keyTmp, ileZnakowDodatkowych):
        keyTmp = keyTmp.lower()
        key = keyTmp.replace(" ", "")

        string = stringTmp.replace(" ", "")
        ilePelnychRzedow = int(len(string) / len(key))
        ileZnakowWOstatnim = len(string) % len(key)
        ileKolumn = len(key)
        ileWszystkichRzedow = ilePelnychRzedow + 1
        if ileZnakowWOstatnim == 0:
            ileWszystkichRzedow -= 1

        sekwencja = self.keySequence(key)

        matrix = []
        for i in range(ileWszystkichRzedow):
            row = []
            for j in range(ileKolumn):
                row.append(' ')
            matrix.append(row)
        indexik = 0

        for x in range(1, len(sekwencja) + 1):
            index = sekwencja.index(x)

            tmp = None
            if index < ileZnakowWOstatnim:
                tmp = ilePelnychRzedow + 1
            else:
                tmp = ilePelnychRzedow

            for i in range(tmp):
                matrix[i][index] = string[indexik]  # kolumna potem wiersz
                indexik += 1

        ileUsun = ileKolumn * ileWszystkichRzedow - indexik + ileZnakowDodatkowych
        return matrix, ileUsun

    def encrypt(self, keyTmp):
        keyTmp = keyTmp.lower()
        key = keyTmp.replace(" ", "")
        ileZnakowDodatkowych = len(keyTmp) - len(key) + 1
        text = self.messageField.text()
        text = text.lower().replace(" ", "")

        sekwencja = self.keySequence(key)
        lista = self.textInMatrix(text, key)
        finalLista = self.textFromMatrix(lista, sekwencja, key, ileZnakowDodatkowych)
        finalMessage = self.splitMatrix(finalLista, sekwencja)
        return finalMessage

    def decrypt(self, keyTmp):
        keyTmp = keyTmp.lower()
        key = keyTmp.replace(" ", "")
        ileZnakowDodatkowych = len(keyTmp) - len(key) + 1
        text = self.encryptedText.text()
        text = text.lower().replace(" ", "")

        decMatrix, ileUsun = self.textIntoColumns(text, key, ileZnakowDodatkowych)
        combinedText = ''.join(ele for sub in decMatrix for ele in sub)
        combinedText = combinedText[:-ileUsun]

        finalDecryptedMatrix, nic = self.textIntoColumns(combinedText, key, ileZnakowDodatkowych)

        decryptedText = ''.join(ele for sub in finalDecryptedMatrix for ele in sub)
        originalText = decryptedText.replace(" ", "")

        finalText = ' '.join([originalText[i:i + 48] for i in range(0, len(originalText), 48)]) #zawijanie rzedami na sile, nie da sie inaczej tego zrobic

        return finalText


##--------------MAIN--------------------------

app = QApplication(sys.argv)

window = Okno()
window.setFixedSize(800,600)
window.setStyleSheet("background-color:  #CCC9DC ;")
window.show()

app.exec_()