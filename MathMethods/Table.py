from PyQt4 import QtGui, QtCore
import numpy as num

class Table(QtGui.QTableWidget):

    def __init__(self, quantity_main_variables, quantity_additional_variables, parent=None):

        QtGui.QTableWidget.__init__(self, parent)

        self.setColumnCount(quantity_main_variables + quantity_additional_variables+ 2)
        self.setRowCount(quantity_additional_variables + 1)
        self.__quantityVariables = quantity_additional_variables + quantity_main_variables

        self.__main_variable_count = quantity_main_variables
        self.__additional_variable_count = quantity_additional_variables
        self.setMinimumHeight(300)
        #self.setAutoScroll(False)
        self.__fill_zeros()
        self.show()

    def __fill_zeros(self):

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QtGui.QTableWidgetItem("0"))

        self.setHorizontalHeaderLabels(["B"]+["X"+str(x) for x in range(1, self.columnCount()-1, 1)]+["Min"])
        self.setVerticalHeaderLabels(["S"+str(x+self.__main_variable_count) for x in range(1, self.rowCount(), 1)]+["F"])

    def __collect_data(self):

        array = num.zeros(shape=(self.rowCount(),self.columnCount()))
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = self.item(i,j)
                array[i][j] = item.text()

        # for i in range(array.shape[0]):
        #     array[i][array.shape[1]-1] = 0

        return array

    def get_array(self):

        return self.__collect_data()

    def get_vertical_headers(self) -> list:

        headers = list()
        for row_index in range(self.rowCount()):
            item = self.verticalHeaderItem(row_index)
            headers.append(item.text())

        return headers

    def set_vertical_headers(self,arrayNames):

        self.setVerticalHeaderLabels(arrayNames)

    def set_array(self, array_values):

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                iteam = self.item(i, j)
                iteam.setText(str(array_values[i][j]))
        pass


