from PyQt4 import QtGui, QtCore
import numpy as num

class Table(QtGui.QTableWidget):

    def __init__(self, quantityVariables, parent=None):
        QtGui.QTableWidget.__init__(self, parent)
        self.setColumnCount(quantityVariables*2 + 3)
        self.setRowCount(quantityVariables + 1)
        self.__quantityVariables = quantityVariables

        self.__fill_zeros()

        self.show()

    tableData = QtCore.pyqtSignal(num.ndarray)

    def __fill_zeros(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QtGui.QTableWidgetItem("0"))

        self.setHorizontalHeaderLabels(["Базис","B"]+[str(x) for x in range(1, self.columnCount()-2, 1)]+["Min"])
        self.setVerticalHeaderLabels([str(x+self.__quantityVariables) for x in range(1, self.rowCount(), 1)]+["F"])


    @QtCore.pyqtSlot()
    def emit_signal_to_send_data(self):
        ''' Give evidence that a bag was punched. '''
        array = self.__collect()
        print("0")
        self.tableData.emit(array)

    def __collect(self):
        array = num.zeros(shape=(self.rowCount(),self.columnCount()))
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = self.item(i,j)
                array[i][j] = item.text()
        return array

    def get_array(self):
        return self.__collect()

    def set_vertical_headers(self,arrayNames):
        self.setVerticalHeaderLabels(arrayNames)

    def set_array(self, array_values):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                iteam = self.item(i,j)
                iteam.setText(str(array_values[i][j]))
        pass


