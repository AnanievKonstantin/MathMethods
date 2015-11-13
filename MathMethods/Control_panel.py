from PyQt4 import QtGui, QtCore

class Control_panel(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        self.__lay = QtGui.QGridLayout()
        self.__apply_btn = QtGui.QPushButton("Apply")
        self.__calc_btn = QtGui.QPushButton("Calc")

        self.__text_rows = QtGui.QLabel("Rows:")
        self.__text_columns = QtGui.QLabel("Columns:")

        self.__input_row_count = QtGui.QInputDialog()
        self.__input_col_count = QtGui.QInputDialog()

        self.__build_elements()

    def __build_elements(self):
        self.__lay.addWidget(self.__text_rows,0,0)
        self.__lay.addWidget(self.__text_columns,0,1)