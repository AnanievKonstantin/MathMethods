from PyQt4 import QtGui, QtCore

class Control_panel(QtGui.QWidget):

    apply_signal = QtCore.pyqtSignal(int)
    calc_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.__lay = QtGui.QGridLayout()
        self.__apply_btn = QtGui.QPushButton("Apply")
        self.__calc_btn = QtGui.QPushButton("Calc")

        self.__text_var = QtGui.QLabel("Variable:")

        self.__input_var_count = QtGui.QLineEdit()

        self.__to_scatter__signals()
        self.__build_window()

        self.show()

    def __build_window(self):
        self.setLayout(self.__lay)
        self.__lay.addWidget(self.__text_var, 0, 0)
        self.__lay.addWidget(self.__input_var_count, 0, 1)
        self.__lay.addWidget(self.__apply_btn, 2, 0)
        self.__lay.addWidget(self.__calc_btn, 2, 1)

    def __getNumber(self):
        return int(self.__input_var_count.text())

    @QtCore.pyqtSlot()
    def emit_apply_signal(self):
        print("emit apply")

        try:
            count = self.__getNumber()
        except ValueError:
            print("Not number")
        else:
            self.apply_signal.emit(count)

    @QtCore.pyqtSlot()
    def emit_calc_signal(self):
        print("emit calc")
        self.calc_signal.emit()

    def __to_scatter__signals(self):
        """
        Установит сигнылы при нажатии кнопок
        :return:
        """
        self.__apply_btn.connect(self.__apply_btn, QtCore.SIGNAL("clicked()"),
                                 self, QtCore.SLOT("emit_apply_signal()"))

        self.__calc_btn.connect(self.__calc_btn, QtCore.SIGNAL("clicked()"),
                                 self, QtCore.SLOT("emit_calc_signal()"))