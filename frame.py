#Importing necessary packages
import os
from functools import partial
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QTableWidget, QVBoxLayout, QPushButton, QMenuBar, QMainWindow, QDialog, QLabel, QMessageBox, QFileDialog, QFrame, QDesktopWidget, QScrollArea, QProgressBar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#Get current working directory
cwd = os.getcwd()

#Importing from Preprocessing Algorithms
sys.path.insert(1, cwd+'/Preprocessing Algorithms')
from row import row
from index import pre_process
from resize import resize

#Importing from object_detection
sys.path.insert(1, cwd+'/object_detection')
from Object_detection_image import detection

#Importing from Classifier
sys.path.insert(1, cwd+'/Classifier/v3')
from classify import classify

sys.path.insert(1, cwd+'/Classifier/Group Classifier')
from TSCM_classifier import TSCM_classifier
#Default Image to be Processed
imagePath = cwd+"/chromosome_data/original 32/original 32.jpg"

#Background Image
currentImage = cwd+"/images/white_bg.jpg"

target = cwd+"/chromosome_data/original 32/"

#To display the Generated Karyotype
class Window2(QMainWindow):              
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generated Karyotype")
        
        global target
        # t = imagePath.split("/")
        imageDir = target+"/karyotype.jpg"
        #label = QLabel(self)
        # imagePath = "G:/Karyotyping/Classifier/UI/karyotype.jpg"
        # pixmap = QPixmap(imagePath)
        # label.setPixmap(pixmap)
        # label.show()
        # label.resize(pixmap.width(),pixmap.height())

        self.central_widget = QWidget()               
        self.setCentralWidget(self.central_widget)    
        lay = QVBoxLayout(self.central_widget)
        label = QLabel(self)
        #imagePath = "G:/Karyotyping/Classifier/UI/karyotype.jpg"
        pixmap = QPixmap(imageDir)
        #pixmap = QPixmap('logo.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        lay.addWidget(label)
        self.setFixedSize(pixmap.width(), pixmap.height())
        self.show()        

