# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CuisineDimension'
#
# Created by: 401219180
#
# WARNING! All changes made in this file will be lost!
#
# vervion:2017.11.03

from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
import sys
import sqlite3
import random
import base64
import os


class MainProject(QtGui.QMainWindow):
    def __init__(self):
        super(MainProject, self).__init__()
        self.music = Music()
        self.initUI()
        self.iniGrid()
        self.wigetIndex = None
        self.ToolFun = ToolFunction()
        self.mainView()

    def closeEvent(self, event):
        ToolFunction().deleteFile("temp")

    def center(self):
        """控件居中"""
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        self.resize(1180, 650)
        self.center()
        self.setWindowTitle(u'りりこの料理教室 version:2017.12.11')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.setObjectName("mainwindow")
        self.mainwidget = QtGui.QWidget()
        self.mainwidget.setObjectName("mainWidget")

        bgList = ["bg/homeskin/home_1.png", "bg/homeskin/home_2.png", "bg/homeskin/home_3.png",
                  "bg/homeskin/home_4.png", "bg/homeskin/home_5.png", "bg/homeskin/home_6.png"]
        bg = random.choice(bgList)
        try:
            decrypt(bg, "temp/bg.png")
        except IOError:
            pass
        stylesheet = "QMainWindow{background-repeat: no-repeat;background-position: center;border-image: url(temp/bg.png);}"
        self.setStyleSheet(stylesheet)

        styleqss = open("qss/gameskinNana.qss", "r")
        styleinfo = styleqss.read()
        self.mainwidget.setStyleSheet(styleinfo)
        styleqss.close()

        # palette添加背景
        # self.setAutoFillBackground(True)
        # palette1 = QtGui.QPalette()
        # # palette1.setColor(self.backgroundRole(), QtGui.QColor(50, 50, 50, 80))  # 设置背景颜色
        # pix = QtGui.QPixmap('ui/homeskin/home_1.png')
        # pix = pix.scaled(self.width(), self.height()).scaled(QtCore.Qt.IgnoreAspectRatio)
        # palette1.setBrush(self.backgroundRole(), QtGui.QBrush(pix))   # 设置背景图片
        # self.setPalette(palette1)

        self.setWindowOpacity(0.96)

        # 新增字体咪咪体
        mimitiid = QtGui.QFontDatabase.addApplicationFont('font/liyifeng.ttf')
        fontInfoList = QtGui.QFontDatabase.applicationFontFamilies(mimitiid)
        fontName = fontInfoList[0]
        self.diyfont = QtGui.QFont(fontName)

        self.groupbtn = QtGui.QPushButton()
        self.groupbtn.setObjectName("headbtn")
        self.groupbtn.setStyleSheet("border-image:url(ui/main/shouye.png)")
        # self.groupbtn.setFont(QtGui.QFont(font))
        self.charactorbtn = QtGui.QPushButton()
        self.charactorbtn.setObjectName("headbtn")
        self.charactorbtn.setStyleSheet("border-image:url(ui/main/shiling.png)")
        # self.charactorbtn.setFont(QtGui.QFont(font))
        self.equipbtn = QtGui.QPushButton()
        self.equipbtn.setObjectName("headbtn")
        self.equipbtn.setStyleSheet("border-image:url(ui/main/zhuangbei.png)")
        # self.equipbtn.setFont(QtGui.QFont(font))
        self.sniperbtn = QtGui.QPushButton()
        self.sniperbtn.setObjectName("headbtn")
        self.sniperbtn.setStyleSheet("border-image:url(ui/main/gongshi.png)")
        # self.sniperbtn.setFont(QtGui.QFont(font))
        self.mapbtn = QtGui.QPushButton()
        self.mapbtn.setObjectName("headbtn")
        self.mapbtn.setStyleSheet("border-image:url(ui/main/gonglue.png)")
        # self.mapbtn.setFont(QtGui.QFont(font))
        self.calculationbtn = QtGui.QPushButton()
        self.calculationbtn.setObjectName("headbtn")
        self.calculationbtn.setStyleSheet("border-image:url(ui/main/jisuan.png)")
        # self.calculation.setFont(QtGui.QFont(font))
        self.consignbtn = QtGui.QPushButton()
        self.consignbtn.setObjectName("headbtn")
        self.consignbtn.setStyleSheet("border-image:url(ui/main/weituo.png)")
        # self.calculation.setFont(QtGui.QFont(font))
        self.dinnerbtn = QtGui.QPushButton()
        self.dinnerbtn.setObjectName("headbtn")
        self.dinnerbtn.setStyleSheet("border-image:url(ui/main/canche.png)")
        # self.calculation.setFont(QtGui.QFont(font))
        self.aboutbtn = QtGui.QPushButton()
        self.aboutbtn.setObjectName("headbtn")
        self.aboutbtn.setStyleSheet("border-image:url(ui/main/guanyu.png)")
        # self.aboutbtn.setFont(QtGui.QFont(font))

        self.bglabel = QtGui.QLabel()

        self.groupbtn.clicked.connect(self.mainView)
        self.charactorbtn.clicked.connect(self.cuisinelist)
        self.equipbtn.clicked.connect(self.equiplist)
        self.mapbtn.clicked.connect(self.maplist)
        self.sniperbtn.clicked.connect(self.sniperlist)
        self.calculationbtn.clicked.connect(self.calculation)
        self.consignbtn.clicked.connect(self.consignlist)
        self.dinnerbtn.clicked.connect(self.dinnerList)
        self.aboutbtn.clicked.connect(self.aboutinfo)

    def iniGrid(self):
        # self.maingrid = QtGui.QGridLayout()
        # self.setLayout(self.maingrid)
        # self.maingrid.setRowStretch(1, 1)

        # mainwindow架构
        self.maingrid = QtGui.QGridLayout()
        self.mainwidget.setLayout(self.maingrid)
        self.setCentralWidget(self.mainwidget)

        self.maingrid.setSpacing(0)
        self.maingrid.setRowStretch(1, 1)
        self.maingrid.setColumnStretch(0, 1)

        # 功能按钮窗体
        self.topwiget = QtGui.QWidget()
        self.topgrid = QtGui.QGridLayout()
        self.topwiget.setLayout(self.topgrid)
        self.maingrid.addWidget(self.topwiget, 1, 1)

        self.topgrid.addWidget(self.groupbtn, 1, 0)
        self.topgrid.addWidget(self.charactorbtn, 2, 0)
        self.topgrid.addWidget(self.equipbtn, 3, 0)
        self.topgrid.addWidget(self.consignbtn, 4, 0)
        self.topgrid.addWidget(self.dinnerbtn, 5, 0)
        self.topgrid.addWidget(self.sniperbtn, 6, 0)
        self.topgrid.addWidget(self.mapbtn, 7, 0)
        self.topgrid.addWidget(self.calculationbtn, 8, 0)
        self.topgrid.addWidget(self.aboutbtn, 9, 0)

        # banner窗体
        self.bannerwiget = QtGui.QWidget()
        self.bannerwiget.setObjectName("bannerwiget")
        self.bannerwiget.setFixedHeight(60)
        self.bannergrid = QtGui.QHBoxLayout()
        # self.bannergrid.addStretch(1)
        self.bannerwiget.setLayout(self.bannergrid)
        self.maingrid.addWidget(self.bannerwiget, 0, 0, 1, 0)

        # 中间窗体
        self.bodywiget = QtGui.QWidget()
        self.bodygrid = QtGui.QGridLayout()
        self.bodywiget.setLayout(self.bodygrid)
        self.maingrid.addWidget(self.bodywiget, 1, 0)
        # self.bodygrid.setRowStretch(0, 1)
        self.bodywiget.setWindowOpacity(1)

    def bgkuang(self):
        """初始化背景框"""
        self.kuangwidget = QtGui.QWidget()
        self.kuangwidget.setObjectName("kuangwidget")
        self.kuanggrid = QtGui.QGridLayout()
        self.kuangwidget.setLayout(self.kuanggrid)

    def inibodywiget(self):
        """初始化body"""
        if self.wigetIndex is None:
            pass
        else:
            for i in self.wigetIndex:
                i.deleteLater()

    def switchlh(self):
        sql = 'SELECT URL_LH,URL_LH2 FROM "fairy_detail"'
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        while (None, None) in info:
            info.remove((None, None))
        lhurl = random.choice(info)
        try:
            decrypt(lhurl[0], "temp/index1.png")
            decrypt(lhurl[1], "temp/index2.png")
        except IOError:
            pass
        stylesheet = "QLabel#sylhLabel{border-image: url('temp/index1.png');}" + \
                     "QLabel#sylhLabel::hover{border-image: url('temp/index2.png');}"

        self.sylhLabel.setStyleSheet(stylesheet)

    def mainView(self):
        """首页"""
        self.music.touchPlay()
        self.inibodywiget()
        self.bodygrid.setRowStretch(0, 0)
        self.bodygrid.setRowStretch(1, 0)
        self.bodygrid.setColumnStretch(0, 1)
        self.bodygrid.setColumnStretch(1, 0)

        self.switchBtn = QtGui.QPushButton()
        self.switchBtn2 = QtGui.QPushButton()
        self.switchBtn.setObjectName("switchBtn")
        self.switchBtn2.setObjectName("switchBtn2")  # 把switch按钮顶到左边
        self.switchBtn.setStyleSheet("border-image:url(ui/banner/qiehuananniu.png)")
        self.switchBtn2.setStyleSheet("background-color: rgba(255,0,0,0);")
        self.switchBtn.setFixedWidth(60)
        self.switchBtn.setFixedHeight(50)
        self.switchBtn2.setFixedWidth(700)

        self.bannergrid.addWidget(self.switchBtn)
        self.bannergrid.addWidget(self.switchBtn2)

        self.switchBtn.clicked.connect(self.switchlh)

        self.sylhLabel = QtGui.QLabel()
        self.sylhLabel.setObjectName("sylhLabel")  # 首页立绘
        self.switchlh()

        self.historyTextBrowser = QtGui.QTextBrowser()
        self.historyTextBrowser.setMinimumWidth(450)
        # self.historyTextBrowser.setFont(QtGui.QFont(self.diyfont))
        self.historyTextBrowser.setObjectName("historyBrowser")  # 更新历史
        self.historyTextBrowser.append(u"\n◆工具改版啦!欢迎各位主厨\n品尝新皮肤,现在工具会随机\n渲染背景哟~")
        self.historyTextBrowser.append(u"◆食灵新增猪扒丼之前各个小\n姐姐资料!")
        self.historyTextBrowser.append(u"◆食灵列表添加烹饪时间!")
        self.historyTextBrowser.append(u"◆食灵明细新增食灵故事!")
        self.historyTextBrowser.append(u"◆新增委托大成功数据和餐车\n数据!")
        self.historyTextBrowser.append(u"◆增加地图速推攻略（来自萌\n百),更多地图攻略可参见萌百!")

        self.bodygrid.addWidget(self.sylhLabel, 0, 0)
        self.bodygrid.addWidget(self.historyTextBrowser, 0, 1)

        self.wigetIndex = [self.switchBtn, self.switchBtn2, self.sylhLabel, self.historyTextBrowser]

    def cuisinelist(self):
        """食灵列表"""
        self.music.touchPlay()
        self.inibodywiget()
        ToolFunction().deleteFile("temp")

        self.bodygrid.setRowStretch(1, 0)
        self.bodygrid.setColumnStretch(0, 1)
        self.bodygrid.setColumnStretch(1, 0)

        self.bgkuang()
        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        # self.kuanggrid.setSpacing(0)  # 设置控件间隔

        self.kuanggrid.setColumnStretch(0, 0)
        self.kuanggrid.setColumnStretch(1, 0)

        sql = ToolFunction.getsql("sql/slList.sql")
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        rowcount = len(info)

        self.bodygrid.addWidget(self.kuangwidget, 0, 0)

        self.tablewiget = QtGui.QTableWidget(rowcount, 21)
        self.tablewiget.verticalHeader().setVisible(False)
        self.tablewiget.cellClicked.connect(self.slDetail)  # 表格信号
        # self.tablewiget.horizontalHeader().sectionClicked.connect(self.fortest2)  # 表头信号

        # self.tablewiget.verticalHeader().setVisible(False)
        # self.tablewiget.horizontalHeader().setVisible(False)
        self.tablewiget.setHorizontalHeaderLabels(
            [u"头像", u"No", u"食灵", u"类型", u"烹饪时间", u"生命", u"攻击", u"防御", u"命中", u"闪避",
             u"暴击", u"攻速", u"石油", u"魔力", u"满生命", u"满攻击", u"满防御", u"满命中", u"满闪避",
             u"石油", u"魔力"])

        for x in range(self.tablewiget.columnCount()):
            headItem = self.tablewiget.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            headItem.setBackgroundColor(QtGui.QColor(25, 20, 20))  # 设置单元格背景颜色
            headItem.setTextColor(QtGui.QColor(200, 111, 30))

            # self.tablewiget.setShowGrid(False)  # 设置网格线

        # self.lbp = QtGui.QLabel()
        # self.lbp.setPixmap(QtGui.QPixmap(U"card/cutin/bmf_n.png"))
        # self.tablewiget.setCellWidget(0, 0, self.lbp)

        # self.tablewiget.horizontalHeader().setStretchLastSection(True)
        # self.tablewiget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        # self.tablewiget.verticalHeader().setStretchLastSection(True)
        # self.tablewiget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # self.tablewiget.resizeRowsToContents()
        self.tablewiget.resizeColumnsToContents()
        # self.tablewiget.resizeColumnToContents(1)
        # self.tablewiget.resizeColumnToContents(3)
        # self.tablewiget.resizeColumnToContents(4)

        self.tablewiget.setColumnWidth(0, 190)
        self.tablewiget.setColumnWidth(1, 28)
        self.tablewiget.setColumnWidth(2, 120)
        self.tablewiget.setColumnWidth(4, 120)

        rowindex = 0
        for i in info:
            columnindex = 0
            for x in i:
                if type(x) == int:
                    info = str(x)
                else:
                    info = x

                # if info is None:  # 调试专用
                #     print "调试用"
                #     print "213"

                if columnindex == 0:
                    self.lbp = QtGui.QLabel()
                    self.lbp.setPixmap(QtGui.QPixmap(info))
                    self.tablewiget.setCellWidget(rowindex, columnindex, self.lbp)
                    columnindex += 1
                elif columnindex == 1:
                    try:
                        self.newItem = QtGui.QTableWidgetItem(info)
                    except TypeError, msg:
                        print msg
                    self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.tablewiget.setItem(rowindex, columnindex, self.newItem)
                    columnindex += 1
                elif columnindex == 3:
                    self.lbp = QtGui.QLabel()
                    self.lbp.setPixmap(QtGui.QPixmap('ui/hero/' + info + '.png'))
                    self.tablewiget.setCellWidget(rowindex, columnindex, self.lbp)
                    columnindex += 1
                    # typeIndex = {"1": u"主食", "2": u"主菜", "3": u"副菜", "4": u"甜点", "5": u"头盘", "6": u"汤饮"}
                    # typeName = typeIndex[info]
                    # self.newItem.setWhatsThis(typeName)
                else:
                    try:
                        self.newItem = QtGui.QTableWidgetItem(info)
                    except TypeError, msg:
                        print msg
                    self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tablewiget.setItem(rowindex, columnindex, self.newItem)
                    columnindex += 1
                    self.newItem.setWhatsThis(info)
            rowindex += 1

        # asd = self.tablewiget.findItems(u"主食", QtCore.Qt.MatchExactly)
        # # self.tablewiget.clear()
        # print asd[0].row()
        # self.tablewiget.setRowHidden(asd[0].row(), True)

        self.tablewiget.setSortingEnabled(True)
        self.kuanggrid.addWidget(self.tablewiget, 0, 0)
        self.wigetIndex = [self.tablewiget, self.kuangwidget]
        # self.tablewiget.cellClicked.connect(self.slDetail)

    def equiplist(self):
        """装备列表"""
        self.music.touchPlay()
        self.inibodywiget()

        sql = 'SELECT TZ_NAME FROM "equip_suit" ORDER BY tz_level DESC, limit_flag;'
        info = ToolFunction.getsqliteInfo(sql, "llcy")

        self.bgkuang()
        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        self.kuanggrid.setSpacing(0)  # 设置控件间隔

        self.tablewiget = QtGui.QTableWidget(3, 1)
        self.tablewiget.setObjectName("tzsxTabel")
        self.tablewiget.setShowGrid(False)
        self.tablewiget.horizontalHeader().setStretchLastSection(True)
        self.tablewiget.verticalHeader().setStretchLastSection(True)
        self.tablewiget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tablewiget.setFixedHeight(100)
        self.tablewiget.setHorizontalHeaderLabels([u"套装属性"])
        self.tablewiget.verticalHeader().setVisible(False)
        self.kuanggrid.addWidget(self.tablewiget, 0, 1)

        self.tablewiget2 = QtGui.QTableWidget(10, 5)
        self.tablewiget2.setObjectName("zbsxTabel")
        self.tablewiget2.setShowGrid(False)
        self.tablewiget2.setHorizontalHeaderLabels([u"品质", u"类型", u"名称", u"基础属性1", u"基础属性2"])
        self.tablewiget2.verticalHeader().setVisible(False)

        self.tablewiget2.verticalHeader().setStretchLastSection(True)
        self.tablewiget2.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.kuanggrid.addWidget(self.tablewiget2, 1, 1)

        self.equipTzList = QtGui.QListWidget()
        self.equipTzList.setObjectName("equipTzList")
        for tzNameIndex in info:
            newItem = QtGui.QListWidgetItem(tzNameIndex[0])
            newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.equipTzList.addItem(newItem)

        self.equipTzList.itemClicked.connect(self.equipEdit)
        self.kuanggrid.addWidget(self.equipTzList, 0, 0, 0, 1)

        self.kuanggrid.setColumnStretch(0, 0)
        self.kuanggrid.setColumnStretch(1, 1)

        # self.tablewiget.verticalHeader().setVisible(False)
        # self.tablewiget.horizontalHeader().setVisible(False)

        self.wigetIndex = [self.tablewiget, self.tablewiget2, self.equipTzList, self.kuangwidget]

    def equipEdit(self):
        """装备列表数据填充"""
        listItemName = unicode(self.equipTzList.currentItem().text())
        sql = "SELECT CASE WHEN LIMIT_FLAG = 'N' THEN '-' ELSE (SELECT MAP_NAME FROM map_info WHERE MAP_NO = LIMIT_FLAG)||ifnull(LIMIT_MAP,'') END getMethod,TZ_ATTR_FIR||' / '||TZ_ATTR_SEC, TZ_ATTR_TRI, b1.code_name, b2.code_name, s.tz_name||e_type_sub equip_name, e_attr_fir, e_attr_sec FROM equip_info t, equip_suit s, (SELECT code, code_name FROM bas_code WHERE code_id = 'equip_type') b2, (SELECT code, code_name FROM bas_code WHERE code_id = 'equip_level') b1 WHERE t.e_level = b1.code AND t.e_type = b2.code AND t.e_tz = s.tz_no AND s.TZ_NAME = '" + listItemName + "' ORDER BY e_type, e_attr_fir,e_attr_sec"
        datainfo = ToolFunction.getsqliteInfo(sql, "llcy")
        # print datainfo
        self.tablewiget.clear()
        self.tablewiget2.clear()
        self.tablewiget.setHorizontalHeaderLabels([u"套装属性"])
        self.tablewiget2.setHorizontalHeaderLabels([u"品质", u"类型", u"名称", u"基础属性1", u"基础属性2"])

        typeIndex = {u"食器": 1, u"厨具": 2, u"餐具": 3}
        rowindex = 0
        for rowData in datainfo:
            columnindex = 0
            for columnData in rowData:
                if type(columnData) == int:
                    info = str(columnData)
                else:
                    info = columnData

                if columnindex < 3:
                    self.newItem = QtGui.QTableWidgetItem(info)
                    # self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.tablewiget.setItem(columnindex, 0, self.newItem)
                    self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                    columnindex += 1
                elif columnindex == 4:
                    self.newItem = QtGui.QTableWidgetItem(info)
                    self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.tablewiget2.setItem(rowindex, columnindex - 3, self.newItem)
                    self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.newItem.setIcon(QtGui.QIcon('ui/equip/' + str(typeIndex[info]) + '.png'))
                    columnindex += 1
                else:
                    self.newItem = QtGui.QTableWidgetItem(info)
                    self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.tablewiget2.setItem(rowindex, columnindex - 3, self.newItem)
                    self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                    columnindex += 1
            rowindex += 1

    def dinnerList(self):
        """餐车数据"""
        self.music.touchPlay()
        self.inibodywiget()

        sql = "SELECT name,type,size,Desc FROM fitment ORDER BY box,box_max,type"
        info = ToolFunction.getsqliteInfo(sql, "llcy")

        sql2 = ToolFunction.getsql("sql/dinerList.sql")
        info2 = ToolFunction.getsqliteInfo(sql2, "llcy")

        self.bgkuang()
        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        # self.kuanggrid.setSpacing(0)  # 设置控件间隔

        rowcount = len(info2)
        self.tablewiget = QtGui.QTableWidget(rowcount, 7)
        self.tablewiget.setObjectName("dishTabel")
        self.tablewiget.setShowGrid(False)
        self.tablewiget.setHorizontalHeaderLabels([u"名称", u"类型", u"特性", u"外形", u"风味", u"营养", u"合计"])
        self.tablewiget.verticalHeader().setVisible(False)
        self.kuanggrid.addWidget(self.tablewiget, 0, 1)
        self.tablewiget.setColumnWidth(0, 120)
        self.tablewiget.setColumnWidth(1, 50)
        self.tablewiget.setColumnWidth(2, 50)
        self.tablewiget.setColumnWidth(3, 50)
        self.tablewiget.setColumnWidth(4, 50)
        self.tablewiget.setColumnWidth(5, 50)
        self.tablewiget.setColumnWidth(6, 50)

        rowcount = len(info)
        self.equipTzList = QtGui.QTableWidget(rowcount, 4)
        self.equipTzList.setObjectName("equipTzList")
        self.equipTzList.setShowGrid(False)
        self.equipTzList.setHorizontalHeaderLabels([u"名称", u"类型", u"规格", u"描述"])
        self.equipTzList.verticalHeader().setVisible(False)
        self.kuanggrid.addWidget(self.equipTzList, 0, 0)
        self.equipTzList.setColumnWidth(1, 50)
        self.equipTzList.setColumnWidth(3, 220)

        rowindex = 0
        for i in info:
            columnindex = 0
            for x in i:
                if type(x) == int:
                    info = str(x)
                else:
                    info = x

                try:
                    self.newItem = QtGui.QTableWidgetItem(info)
                except TypeError, msg:
                    print msg
                self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.equipTzList.setItem(rowindex, columnindex, self.newItem)
                columnindex += 1
                self.newItem.setWhatsThis(info)
            rowindex += 1

        rowindex = 0
        for i in info2:
            columnindex = 0
            for x in i:
                if type(x) == int:
                    info2 = str(x)
                else:
                    info2 = x

                try:
                    self.newItem = QtGui.QTableWidgetItem(info2)
                except TypeError, msg:
                    print msg
                self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tablewiget.setItem(rowindex, columnindex, self.newItem)
                columnindex += 1
                self.newItem.setWhatsThis(info2)
            rowindex += 1

        self.kuanggrid.setColumnStretch(0, 1)
        self.kuanggrid.setColumnStretch(1, 1)

        self.tablewiget.setSortingEnabled(True)
        self.equipTzList.setSortingEnabled(True)
        # self.tablewiget.verticalHeader().setVisible(False)
        # self.tablewiget.horizontalHeader().setVisible(False)

        self.wigetIndex = [self.tablewiget, self.equipTzList, self.kuangwidget]

    def consignlist(self):
        """委托列表"""
        self.music.touchPlay()
        self.inibodywiget()
        ToolFunction().deleteFile("temp")

        self.bodygrid.setRowStretch(1, 0)
        self.bodygrid.setColumnStretch(0, 1)
        self.bodygrid.setColumnStretch(1, 0)

        self.bgkuang()
        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        # self.kuanggrid.setSpacing(0)  # 设置控件间隔

        self.kuanggrid.setColumnStretch(0, 0)
        self.kuanggrid.setColumnStretch(1, 0)

        sql = ToolFunction.getsql("sql/wtList.sql")
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        rowcount = len(info)

        self.bodygrid.addWidget(self.kuangwidget, 0, 0)

        self.tablewiget = QtGui.QTableWidget(rowcount, 15)
        self.tablewiget.verticalHeader().setVisible(False)
        # self.tablewiget.horizontalHeader().sectionClicked.connect(self.fortest2)  # 表头信号

        # self.tablewiget.verticalHeader().setVisible(False)
        # self.tablewiget.horizontalHeader().setVisible(False)
        self.tablewiget.setHorizontalHeaderLabels(
            [u"地图", u"时长", u"食油", u"魔力", u"食材", u"调料", u"获得经验", u"其他", u"大成功条件；基础条件", u"每小时总量",
             u"食油", u"魔力", u"食材", u"调料", u"经验"])

        for x in range(self.tablewiget.columnCount()):
            headItem = self.tablewiget.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            headItem.setBackgroundColor(QtGui.QColor(25, 20, 20))  # 设置单元格背景颜色
            headItem.setTextColor(QtGui.QColor(200, 111, 30))

            # self.tablewiget.setShowGrid(False)  # 设置网格线

        # self.lbp = QtGui.QLabel()
        # self.lbp.setPixmap(QtGui.QPixmap(U"card/cutin/bmf_n.png"))
        # self.tablewiget.setCellWidget(0, 0, self.lbp)

        # self.tablewiget.horizontalHeader().setStretchLastSection(True)
        # self.tablewiget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        # self.tablewiget.verticalHeader().setStretchLastSection(True)
        # self.tablewiget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # self.tablewiget.resizeRowsToContents()
        self.tablewiget.resizeColumnsToContents()
        # self.tablewiget.resizeColumnToContents(1)
        # self.tablewiget.resizeColumnToContents(3)
        # self.tablewiget.resizeColumnToContents(4)

        self.tablewiget.setColumnWidth(0, 40)
        self.tablewiget.setColumnWidth(1, 70)
        self.tablewiget.setColumnWidth(2, 50)
        self.tablewiget.setColumnWidth(3, 50)
        self.tablewiget.setColumnWidth(4, 50)
        self.tablewiget.setColumnWidth(5, 50)
        self.tablewiget.setColumnWidth(6, 80)
        self.tablewiget.setColumnWidth(8, 200)
        self.tablewiget.setColumnWidth(10, 50)
        self.tablewiget.setColumnWidth(11, 50)
        self.tablewiget.setColumnWidth(12, 50)
        self.tablewiget.setColumnWidth(13, 50)
        self.tablewiget.setColumnWidth(14, 70)

        rowindex = 0
        for i in info:
            columnindex = 0
            for x in i:
                if type(x) == int:
                    info = str(x)
                else:
                    info = x

                try:
                    self.newItem = QtGui.QTableWidgetItem(info)
                except TypeError, msg:
                    print msg
                self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tablewiget.setItem(rowindex, columnindex, self.newItem)
                columnindex += 1
                self.newItem.setWhatsThis(info)
            rowindex += 1

        self.tablewiget.setSortingEnabled(True)
        # asd = self.tablewiget.findItems(u"龙须糖", QtCore.Qt.MatchContains)
        # self.tablewiget.clear()
        # self.tablewiget.setItem(0,0,asd[0])
        self.kuanggrid.addWidget(self.tablewiget, 0, 0)
        self.wigetIndex = [self.tablewiget, self.kuangwidget]
        # self.tablewiget.cellClicked.connect(self.slDetail)

    def sniperlist(self):
        """狙击公式"""
        self.music.touchPlay()
        self.inibodywiget()
        self.bodygrid.setRowStretch(0, 1)
        self.bodygrid.setRowStretch(1, 0)
        self.bodygrid.setColumnStretch(0, 0)
        self.bodygrid.setColumnStretch(1, 0)
        self.bgkuang()
        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        # self.kuanggrid.setSpacing(0)  # 设置控件间隔

        sql = ToolFunction.getsql("sql/sniper.sql")
        info = ToolFunction.getsqliteInfo(sql, "llcy")

        rowcount = len(info)
        self.tablewiget = QtGui.QTableWidget(rowcount, 9)
        self.tablewiget.setHorizontalHeaderLabels([u"食油", u"魔力", u"食材", u"主食", u"主菜", u"副菜",
                                                   u"甜品", u"头盘", u"汤饮"])
        self.kuanggrid.addWidget(self.tablewiget, 0, 0)
        self.tablewiget.horizontalHeader().setStretchLastSection(True)
        self.tablewiget.verticalHeader().setStretchLastSection(True)
        self.tablewiget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tablewiget.verticalHeader().setVisible(False)
        self.tablewiget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        rowindex = 0
        for i in info:
            columnindex = 0
            for x in i:
                if type(x) == int:
                    info = str(x)
                else:
                    info = x
                if "1" in info:
                    info = u"√"
                elif "0" == info:
                    info = "-"
                else:
                    pass
                self.newItem = QtGui.QTableWidgetItem(info)
                self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.tablewiget.setItem(rowindex, columnindex, self.newItem)
                self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
                columnindex += 1
                self.newItem.setWhatsThis(info)
            rowindex += 1

        self.tablewiget.setSortingEnabled(True)  # 排序

        self.sniperText = QtGui.QTextBrowser()
        self.sniperText.setObjectName("sniper_bz")  # 狙击备注
        self.kuanggrid.addWidget(self.sniperText, 1, 0)
        self.sniperText.setFixedHeight(100)
        self.sniperText.append(u"◆食油，魔力，食材影响出货种类，调料建议400以上，公式不保证概率，请洗脸后尝试。")
        self.sniperText.append(
            u"◆烹饪限定食灵：白米饭,热香饼,那不勒斯披萨,佛跳墙,玉子烧,甜甜圈,香菜戚风蛋糕,关东煮,冰糖燕窝,冬荫功,冬瓜盅,叫花鸡,焦糖布丁,提拉米苏,荣耀女仆蛋挞,香槟,西芹百合,苏格兰蛋,罗宋汤,肴肉,猫饭,韩式泡菜")

        self.wigetIndex = [self.tablewiget, self.sniperText, self.kuangwidget]

    def maplist(self):
        """地图列表"""
        self.music.touchPlay()
        self.inibodywiget()
        self.bodygrid.setRowStretch(0, 0)
        self.bodygrid.setRowStretch(1, 0)
        self.bodygrid.setColumnStretch(0, 0)
        self.bodygrid.setColumnStretch(1, 0)

        self.bgkuang()
        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        self.kuanggrid.setSpacing(0)  # 设置控件间隔

        sql = 'SELECT TZ_NAME FROM "equip_suit" ORDER BY tz_level DESC, limit_flag;'
        info = ToolFunction.getsqliteInfo(sql, "llcy")

        self.mapLabel = QtGui.QLabel()
        self.mapLabel.setObjectName("mapLabel")
        self.kuanggrid.addWidget(self.mapLabel, 0, 1, 0, 1)

        self.mapList1 = QtGui.QListWidget()
        self.mapList1.setObjectName("mapList1")
        self.mapList1.setMaximumWidth(180)
        self.mapList1.setMaximumHeight(200)
        # info = [u"轻度1-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6",
        #         u"轻度2-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6",
        #         u"轻度3-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6",
        #         u"轻度4-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6",
        #         u"轻度5-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6",
        #         u"轻度6-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6",
        #         u"轻度1-1", u"轻度1-2", u"轻度1-3", u"轻度1-4", u"轻度1-5", u"轻度1-6", ]
        info = [u"欧罗巴大陆", u"美利坚大陆", u"和风岛", u"次元小屋", u"中华大陆", u"次元壁(暂无)"]
        for tzNameIndex in info:
            newItem = QtGui.QListWidgetItem(tzNameIndex)
            newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.mapList1.addItem(newItem)

        self.mapList2 = QtGui.QListWidget()
        self.mapList2.setObjectName("mapList2")
        self.mapList2.setMaximumWidth(180)
        info = [u"轻度1", u"轻度2", u"轻度3", u"轻度4", u"轻度5", u"轻度6",
                u"重度1", u"重度2", u"重度3", u"重度4", u"重度5", u"重度6", ]
        for tzNameIndex in info:
            newItem = QtGui.QListWidgetItem(tzNameIndex)
            newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.mapList2.addItem(newItem)

        self.mapList1.itemClicked.connect(self.getMap)
        self.mapList2.itemClicked.connect(self.getMap)

        self.kuanggrid.addWidget(self.mapList1, 0, 0)
        self.kuanggrid.addWidget(self.mapList2, 1, 0)

        self.kuanggrid.setColumnStretch(0, 0)
        self.kuanggrid.setColumnStretch(1, 1)

        qss = "border-image:url(map/mapMain.png);"
        self.mapLabel.setStyleSheet(qss)

        self.wigetIndex = [self.mapList1, self.mapList2, self.mapLabel, self.kuangwidget]

    def getMap(self):
        """获取要查看的地图"""
        listRow1 = self.mapList1.currentRow() + 1
        listRow2 = self.mapList2.currentRow() + 1
        if listRow1 == 0 or listRow2 == 0:
            pass
            mapurl = None
        else:
            mapurl = "map/" + unicode(listRow1) + "/" + unicode(listRow2) + ".png"

        if listRow1 == 6 or mapurl is None:
            pass
        else:
            qss = "border-image:url(\'" + mapurl + "\');"
            self.mapLabel.setStyleSheet(qss)

    def calculation(self):
        """计算"""
        self.music.touchPlay()
        self.inibodywiget()
        self.bodygrid.setRowStretch(0, 0)
        self.bodygrid.setRowStretch(1, 0)
        self.bodygrid.setColumnStretch(0, 0)
        self.bodygrid.setColumnStretch(1, 0)

        self.bgkuang()

        self.kuanggrid.setColumnStretch(0, 1)
        self.kuanggrid.setColumnStretch(1, 4)

        self.bodygrid.addWidget(self.kuangwidget, 0, 0)
        # self.kuanggrid.setSpacing(0)  # 设置控件间隔

        self.levelBox = QtGui.QGroupBox(u"等级计算")
        self.levelBoxGrid = QtGui.QGridLayout()
        self.levelBox.setLayout(self.levelBoxGrid)

        self.equipBox = QtGui.QGroupBox(u"装备计算")
        self.equipBoxGrid = QtGui.QGridLayout()
        self.equipBox.setLayout(self.equipBoxGrid)

        self.nowlevLabel = QtGui.QLabel(u"当前等级")
        self.nowexpLabel = QtGui.QLabel(u"当前经验")
        self.taglevLabel = QtGui.QLabel(u"目标等级")
        self.expLabel = QtGui.QLabel(u"每局经验")
        self.expResultText = QtGui.QTextBrowser()

        self.nowlevLabel2 = QtGui.QLabel(u"当前等级")
        self.taglevLabel2 = QtGui.QLabel(u"目标等级")
        self.equipNumResultText = QtGui.QTextBrowser()

        self.nowlevLabel.setObjectName("calculationLabel")
        self.nowexpLabel.setObjectName("calculationLabel")
        self.taglevLabel.setObjectName("calculationLabel")
        self.expLabel.setObjectName("calculationLabel")
        self.nowlevLabel2.setObjectName("calculationLabel")
        self.taglevLabel2.setObjectName("calculationLabel")
        self.expResultText.setObjectName("calculationText")
        self.equipNumResultText.setObjectName("calculationText")

        self.nowlevEntry = QtGui.QLineEdit()
        self.nowexpEntry = QtGui.QLineEdit()
        self.taglevpEntry = QtGui.QLineEdit()
        self.expEntry = QtGui.QLineEdit()
        self.nowlevEntry.setObjectName("calculationEntry")
        self.nowexpEntry.setObjectName("calculationEntry")
        self.taglevpEntry.setObjectName("calculationEntry")
        self.expEntry.setObjectName("calculationEntry")

        self.nowlevEntry2 = QtGui.QLineEdit()
        self.taglevpEntry2 = QtGui.QLineEdit()
        self.nowlevEntry2.setObjectName("calculationEntry")
        self.taglevpEntry2.setObjectName("calculationEntry")

        self.jsgo = QtGui.QPushButton("Go!")
        self.jsgo2 = QtGui.QPushButton("Go!")
        self.jsgo.clicked.connect(self.calculation_go1)
        self.jsgo2.clicked.connect(self.calculation_go2)

        self.kuanggrid.addWidget(self.levelBox, 0, 0)
        self.kuanggrid.addWidget(self.equipBox, 1, 0)

        self.levelBoxGrid.addWidget(self.nowexpLabel, 0, 0)
        self.levelBoxGrid.addWidget(self.nowexpEntry, 0, 1)
        self.levelBoxGrid.addWidget(self.nowlevLabel, 1, 0)
        self.levelBoxGrid.addWidget(self.nowlevEntry, 1, 1)
        self.levelBoxGrid.addWidget(self.taglevLabel, 2, 0)
        self.levelBoxGrid.addWidget(self.taglevpEntry, 2, 1)
        self.levelBoxGrid.addWidget(self.expLabel, 3, 0)
        self.levelBoxGrid.addWidget(self.expEntry, 3, 1)
        self.levelBoxGrid.addWidget(self.jsgo, 4, 0)
        self.levelBoxGrid.addWidget(self.expResultText, 5, 0, 1, 0)

        self.equipBoxGrid.addWidget(self.nowlevLabel2, 0, 0)
        self.equipBoxGrid.addWidget(self.nowlevEntry2, 0, 1)
        self.equipBoxGrid.addWidget(self.taglevLabel2, 1, 0)
        self.equipBoxGrid.addWidget(self.taglevpEntry2, 1, 1)
        self.equipBoxGrid.addWidget(self.jsgo2, 2, 0)
        self.equipBoxGrid.addWidget(self.equipNumResultText, 3, 0, 1, 0)

        # 右侧装备选择
        sql = ToolFunction.getsql("sql/calculation/jsfindsl.sql")
        info = ToolFunction.getsqliteInfo(sql, "llcy")

        self.equipChooseBox = QtGui.QGroupBox(u"装备选择")
        self.equipChooseGrid = QtGui.QGridLayout()
        self.equipChooseBox.setLayout(self.equipChooseGrid)

        self.hpcheck = QtGui.QCheckBox(u"2百分比生命")
        self.hpcheck.setObjectName("hpcheck")

        # 类型下拉框
        typeList = []
        for typeIndex in info:
            typeList.append(typeIndex[0])
        typeList = list(set(typeList))
        typeList2 = []
        for index in typeList:
            typeList2.append(slTpyeDictory[index])

        self.typeCombox = QtGui.QComboBox()
        self.typeCombox.addItems(typeList2)
        self.typeCombox.currentIndexChanged.connect(self.calculationNameEdit)

        # 名字下拉框
        nameList = [u"扬州炒饭", u"方包", u"馄饨"]
        # for nameIndex in info:
        #     nameList.append(nameIndex[1])
        self.slCombox = QtGui.QComboBox()
        self.slCombox.addItems(nameList)

        # 套装下拉框
        self.equipSetCombox = QtGui.QComboBox()
        equipSql = 'SELECT TZ_NAME FROM "equip_suit" where tz_level = 5 ORDER BY tz_level DESC, limit_flag;'
        info = ToolFunction.getsqliteInfo(equipSql, "llcy")
        for name in info:
            self.equipSetCombox.addItem(name[0])
        self.equipSetCombox.currentIndexChanged.connect(self.tableWareEdit)

        # 刀叉下拉框
        self.dcCombox = QtGui.QComboBox()
        self.dcCombox.addItem(u"【望月叉】0暴")
        self.dcCombox.addItem(u"【望月叉】80暴")
        # self.dcCombox.addItem(u"【金勺】0暴")
        self.dcCombox.setMinimumWidth(150)

        self.jsgo3 = QtGui.QPushButton("Go!")
        self.jsgo3.clicked.connect(self.calculation_go3)

        # 筛选表格
        self.skillText = QtGui.QTextBrowser()
        self.skillText.setObjectName("skillText")
        self.tableLabel = QtGui.QLabel(u"当前食灵属性:")
        self.tableLabel.setObjectName("calculationLabel2")
        self.tablewiget = QtGui.QTableWidget(1, 7)
        # self.tablewiget.setObjectName("dishTabel")
        self.tablewiget.setShowGrid(False)
        self.tablewiget.setHorizontalHeaderLabels(
            [u"满生命", u"满攻击", u"满防御", u"满命中", u"满闪避", u"暴击值", u"暴伤值", u"技能", u"固有技能"])
        self.tablewiget.verticalHeader().setVisible(False)
        self.tablewiget.horizontalHeader().setStretchLastSection(True)
        self.tablewiget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # 推荐表格
        self.tableLabel2 = QtGui.QLabel(u"食灵+套装洗练结果汇总:")
        self.tableLabel2.setObjectName("calculationLabel2")

        self.tablewiget2 = QtGui.QTableWidget(18, 7)
        # self.tablewiget.setObjectName("dishTabel")
        self.tablewiget2.setShowGrid(False)
        self.tablewiget2.setHorizontalHeaderLabels(
            [u"百分比攻击个数", u"百分比暴击个数", u"百分比暴伤", u"最终暴击百分比", u"实际攻击", u"期望伤害", u"最高伤害"])
        self.tablewiget2.verticalHeader().setVisible(False)
        self.tablewiget2.horizontalHeader().setStretchLastSection(True)
        self.tablewiget2.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.kuanggrid.addWidget(self.equipChooseBox, 0, 1, 0, 1)
        self.equipChooseGrid.addWidget(self.hpcheck, 0, 0)
        self.equipChooseGrid.addWidget(self.typeCombox, 0, 1)
        self.equipChooseGrid.addWidget(self.slCombox, 0, 2)
        self.equipChooseGrid.addWidget(self.equipSetCombox, 0, 3)
        self.equipChooseGrid.addWidget(self.dcCombox, 0, 4)
        self.equipChooseGrid.addWidget(self.jsgo3, 0, 5)
        self.equipChooseGrid.addWidget(self.tableLabel, 1, 0)
        self.equipChooseGrid.addWidget(self.skillText, 2, 0, 1, 6)
        self.equipChooseGrid.addWidget(self.tablewiget, 3, 0, 6, 0)
        self.equipChooseGrid.addWidget(self.tableLabel2, 4, 0)
        self.equipChooseGrid.addWidget(self.tablewiget2, 5, 0, 6, 0)

        self.wigetIndex = [self.kuangwidget]

    def calculationNameEdit(self):
        slnumb = self.typeCombox.currentIndex() + 1
        if slnumb == 4 or slnumb == 5:
            slnumb += 1
        sql = ToolFunction.getsql("sql/calculation/jsfindsl2.sql") % slnumb
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        nameList = []
        for nameIndex in info:
            nameList.append(nameIndex[1])
        self.slCombox.clear()
        self.slCombox.addItems(nameList)

    def tableWareEdit(self):
        tzName = unicode(self.equipSetCombox.currentText())

        sql = ToolFunction.getsql("sql/calculation/jsfindsl3.sql") % tzName.encode("utf-8")
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        nameList = []
        for nameIndex in info:
            nameList.append(nameIndex[0])
        self.dcCombox.clear()
        self.dcCombox.addItems(nameList)

    def calculation_go1(self):
        nowlevel = self.nowlevEntry.text()
        nowexp = self.nowexpEntry.text()
        taglevel = self.taglevpEntry.text()
        exp = self.expEntry.text()
        if str(nowlevel) == '' or str(taglevel) == '' or str(exp) == '':
            self.expResultText.clear()
            self.expResultText.append(u"请在上面输入数字")
            return
        sql = "select (sum(fairy_exp)-(" + str(nowexp) + "0/10)) / " + str(exp) + "+1 from (select fairy_exp from level_exp where level >= '" + str(
            nowlevel) + "' and level <'" + str(taglevel) + "')"
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        result = u"大约需要" + str(info[0][0]) + u"场战斗"
        self.expResultText.clear()
        self.expResultText.append(result)

    def calculation_go2(self):
        nowlevel = self.nowlevEntry2.text()
        taglevel = self.taglevpEntry2.text()
        if str(nowlevel) == '' or str(taglevel) == '':
            self.equipNumResultText.clear()
            self.equipNumResultText.append(u"请合理输入数字")
            return
        if int(nowlevel) < 10 and 10 >= int(taglevel) > int(nowlevel):
            sql = 'SELECT number/40,number/60,number/80 FROM (SELECT ((SELECT equip_exp FROM level_exp WHERE level = ' + str(
                taglevel) + ")-(SELECT equip_exp FROM level_exp WHERE level = " + str(nowlevel) + ")) AS number)"
            info = ToolFunction.getsqliteInfo(sql, "llcy")
            result = u"狗粮大约需要" + str(info[0][0]) + u"个白或" + str(info[0][1]) + u"个蓝或" + str(info[0][2]) + u"个紫"
            self.equipNumResultText.clear()
            self.equipNumResultText.append(result)
            return
        self.equipNumResultText.clear()
        self.equipNumResultText.append(u"请合理输入数字")

    def calculation_go3(self):
        tzName = self.equipSetCombox.currentText()
        sql = "SELECT TZ_NO FROM equip_suit WHERE TZ_NAME=\'" + unicode(tzName) + "\';"
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        tzno = info[0][0]

        slName = self.slCombox.currentText()
        sql = "SELECT SL_NO FROM fairy_detail WHERE SL_NAME=\'" + unicode(slName) + "\';"
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        slno = info[0][0]

        if u"金叉" in self.dcCombox.currentText():
            bj = 80
            bs = 120
        elif u"金筷" in self.dcCombox.currentText():
            bj = 100
            bs = 50
        elif u"金勺" in self.dcCombox.currentText():
            bj = 0
            bs = 0
        elif u"蝠" in self.dcCombox.currentText():
            bj = 80
            bs = 120
        elif u"【望月叉】0暴" in self.dcCombox.currentText():
            bj = 0
            bs = 50
        elif u"【望月叉】80暴" in self.dcCombox.currentText():
            bj = 80
            bs = 120
        elif u"琴" in self.dcCombox.currentText():
            bj = 0
            bs = 0
        else:
            print u"筷叉读取错误"
            return

        # 筛选表格填充
        sql = ToolFunction.getsql("sql/calculation/calculationResult.sql") % (tzno, slno, slno, slno, bj, bs)
        infoIndex = ToolFunction.getsqliteInfo(sql, "llcy")
        self.tablewiget.clear()
        self.tablewiget.setHorizontalHeaderLabels(
            [u"满生命", u"满攻击", u"满防御", u"满命中", u"满闪避", u"暴击值", u"暴伤值", u"技能", u"固有技能"])

        self.skillText.clear()
        self.skillText.append(infoIndex[0][7])
        self.skillText.append(infoIndex[0][8])

        columnindex = 0
        for i in infoIndex[0]:
            if type(i) == int:
                info = str(i)
            else:
                info = i
            try:
                self.newItem = QtGui.QTableWidgetItem(info)
            except TypeError, msg:
                print msg
            self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.tablewiget.setItem(0, columnindex, self.newItem)
            columnindex += 1
            self.newItem.setWhatsThis(info)

        # 推荐表格填充
        sl_BJ = infoIndex[0][5]
        sl_BS = infoIndex[0][6]
        max_GJ = infoIndex[0][1]
        skill = infoIndex[0][9]

        if self.hpcheck.isChecked():
            sl_HP = 2
        else:
            sl_HP = 0

        sql = ToolFunction.getsql("sql/calculation/xljgResult.sql") % (sl_HP, sl_BJ, sl_BS, max_GJ, skill)
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        self.tablewiget2.clear()
        self.tablewiget2.setHorizontalHeaderLabels(
            [u"百分比攻击个数", u"百分比暴击个数", u"百分比暴伤", u"最终暴击百分比", u"实际攻击", u"期望伤害", u"最高伤害"])
        self.tablewiget2.setSortingEnabled(False)
        rowindex = 0
        for i in info:
            columnindex = 0
            for x in i:
                if type(x) == int:
                    info = str(x)
                else:
                    info = x

                # if info is None:  # 调试专用
                #     print "调试用"
                #     print "213"
                try:
                    self.newItem = QtGui.QTableWidgetItem(info)
                except TypeError, msg:
                    print msg
                self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.tablewiget2.setItem(rowindex, columnindex, self.newItem)
                columnindex += 1
                self.newItem.setWhatsThis(info)
            rowindex += 1
        self.tablewiget2.setSortingEnabled(True)

    def aboutinfo(self):
        """关于界面"""
        self.music.touchPlay()
        self.inibodywiget()

        self.bodygrid.setColumnStretch(0, 1)
        self.bodygrid.setColumnStretch(1, 0)
        self.bodygrid.setSpacing(0)

        # 设置左右框架
        self.leftwiget = QtGui.QWidget()
        self.rightwiget = QtGui.QWidget()
        self.bodygrid.addWidget(self.leftwiget, 0, 0)
        self.bodygrid.addWidget(self.rightwiget, 0, 1)
        self.leftgrid = QtGui.QGridLayout()
        self.rightgrid = QtGui.QGridLayout()
        self.leftwiget.setLayout(self.leftgrid)
        self.rightwiget.setLayout(self.rightgrid)
        self.leftwiget.setObjectName("aboutLeft")
        self.rightwiget.setObjectName("aboutRight")
        self.rightwiget.setFixedWidth(180)

        # 左框架
        self.sywiget = QtGui.QWidget()
        self.sywiget.setObjectName("main_sy")  # 首页
        self.leftgrid.addWidget(self.sywiget, 0, 0)
        self.sygrid = QtGui.QGridLayout()
        self.sywiget.setLayout(self.sygrid)

        self.instructionsLabel = QtGui.QLabel(u"使用说明")
        self.instructionsLabel.setObjectName("instructionsLabel")
        self.instructionsLabel.setMaximumHeight(190)
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.sygrid.addWidget(self.instructionsLabel, 0, 1, 1, 3)

        def setsybtn(grid, btnName, row, column):
            """创建首页btn"""
            sybtn = QtGui.QPushButton(btnName)
            sybtn.setFixedSize(100, 30)
            sybtn.setObjectName("sybtn")
            grid.addWidget(sybtn, row, column)
            return sybtn

        self.sybtn1 = setsybtn(self.sygrid, u"声  明", 1, 0)
        self.sybtn2 = setsybtn(self.sygrid, u"食灵说明", 1, 1)
        self.sybtn3 = setsybtn(self.sygrid, u"计算说明", 1, 2)
        self.sybtn4 = setsybtn(self.sygrid, u"狙击说明", 1, 3)
        self.sybtn5 = setsybtn(self.sygrid, u"地图说明", 1, 4)
        self.sybtn1.clicked.connect(lambda: self.aboutViewEdit(1))
        self.sybtn2.clicked.connect(lambda: self.aboutViewEdit(2))
        self.sybtn3.clicked.connect(lambda: self.aboutViewEdit(3))
        self.sybtn4.clicked.connect(lambda: self.aboutViewEdit(4))
        self.sybtn5.clicked.connect(lambda: self.aboutViewEdit(5))

        self.syText = QtGui.QTextBrowser()
        self.syText.setObjectName("syText")
        self.syText.setFixedHeight(370)
        self.syText.append(u"\n◆欢迎使用本工具！初次使用可以在此处查看使用帮助，有任何疑问和建议可以联系作者。")
        self.syText.append(u"◆本工具灵感来自于《谁在呼唤舰队》，特此致敬")
        self.syText.append(u"◆本工具所有基础资源来自萌百黑大@划破黑夜,特此鸣谢")
        self.syText.append(u"◆本工具旨在辅助玩家了解游戏信息，工具界面大致还原游戏界面是为了让玩家对工具产生亲切感。禁止窃取、泄露本工具美术资源，任何非法和损害他人利益行为与作者无关！")
        self.sygrid.addWidget(self.syText, 3, 0, 1, 5)

        # 右框架
        self.text = QtGui.QTextEdit()
        self.text.setObjectName("rightInfo")
        # self.text.setHtml("<img src='ui/logo.png' width=10% heigth=10%>")
        self.text.append("<img src='ui/logo.png'>")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setTextColor(QtGui.QColor("#FFF3EE"))
        self.text.append(u"欢迎加入我们\nQQ群:621285038\n")
        # self.text.setTextColor(QtGui.QColor("#DC143C"))
        self.text.setFontPointSize(15)
        self.text.append(u"界面设计")
        self.text.setFontPointSize(10)
        self.text.append(u"呐呐\n玉引\n莉莉子\n")
        self.text.setFontPointSize(15)
        self.text.append(u"开发制作")
        self.text.setFontPointSize(10)
        self.text.append(u"莉莉子\n")
        self.text.setFontPointSize(15)
        self.text.append(u"数据")
        self.text.setFontPointSize(10)
        self.text.append(u"玉引\n")
        self.text.setFontPointSize(15)
        self.text.append(u"美工/UI")
        self.text.setFontPointSize(10)
        self.text.append(u"呐呐\n小四\n")
        self.text.append(u"bug或意见反馈,微博私信@Elza_Scarlet")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.rightgrid.addWidget(self.text, 0, 0)
        self.wigetIndex = [self.leftwiget, self.rightwiget]

    def aboutViewEdit(self, index):
        """首页编辑"""
        self.music.touchPlay()
        if index == 1:
            self.syText.clear()
            self.syText.append(u"\n◆欢迎使用本工具！初次使用可以在此处查看使用帮助，有任何疑问和建议可以联系作者。")
            self.syText.append(u"◆本工具灵感来自于《谁在呼唤舰队》，特此致敬")
            self.syText.append(u"◆本工具所有基础资源来自萌百黑大@划破黑夜,特此鸣谢")
            self.syText.append(u"◆本工具旨在辅助玩家了解游戏信息，工具界面大致还原游戏界面是为了让玩家对工具产生亲切感。禁止窃取、泄露本工具美术资源，任何非法和损害他人利益行为与作者无关！")
        elif index == 2:
            self.syText.clear()
            self.syText.append(u"\n◆食灵界面目前提供食灵列表和食灵详细信息查看")
            self.syText.append(u"◆食灵列表的满级数据为满品满强化满好感数据")
            self.syText.append(u"◆食灵列表的满级数据由推算得出，如有较大误差，请向制作组反馈")
            self.syText.append(u"◆搜索功能少女祈祷中...")
        elif index == 3:
            self.syText.clear()
            self.syText.append(u"\n◆等级计算中，当前经验非必填项，填写完等级和每局经验即可计算")
            self.syText.append(u"◆装备计算中，提供等级即可计算")
            self.syText.append(u"◆装备选择仅作一个粗略的计算，其中：")
            self.syText.append(u"　装备中非暴击和暴伤的加成将被忽略")
            self.syText.append(u"　装备对料理技的增益将被考虑，固有技仅显示，未计入")
            self.syText.append(u"　神厨7%加成应生效，未计入，在最终结果之后再乘1.07为正确结果")
            self.syText.append(u"　最高伤害计算方式为：面板攻击 *（暴击 * 暴伤）* 技能伤害")
            self.syText.append(u"　期望伤害计算方式为：面板攻击 *（（1-暴击）+ 暴击 * 暴伤）* 技能伤害")
        elif index == 4:
            self.syText.clear()
            self.syText.append(u"\n◆狙击公式大致提供了自由狙击供玩家使用")
            self.syText.append(u"◆狙击公式提供数值为最低出货数值，不保证概率，请洗脸后尝试")
        else:
            self.syText.clear()
            self.syText.append(u"\n◆该攻略为【使用最短天数通关攻略】，不一定适合开荒")
            self.syText.append(u"◆最短天数不一定意味着最低耗")
            self.syText.append(u"◆意在高效完成魔力炉和每日，治好多年强迫症")
            self.syText.append(u"◆速推攻略由小四制图，文字内容由萌百pai提供，感激~")
            self.syText.append(u"◆三蛋糕攻略已在【萌娘百科 料理次元】登陆，如有需要可前往萌百查询")

    def slDetail(self):
        """食灵详情"""
        indexColumn = self.tablewiget.currentColumn()
        if indexColumn == 0:
            pass
        else:
            return
        indexRow = self.tablewiget.currentRow()
        slnumb = self.tablewiget.item(indexRow, 1).text()
        sql = 'SELECT URL_LH,URL_LH2,"   "||SL_NAME,SL_LEVEL,TJ_JN,TJ_ZP,TJ_HP,TJ_GJ,TJ_GS,TJ_MZ,TJ_FY,TJ_SB,SKILL_NAME,SKILL_DESC,SKILL_GY_NAME,SKILL_GY_DESC,GROUP_DECS,SL_TYPE,ifnull(SL_STORY,""),"次数："||SKILL_COUNT,"消耗："||SKILL_CONS FROM "fairy_detail" WHERE SL_NO = ' + str(
            slnumb) + ';'
        # print sql
        info = ToolFunction.getsqliteInfo(sql, "llcy")
        # print info

        self.inibodywiget()

        self.detailWidget = QtGui.QWidget()
        self.detailFrameGrid = QtGui.QGridLayout()
        self.detailWidget.setLayout(self.detailFrameGrid)
        self.bodygrid.addWidget(self.detailWidget, 0, 0)
        self.detailWidget.setObjectName("SLdetail")
        self.detailFrameGrid.setColumnStretch(0, 1)
        self.detailFrameGrid.setColumnStretch(1, 1)

        # 左边贴图
        self.cuisineLable = QtGui.QLabel()
        self.cuisineLable.setObjectName("lhLabel")
        self.detailFrameGrid.addWidget(self.cuisineLable, 0, 0)
        try:
            decrypt(info[0][0], "temp/index1.png")
            decrypt(info[0][1], "temp/index2.png")
        except IOError:
            pass
        stylesheet = "QLabel#lhLabel{border-image: url('temp/index1.png');}" + \
                     "QLabel#lhLabel::hover{border-image: url('temp/index2.png');}"
        self.cuisineLable.setStyleSheet(stylesheet)

        # 右边窗体
        self.attributeList = QtGui.QTableWidget(23, 4)
        self.attributeList.setObjectName("sl_Attri")
        self.detailFrameGrid.addWidget(self.attributeList, 0, 1)
        self.attributeList.verticalHeader().setVisible(False)
        self.attributeList.horizontalHeader().setVisible(False)
        self.attributeList.setShowGrid(False)
        self.attributeList.setSpan(0, 0, 1, 3)
        self.attributeList.setSpan(1, 0, 1, 2)
        self.attributeList.setSpan(5, 0, 2, 4)
        self.attributeList.setSpan(8, 0, 2, 4)
        self.attributeList.setSpan(11, 0, 2, 4)
        self.attributeList.setSpan(14, 0, 9, 4)

        self.newItem = QtGui.QTableWidgetItem(info[0][2])
        self.lbp2 = QtGui.QLabel()
        self.lbp2.setPixmap(QtGui.QPixmap('ui/hero/' + str(info[0][17]) + '.png'))
        self.attributeList.setCellWidget(0, 0, self.lbp2)
        self.newItem.setFont(QtGui.QFont("youyuan", 16, 100))
        # self.newItem.setIcon(QtGui.QIcon('ui/hero/'+str(info[0][15])+'.png'))
        # self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.attributeList.setItem(0, 0, self.newItem)
        self.lbp2 = QtGui.QLabel()
        self.lbp2.setPixmap(QtGui.QPixmap('ui/hero/star' + str(info[0][3]) + '.png'))
        self.attributeList.setCellWidget(1, 0, self.lbp2)

        self.slDetailEdit(u'技能', info[0][4], 2, 0)
        self.slDetailEdit(u'生命', info[0][6], 2, 1)
        self.slDetailEdit(u'攻速', info[0][8], 2, 2)
        self.slDetailEdit(u'防御', info[0][10], 2, 3)
        self.slDetailEdit(u'装盘', info[0][5], 3, 0)
        self.slDetailEdit(u'攻击', info[0][7], 3, 1)
        self.slDetailEdit(u'命中', info[0][9], 3, 2)
        self.slDetailEdit(u'闪避', info[0][11], 3, 3)

        self.newItem = QtGui.QTableWidgetItem(u"料理技")
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.newItem.setFont(QtGui.QFont("youyuan", 16, 100))
        self.attributeList.setItem(4, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][12])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(4, 1, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][19])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(4, 2, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][20])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(4, 3, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][13])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(5, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(u"固有技")
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.newItem.setFont(QtGui.QFont("youyuan", 14, 100))
        self.attributeList.setItem(7, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][14])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(7, 1, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][15])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(8, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(u"装盘效果")
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.newItem.setFont(QtGui.QFont("youyuan", 14, 100))
        self.attributeList.setItem(10, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][16])
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(11, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(u"食灵简介")
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.newItem.setFont(QtGui.QFont("youyuan", 14, 100))
        self.attributeList.setItem(13, 0, self.newItem)

        self.newItem = QtGui.QTableWidgetItem(info[0][18])
        self.newItem.setTextAlignment(QtCore.Qt.AlignTop)
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)
        self.attributeList.setItem(14, 0, self.newItem)

        self.wigetIndex = [self.detailWidget]

    def slDetailEdit(self, attr, info, row, column):
        """食灵详情数据填充"""
        msg = attr + "  " + str(info)
        iconUrl = {u"技能": 'ui/hero/skill.png', u"装盘": 'ui/hero/skill.png', u"生命": 'ui/hero/hp.png',
                   u"攻击": 'ui/hero/atk.png', u"攻速": 'ui/hero/atkSpeed.png', u"命中": 'ui/hero/hit.png',
                   u"防御": 'ui/hero/phyDef.png', u"闪避": 'ui/hero/miss.png', }
        self.newItem = QtGui.QTableWidgetItem(msg)
        self.newItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.newItem.setFlags(QtCore.Qt.ItemIsEnabled)  # 不允许点击表格内容
        self.newItem.setIcon(QtGui.QIcon(iconUrl[attr]))
        self.attributeList.setItem(row, column, self.newItem)

    def fortest(self):
        print "ok"


