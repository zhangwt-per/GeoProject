# -*- coding: utf-8 -*-
import code
import locale
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTextCodec, QStringList
from PyQt4.QtGui import QStringListModel, QMessageBox

import data_map
import value_base
from geo_map import create_data_map

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


class mapshow(QtGui.QMainWindow):
    year_left_qslm = QStringListModel(value_base.inital_years)
    year_right_qslm = QStringListModel()
    index_left_qslm = QStringListModel(value_base.inital_indexs)
    index_right_qslm = QStringListModel()
    area_left_qslm = QStringListModel(value_base.inital_areas)
    area_right_qslm = QStringListModel()

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QTextCodec.setCodecForTr(QTextCodec.codecForName("system"))
        QTextCodec.setCodecForCStrings(QTextCodec.codecForName("system"))
        QTextCodec.setCodecForLocale(QTextCodec.codecForName("system"))

    def setupUi(self, MainWindow):
        self.qslm_reset()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(980, 700)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 700, 700))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 72, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 72, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 480, 72, 25))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.change_combo = QtGui.QComboBox(self.centralwidget)
        self.change_combo.setGeometry(QtCore.QRect(10, 20, 120, 25))
        self.change_combo.setObjectName(_fromUtf8("change_combo"))
        self.change_combo.addItems(value_base.map_type)

        self.output_btn = QtGui.QPushButton(self.centralwidget)
        self.output_btn.setGeometry(QtCore.QRect(140, 20, 120, 25))
        self.output_btn.setObjectName(_fromUtf8("output_btn"))
        self.output_btn.clicked.connect(self.output)

        self.year_left_list = QtGui.QListView(self.centralwidget)
        self.year_left_list.setGeometry(QtCore.QRect(10, 90, 120, 150))
        self.year_left_list.setObjectName(_fromUtf8("year_left_list"))
        self.year_left_list.setModel(self.year_left_qslm)
        self.year_left_list.doubleClicked.connect(self.year_toright)

        self.year_right_list = QtGui.QListView(self.centralwidget)
        self.year_right_list.setGeometry(QtCore.QRect(140, 90, 120, 150))
        self.year_right_list.setObjectName(_fromUtf8("year_right_list"))
        self.year_right_list.setModel(self.year_right_qslm)
        self.year_right_list.doubleClicked.connect(self.year_toleft)

        self.index_left_list = QtGui.QListView(self.centralwidget)
        self.index_left_list.setGeometry(QtCore.QRect(10, 300, 120, 150))
        self.index_left_list.setObjectName(_fromUtf8("index_left_list"))
        self.index_left_list.setModel(self.index_left_qslm)
        self.index_left_list.doubleClicked.connect(self.index_toright)

        self.index_right_list = QtGui.QListView(self.centralwidget)
        self.index_right_list.setGeometry(QtCore.QRect(140, 300, 120, 150))
        self.index_right_list.setObjectName(_fromUtf8("index_right_list"))
        self.index_right_list.setModel(self.index_right_qslm)
        self.index_right_list.doubleClicked.connect(self.index_toleft)

        self.area_left_list = QtGui.QListView(self.centralwidget)
        self.area_left_list.setGeometry(QtCore.QRect(10, 510, 120, 150))
        self.area_left_list.setObjectName(_fromUtf8("area_left_list"))
        self.area_left_list.setModel(self.area_left_qslm)
        self.area_left_list.doubleClicked.connect(self.area_toright)

        self.area_right_list = QtGui.QListView(self.centralwidget)
        self.area_right_list.setGeometry(QtCore.QRect(140, 510, 120, 150))
        self.area_right_list.setObjectName(_fromUtf8("area_right_list"))
        self.area_right_list.setModel(self.area_right_qslm)
        self.area_right_list.doubleClicked.connect(self.area_toleft)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def qslm_reset(self):
        self.year_left_qslm.setStringList(value_base.inital_years)
        self.year_right_qslm.removeRows(0, self.year_right_qslm.rowCount())
        self.index_left_qslm.setStringList(value_base.inital_indexs)
        self.index_right_qslm.removeRows(0, self.index_right_qslm.rowCount())
        self.area_left_qslm.setStringList(value_base.inital_areas)
        self.area_right_qslm.removeRows(0, self.area_right_qslm.rowCount())
        value_base.current_indexs = []
        value_base.current_areas = []
        value_base.current_years = []

    def inspect_qslm(self):
        if self.year_right_qslm.rowCount() > 10 or self.index_right_qslm.rowCount() > 10 or self.area_right_qslm.rowCount() < 0 or self.year_right_qslm.rowCount() < 0 or self.index_right_qslm.rowCount() < 0 or self.area_right_qslm.rowCount() < 0:
            QMessageBox.information(self,
                                    u"Tips",
                                    u"数据地图年份、指标、地图数量都需小于10")
            return True
        else:
            return False

    def year_toright(self):
        row = self.year_left_list.currentIndex().row()
        left_row = self.year_left_qslm.index(row).row()
        left_text = self.year_left_qslm.index(row).data()
        right_row = self.year_right_qslm.rowCount()
        self.year_left_qslm.removeRow(left_row)
        self.year_right_qslm.insertRow(right_row)
        self.year_right_qslm.setData(self.year_right_qslm.index(right_row), left_text)

    def year_toleft(self):
        row = self.year_right_list.currentIndex().row()
        right_row = self.year_right_qslm.index(row).row()
        right_text = self.year_right_qslm.index(row).data()
        left_row = self.year_left_qslm.rowCount()
        self.year_right_qslm.removeRow(right_row)
        self.year_left_qslm.insertRow(left_row)
        self.year_left_qslm.setData(self.year_left_qslm.index(left_row), right_text)

    def index_toright(self):
        row = self.index_left_list.currentIndex().row()
        left_row = self.index_left_qslm.index(row).row()
        left_text = self.index_left_qslm.index(row).data()
        right_row = self.index_right_qslm.rowCount()
        self.index_left_qslm.removeRow(left_row)
        self.index_right_qslm.insertRow(right_row)
        self.index_right_qslm.setData(self.index_right_qslm.index(right_row), left_text)

    def index_toleft(self):
        row = self.index_right_list.currentIndex().row()
        right_row = self.index_right_qslm.index(row).row()
        right_text = self.index_right_qslm.index(row).data()
        left_row = self.index_left_qslm.rowCount()
        self.index_right_qslm.removeRow(right_row)
        self.index_left_qslm.insertRow(left_row)
        self.index_left_qslm.setData(self.index_left_qslm.index(left_row), right_text)

    def area_toright(self):
        row = self.area_left_list.currentIndex().row()
        left_row = self.area_left_qslm.index(row).row()
        left_text = self.area_left_qslm.index(row).data()
        right_row = self.area_right_qslm.rowCount()
        self.area_left_qslm.removeRow(left_row)
        self.area_right_qslm.insertRow(right_row)
        self.area_right_qslm.setData(self.area_right_qslm.index(right_row), left_text)

    def area_toleft(self):
        row = self.area_right_list.currentIndex().row()
        right_row = self.area_right_qslm.index(row).row()
        right_text = self.area_right_qslm.index(row).data()
        left_row = self.area_left_qslm.rowCount()
        self.area_right_qslm.removeRow(right_row)
        self.area_left_qslm.insertRow(left_row)
        self.area_left_qslm.setData(self.area_left_qslm.index(left_row), right_text)

    def output(self):
        map_type = unicode(self.change_combo.currentText())
        if map_type == value_base.map_type[0]:
            self.geo_map()
            print u"数据地图"
        elif map_type == value_base.map_type[1]:
            self.bar_map()
            print u"柱状图"
        elif map_type == value_base.map_type[2]:
            self.line_map()
            print u"折线图"
        elif map_type == value_base.map_type[3]:
            self.radar_map()
            print u"雷达图"

    def geo_map(self):
        if self.year_right_qslm.rowCount() != 1 or self.index_right_qslm.rowCount() != 1 or self.area_right_qslm.rowCount() != 1:
            QMessageBox.information(self,
                                    u"Tips",
                                    u"数据地图年份、指标、地图数量尽可单选")
            return
        for i in self.index_right_qslm.stringList():
            value_base.current_indexs.append(unicode(i))
        for i in self.year_right_qslm.stringList():
            value_base.current_years.append(unicode(i))
        year = value_base.current_years[0]
        png = QtGui.QPixmap(
            create_data_map(year, value_base.veti_data_dict[year], value_base.index_dict[value_base.current_indexs[0]])).scaled(
            self.label.width(), self.label.height())
        self.label.setPixmap(png)
        self.qslm_reset()

    def bar_map(self):
        if self.inspect_qslm():
            return
        for i in self.index_right_qslm.stringList():
            value_base.current_indexs.append(unicode(i))
        for i in self.year_right_qslm.stringList():
            value_base.current_years.append(unicode(i))
        for i in self.area_right_qslm.stringList():
            value_base.current_areas.append(unicode(i))
        data_map.bar_map()

        self.qslm_reset()

    def line_map(self):
        if self.inspect_qslm():
            return
        for i in self.index_right_qslm.stringList():
            value_base.current_indexs.append(unicode(i))
        for i in self.year_right_qslm.stringList():
            value_base.current_years.append(unicode(i))
        for i in self.area_right_qslm.stringList():
            value_base.current_areas.append(unicode(i))
        data_map.line_map()
        self.qslm_reset()

    def radar_map(self):
        if self.inspect_qslm():
            return
        for i in self.index_right_qslm.stringList():
            value_base.current_indexs.append(unicode(i))
            value_base.radar_schema.append((unicode(i), 100))
        for i in self.year_right_qslm.stringList():
            value_base.current_years.append(unicode(i))
        for i in self.area_right_qslm.stringList():
            value_base.current_areas.append(unicode(i))
        data_map.radar_map()
        self.qslm_reset()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "村镇生态环境指数计算", None))
        self.output_btn.setText(_translate("MainWindow", "确   定", None))
        self.label_2.setText(_translate("MainWindow", "选择年份", None))
        self.label_3.setText(_translate("MainWindow", "选择指标", None))
        self.label_4.setText(_translate("MainWindow", "选择地区", None))