# flag = 1
#Interactive Drag and Drop Space to arrange the chromosomes
class DragWindow(QWidget):
    def __init__(self):
        super().__init__()
        lst = ['chr_1', 'chr_2', 'chr_3', 'chr_4', 'chr_5', 'chr_6', 'chr_7', 'chr_8', 'chr_9', 'chr_10', 'chr_11', 'chr_12', 'chr_13', 'chr_14', 'chr_15', 'chr_16', 'chr_17', 'chr_18', 'chr_19', 'chr_20', 'chr_21', 'chr_22', 'chr_x', 'chr_y']
        #Predicted Dict
        #predicted = {'1.jpg': 'chr_1', '11.jpg': 'chr_4', '12.jpg': 'chr_8', '13.jpg': 'chr_x', '15.jpg': 'chr_8', '16.jpg': 'chr_4', '17.jpg': 'chr_16', '18.jpg': 'chr_15', '19.jpg': 'chr_16', '22.jpg': 'chr_16', '23.jpg': 'chr_15', '24.jpg': 'chr_16', '25.jpg': 'chr_4', '27.jpg': 'chr_1', '31.jpg': 'chr_14', '34.jpg': 'chr_13', '35.jpg': 'chr_20', '36.jpg': 'chr_20', '37.jpg': 'chr_13', '38.jpg': 'chr_16', '42.jpg': 'chr_x', '44.jpg': 'chr_16', '45.jpg': 'chr_16', '46.jpg': 'chr_19', '5.jpg': 'chr_17', '6.jpg': 'chr_16'}
        # global flag

        #Unpredicted Dict
        #unpredicted = {'10.jpg': 'chr_5', '14.jpg': 'chr_16', '2.jpg': 'chr_3', '20.jpg': 'chr_14', '21.jpg': 'chr_2', '26.jpg': 'chr_20', '28.jpg': 'chr_1', '29.jpg': 'chr_6', '3.jpg': 'chr_4', '30.jpg': 'chr_15', '32.jpg': 'chr_x', '33.jpg': 'chr_22', '39.jpg': 'chr_17', '4.jpg': 'chr_6', '40.jpg': 'chr_19', '41.jpg': 'chr_14', '43.jpg': 'chr_21', '7.jpg': 'chr_9', '8.jpg': 'chr_16', '9.jpg': 'chr_9'}

        global predicted
        global unpredicted
        global length_dict
        global imagePath
        global TSCM_predicted
        global TSCM_unpredicted

        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()
        self.generateButton = QPushButton("Generate Karyotype")
        self.generateButton.clicked.connect(self.generate)
        self.resetButton = QPushButton("Reset")
        self.resetButton.clicked.connect(partial(self.generateList,lst,predicted,unpredicted))
        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.back)

        self.myListWidget1.setViewMode(QListWidget.IconMode)
        self.myListWidget2.setViewMode(QListWidget.IconMode)

        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)
        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)
        self.myListWidget1.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.myListWidget2.setDefaultDropAction(QtCore.Qt.MoveAction)

        #self.setGeometry(0, 0, 1920, 1024)
        self.setFixedSize(1366,668)

        self.myListWidget1.setIconSize(QSize(110,110))
        self.myListWidget2.setIconSize(QSize(110,110))

        self.myLayout = QHBoxLayout()
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        #self.vbox1 = QVBoxLayout()
        #self.vbox1.addWidget(self.backButton)
        #self.myLayout.addLayout(self.vbox1)
        self.myLayout.addWidget(self.myListWidget1)
        self.myLayout.addWidget(self.myListWidget2)
        
        self.hbox.addWidget(self.generateButton)
        self.hbox.addWidget(self.resetButton)
        self.hbox.addWidget(self.backButton)
        self.vbox.addLayout(self.myLayout)
        self.vbox.addLayout(self.hbox)
        # print(lst)
        # if(flag == 0):
        # self.generateList(lst,predicted,unpredicted)
        # else:
        self.generateList(lst,TSCM_predicted,TSCM_unpredicted)
        #wid = QWidget(self)
        #self.setCentralWidget(wid)
        #wid.setLayout(self.vbox)
        #wid.setLayout(self.VmyLayout)
        self.setWindowTitle('Drag and Drop');
        self.setLayout(self.vbox)
        #self.CreateMenu()
        self.show()
    
    # def openDialog(self):
    #   mydialog = QDialog()
    #   mydialog.setModal(True)
    #   mydialog.exec()

    def generate(self):
        # global imagePath
        global target
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Successfully Generated")
        msg.setIcon(QMessageBox.Information)
        msg.buttonClicked.connect(self.showKaryotype)
        # mydialog = QDialog(self)
        # mydialog.setModal(True)
        # label = QLabel(self)
        # imagePath = "G:/Karyotyping/Classifier/UI/karyotype.jpg"
        # pixmap = QPixmap(imagePath)
        # label.setPixmap(pixmap)
        # label.show()
        # label.resize(pixmap.width(),pixmap.height())
        # mydialog.exec()
        # print("clicked")
        itemsTextList =  [str(self.myListWidget2.item(i).text()) for i in range(self.myListWidget2.count())]
        print(itemsTextList)
        order = []
        for i in itemsTextList:
          print(i)
          t = i.split(".")
          print(t)
          order.append(t[0]+".jpg")
        print(order)
        row(order,target)
        x = msg.exec_()


    def showKaryotype(self,i):
        print("works")
        self.window2()

    def window2(self):
        self.w = Window2()
        self.w.show()
        #self.hide()        

    def back(self):
        self.w = Window()
        self.w.show()
        self.hide()        

    def generateList(self,lst,predicted,unpredicted):
        #global lst
        global target
        self.myListWidget1.clear()
        self.myListWidget2.clear()
        print(predicted)
        print(unpredicted)
        key = []
        for i in lst:
            print(i)
            key.append([k for k,v in predicted.items() if v == i])
            key.append([k for k,v in unpredicted.items() if v == i])
            #print(p_key)   
            #print(up_key)
        #print(key)
        key = [x for x in key if x != []]
        #print(key)
        order = []
        for i in range(len(key)):
            for j in key[i]:
                order.append(j)
        print(order)

        #from graph
        # length = [('43.jpg', 3.236067977499777), ('33.jpg', 7.071067811865483), ('41.jpg', 10.964724878577353), ('46.jpg', 12.034999410188222), ('31.jpg', 12.42723722081092), ('36.jpg', 13.17881648958412), ('26.jpg', 14.587319925722593), ('20.jpg', 14.882824613967331), ('34.jpg', 17.45929849618171), ('45.jpg', 17.990176050687683), ('23.jpg', 18.30835512550115), ('17.jpg', 18.56110321786805), ('22.jpg', 18.637345388044217), ('38.jpg', 18.734204403865945), ('14.jpg', 20.2921628262268), ('35.jpg', 21.49734604545561), ('40.jpg', 21.934712330176136), ('37.jpg', 22.624561243389792), ('30.jpg', 22.87916646860505), ('5.jpg', 24.42346214554805), ('44.jpg', 27.695265004878895), ('9.jpg', 27.94202675370851), ('39.jpg', 28.432097519840912), ('18.jpg', 29.532901616576865), ('6.jpg', 31.29894847906794), ('19.jpg', 33.24958456876382), ('12.jpg', 33.4073821587324), ('29.jpg', 33.90908243369089), ('28.jpg', 37.54283981688735), ('32.jpg', 39.49442544603043), ('24.jpg', 39.63496546878376), ('25.jpg', 41.44939319582502), ('7.jpg', 42.836499520552934), ('8.jpg', 42.84934761355323), ('11.jpg', 44.0752049627969), ('4.jpg', 44.338105647958194), ('13.jpg', 44.53810290119516), ('16.jpg', 47.44687380130529), ('3.jpg', 49.38592789078901), ('10.jpg', 49.53932107566584), ('2.jpg', 49.72443909046185), ('15.jpg', 53.7317540349579), ('21.jpg', 65.05739786074896), ('27.jpg', 67.50474637686915), ('1.jpg', 73.56442943155982), ('42.jpg', 104.4383612537255)]


        # t = imagePath.split("/")
        rootdir = target+"/Resized/vertical"
        #rootdir = "G:/Karyotyping/Classifier/images/resized"
        count = 0
        for subdir, dirs, files in os.walk(rootdir):
            files.sort(key=lambda x:(int(x[:-4]), int(x[:-4])))
            for file in order:
                #print(file)
                a = os.path.join(subdir,file)
                t = file.split(".")
                if file in predicted:
                    l1 = QListWidgetItem(QIcon(a), t[0]+"."+predicted[file])
                    l1.setBackground(QtGui.QColor("#008000"))

                    #l1.setTextAlignment(0) 
                else:
                    l1 = QListWidgetItem(QIcon(a), t[0]+"."+unpredicted[file])
                    l1.setBackground(QtGui.QColor("#FF0000"))
                    #l1.setTextAlignment(0)
                l1.setToolTip(str(length_dict[file]))
                #lst.append(file+":"+l1.data(0))        
                count+=1
                self.myListWidget1.insertItem(count, l1)


        itemsTextList =  [str(self.myListWidget1.item(i).text()) for i in range(self.myListWidget1.count())]
        print(itemsTextList)
        


