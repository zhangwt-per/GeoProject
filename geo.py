# coding: UTF-8
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTextCodec, QStringList
from PyQt4.QtGui import QMainWindow, QStringListModel
import veti
import map_show
import value_base

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QMainWindow):
    left_strlist = QStringList()

    left_strm = QStringListModel(left_strlist)

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        QTextCodec.setCodecForCStrings(QTextCodec.codecForName("utf-8"))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(561, 353)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.evalution_area_edit = QtGui.QLineEdit(self.centralwidget)
        self.evalution_area_edit.setGeometry(QtCore.QRect(110, 40, 113, 21))
        self.evalution_area_edit.setObjectName(_fromUtf8("evalution_area_edit"))
        self.evalution_area_edit.setText(u'jx_2调镇界')
        self.evalution_area_label = QtGui.QLabel(self.centralwidget)
        self.evalution_area_label.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.evalution_area_label.setObjectName(_fromUtf8("evalution_area_label"))
        self.evalution_id_edit = QtGui.QLineEdit(self.centralwidget)
        self.evalution_id_edit.setGeometry(QtCore.QRect(110, 70, 113, 21))
        self.evalution_id_edit.setObjectName(_fromUtf8("evalution_edit_edit"))
        self.evalution_id_edit.setText('OID@')
        self.area_id_label = QtGui.QLabel(self.centralwidget)
        self.area_id_label.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.area_id_label.setObjectName(_fromUtf8("area_id_label"))
        self.input_button = QtGui.QPushButton(self.centralwidget)
        self.input_button.setGeometry(QtCore.QRect(230, 40, 93, 21))
        self.input_button.setObjectName(_fromUtf8("input_button"))
        self.connect(self.input_button, QtCore.SIGNAL('clicked()'), self.input_dir)

        self.input_shp_button = QtGui.QPushButton(self.centralwidget)
        self.input_shp_button.setGeometry(QtCore.QRect(230, 100, 93, 21))
        self.input_shp_button.setObjectName(_fromUtf8("input_button"))
        self.connect(self.input_shp_button, QtCore.SIGNAL('clicked()'), self.input_shp_dir)

        self.input_label = QtGui.QTextBrowser(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(340, 40, 180, 21))
        self.input_label.setObjectName(_fromUtf8("input_label"))

        self.output_label = QtGui.QTextBrowser(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(340, 70, 180, 21))
        self.output_label.setObjectName(_fromUtf8("output_label"))

        self.input_shp_label = QtGui.QTextBrowser(self.centralwidget)
        self.input_shp_label.setGeometry(QtCore.QRect(340, 100, 180, 21))
        self.input_shp_label.setObjectName(_fromUtf8("input_shp_label"))

        self.output_button = QtGui.QPushButton(self.centralwidget)
        self.output_button.setGeometry(QtCore.QRect(230, 70, 93, 21))
        self.output_button.setObjectName(_fromUtf8("output_button"))

        self.connect(self.output_button, QtCore.SIGNAL('clicked()'), self.output_dir)
        self.input_area_list = QtGui.QListView(self.centralwidget)
        self.input_area_list.setGeometry(QtCore.QRect(10, 170, 111, 141))
        self.input_area_list.setObjectName(_fromUtf8("input_area_list"))
        self.input_area_button = QtGui.QPushButton(self.centralwidget)
        self.input_area_button.setGeometry(QtCore.QRect(130, 140, 51, 21))
        self.input_area_button.setObjectName(_fromUtf8("input_area_button"))
        self.connect(self.input_area_button, QtCore.SIGNAL('clicked()'), self.input_area)
        self.evalution_edit_edit_2 = QtGui.QLineEdit(self.centralwidget)
        self.evalution_edit_edit_2.setGeometry(QtCore.QRect(10, 140, 113, 21))
        self.evalution_edit_edit_2.setObjectName(_fromUtf8("evalution_edit_edit_2"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.agr_edit = QtGui.QLineEdit(self.centralwidget)
        self.agr_edit.setGeometry(QtCore.QRect(230, 140, 151, 21))
        self.agr_edit.setObjectName(_fromUtf8("agr_edit"))
        self.agr_edit.setText("11, 12")
        self.agr_label = QtGui.QLabel(self.centralwidget)
        self.agr_label.setGeometry(QtCore.QRect(190, 140, 41, 21))
        self.agr_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.agr_label.setObjectName(_fromUtf8("agr_label"))

        self.frt_label = QtGui.QLabel(self.centralwidget)
        self.frt_label.setGeometry(QtCore.QRect(190, 170, 41, 21))
        self.frt_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.frt_label.setObjectName(_fromUtf8("frt_label"))
        self.frt_edit = QtGui.QLineEdit(self.centralwidget)
        self.frt_edit.setGeometry(QtCore.QRect(230, 170, 151, 21))
        self.frt_edit.setObjectName(_fromUtf8("frt_edit"))
        self.frt_edit.setText("21, 22, 23, 24")

        self.grs_label = QtGui.QLabel(self.centralwidget)
        self.grs_label.setGeometry(QtCore.QRect(190, 200, 41, 21))
        self.grs_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.grs_label.setObjectName(_fromUtf8("grs_label"))
        self.grs_edit = QtGui.QLineEdit(self.centralwidget)
        self.grs_edit.setGeometry(QtCore.QRect(230, 200, 151, 21))
        self.grs_edit.setObjectName(_fromUtf8("grs_edit"))
        self.grs_edit.setText("31, 32, 33")

        self.wat_label = QtGui.QLabel(self.centralwidget)
        self.wat_label.setGeometry(QtCore.QRect(190, 230, 41, 21))
        self.wat_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.wat_label.setObjectName(_fromUtf8("wat_label"))
        self.wat_edit = QtGui.QLineEdit(self.centralwidget)
        self.wat_edit.setGeometry(QtCore.QRect(230, 230, 151, 21))
        self.wat_edit.setObjectName(_fromUtf8("wat_edit"))
        self.wat_edit.setText("41, 43, 46")

        self.bul_label = QtGui.QLabel(self.centralwidget)
        self.bul_label.setGeometry(QtCore.QRect(190, 260, 41, 21))
        self.bul_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.bul_label.setObjectName(_fromUtf8("bul_label"))
        self.bul_edit = QtGui.QLineEdit(self.centralwidget)
        self.bul_edit.setGeometry(QtCore.QRect(230, 260, 151, 21))
        self.bul_edit.setObjectName(_fromUtf8("bul_edit"))
        self.bul_edit.setText("51, 52, 53")

        self.uus_label = QtGui.QLabel(self.centralwidget)
        self.uus_label.setGeometry(QtCore.QRect(190, 290, 41, 21))
        self.uus_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.uus_label.setObjectName(_fromUtf8("uus_label"))
        self.uus_edit = QtGui.QLineEdit(self.centralwidget)
        self.uus_edit.setGeometry(QtCore.QRect(230, 290, 151, 21))
        self.uus_edit.setObjectName(_fromUtf8("uus_edit"))
        self.uus_edit.setText("64")

        self.start_button = QtGui.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(350, 10, 91, 28))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.connect(self.start_button, QtCore.SIGNAL('clicked()'), self.start)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(10, 318, 500, 30)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def input_area(self):
        if unicode(self.evalution_edit_edit_2.text()) != "":
            index = self.left_strm.rowCount()
            self.left_strm.insertRow(index)
            self.left_strm.setData(self.left_strm.index(index), unicode(self.evalution_edit_edit_2.text()))
            self.evalution_edit_edit_2.clear()
            self.input_area_list.setModel(self.left_strm)

    def input_dir(self):
        tmp_dir = QtGui.QFileDialog.getExistingDirectory()
        if len(tmp_dir) > 0:
            value_base.input_dir = tmp_dir
        self.input_label.setText(tmp_dir)
        value_base.input_dir = tmp_dir

    def input_shp_dir(self):
        tmp_dir = QtGui.QFileDialog.getOpenFileName()
        if len(tmp_dir) > 0:
            value_base.input_shp_dir = tmp_dir
        self.input_shp_label.setText(tmp_dir)
        value_base.input_shp_dir = tmp_dir

    def output_dir(self):
        tmp_dir = QtGui.QFileDialog.getExistingDirectory()
        if len(tmp_dir) > 0:
            value_base.output_dir = tmp_dir
        self.output_label.setText(tmp_dir)
        value_base.output_dir = tmp_dir

    def start(self):
        for i in self.left_strm.stringList():
            value_base.inital_years.append(unicode(i))
        self.step = 0
        agr_list = list(map(int, self.agr_edit.text().split(",")))
        frt_list = list(map(int, self.frt_edit.text().split(",")))
        grs_list = list(map(int, self.grs_edit.text().split(",")))
        wat_list = list(map(int, self.wat_edit.text().split(",")))
        bul_list = list(map(int, self.bul_edit.text().split(",")))
        uus_list = list(map(int, self.uus_edit.text().split(",")))
        value_base.codes = {
            'AGR': agr_list,
            'FRT': frt_list,
            'GRS': grs_list,
            'WAT': wat_list,
            'BUL': bul_list,
            'UUS': uus_list
        }
        value_base.regions = unicode(self.evalution_area_edit.text())
        value_base.idField = unicode(self.evalution_id_edit.text())
        veti.veti_input(self)

        self.hide()
        self.ui = map_show.mapshow()
        self.ui.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "村镇生态环境指数计算", None))
        self.evalution_area_label.setText(_translate("MainWindow", "设置评价区域：", None))
        self.area_id_label.setText(_translate("MainWindow", "区域ID和名称：", None))
        self.input_button.setText(_translate("MainWindow", "选择输入", None))
        self.input_shp_button.setText(_translate("MainWindow", "选择shp", None))
        self.input_label.setText(_translate("MainWindow", "选择输入文件", None))
        self.input_shp_label.setText(_translate("MainWindow", "选择shp文件", None))
        self.output_label.setText(_translate("MainWindow", "选择输出文件", None))
        self.output_button.setText(_translate("MainWindow", "选择输出", None))
        self.input_area_button.setText(_translate("MainWindow", "输入", None))
        self.label.setText(_translate("MainWindow", "评价区域设置", None))
        self.label_2.setText(_translate("MainWindow", "地区时段设置", None))
        self.agr_label.setText(_translate("MainWindow", "AGR:", None))
        self.frt_label.setText(_translate("MainWindow", "FRT:", None))
        self.grs_label.setText(_translate("MainWindow", "GRS:", None))
        self.wat_label.setText(_translate("MainWindow", "WAT:", None))
        self.bul_label.setText(_translate("MainWindow", "BUL:", None))
        self.uus_label.setText(_translate("MainWindow", "UUS:", None))
        self.start_button.setText(_translate("MainWindow", "运 行", None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = Ui_MainWindow()
    myapp.show()
    app.exec_()
