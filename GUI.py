# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UInew.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.insert(0, 'JPEG_ENCODER')
from utils import *
dict_Alg={0:"JPEG encoder with Huffman Coding",1:"JPEG encoder LZW Coding",
                2: "JPEG encoder Arithmetic Coding",3:"LZW Lossless Coding"}
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Bien khoi tao rieng
        self.fileNameImg=""
        self.fileNameTest=""
        self.flagalgorithm = 0 # 0 - MultinomialNB, 1 - BernoulliNB ,2 -KNeighborsClassifier, 3 - DecisionTreeClassifier 
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 531)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background:rgb(230, 230, 230)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.left_window = QtWidgets.QWidget(self.centralwidget)
        self.left_window.setGeometry(QtCore.QRect(0, 0, 301, 531))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.left_window.setFont(font)
        self.left_window.setStyleSheet("background:rgb(50, 67, 71);\n"
"color:white;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.left_window.setObjectName("left_window")
        self.tabWidget = QtWidgets.QTabWidget(self.left_window)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 271, 211))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.train_tab = QtWidgets.QWidget()
        self.train_tab.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.train_tab.setFont(font)
        self.train_tab.setStyleSheet("")
        self.train_tab.setObjectName("train_tab")
        self.label_filetrain = QtWidgets.QLabel(self.train_tab)
        self.label_filetrain.setGeometry(QtCore.QRect(10, 10, 221, 16))
        self.label_filetrain.setObjectName("label_filetrain")
        self.btn_openfileimg = QtWidgets.QPushButton(self.train_tab)
        self.btn_openfileimg.setGeometry(QtCore.QRect(70, 70, 111, 31))
        self.btn_openfileimg.setObjectName("btn_openfileimg")
        self.label_train = QtWidgets.QLabel(self.train_tab)
        self.label_train.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.label_train.setObjectName("label_train")
        self.btn_train = QtWidgets.QPushButton(self.train_tab)
        self.btn_train.setGeometry(QtCore.QRect(70, 140, 111, 31))
        self.btn_train.setObjectName("btn_train")
        self.line_train = QtWidgets.QLineEdit(self.train_tab)
        self.line_train.setGeometry(QtCore.QRect(10, 40, 221, 20))
        self.line_train.setObjectName("line_train")
        self.tabWidget.addTab(self.train_tab, "")
        self.test_tab = QtWidgets.QWidget()
        self.test_tab.setEnabled(True)
        self.test_tab.setStyleSheet("")
        self.test_tab.setObjectName("test_tab")
        self.line_test = QtWidgets.QLineEdit(self.test_tab)
        self.line_test.setGeometry(QtCore.QRect(10, 40, 221, 20))
        self.line_test.setObjectName("line_test")
        self.widget_2 = QtWidgets.QWidget(self.test_tab)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 241, 171))
        self.widget_2.setObjectName("widget_2")
        self.btn_testfile = QtWidgets.QPushButton(self.widget_2)
        self.btn_testfile.setGeometry(QtCore.QRect(40, 120, 141, 23))
        self.btn_testfile.setObjectName("btn_testfile")
        self.btn_openfiletest = QtWidgets.QPushButton(self.widget_2)
        self.btn_openfiletest.setGeometry(QtCore.QRect(50, 40, 111, 23))
        self.btn_openfiletest.setObjectName("btn_openfiletest")
        self.label_train_2 = QtWidgets.QLabel(self.widget_2)
        self.label_train_2.setGeometry(QtCore.QRect(20, 80, 151, 16))
        self.label_train_2.setObjectName("label_train_2")
        self.label_filetrain_2 = QtWidgets.QLabel(self.widget_2)
        self.label_filetrain_2.setGeometry(QtCore.QRect(20, 0, 221, 20))
        self.label_filetrain_2.setObjectName("label_filetrain_2")
        self.widget_3 = QtWidgets.QWidget(self.test_tab)
        self.widget_3.setGeometry(QtCore.QRect(0, 40, 221, 111))
        self.widget_3.setVisible(False)
        self.widget_3.setObjectName("widget_3")
        self.linetest = QtWidgets.QLineEdit(self.widget_3)
        self.linetest.setGeometry(QtCore.QRect(10, 40, 201, 20))
        self.linetest.setObjectName("linetest")
        self.btn_testline = QtWidgets.QPushButton(self.widget_3)
        self.btn_testline.setGeometry(QtCore.QRect(70, 70, 75, 23))
        self.btn_testline.setObjectName("btn_testline")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.test_tab, "")
        self.setting_tab = QtWidgets.QWidget()
        self.setting_tab.setEnabled(True)
        self.setting_tab.setStyleSheet("")
        self.setting_tab.setObjectName("setting_tab")
        self.groupBox_4 = QtWidgets.QGroupBox(self.setting_tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 221, 181))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setChecked(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self._flagHM = QtWidgets.QRadioButton(self.groupBox_4)
        self._flagHM.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self._flagHM.setChecked(True)
        self._flagHM.setObjectName("_flagHM")
        self._flagLZW = QtWidgets.QRadioButton(self.groupBox_4)
        self._flagLZW.setGeometry(QtCore.QRect(10, 50, 201, 17))
        self._flagLZW.setObjectName("_flagLZW")
        self._flagARTH = QtWidgets.QRadioButton(self.groupBox_4)
        self._flagARTH.setGeometry(QtCore.QRect(10, 70, 201, 17))
        self._flagARTH.setObjectName("_flagARTH")
        self._flagLZW_ll = QtWidgets.QRadioButton(self.groupBox_4)
        self._flagLZW_ll.setGeometry(QtCore.QRect(10, 130, 201, 17))
        self._flagLZW_ll.setObjectName("_flagLZW_ll")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(0, 100, 161, 17))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.setting_tab, "")
        self.widget_thongtinnhom = QtWidgets.QTextBrowser(self.left_window)
        self.widget_thongtinnhom.setGeometry(QtCore.QRect(10, 340, 256, 161))
        self.widget_thongtinnhom.setObjectName("widget_thongtinnhom")
        self.widget_status = QtWidgets.QWidget(self.left_window)
        self.widget_status.setGeometry(QtCore.QRect(10, 240, 251, 80))
        self.widget_status.setObjectName("widget_status")
        self.label_trangthai = QtWidgets.QLabel(self.widget_status)
        self.label_trangthai.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_trangthai.setObjectName("label_trangthai")
        self.status_program = QtWidgets.QLabel(self.widget_status)
        self.status_program.setGeometry(QtCore.QRect(10, 30, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.status_program.setFont(font)
        self.status_program.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 172, 5)")
        self.status_program.setObjectName("status_program")

        self.groupBox_output = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_output.setGeometry(QtCore.QRect(310, 280, 371, 245))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_output.setFont(font)
        self.groupBox_output.setObjectName("groupBox_output")
        self.area_output = QtWidgets.QTextBrowser(self.groupBox_output)
        self.area_output.setGeometry(QtCore.QRect(10, 30, 350, 205))
        self.area_output.setStyleSheet("background:rgb(255, 255, 255)")
        self.area_output.setObjectName("area_output")
        
        self.groupBox_info_img = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_info_img.setGeometry(QtCore.QRect(310, 10, 371, 130))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_info_img.setFont(font)
        self.groupBox_info_img.setObjectName("groupBox_info_img")
        self.area_info_img = QtWidgets.QTextBrowser(self.groupBox_info_img)
        self.area_info_img.setGeometry(QtCore.QRect(8, 28, 355, 95))
        self.area_info_img.setStyleSheet("background:rgb(255, 255, 255)")
        self.area_info_img.setObjectName("area_info_img")
        ##
        self.groupBox_info_decode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_info_decode.setGeometry(QtCore.QRect(310, 145, 371, 130))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_info_decode.setFont(font)
        self.groupBox_info_decode.setObjectName("groupBox_info_decode")
        self.area_info_decode = QtWidgets.QTextBrowser(self.groupBox_info_decode)
        self.area_info_decode.setGeometry(QtCore.QRect(8, 28, 355, 95))
        self.area_info_decode.setStyleSheet("background:rgb(255, 255, 255)")
        self.area_info_decode.setObjectName("area_info_decode")

        self.label_img_before = QtWidgets.QLabel(self.centralwidget)
        self.label_img_before.setGeometry(QtCore.QRect(750, 10, 221, 20))
        self.label_img_before.setObjectName("label_img_before")
        self.label_img_before.setFont(font)
        self.img_before = QtWidgets.QLabel(self.centralwidget)
        self.img_before.setGeometry(QtCore.QRect(750, 30, 300, 400))
        self.img_before.setAlignment(QtCore.Qt.AlignTop)

        
        self.label_img_after = QtWidgets.QLabel(self.centralwidget)
        self.label_img_after.setGeometry(QtCore.QRect(750, 265, 221, 20))
        self.label_img_after.setObjectName("label_img_after")
        self.label_img_after.setFont(font)
        self.img_after = QtWidgets.QLabel(self.centralwidget)
        self.img_after.setGeometry(QtCore.QRect(750, 290, 320, 400))
        self.img_after.setAlignment(QtCore.Qt.AlignTop)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_toggle(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project compression and decompress"))
        self.label_filetrain.setText(_translate("MainWindow", "Chọn ảnh cần nén"))
        self.btn_openfileimg.setText(_translate("MainWindow", "Open File"))
        self.label_train.setText(_translate("MainWindow", "Nhấn để nén"))
        self.btn_train.setText(_translate("MainWindow", "Start Compress"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.train_tab), _translate("MainWindow", "Compress"))
        self.btn_testfile.setText(_translate("MainWindow", "Start Decompress"))
        self.btn_openfiletest.setText(_translate("MainWindow", "Open File Nén"))
        self.label_train_2.setText(_translate("MainWindow", "Nhấn để giải nén"))
        self.label_filetrain_2.setText(_translate("MainWindow", "Chọn file nén"))
        self.btn_testline.setText(_translate("MainWindow", "Test Data"))
        self.label_5.setText(_translate("MainWindow", "Input Text:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_tab), _translate("MainWindow", "Decompress"))
        self.groupBox_4.setTitle(_translate("MainWindow", "JPEG encoding with:"))
        self._flagHM.setText(_translate("MainWindow", "Huffman Coding"))
        self._flagLZW.setText(_translate("MainWindow", "LZW Coding"))
        self._flagARTH.setText(_translate("MainWindow", "Arithmetic Coding"))
        self._flagLZW_ll.setText(_translate("MainWindow", "LZW Coding"))
        self.label.setText(_translate("MainWindow", "Lossless Compression:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_tab), _translate("MainWindow", "Setting"))
        self.widget_thongtinnhom.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Môn học:            <span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-weight:600; color:#34d9d4;\">Tính toán đa phương tiên</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; color:#ffffff;\">Lớp: </span><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-weight:600; color:#34d9d4;\">CS232.J11.KHTN</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nhóm thực hiện:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; background-color:transparent;\">NGUYỄN MINH DŨNG - 15520138</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-size:8pt; background-color:transparent;\">TRỊNH HOÀNG NGỌC -15520556</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-size:8pt; background-color:transparent;\">NGUYỄN QUỐC DANH - 15520092</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-size:8pt; background-color:transparent;\">NGUYỄN ĐỨC ANH - 15520021</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-size:8pt;\">VŨ LÊ HOÀNG MINH - 15520498</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_trangthai.setText(_translate("MainWindow", "TRẠNG THÁI:"))
        self.status_program.setText(_translate("MainWindow", "Bắt Đầu"))
        self.groupBox_output.setTitle(_translate("MainWindow", "Log"))
        self.groupBox_info_img.setTitle(_translate("MainWindow", "Info Original Image"))
        self.groupBox_info_decode.setTitle(_translate("MainWindow", "Info Compressed Image"))
        self.label_img_before.setText(_translate("MainWindow", "Ảnh ban đầu "))
        self.label_img_after.setText(_translate("MainWindow", "Ảnh sau khi nén "))

    def btn_toggle(self, MainWindow):
        self.btn_openfileimg.clicked.connect(self.openfiletrain)
        self.btn_openfiletest.clicked.connect(self.openfiletest)
        self.btn_train.clicked.connect(self.doTrain)
        self.btn_testfile.clicked.connect(self.doTestFile)
        self._flagHM.toggled.connect(lambda:self.setalgorithm(0))
        self._flagLZW.toggled.connect(lambda:self.setalgorithm(1))
        self._flagARTH.toggled.connect(lambda:self.setalgorithm(2))
        self._flagLZW_ll.toggled.connect(lambda:self.setalgorithm(3))
    def setalgorithm(self,flagalg):
        self.flagalgorithm=flagalg

    def printInfoFile(self,filepath):
        size_file= os.path.getsize(filepath)/1000
        output_info = "Info Fileload:\nPath: {} \nSize: {} KB\n===============================".format(filepath[filepath.rfind('/')+1:],size_file)
        return output_info
    def printAlg(self,flag_alg):
        return "Algorithm : {} \n===============================".format(dict_Alg[flag_alg])
    def info_img(self,path,flag_alg):
        img = cv2.imread(path)
        try: 
            if img == None:
                output_info = "Please choose file image"
                return output_info
        except:
            h,w = img.shape[:2]
            size_img= os.path.getsize(path)/1000
            output_info = "Info Image:\nPath: {} \nSize: {} KB \nWidthxHeight:{}x{}".format(path[path.rfind('/')+1:],size_img,w,h)
            return output_info

    def openfiletrain(self):
        self.line_train.setText(self.setExistingDirectory())
        self.status_program.setText("Đã chọn File ảnh")
        print(self.line_train.text())
        self.area_info_img.setText("")
        self.area_info_img.append(self.printAlg(self.flagalgorithm))
        self.area_info_img.append(self.info_img(self.line_train.text(),self.flagalgorithm))
        pixmap = QtGui.QPixmap(self.line_train.text())
        self.img_before.setPixmap(pixmap.scaled(300, 250, QtCore.Qt.KeepAspectRatio))
        
    def openfiletest(self):
        self.line_test.setText(self.setExistingDirectory())
        self.area_info_decode.setText("")
        self.area_info_decode.append(self.printInfoFile(self.line_test.text()))
        self.status_program.setText("Đã chọn File Nén")
        print(self.line_train.text())
    def doTrain(self):
        print(self.line_train.text())
        print(self.flagalgorithm)
        self.area_output.setText("")
        if(self.line_train.text()==''):
            self.status_program.setText('Vui lòng chọn file ảnh')
        else:
            # Thực hiện hàm train dữ liệu với biến truyền vào file name là self.dirfile
             #Thay bằng hàm
            result = compress(self.line_train.text(),self.flagalgorithm)
            self.status_program.setText('Đã Nén xong')
            self.area_output.append(result)
            print("Nén")
            return
    def setExistingDirectory(self): 
        filename = QtWidgets.QFileDialog.getOpenFileName()[0]
        return(filename)          

    def doTestFile(self):
        self.area_info_decode.append(self.printAlg(self.flagalgorithm))
        path_img,result =decompress(self.line_test.text(),self.flagalgorithm)
        self.area_info_decode.append(self.info_img(path_img,self.flagalgorithm))
        self.status_program.setText("Đã giải nén xong")
        self.area_output.append(result)
        pixmap = QtGui.QPixmap(path_img)
        self.img_after.setPixmap(pixmap.scaled(300, 250, QtCore.Qt.KeepAspectRatio))
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

