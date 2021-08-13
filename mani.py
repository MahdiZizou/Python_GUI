#In 103 and 104 of Udemy course, it talks about how to make a qml file.
#qml file defines the interface of a window when runnig an application
#qml itself needs a separte course so it skipped it.

#we do not want to write a qml so we use layout which has certain interface. 

#also we can use Qt Creator UI version to design our desire layout

#%% Sample 1: Designing GUI by QtPy programming in python
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout, 
                             QPushButton, QLabel) #when you want to import many things, use ()
 
class MainWindow(QWidget):
    #CONSTANT from here to ***
    def __init__(self):
        super().__init__()
        self.init__ui() #this function is defiend below
    #***
    
    def init__ui(self):
        
        Label = QLabel("I am a label!")
        
        #creating some buttoms:
        okButtom = QPushButton("OK")
        cancelBottom = QPushButton("Cancel")
        HiButtom = QPushButton("Hi!")
        
        #creating a layout:
        horizental = QHBoxLayout() #if you change to QVBoxlayout(), buttoms will place vertically.
        
        horizental.addStretch() #if you comment this, when you stretch the windows, buttoms will stretch
                                #by this command, buttoms sizes are constant
        horizental.addWidget(okButtom)
        horizental.addWidget(cancelBottom)
        
        vertical = QVBoxLayout()
        vertical.addStretch() 
        
        #The ORDER of adding widgets matters:
        vertical.addWidget(Label)
        vertical.addWidget(HiButtom)
        
        vertical.addLayout(horizental)
        
        #CONSTANT from here to    
        self.setLayout(vertical) #main layout is vertical
        self.setWindowTitle("This is my layout")
        self.show()
        #***

#CONSTANT from here to            
# starting the QApplication from main.py and this is constant:
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
#***  
  
#%% Sample 2: Designing GUI by QtCreator software and then import interface to python
from PyQt5 import QtWidgets
import sys

#Step 1: open Qt Creator and make a new project 
#Step 2: design your desired interface there
#Step 3: save final file as .ui file and copy it to py file directory
#Step 4: open .ui file and check what is the name of class in very first lines; e.g.:
         # <widget class="QDialog" name="Dialog"> so:
#Step 5: place QtWidgets.QDialog below when inheriting MainWindow class

#Note: you can also change the layout by changing .ui file but you need to know ui coding

class MainWindow1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('basic.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow1()
app.exec_()

class MainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('basic2.ui', self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow2()
app.exec_()

#%% Sample 3: Click counter
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout, 
                             QPushButton, QLabel, QLineEdit) 
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init__ui() 
        self.counter = 0 #you add self to be able to call it later

    def init__ui(self):
        
        label = QLabel("Name: ")
        name_input = QLineEdit()
        
        self.button = QPushButton("Clicked: 0") #by adding self to button, you make it a variable and you can call it all over the class
        
        self.button.clicked.connect(self.clickedButton)  #here we conned UI and pyton when clicking       
        self.button.pressed.connect(self.pressedButton)  #here we conned UI and pyton when pressing mouse      
        self.button.released.connect(self.releasedButton)  #here we conned UI and pyton when releasing mouse      
                                              
        h = QHBoxLayout()
        h.addWidget(label)
        h.addWidget(name_input)
        
        v = QVBoxLayout()
        v.addLayout(h)
        v.addWidget(self.button)
        
        self.setLayout(v) #main layout is vertical
        
        self.setWindowTitle("This is my layout")
        
        self.show()
    
    def clickedButton(self): 
            print("This is clicked")
            self.counter += 1 #whenever you call this function, it add 1 to counter
            self.button.setText("Clicked:" + str(self.counter))
            
    def pressedButton(self):
            print("This is pressed")
    
    def releasedButton(self):
            print("This is released")

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 

#%% Sample 4: Labeling
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout, 
                             QPushButton, QLabel, QLineEdit) 
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init__ui() 

    def init__ui(self):
        
        self.text_label = QLabel("No name yet, so I do nothing!")
        
        self.label = QLabel("Name:")
        
        self.name_input = QLineEdit()
        
        self.button = QPushButton("Set Name") #by adding self to button, you make it a variable and you can call it all over the class
                                           
        self.button.clicked.connect(self.alterName)
        
        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)
        
        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)
        
        self.setLayout(v) #main layout is vertical
        
        self.setWindowTitle("This is my layout")
        
        self.show()
    
    def alterName(self):
        inputed_text = self.name_input.text()
        self.text_label.setText("You entered: " + inputed_text )
        self.setWindowTitle(inputed_text + "'s window")
        print(inputed_text)
        
    

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    
#%% Sample 5: Making a grid
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class Application(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculator")
        
        self.CreatApp()
        
        self.show()
        
    def CreatApp(self):
        
        self.grid = QGridLayout() #we have HBox and VBox as well as Grid in QtPy
        
        buttom_1 = QPushButton("B1")
        buttom_2 = QPushButton("B2")
        buttom_3 = QPushButton("B3")
        buttom_4 = QPushButton("Last B")
        
        self.grid.addWidget(buttom_1, 0,0,1,1) #it means in first row and first col, give one row and one col to buttom_1
        self.grid.addWidget(buttom_2, 0,1,1,1)
        self.grid.addWidget(buttom_3, 0,2,1,1)
        self.grid.addWidget(buttom_4, 1,0,1,3)
        
        self.setLayout(self.grid)
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())

#%% Sample 6: Making a calculator
import sys
from PyQt5.QtWidgets import * 
 
# Here Button class would be inherited by Application class.
# in this class we define the function of each buttom:
class Button():
    
    def __init__(self, text, results):
        
        #here we put button function as a text like: +,7,...
        self.text = text
        
        self.results = results
        
        #we connect text to a button and then button to a function
        self.b = QPushButton(str(text))
        self.b.clicked.connect(lambda: self.handleInput(self.text)) #do not forger to use lambda!!!
    
    def handleInput(self, value):
        if value is "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif value is "AC":
            self.results.setText("")
        elif value is "Del":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        elif value is "%":
            current_value = self.results.text()
            v = float(current_value)/100
            self.results.setText(str(v))
        else:
            current_value = self.results.text()
            new_value = current_value + str(value)
            self.results.setText(new_value)
            
# In this class we just make a UI interface:
class Application(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculator")
        
        self.CreatApp()
                
    def CreatApp(self):
        
        grid = QGridLayout() #we have HBox and VBox as well as Grid in QtPy
        
        buttons = ["AC","Del","%","/",
                   7,8,9, "*",
                   4,5,6, "-",
                   1,2,3, "+",
                   0,".","="]
        
        #here we add input and we see results in a slot in first row:
        display=  QLineEdit() #display is a QLineEdit so it is the text we put in.
        
        grid.addWidget(display,0,0,1,4)
        #
        
        #here from second row so on, we add buttoms:
        row = 1
        col = 0
        
        for button in buttons:
            if col>3:
                col = 0
                row += 1 
            
            button_object = Button(button, display)
            
            if button == "=":
                grid.addWidget(button_object.b, row, col, 1, 2) #b itself is a PushButton
            else:
                grid.addWidget(button_object.b, row, col, 1, 1)
            
            col += 1
            #
            
        
        self.show()
        self.setLayout(grid)
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())