predicted = {}
unpredicted = {}
length_dict = {}
TSCM_predicted = {}
TSCM_unpredicted = {}

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1366,678)
        #self.setMaximumSize(1000, 1000)
        #self.resize(700, 494)

        #created layout
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.vbox1 = QVBoxLayout()

        self.setWindowTitle('Karyotyping')

        self.setWindowFlags(QtCore.Qt.Window)

        #created menu
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, width, 20))
        file = self.menubar.addMenu("File")
        #operations = self.menubar.addMenu("Operations")
        view = self.menubar.addMenu("View")

        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        #self.actionPre = QtWidgets.QAction(self)
        #self.actionPre.setObjectName("actionPre")
        #self.actionDetection = QtWidgets.QAction(self)
        #self.actionDetection.setObjectName("actionDetection")
        self.actionCropped = QtWidgets.QAction(self)
        self.actionCropped.setObjectName("actionCropped")
        self.actionThreshold = QtWidgets.QAction(self)
        self.actionThreshold.setObjectName("actionThreshold")
        self.actionSkeleton = QtWidgets.QAction(self)
        self.actionSkeleton.setObjectName("actionSkeleton")
        #self.actionSmoothing = QtWidgets.QAction(self)
        #self.actionSmoothing.setObjectName("actionSmoothing")
        self.actionMax = QtWidgets.QAction(self)
        self.actionMax.setObjectName("actionMax")
        self.actionNoise = QtWidgets.QAction(self)
        self.actionNoise.setObjectName("actionNoise")
        self.actionRotated = QtWidgets.QAction(self)
        self.actionRotated.setObjectName("actionRotated")
        self.actionGraph = QtWidgets.QAction(self)
        self.actionGraph.setObjectName("actionGraph")



        file.addAction(self.actionOpen)
        file.addAction(self.actionSave)
        #operations.addAction(self.actionPre)
        #operations.addAction(self.actionDetection)
        view.addAction(self.actionCropped)
        view.addAction(self.actionThreshold)
        view.addAction(self.actionMax)
        view.addAction(self.actionSkeleton)
        view.addAction(self.actionNoise)
        #view.addAction(self.actionSmoothing)
        view.addAction(self.actionRotated)
        view.addAction(self.actionGraph)

        self.menubar.addAction(file.menuAction())
        #self.menubar.addAction(operations.menuAction())
        self.menubar.addAction(view.menuAction())


        #creating path
        self.path = QtWidgets.QLabel(self)
        #self.path.setGeometry(QtCore.QRect(10, 20, 511, 20))
        self.path.setIndent(10)
        self.path.setObjectName("path")

        #image of left side
        # self.frameImage = QtWidgets.QFrame(self)
        # self.frameImage.setGeometry(QtCore.QRect(10, 50, 600, 500))
        # self.frameImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frameImage.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.frameImage.setMidLineWidth(1)
        # self.frameImage.setObjectName("frameImage")
        # self.frameImage.setStyleSheet("background-color:white")
        # self.frameImage.resize(300,300)


        global currentImage
        self.image = QtWidgets.QLabel(self)
        self.image.setGeometry(QtCore.QRect(0, 0, 600, 500))
        #self.image.setText("Input")
        self.image.setPixmap(QtGui.QPixmap(currentImage))
        self.image.setObjectName("image")

        #creating middle buttons
        # self.side_frame = QtWidgets.QFrame(self)
        # self.side_frame.setGeometry(QtCore.QRect((width/2)-25, 50, 200, height-150))
        # self.side_frame.setAutoFillBackground(False)
        # self.side_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.side_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.side_frame.setMidLineWidth(1)
        # self.side_frame.setObjectName("side_frame")

        self.karyotypeButton = QtWidgets.QPushButton(self)
        self.karyotypeButton.setGeometry(QtCore.QRect(40, 197, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        self.karyotypeButton.setFont(font)
        self.karyotypeButton.setAutoDefault(False)
        self.karyotypeButton.setObjectName("karyotypeButton")

        self.originalButton = QtWidgets.QPushButton(self)
        self.originalButton.setGeometry(QtCore.QRect(40, 277, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        self.originalButton.setFont(font)
        self.originalButton.setDefault(False)
        self.originalButton.setFlat(False)
        self.originalButton.setObjectName("originalButton")

        self.dragButton = QtWidgets.QPushButton(self)
        self.dragButton.setGeometry(QtCore.QRect(40, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        self.dragButton.setFont(font)
        self.dragButton.setDefault(False)
        self.dragButton.setFlat(False)
        self.dragButton.setObjectName("dragButton")

        self.processButton = QtWidgets.QPushButton(self)
        self.processButton.setGeometry(QtCore.QRect(40, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        self.processButton.setFont(font)
        self.processButton.setDefault(False)
        self.processButton.setFlat(False)
        self.processButton.setObjectName("processButton")


        # self.classifyButton = QtWidgets.QPushButton(self)
        # self.classifyButton.setGeometry(QtCore.QRect(40, 350, 131, 31))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI Historic")
        # font.setPointSize(8)
        # self.classifyButton.setFont(font)
        # self.classifyButton.setDefault(False)
        # self.classifyButton.setFlat(False)
        # self.classifyButton.setObjectName("classifyButton")

        self.viewButton = QtWidgets.QPushButton(self)
        self.viewButton.setGeometry(QtCore.QRect(40, 350, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(8)
        self.viewButton.setFont(font)
        self.viewButton.setDefault(False)
        self.viewButton.setFlat(False)
        self.viewButton.setObjectName("viewButton")


        # self.viewTSCMButton = QtWidgets.QPushButton(self)
        # self.viewTSCMButton.setGeometry(QtCore.QRect(40, 350, 131, 31))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI Historic")
        # font.setPointSize(8)
        # self.viewTSCMButton.setFont(font)
        # self.viewTSCMButton.setDefault(False)
        # self.viewTSCMButton.setFlat(False)
        # self.viewTSCMButton.setObjectName("viewButton")


        # self.dragTSCMButton = QtWidgets.QPushButton(self)
        # self.dragTSCMButton.setGeometry(QtCore.QRect(40, 350, 131, 31))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI Historic")
        # font.setPointSize(8)
        # self.dragTSCMButton.setFont(font)
        # self.dragTSCMButton.setDefault(False)
        # self.dragTSCMButton.setFlat(False)
        # self.dragTSCMButton.setObjectName("dragButton")

        #image in the right
        # self.frameResult = QtWidgets.QFrame(self)
        # self.frameResult.setGeometry(QtCore.QRect(860, 50, 600, 500))
        # self.frameResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frameResult.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.frameResult.setMidLineWidth(1)
        # self.frameResult.setObjectName("frameResult")

        self.myListWidget_right = QListWidget()
        self.myListWidget_right.setViewMode(QListWidget.IconMode)
        self.myListWidget_right.setIconSize(QSize(120,120))
        self.myListWidget_right.setFixedSize(568,576)



        # self.result = QtWidgets.QLabel(self)
        # self.result.setGeometry(QtCore.QRect(0, 20, 500, height-150))
        # #self.result.setText("Output")
        # self.result.setPixmap(QtGui.QPixmap("images/white_bg.jpg"))
        # self.result.setObjectName("result")



        #self.hbox.addWidget(self.frameImage)
        self.hbox.addWidget(self.image)

        self.vbox.addWidget(self.originalButton)
        self.vbox.addWidget(self.processButton)
        self.vbox.addWidget(self.karyotypeButton)
        self.vbox.addWidget(self.dragButton)
        self.vbox.addWidget(self.viewButton)
        # self.vbox.addWidget(self.classifyButton)
        # self.vbox.addWidget(self.dragTSCMButton)
        # self.vbox.addWidget(self.viewTSCMButton)
        

        self.hbox.addLayout(self.vbox)
        #self.hbox.addWidget(self.side_frame)
        #self.hbox.addWidget(self.frameResult)
        self.hbox.addWidget(self.myListWidget_right) #result
        self.vbox1.addWidget(self.path)
        self.vbox1.addLayout(self.hbox)


        #log
        # self.frameLog = QtWidgets.QFrame(self)
        # self.frameLog.setGeometry(QtCore.QRect(0, height-100, height, 800))
        # self.frameLog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frameLog.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.frameLog.setMidLineWidth(1)
        # self.frameLog.setObjectName("frameLog")

        # self.log = QtWidgets.QLabel(self.frameLog)
        # self.log.setGeometry(QtCore.QRect(10, 10, 41, 16))
        # self.log.setIndent(7)
        # self.log.setObjectName("log")

        # self.log_details = QtWidgets.QLabel(self.frameLog)
        # self.log_details.setGeometry(QtCore.QRect(60, 10, 750, 220))
        # self.log_details.setAutoFillBackground(False)
        # self.log_details.setScaledContents(True)
        # self.log_details.setWordWrap(True)
        # self.log_details.setIndent(10)
        # self.log_details.setObjectName("log_details")


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



        #action listeners that call the needed function
        self.actionOpen.triggered.connect(self.open_file)

        self.actionCropped.triggered.connect(partial(self.display_preprocessed,"cropped"))
        self.actionThreshold.triggered.connect(partial(self.display_preprocessed,"threshold"))
        self.actionMax.triggered.connect(partial(self.display_preprocessed,"Original_after_max"))
        self.actionSkeleton.triggered.connect(partial(self.display_preprocessed,"skeleton"))
        self.actionNoise.triggered.connect(partial(self.display_preprocessed,"noise_removed"))
        #self.actionSmoothing.triggered.connect(partial(self.display_preprocessed,"smoothened"))
        self.actionRotated.triggered.connect(partial(self.display_preprocessed,"vertical"))
        self.actionGraph.triggered.connect(partial(self.display_preprocessed,"graph"))

        self.originalButton.clicked.connect(self.detect)
        self.dragButton.clicked.connect(self.openWindow)
        self.processButton.clicked.connect(self.process)
        self.karyotypeButton.clicked.connect(self.TSCMclassifier)
        # self.classifyButton.clicked.connect(self.TSCMclassifier)
        self.viewButton.clicked.connect(self.view)
        # self.viewTSCMButton.clicked.connect(self.view)
        # self.dragTSCMButton.clicked.connect(partial(self.openWindow,1))

        #display_preprocessed(self,"vertical")

        # wid = QWidget(self)
        # self.setCentralWidget(wid)
        # wid.setLayout(self.hbox)
        self.setLayout(self.vbox1)
        self.show()

    def view(self):
        global imagePath
        global target
        self.w = Window2()
        #t = imagePath.split("/")
        rootdir = target+"/karyotype.jpg"
        self.path.setText("Path: "+rootdir)

        self.w.show()
        #self.hide() 

    #To open an image    
    def open_file(self):
        name = QFileDialog.getOpenFileName(self,"Open Image", './chromosome_data', "Image files (*.jpg *.png *.bmp)")
        global imagePath
        global currentImage
        global target

        imagePath = name[0]
        currentImage = imagePath
        pixmap = QtGui.QPixmap(imagePath)
        temp = imagePath.split("/")
        imageName = temp[-1]
        folderName = imageName.split(".")
        folderName = folderName[0]
        target = cwd+"/chromosome_data/"+folderName
        if not os.path.exists(target):
        	os.mkdir(target)
        self.image.setPixmap(QtGui.QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
        self.path.setText("Path: "+imagePath)

    #To view the intermediate steps of pre-processing and length determination
    def display_preprocessed(self,folder):
        
        global target
        self.myListWidget_right.clear()
        rootdir = target+"/Resized/"+folder
        self.path.setText("Path: "+rootdir)
        count = 0
        for subdir, dirs, files in os.walk(rootdir):
            files.sort(key=lambda x:(int(x[:-4]), int(x[:-4])))
            for file in files:
                #print(file)
                a = os.path.join(subdir,file)
                t = file.split(".")
                # if file in predicted:
                l1 = QListWidgetItem(QIcon(a), file)
                count+=1
                self.myListWidget_right.insertItem(count, l1)
        itemsTextList =  [str(self.myListWidget_right.item(i).text()) for i in range(self.myListWidget_right.count())]
        print(itemsTextList)

    #To detect individual chromosomes using Faster RCNN    
    def detect(self):
        
        global imagePath
        global target
        detection(imagePath,target)
        resize(target,"cropped")
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Successfully Detected")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    #To perform preprocessing steps on the detected chromosomes
    def process(self):

        global imagePath
        global target
        global length_dict
        # print("works")
        len_dict = pre_process(target)
        length_dict = len_dict
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Successfully Processed")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        
    #To classify the chromosomes
    # def classify(self):

    #     global target
    #     global predicted
    #     global unpredicted
    #     pred,unpred = classify(target)
    #     print(pred)
    #     print(unpred)
    #     predicted = pred
    #     unpredicted = unpred
    #     msg = QMessageBox()
    #     msg.setWindowTitle("Information")
    #     msg.setText("Successfully Classified")
    #     msg.setIcon(QMessageBox.Information)
    #     #msg.buttonClicked.connect(self.showKaryotype)
    #     x = msg.exec_()
        
    def TSCMclassifier(self):

        global target
        global TSCM_predicted
        global TSCM_unpredicted
        pred,unpred = TSCM_classifier(target)
        # print(pred)
        # print(unpred)
        TSCM_predicted = pred
        TSCM_unpredicted = unpred
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Successfully Classified")
        msg.setIcon(QMessageBox.Information)
        #msg.buttonClicked.connect(self.showKaryotype)
        x = msg.exec_()

    def openWindow(self):

        self.w = DragWindow()
        self.w.show()
        #self.window = QtWidgets.QMainWindow()
        #self.ui = Window()
        #self.ui.setupUi(self.window)
        self.hide()
        #self.window.show()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        #Buttons
        self.karyotypeButton.setText(_translate("MainWindow", "Classify"))
        self.originalButton.setText(_translate("MainWindow", "Detect"))
        self.dragButton.setText(_translate("MainWindow", "Edit"))
        self.processButton.setText(_translate("MainWindow", "Process"))
        self.viewButton.setText(_translate("MainWindow", "View"))
        # self.classifyButton.setText(_translate("MainWindow", "TSCM Classifier"))
        # self.dragTSCMButton.setText(_translate("MainWindow", "Edit TSCM Output"))
        # self.viewTSCMButton.setText(_translate("MainWindow", "View TSCM Output"))


        self.path.setText(_translate("MainWindow", "Path: "))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        
        self.actionCropped.setText(_translate("MainWindow", "Cropped Images"))
        #self.action.setShortcut(_translate("MainWindow", "Ctrl+P"))
        
        self.actionThreshold.setText(_translate("MainWindow", "Threshold Output"))
        #self.actionDetection.setShortcut(_translate("MainWindow", "Ctrl+D"))

        self.actionMax.setText(_translate("MainWindow", "Connected Components Output"))
        #self.actionThreshold.setShortcut(_translate("MainWindow", "Ctrl+T"))

        self.actionSkeleton.setText(_translate("MainWindow", "Skeleton"))
        #self.actionMax.setShortcut(_translate("MainWindow", "Ctrl+M"))

        self.actionNoise.setText(_translate("MainWindow", "Noise"))
        #self.actionSkeletonize.setShortcut(_translate("MainWindow", "Ctrl+K"))
        #self.actionSmoothing.setText(_translate("MainWindow", "Smoothening"))
        #self.actionSmoothing.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionGraph.setText(_translate("MainWindow", "Graph"))

        self.actionRotated.setText(_translate("MainWindow", "Rotated"))

        self.show()

App = QApplication(sys.argv)
width = QDesktopWidget().screenGeometry(-1).width()
height = QDesktopWidget().screenGeometry(-1).height()
print(width)
print(height)
splash_pix = QtGui.QPixmap('images/splash.png')
splash_pix=splash_pix.scaled(width, height)
splash = QtWidgets.QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
splash.setEnabled(False)
progressBar = QtWidgets.QProgressBar(splash)
progressBar.setMaximum(10)
progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
splash.show()

for i in range(1, 11):
    progressBar.setValue(i)
    t = time.time()
    while time.time() < t + 0.1:
       App.processEvents()

time.sleep(1)
window = Window() 
window.show()
splash.finish(window)
window.showMaximized()              
sys.exit(App.exec())