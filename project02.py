import hou
import importlib

from PySide2 import QtWidgets, QtGui, QtCore
import Project2_ui

# signal (ui) - slot (funtion)

class Custom(QtWidgets.QWidget, Project2_ui.Ui_Form):

    def __init__(self, parent=None):
        #super(Custom, self).__init__(parent)
        pass
        #self.signalfunc()

        self.__node = hou.node('/obj/geo1/controller')


    def signalfunc(self):
        self.doubleSpinBox_location_x.valueChanged.connect(self.slot_locationx)
        self.doubleSpinBox_location_y.valueChanged.connect(self.slot_locationy)
        self.doubleSpinBox_location_z.valueChanged.connect(self.slot_locationz)
        self.radioButton_scale_lock.toggled.connect(self.slot_locationlock)
        self.pushButton_location_reset.clicked.connect(self.slot)

        self.doubleSpinBox_rotation_x.valueChanged.connect()
        self.doubleSpinBox_rotation_y.valueChanged.connect()
        self.doubleSpinBox_rotation_z.valueChanged.connect()

        self.doubleSpinBox_scale_x.valueChanged.connect()
        self.doubleSpinBox_scale_y.valueChanged.connect()
        self.doubleSpinBox_scale_z.valueChanged.connect()
        self.horizontalSlider_scale_uniform.valueChanged.connect()


    def slot_locationx(self, val):
        if (self.slot_locationlock==True):
            return
        self.node.parm('locationx').set(val)

    def slot_locationy(self, val):
        if (self.slot_locationlock == True):
            return
        self.node.parm('locatiny').set(val)

    def slot_locationz(self, val):
        if (self.slot_locationlock == True):
            return
        self.node.parm('locationz').set(val)

    def slot_locationlock(self, val: bool):
        return val


    @property
    def node(self):
        return self.__node

    #@node.setter
    #def node(self):
    #    self.__node = lamda