class Music:
    def __init__(self):
        path = "music/ui/se_ui_001_x_2.mp3"
        self.touth = Phonon.createPlayer(Phonon.MusicCategory, Phonon.MediaSource(path))

    def touchPlay(self):
        self.touth.stop()
        self.touth.play()


class ToolFunction:
    def __init__(self):
        pass

    @staticmethod
    def getsqliteInfo(sql, dbName):
        con = sqlite3.connect(dbName)
        cur = con.cursor()
        cur.execute(sql)
        info = cur.fetchall()
        cur.close()
        return info

    @staticmethod
    def getsql(sqlurl):
        sqlfile = open(sqlurl, "rb")
        sql = sqlfile.read()
        sqlfile.close()
        return sql

    @staticmethod
    def deleteFile(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                fullpath = os.path.join(dirpath, filename)
                os.remove(fullpath)


def decrypt(images_path, imgUrl):
    f = open(images_path, 'rb')
    filedata = f.read()
    filesize = f.tell()
    f.close()

    info = base64.b64decode(filedata)
    file_byte_array = bytearray(info)

    decrypt_file_byte_array = bytearray(0)
    for byte in file_byte_array:
        decrypt_bype = byte ^ encrypt_key
        decrypt_file_byte_array.append(decrypt_bype)

    # os.remove(images_path)
    f2 = open(imgUrl, 'wb')
    f2.write(decrypt_file_byte_array)
    f2.close()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainProject()
    ex.show()
    sys.exit(app.exec_())


encrypt_key = 95
slTpyeDictory = {
    "1": u"主食", "2": u"主菜", "3": u"副菜", "4": u"甜点", "5": u"头盘", "6": u"汤饮",
    1: u"主食", 2: u"主菜", 3: u"副菜", 4: u"甜点", 5: u"头盘", 6: u"汤饮",
}

if __name__ == '__main__':
    main()
