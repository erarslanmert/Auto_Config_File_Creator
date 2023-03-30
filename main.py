import time

from PyQt5 import QtCore, QtGui, QtWidgets
import math
import threading
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QLabel, qApp
import multiprocessing

coord_3 = [0,0]
coord_3_imaginary = [0,0]
coord_s3 = [0,0]
coord_s3_imaginary = [0,0]
coord_t3 = [0,0]
coord_t3_imaginary = [0,0]
coord_f3 = [0,0]
coord_f3_imaginary = [0,0]



class DraggableGraphicsItemSignaller(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPointF)

    def __init__(self):
        super().__init__()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 130, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 91, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 91, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 41))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 10, 111, 41))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 91, 41))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 290, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 210, 141, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 280, 91, 41))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 91, 41))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 250, 141, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 370, 141, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 360, 91, 41))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(120, 410, 141, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 440, 91, 41))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(120, 450, 141, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 400, 91, 41))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 530, 141, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 520, 91, 41))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 570, 141, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 600, 91, 41))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 610, 141, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 560, 91, 41))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(230, 20, 31, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 170, 111, 41))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(230, 180, 31, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 330, 111, 41))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(230, 340, 31, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(120, 490, 111, 41))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(230, 500, 31, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 21, 16))
        self.label.setObjectName("label")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(270, 90, 21, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(270, 130, 21, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(270, 290, 21, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(270, 250, 21, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(270, 210, 21, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(270, 450, 21, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(270, 410, 21, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(270, 370, 21, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(270, 610, 21, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(270, 570, 21, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(270, 530, 21, 16))
        self.label_28.setObjectName("label_28")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 20, 681, 611))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 660, 991, 141))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(5)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.DraggableRectItem = self.make_GraphicsItem_draggable(QtWidgets.QGraphicsEllipseItem)
        self.DraggableRectItem_2 = self.make_GraphicsItem_draggable_2(QtWidgets.QGraphicsEllipseItem)
        self.DraggableRectItem_3 = self.make_GraphicsItem_draggable_3(QtWidgets.QGraphicsEllipseItem)
        self.DraggableRectItem_4 = self.make_GraphicsItem_draggable_4(QtWidgets.QGraphicsEllipseItem)
        self.scene = QtWidgets.QGraphicsScene(340,20,661,601)

        self.handle_item = self.DraggableRectItem()
        self.handle_item.setRect(805, 451, 35, 35)
        self.scene.addItem(self.handle_item)
        self.handle_item_2 = self.DraggableRectItem_2()
        self.handle_item_2.setRect(505, 451, 35, 35)
        self.scene.addItem(self.handle_item_2)
        self.handle_item_3 = self.DraggableRectItem_3()
        self.handle_item_3.setRect(805, 151, 35, 35)
        self.scene.addItem(self.handle_item_3)
        self.handle_item_4 = self.DraggableRectItem_4()
        self.handle_item_4.setRect(505, 151, 35, 35)
        self.scene.addItem(self.handle_item_4)

        self.pixmap = QPixmap("AMMS.png")
        self.pixmapitem = self.scene.addPixmap(self.pixmap)
        self.pixmapitem.moveBy(750, 400)
        self.pixmap_2 = QPixmap("AMMS.png")
        self.pixmapitem_2 = self.scene.addPixmap(self.pixmap_2)
        self.pixmapitem_2.moveBy(450, 400)
        self.pixmap_3 = QPixmap("AMMS.png")
        self.pixmapitem_3 = self.scene.addPixmap(self.pixmap_3)
        self.pixmapitem_3.moveBy(756, 100)
        self.pixmap_4 = QPixmap("AMMS.png")
        self.pixmapitem_4 = self.scene.addPixmap(self.pixmap_3)
        self.pixmapitem_4.moveBy(456, 100)
        
        self.line = QtWidgets.QGraphicsLineItem(825,470,525,470)
        self.scene.addItem(self.line)
        self.text = QtWidgets.QGraphicsTextItem('150 cm')
        self.scene.addItem(self.text)
        self.text.moveBy(675,470)

        self.line_2 = QtWidgets.QGraphicsLineItem(825, 470, 825, 170)
        self.scene.addItem(self.line_2)
        self.text_2 = QtWidgets.QGraphicsTextItem('150 cm')
        self.scene.addItem(self.text_2)
        self.text_2.moveBy(825, 320)

        self.line_3 = QtWidgets.QGraphicsLineItem(825, 470, 525, 170)
        self.scene.addItem(self.line_3)
        self.text_3 = QtWidgets.QGraphicsTextItem('212 cm')
        self.scene.addItem(self.text_3)
        self.text_3.moveBy(675, 320)

        self.line_4 = QtWidgets.QGraphicsLineItem(525, 470, 525, 170)
        self.scene.addItem(self.line_4)
        self.text_4 = QtWidgets.QGraphicsTextItem('150 cm')
        self.scene.addItem(self.text_4)
        self.text_4.moveBy(525, 320)

        self.line_5 = QtWidgets.QGraphicsLineItem(525, 470, 825, 170)
        self.scene.addItem(self.line_5)
        self.text_5 = QtWidgets.QGraphicsTextItem('212 cm')
        self.scene.addItem(self.text_5)
        self.text_5.moveBy(675, 320)

        self.line_6 = QtWidgets.QGraphicsLineItem(525, 170, 825, 170)
        self.scene.addItem(self.line_6)
        self.text_6 = QtWidgets.QGraphicsTextItem('150 cm')
        self.scene.addItem(self.text_6)
        self.text_6.moveBy(675, 170)
        
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.horizontalLayout.addWidget(self.view)

        t1 = threading.Thread(target=lambda:self.update_scene())
        t1.start()

    def update_scene(self):
        global coord_3, coord_3_imaginary
        global coord_s3, coord_s3_imaginary
        global coord_t3, coord_t3_imaginary
        global coord_f3, coord_f3_imaginary
        while True:
            if float(coord_3_imaginary[0]) != float(coord_3[0]) and float(coord_3_imaginary[1]) != float(coord_3[1]):
                self.scene.removeItem(self.pixmapitem)
                self.scene.removeItem(self.line)
                self.scene.removeItem(self.text)
                self.scene.removeItem(self.line_2)
                self.scene.removeItem(self.text_2)
                self.scene.removeItem(self.line_3)
                self.scene.removeItem(self.text_3)
                self.pixmapitem.setPos(750 + float(coord_3[0]), 400 + float(coord_3[1]))
                coord_3_imaginary = coord_3
                distance = ((((825 + float(coord_3[0])) - (525 + float(coord_s3[0]))) ** 2 +
                             ((470 + float(coord_3[1])) - (470 + float(coord_s3[1]))) ** 2) ** 0.5) / 2
                self.line = QtWidgets.QGraphicsLineItem(825 + float(coord_3[0]), 470 + float(coord_3[1]),
                                                        525 + float(coord_s3[0]), 470 + float(coord_s3[1]))
                self.text = QtWidgets.QGraphicsTextItem(str(int(distance)) + 'cm')
                self.text.setPos((825 + float(coord_3[0]) + 525 + float(coord_s3[0])) / 2,
                                 (470 + float(coord_3[1]) + 470 + float(coord_s3[1])) / 2)
                distance_2 = ((((825 + float(coord_3[0])) - (825 + float(coord_t3[0]))) ** 2 +
                               ((470 + float(coord_3[1])) - (170 + float(coord_t3[1]))) ** 2) ** 0.5) / 2
                self.line_2 = QtWidgets.QGraphicsLineItem(825 + float(coord_3[0]), 470 + float(coord_3[1]),
                                                          825 + float(coord_t3[0]), 170 + float(coord_t3[1]))
                self.text_2 = QtWidgets.QGraphicsTextItem(str(int(distance_2)) + 'cm')
                self.text_2.setPos((825 + float(coord_3[0]) + 825 + float(coord_t3[0])) / 2,
                                   (470 + float(coord_3[1]) + 170 + float(coord_t3[1])) / 2)
                distance_3 = ((((825 + float(coord_3[0])) - (525 + float(coord_f3[0]))) ** 2 +
                               ((470 + float(coord_3[1])) - (170 + float(coord_f3[1]))) ** 2) ** 0.5) / 2
                self.line_3 = QtWidgets.QGraphicsLineItem(825 + float(coord_3[0]), 470 + float(coord_3[1]),
                                                          525 + float(coord_f3[0]), 170 + float(coord_f3[1]))
                self.text_3 = QtWidgets.QGraphicsTextItem(str(int(distance_3)) + 'cm')
                self.text_3.setPos((825 + float(coord_3[0]) + 525 + float(coord_f3[0])) / 2,
                                   (470 + float(coord_3[1]) + 170 + float(coord_f3[1])) / 2)

                self.scene.addItem(self.pixmapitem)
                self.scene.addItem(self.line)
                self.scene.addItem(self.text)
                self.scene.addItem(self.line_2)
                self.scene.addItem(self.text_2)
                self.scene.addItem(self.line_3)
                self.scene.addItem(self.text_3)

            elif float(coord_s3_imaginary[0]) != float(coord_s3[0]) and\
                    float(coord_s3_imaginary[1]) != float(coord_s3[1]):
                self.scene.removeItem(self.pixmapitem_2)
                self.scene.removeItem(self.line)
                self.scene.removeItem(self.text)
                self.scene.removeItem(self.line_4)
                self.scene.removeItem(self.text_4)
                self.scene.removeItem(self.line_5)
                self.scene.removeItem(self.text_5)
                self.pixmapitem_2.setPos(450 + float(coord_s3[0]), 400 + float(coord_s3[1]))
                coord_s3_imaginary = coord_s3
                distance = ((((825 + float(coord_3[0])) - (525 + float(coord_s3[0]))) ** 2 +
                             ((470 + float(coord_3[1])) - (470 + float(coord_s3[1]))) ** 2) ** 0.5) / 2
                self.line = QtWidgets.QGraphicsLineItem(825 + float(coord_3[0]), 470 + float(coord_3[1]),
                                                        525 + float(coord_s3[0]), 470 + float(coord_s3[1]))
                self.text = QtWidgets.QGraphicsTextItem(str(int(distance)) + 'cm')
                self.text.setPos((825 + float(coord_3[0]) + 525 + float(coord_s3[0])) / 2,
                                 (470 + float(coord_3[1]) + 470 + float(coord_s3[1])) / 2)
                distance_4 = ((((525 + float(coord_s3[0])) - (825 + float(coord_t3[0]))) ** 2 +
                               ((470 + float(coord_s3[1])) - (170 + float(coord_t3[1]))) ** 2) ** 0.5) / 2
                self.line_4 = QtWidgets.QGraphicsLineItem(825 + float(coord_3[0]), 470 + float(coord_3[1]),
                                                          825 + float(coord_t3[0]), 170 + float(coord_t3[1]))
                self.text_4 = QtWidgets.QGraphicsTextItem(str(int(distance_4)) + 'cm')
                self.text_4.setPos((525 + float(coord_s3[0]) + 825 + float(coord_t3[0])) / 2,
                                   (470 + float(coord_s3[1]) + 170 + float(coord_t3[1])) / 2)
                distance_5 = ((((525 + float(coord_s3[0])) - (525 + float(coord_f3[0]))) ** 2 +
                               ((470 + float(coord_s3[1])) - (170 + float(coord_f3[1]))) ** 2) ** 0.5) / 2
                self.line_5 = QtWidgets.QGraphicsLineItem(825 + float(coord_3[0]), 470 + float(coord_3[1]),
                                                          525 + float(coord_f3[0]), 170 + float(coord_f3[1]))
                self.text_5 = QtWidgets.QGraphicsTextItem(str(int(distance_5)) + 'cm')
                self.text_5.setPos((525 + float(coord_s3[0]) + 525 + float(coord_f3[0])) / 2,
                                   (470 + float(coord_s3[1]) + 170 + float(coord_f3[1])) / 2)
                self.scene.addItem(self.pixmapitem_2)
                self.scene.addItem(self.line)
                self.scene.addItem(self.text)
                self.scene.addItem(self.line_4)
                self.scene.addItem(self.text_4)
                self.scene.addItem(self.line_5)
                self.scene.addItem(self.text_5)

            elif float(coord_t3_imaginary[0]) != float(coord_t3[0]) and\
                    float(coord_t3_imaginary[1]) != float(coord_t3[1]):
                self.pixmapitem_3.setPos(750 + float(coord_t3[0]), 100 + float(coord_t3[1]))
                self.pixmapitem_3.update()
                coord_t3_imaginary = coord_t3

            elif float(coord_f3_imaginary[0]) != float(coord_f3[0]) and float(coord_f3_imaginary[1]) != float(
                    coord_f3[1]):
                self.pixmapitem_4.setPos(450 + float(coord_f3[0]), 100 + float(coord_f3[1]))
                self.pixmapitem_4.update()
                coord_f3_imaginary = coord_f3
            else:
                pass

    def make_GraphicsItem_draggable(self, parent):
        global coord_3
        class DraggableGraphicsItem(parent):
            def __init__(self, *args, **kwargs):
                parent.__init__(self, *args, **kwargs)
                self.parent = parent
                self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable |
                              QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
                self.signaller = DraggableGraphicsItemSignaller()
            def itemChange(self, change, value):
                global coord_3
                if change == QtWidgets.QGraphicsItem.ItemPositionChange:
                    self.signaller.positionChanged.emit(value)
                    coord = str(value).split("(")
                    coord_2 = coord[-1].split(")")
                    coord_3 = coord_2[0].split(", ")
                return parent.itemChange(self, change, value)

        return DraggableGraphicsItem

    def make_GraphicsItem_draggable_2(self, parent):
        global coord_s3
        class DraggableGraphicsItem(parent):
            def __init__(self, *args, **kwargs):
                parent.__init__(self, *args, **kwargs)
                self.parent = parent
                self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable |
                              QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
                self.signaller = DraggableGraphicsItemSignaller()
            def itemChange(self, change, value):
                global coord_s3
                if change == QtWidgets.QGraphicsItem.ItemPositionChange:
                    self.signaller.positionChanged.emit(value)
                    coord = str(value).split("(")
                    coord_2 = coord[-1].split(")")
                    coord_s3 = coord_2[0].split(", ")
                return parent.itemChange(self, change, value)

        return DraggableGraphicsItem

    def make_GraphicsItem_draggable_3(self, parent):
        global coord_t3
        class DraggableGraphicsItem(parent):
            def __init__(self, *args, **kwargs):
                parent.__init__(self, *args, **kwargs)
                self.parent = parent
                self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable |
                              QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
                self.signaller = DraggableGraphicsItemSignaller()
            def itemChange(self, change, value):
                global coord_t3
                if change == QtWidgets.QGraphicsItem.ItemPositionChange:
                    self.signaller.positionChanged.emit(value)
                    coord = str(value).split("(")
                    coord_2 = coord[-1].split(")")
                    coord_t3 = coord_2[0].split(", ")
                return parent.itemChange(self, change, value)

        return DraggableGraphicsItem

    def make_GraphicsItem_draggable_4(self, parent):
        global coord_f3
        class DraggableGraphicsItem(parent):
            def __init__(self, *args, **kwargs):
                parent.__init__(self, *args, **kwargs)
                self.parent = parent
                self.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable |
                              QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
                self.signaller = DraggableGraphicsItemSignaller()
            def itemChange(self, change, value):
                global coord_f3
                if change == QtWidgets.QGraphicsItem.ItemPositionChange:
                    self.signaller.positionChanged.emit(value)
                    coord = str(value).split("(")
                    coord_2 = coord[-1].split(")")
                    coord_f3 = coord_2[0].split(", ")
                return parent.itemChange(self, change, value)

        return DraggableGraphicsItem

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VCASTLE - Mission File Generator"))
        self.label_2.setText(_translate("MainWindow", "Distance to Third AMMS"))
        self.label_3.setText(_translate("MainWindow", "Distance to Seconder AMMS"))
        self.label_4.setText(_translate("MainWindow", "Distance to Fourth AMMS"))
        self.label_5.setText(_translate("MainWindow", "Primer AMMS  -   NO:"))
        self.label_6.setText(_translate("MainWindow", "Distance to Primer AMMS"))
        self.label_8.setText(_translate("MainWindow", "Distance to Fourth AMMS"))
        self.label_9.setText(_translate("MainWindow", "Distance to Third AMMS"))
        self.label_10.setText(_translate("MainWindow", "Distance to Primer AMMS"))
        self.label_12.setText(_translate("MainWindow", "Distance to Fourth AMMS"))
        self.label_13.setText(_translate("MainWindow", "Distance to Seconder AMMS"))
        self.label_14.setText(_translate("MainWindow", "Distance to Primer AMMS"))
        self.label_16.setText(_translate("MainWindow", "Distance to Third AMMS"))
        self.label_17.setText(_translate("MainWindow", "Distance to Seconder AMMS"))
        self.label_7.setText(_translate("MainWindow", "Seconder AMMS - NO:"))
        self.label_11.setText(_translate("MainWindow", "Third AMMS   -    NO:"))
        self.label_15.setText(_translate("MainWindow", "Fourth AMMS  -   NO:"))
        self.label.setText(_translate("MainWindow", "cm"))
        self.label_18.setText(_translate("MainWindow", "cm"))
        self.label_19.setText(_translate("MainWindow", "cm"))
        self.label_20.setText(_translate("MainWindow", "cm"))
        self.label_21.setText(_translate("MainWindow", "cm"))
        self.label_22.setText(_translate("MainWindow", "cm"))
        self.label_23.setText(_translate("MainWindow", "cm"))
        self.label_24.setText(_translate("MainWindow", "cm"))
        self.label_25.setText(_translate("MainWindow", "cm"))
        self.label_26.setText(_translate("MainWindow", "cm"))
        self.label_27.setText(_translate("MainWindow", "cm"))
        self.label_28.setText(_translate("MainWindow", "cm"))


def createmissiondialog():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

t = threading.Thread(target=createmissiondialog)
t.start()
