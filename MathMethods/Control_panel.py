from PyQt4 import QtGui, QtCore

class Control_panel(QtGui.QWidget):

    apply_signal = QtCore.pyqtSignal(int, int)
    calc_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.__lay = QtGui.QGridLayout()

        self.__mode_switcher = QtGui.QComboBox()
        self.__mode_switcher.addItems(["max", "min"])

        self.__apply_btn = QtGui.QPushButton("Apply")
        self.__calc_btn = QtGui.QPushButton("Calc")

        self.__text_var_x = QtGui.QLabel("Основные переменные:")
        self.__text_var_s = QtGui.QLabel("Дополнительные переменные:")
        self.__text_mode_calculation = QtGui.QLabel("Режим вычисления: ")

        self.__input_var_x= QtGui.QLineEdit()
        self.__input_var_s= QtGui.QLineEdit()

        self.__to_scatter__signals()
        self.__build_window()

        QtCore.QObject.connect(self.__mode_switcher, QtCore.SIGNAL("currentIndexChanged(int)"),
                               self,QtCore.SLOT("set_mod(int)"))


        self.show()

    def __build_window(self):
        self.setLayout(self.__lay)
        self.__lay.addWidget(self.__text_var_x, 0, 0)
        self.__lay.addWidget(self.__input_var_x, 0, 1)

        self.__lay.addWidget(self.__text_var_s, 1, 0)
        self.__lay.addWidget(self.__input_var_s, 1, 1)

        self.__lay.addWidget(self.__text_mode_calculation, 2, 0)
        self.__lay.addWidget(self.__mode_switcher)

        self.__lay.addWidget(self.__apply_btn, 3, 0)
        self.__lay.addWidget(self.__calc_btn, 3, 1)

    @QtCore.pyqtSlot(int)
    def set_mod(self, int):
        self.emit_apply_signal()

    def __getNumber(self):
        return int(self.__input_var_x.text()), int(self.__input_var_s.text())

    def get_mode(self) -> str:
        print("!!!: ", self.__mode_switcher.itemText(self.__mode_switcher.currentIndex()))
        return self.__mode_switcher.itemText(self.__mode_switcher.currentIndex())

    @QtCore.pyqtSlot()
    def emit_apply_signal(self):
        print("emit apply")

        try:
            count_x, count_s = self.__getNumber()
        except ValueError:
            print("Not number")
        else:
            self.apply_signal.emit(count_x, count_s)

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