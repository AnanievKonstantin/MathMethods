import sys
from PyQt4 import QtGui, QtCore
import numpy as num
from MathMethods import Table, Model, Control_panel


class Controller(QtGui.QApplication):

    def __init__(self,parent=None):
        QtGui.QApplication.__init__(self, sys.argv)

        self.__lay = QtGui.QVBoxLayout()
        self.__window = QtGui.QWidget()
        self.__window.setWindowTitle("MM")
        self.__table_list = list()
        self.__label_list = list()
        self.__model = Model.Model()
        self.__step_number = 0

        self.__control_panel = Control_panel.Control_panel()

        self.__build_window()
        self.__to_scatter__action()

        self.__window.show()

    def play(self):
        self.exec_()

    def __create_table(self, name,var_count):
        label = QtGui.QLabel(name)
        self.__lay.addWidget(label)

        table = Table.Table(var_count)
        self.__lay.addWidget(table)
        self.__table_list.append(table)
        self.__label_list.append(label)

        return table

    def __build_window(self):
        self.__window.setLayout(self.__lay)
        self.__lay.addWidget(self.__control_panel)

    def __to_scatter__action(self):
        """
        Установит отклик на сигналы от панели управления
        :return:
        """
        self.__control_panel.connect(self.__control_panel, QtCore.SIGNAL("apply_signal(int)"),
                                     self, QtCore.SLOT("apply_table_data(int)"))

        self.__control_panel.connect(self.__control_panel, QtCore.SIGNAL("calc_signal()"),
                                     self, QtCore.SLOT("calculate()"))

    @QtCore.pyqtSlot()
    def calculate(self):
        if len(self.__table_list) != 0:
            #current_table = self.__create_table("Step: "+str(self.__step_number),3)
            a = 3

        else:
            print("Empty table")

    @QtCore.pyqtSlot(int)
    def apply_table_data(self, var_count):
        for table in self.__table_list:
            self.__lay.removeWidget(table)
            table.close()

        for label in self.__label_list:
            self.__lay.removeWidget(label)
            # label.widget().deleteLater()
            #self.__lay.itemAt(0).widget().close()

        self.__table_list.clear()
        self.__label_list.clear()
        self.__step_number = 0
        self.__create_table("First", var_count)

