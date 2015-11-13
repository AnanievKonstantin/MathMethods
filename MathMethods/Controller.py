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
        self.__control_panel = Control_panel.Control_panel()

        self.__build_window()
        self.__to_scatter__action()

        self.__window.show()

    def play(self):
        self.exec_()

    def __create_table(self, name,var_count):
        self.__lay.addWidget(QtGui.QLabel(name))

        table = Table.Table(var_count)
        self.__lay.addWidget(table)
        self.__table_list.append(table)

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

        self.__control_panel.connect(self.__control_panel, QtCore.SIGNAL("calc_signal(int)"),
                                     self, QtCore.SLOT("calculate()"))

    @QtCore.pyqtSlot()
    def calculate(self):
        if len(self.__table_list) != 0:
            #calc
            a = 3
        else:
            print("Empty table")

    @QtCore.pyqtSlot(int)
    def apply_table_data(self, var_count):
        self.__create_table("First", var_count)


# def main():

#
#     table = Table.Table(2)
#     table2 = Table.Table(3)
#     table3 = Table.Table(4)
#     lay.addWidget(table)
#     lay.addWidget(table2)
#     lay.addWidget(table3)
#     window.setLayout(lay)
#
#     model = Model.Model()
#
#     btn = QtGui.QPushButton("I BTN")
#     btn.connect(btn, QtCore.SIGNAL("clicked()"),
#                 lambda: model.calculate_simplex_method(table.get_array()))
#
#     # model.connect(model,QtCore.SIGNAL("calculationSuccess(int)"),
#     #               lambda : table.setArry(model.getArray()))
#
#     lay.addWidget(btn)
#

#
# main()
