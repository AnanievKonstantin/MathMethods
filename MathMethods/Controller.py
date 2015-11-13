import sys
from PyQt4 import QtGui, QtCore
import numpy as num
from MathMethods import Table, Model, Control_panel


class Controller(QtGui.QApplication):

    def __init__(self,parent=None):
        QtGui.QApplication.__init__(self, sys.argv)

        self.__lay = QtGui.QVBoxLayout()
        self.__window = QtGui.QWidget()
        self.__window.setLayout(self.__lay)
        self.__window.setWindowTitle("MM")
        self.__table_list = list()
        self.__label_list = list()

        self.__window.show()

    def play(self):
        self.exec_()

    def __create_table(self, name):
        self.__lay.addWidget(QtGui.QLabel(name))

        table = Table.Table(2)
        self.__lay.addWidget(table)
        self.__table_list.append(table)

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
