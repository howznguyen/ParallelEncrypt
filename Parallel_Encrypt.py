# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Parallel_Encrypt_Ver2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from handle.worker import *
import handle.main as handle
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 589)
        self.file_open = ""
        self.file_save = ""
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblTitle = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_3.addWidget(self.lblTitle, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grbxFile = QtWidgets.QGroupBox(self.frame_3)
        self.grbxFile.setObjectName("grbxFile")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.grbxFile)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnOpen = QtWidgets.QPushButton(self.grbxFile)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout_2.addWidget(self.btnOpen)
        self.btnSave = QtWidgets.QPushButton(self.grbxFile)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout_2.addWidget(self.btnSave)
        self.verticalLayout_2.addWidget(self.grbxFile)
        self.grbxType = QtWidgets.QGroupBox(self.frame_3)
        self.grbxType.setObjectName("grbxType")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.grbxType)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioEncrypt = QtWidgets.QRadioButton(self.grbxType)
        self.radioEncrypt.setObjectName("radioEncrypt")
        self.radioEncrypt.setChecked(True)       
        self.horizontalLayout_3.addWidget(self.radioEncrypt)
        self.radioDecrypt = QtWidgets.QRadioButton(self.grbxType)
        self.radioDecrypt.setObjectName("radioDecrypt")
        self.horizontalLayout_3.addWidget(self.radioDecrypt)
        self.verticalLayout_2.addWidget(self.grbxType)
        self.grbxCipher = QtWidgets.QGroupBox(self.frame_3)
        self.grbxCipher.setObjectName("grbxCipher")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.grbxCipher)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cboCipher = QtWidgets.QComboBox(self.grbxCipher)
        self.cboCipher.setObjectName("cboCipher")
        self.horizontalLayout_4.addWidget(self.cboCipher)
        self.verticalLayout_2.addWidget(self.grbxCipher)
        self.grbxSequent = QtWidgets.QGroupBox(self.frame_3)
        self.grbxSequent.setObjectName("grbxSequent")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.grbxSequent)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnSequent = QtWidgets.QPushButton(self.grbxSequent)
        self.btnSequent.setObjectName("btnSequent")
        self.horizontalLayout_5.addWidget(self.btnSequent)
        self.lineSequent = QtWidgets.QLineEdit(self.grbxSequent)
        self.lineSequent.setEnabled(False)
        self.lineSequent.setObjectName("lineSequent")
        self.horizontalLayout_5.addWidget(self.lineSequent)
        self.verticalLayout_2.addWidget(self.grbxSequent)
        self.grbxParallel = QtWidgets.QGroupBox(self.frame_3)
        self.grbxParallel.setObjectName("grbxParallel")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.grbxParallel)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnParallel = QtWidgets.QPushButton(self.grbxParallel)
        self.btnParallel.setObjectName("btnParallel")
        self.horizontalLayout_6.addWidget(self.btnParallel)
        self.spinThread = QtWidgets.QSpinBox(self.grbxParallel)
        self.spinThread.setObjectName("spinThread")
        self.horizontalLayout_6.addWidget(self.spinThread)
        self.lineParallel = QtWidgets.QLineEdit(self.grbxParallel)
        self.lineParallel.setEnabled(False)
        self.lineParallel.setObjectName("lineParallel")
        self.horizontalLayout_6.addWidget(self.lineParallel)
        self.verticalLayout_2.addWidget(self.grbxParallel)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableResult = QtWidgets.QTableWidget(self.frame_2)
        self.tableResult.setObjectName("tableResult")
        self.tableResult.setColumnCount(0)
        self.tableResult.setRowCount(0)
        self.verticalLayout.addWidget(self.tableResult)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSaveRe = QtWidgets.QPushButton(self.frame_4)
        self.btnSaveRe.setMinimumSize(QtCore.QSize(0, 0))
        self.btnSaveRe.setObjectName("btnSaveRe")
        self.horizontalLayout.addWidget(self.btnSaveRe)
        self.btnClearRe = QtWidgets.QPushButton(self.frame_4)
        self.btnClearRe.setObjectName("btnClearRe")
        self.horizontalLayout.addWidget(self.btnClearRe)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_7.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.threadpool = QThreadPool()
        ## Event 
        self.load_data()
        self.btnOpen.clicked.connect(self.open_file)
        self.btnSave.clicked.connect(self.save_file)
        self.btnSequent.clicked.connect(self.sequential)
        self.btnParallel.clicked.connect(self.parallel)
        self.btnSaveRe.clicked.connect(self.save_result)
        self.btnClearRe.clicked.connect(self.clear_result)
    
    def load_data(self):
        
        # Load Combobox
        listCipher = ["Ceasar","Vigenere"]
        self.cboCipher.addItems(listCipher)
        # Load Spin Box
        self.spinThread.setMinimum(2)
        self.spinThread.setMaximum(2048)
        self.spinThread.setValue(2)
        # Load Table Result
        self.tableResult.setColumnCount(4)
        self.tableResult.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = ["Cipher","Type","Sequential","Parallel"]
        for x in range(4):
            item = QTableWidgetItem()
            item.setText(header[x])
            self.tableResult.setHorizontalHeaderItem(x, item)
        self.tableResult.horizontalHeader().setStretchLastSection(True)
            
    
    def open_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self,"Open File","","Text files (*.txt)")
        self.file_open = fileName[0]

    def save_file(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"","Text files (*.txt)")
        self.file_save = fileName[0]

    def sequential(self):
        if(len(self.file_open) > 0 and len(self.file_save) > 0):
            cipher = self.cboCipher.currentText()
            encrypt = self.radioEncrypt.isChecked()
            key = self.dialogKey()
            if(key != None):
                worker = Worker(handle.sequential,cipher=cipher,encrypt=encrypt,key=key,input_file=self.file_open,output_file=self.file_save) # Any other args, kwargs are passed to the run function
                worker.signals.result.connect(self.print_output_sequential)
                worker.signals.finished.connect(self.thread_complete)
                worker.signals.progress.connect(self.progress_fn_sequential)
                # time = handle.sequential(cipher,encrypt,key,self.file_open,self.file_save)
                # Execute
                self.threadpool.start(worker)
                
            else:
                msg = QMessageBox() 
                msg.setText("Require choose key for cipher!!!")
                msg.exec()
        else:
            msg = QMessageBox() 
            msg.setText("Require choose input file and output file!!!")
            msg.exec()
            
    def parallel(self):
        if(len(self.file_open) > 0 and len(self.file_save) > 0):
            thread = self.spinThread.value()
            cipher = self.cboCipher.currentText()
            encrypt = self.radioEncrypt.isChecked()
            key = self.dialogKey()
            if(key != None):
                worker = Worker(handle.parallel,cipher=cipher,encrypt=encrypt,key=key,input_file=self.file_open,output_file=self.file_save,thread=thread) # Any other args, kwargs are passed to the run function
                worker.signals.result.connect(self.print_output_parallel)
                worker.signals.finished.connect(self.thread_complete)
                worker.signals.progress.connect(self.progress_fn_parallel)
                # time = handle.parallel(cipher,encrypt,key,self.file_open,self.file_save,thread)
                # self.lineParallel.setText(str(time)+ " ms")
                self.threadpool.start(worker)
            else:
                msg = QMessageBox() 
                msg.setText("Require choose key for cipher!!!")
                msg.exec()
        else:
            msgBox = QMessageBox() 
            msgBox.setText("Require choose input file and output file!!!")
            msgBox.exec()
    
    def save_result(self):
        cipher = self.cboCipher.currentText()
        type = "Encrypt" if self.radioEncrypt.isChecked() else "Decrypt"
        sequential = self.lineSequent.text()
        parallel = self.lineParallel.text()
        if len(sequential.strip()) > 0 and len(parallel.strip()) > 0 :
            rowPosition = self.tableResult.rowCount()
            self.tableResult.insertRow(rowPosition)
            self.tableResult.setItem(rowPosition , 0, QTableWidgetItem(cipher))
            self.tableResult.setItem(rowPosition , 1, QTableWidgetItem(type))
            self.tableResult.setItem(rowPosition , 2, QTableWidgetItem(sequential))
            self.tableResult.setItem(rowPosition , 3, QTableWidgetItem(parallel))  
            self.open_file = None
            self.save_file = None
            self.lineSequent.setText("")
            self.lineParallel.setText("")
        else:
            msg = QMessageBox() 
            msg.setText("You must handle all before save result!!!")
            msg.exec()     
        
    def clear_result(self):
        self.tableResult.setRowCount(0)

            
    def dialogKey(self):
        cipher = self.cboCipher.currentText()
        if(cipher == "Ceasar"):
            key, okPressed = QInputDialog.getInt(self, "Set key for "+cipher+" Cipher","Value:", 0, 0, 204, 1)
        elif (cipher == "Vigenere"):
            x = open(self.file_open, 'r').read()
            key, okPressed = QInputDialog.getText(self, "Set key for "+cipher+" Cipher","Value:", QLineEdit.Normal, "")
            if(len(key) > len(x)):
                return None
        if okPressed and len(str(key))>0:
            return key
        else:
            return None               
        
    def progress_fn_sequential(self, n):
        self.lineSequent.setText(str(n)+ "%")
    
    def progress_fn_parallel(self, n):
         self.lineParallel.setText(str(n)+ "%")       


    def print_output_sequential(self, s):
        self.lineSequent.setText(str(s))
        
    def print_output_parallel(self, s):
        self.lineParallel.setText(str(s))

    def thread_complete(self):
        print("THREAD COMPLETE!")
        # self.lineSequent.setText(str(time)+ " ms")
        
       

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Parallel Encrypt"))
        self.lblTitle.setText(_translate("Form", "PARALLEL ENCRYPT"))
        self.grbxFile.setTitle(_translate("Form", "File"))
        self.btnOpen.setText(_translate("Form", "Open"))
        self.btnSave.setText(_translate("Form", "Save"))
        self.grbxType.setTitle(_translate("Form", "Type"))
        self.radioEncrypt.setText(_translate("Form", "Encrypt"))
        self.radioDecrypt.setText(_translate("Form", "Decrypt"))
        self.grbxCipher.setTitle(_translate("Form", "Type of Cipher"))
        self.grbxSequent.setTitle(_translate("Form", "Sequential"))
        self.btnSequent.setText(_translate("Form", "Sequential"))
        self.grbxParallel.setTitle(_translate("Form", "Parallel"))
        self.btnParallel.setText(_translate("Form", "Parallel"))
        self.btnSaveRe.setText(_translate("Form", "Save Result"))
        self.btnClearRe.setText(_translate("Form", "Clear Result"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
    