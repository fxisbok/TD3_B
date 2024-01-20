# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Project2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(545, 535)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_Scale = QGroupBox(self.tab_3)
        self.groupBox_Scale.setObjectName(u"groupBox_Scale")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_Scale)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.doubleSpinBox_scale_x = QDoubleSpinBox(self.groupBox_Scale)
        self.doubleSpinBox_scale_x.setObjectName(u"doubleSpinBox_scale_x")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_scale_x)

        self.doubleSpinBox_scale_y = QDoubleSpinBox(self.groupBox_Scale)
        self.doubleSpinBox_scale_y.setObjectName(u"doubleSpinBox_scale_y")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_scale_y)

        self.doubleSpinBox_scale_z = QDoubleSpinBox(self.groupBox_Scale)
        self.doubleSpinBox_scale_z.setObjectName(u"doubleSpinBox_scale_z")

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_scale_z)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_scale_lock = QRadioButton(self.groupBox_Scale)
        self.radioButton_scale_lock.setObjectName(u"radioButton_scale_lock")

        self.horizontalLayout_8.addWidget(self.radioButton_scale_lock)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.pushButton_scale_reset = QPushButton(self.groupBox_Scale)
        self.pushButton_scale_reset.setObjectName(u"pushButton_scale_reset")

        self.horizontalLayout_8.addWidget(self.pushButton_scale_reset)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.groupBox_Scale)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.horizontalSlider_scale_uniform = QSlider(self.groupBox_Scale)
        self.horizontalSlider_scale_uniform.setObjectName(u"horizontalSlider_scale_uniform")
        self.horizontalSlider_scale_uniform.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.horizontalSlider_scale_uniform)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.groupBox_Scale, 2, 0, 1, 1)

        self.groupBox_Rotation = QGroupBox(self.tab_3)
        self.groupBox_Rotation.setObjectName(u"groupBox_Rotation")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_Rotation)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.doubleSpinBox_rotation_x = QDoubleSpinBox(self.groupBox_Rotation)
        self.doubleSpinBox_rotation_x.setObjectName(u"doubleSpinBox_rotation_x")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_rotation_x)

        self.doubleSpinBox_rotation_y = QDoubleSpinBox(self.groupBox_Rotation)
        self.doubleSpinBox_rotation_y.setObjectName(u"doubleSpinBox_rotation_y")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_rotation_y)

        self.doubleSpinBox_rotation_z = QDoubleSpinBox(self.groupBox_Rotation)
        self.doubleSpinBox_rotation_z.setObjectName(u"doubleSpinBox_rotation_z")

        self.horizontalLayout_4.addWidget(self.doubleSpinBox_rotation_z)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_rotation_lock = QRadioButton(self.groupBox_Rotation)
        self.radioButton_rotation_lock.setObjectName(u"radioButton_rotation_lock")

        self.horizontalLayout.addWidget(self.radioButton_rotation_lock)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_rotation_reset = QPushButton(self.groupBox_Rotation)
        self.pushButton_rotation_reset.setObjectName(u"pushButton_rotation_reset")
        self.pushButton_rotation_reset.setBaseSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.pushButton_rotation_reset)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox_Rotation, 1, 0, 1, 1)

        self.groupBox_Location = QGroupBox(self.tab_3)
        self.groupBox_Location.setObjectName(u"groupBox_Location")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_Location)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.doubleSpinBox_location_x = QDoubleSpinBox(self.groupBox_Location)
        self.doubleSpinBox_location_x.setObjectName(u"doubleSpinBox_location_x")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_location_x)

        self.doubleSpinBox_location_y = QDoubleSpinBox(self.groupBox_Location)
        self.doubleSpinBox_location_y.setObjectName(u"doubleSpinBox_location_y")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_location_y)

        self.doubleSpinBox_location_z = QDoubleSpinBox(self.groupBox_Location)
        self.doubleSpinBox_location_z.setObjectName(u"doubleSpinBox_location_z")

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_location_z)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_location_lock = QRadioButton(self.groupBox_Location)
        self.radioButton_location_lock.setObjectName(u"radioButton_location_lock")

        self.horizontalLayout_6.addWidget(self.radioButton_location_lock)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.pushButton_location_reset = QPushButton(self.groupBox_Location)
        self.pushButton_location_reset.setObjectName(u"pushButton_location_reset")

        self.horizontalLayout_6.addWidget(self.pushButton_location_reset)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.groupBox_Location, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_Scale.setTitle(QCoreApplication.translate("Form", u"Scale", None))
        self.radioButton_scale_lock.setText(QCoreApplication.translate("Form", u"lock", None))
        self.pushButton_scale_reset.setText(QCoreApplication.translate("Form", u"reset", None))
        self.label.setText(QCoreApplication.translate("Form", u"Uniform scale", None))
        self.groupBox_Rotation.setTitle(QCoreApplication.translate("Form", u"Rotation", None))
        self.radioButton_rotation_lock.setText(QCoreApplication.translate("Form", u"lock", None))
        self.pushButton_rotation_reset.setText(QCoreApplication.translate("Form", u"reset", None))
        self.groupBox_Location.setTitle(QCoreApplication.translate("Form", u"Location", None))
        self.radioButton_location_lock.setText(QCoreApplication.translate("Form", u"lock", None))
        self.pushButton_location_reset.setText(QCoreApplication.translate("Form", u"reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Transform", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"File", None))
    # retranslateUi

