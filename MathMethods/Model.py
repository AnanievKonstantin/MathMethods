from PyQt4 import QtGui, QtCore
import numpy as num


class Model(QtCore.QObject):

    calculationSuccess = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        pass

    def calculate_simplex_method(self,array):
        print(array)
        print("start: calculate_simplex_method")
        mainCol = self.__find_main_column();
        mainRow = self.__find_main_row();
        self.__rect_method(mainCol,mainRow,array)
        print("end: calculate_simplex_method")


        return array

    def __find_main_column(self):
        print("__find_main_column")
        return 0


    def __find_main_row(self):
        print("__find_main_row")
        return 0

    def __rect_method(self, col, row, array):
        print("__rect_method")
        pass