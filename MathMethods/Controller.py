import sys
from PyQt4 import QtGui, QtCore
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

        self.__variable_count = 0
        self.__verb_count = 0

        self.__control_panel = Control_panel.Control_panel()

        self.__build_window()
        self.__to_scatter__action()

        self.__window.show()

    def play(self):
        self.exec_()

    def __create_table(self, name,var_x,var_s):
        label = QtGui.QLabel(name)
        self.__lay.addWidget(label)

        table = Table.Table(var_x, var_s)
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
        self.__control_panel.connect(self.__control_panel, QtCore.SIGNAL("apply_signal(int,int)"),
                                     self, QtCore.SLOT("apply_table_data(int,int)"))

        self.__control_panel.connect(self.__control_panel, QtCore.SIGNAL("calc_signal()"),
                                     self, QtCore.SLOT("calculate()"))

    @QtCore.pyqtSlot()
    def calculate(self):
        print("IN-----------")

        work = True
        current_table_index = 0
        state_calculation = tuple()
        current_table = None

        if len(self.__table_list) != 0:
            while(work):
                table_to_calc = self.__table_list[current_table_index]
                current_table_index +=1
                state_calculation = self.__model.calculate_simplex_method(table_to_calc.get_array())

                work = state_calculation[2]
                current_table = self.__create_table("Step: "+str(self.__step_number),self.__variable_count,self.__verb_count)
                current_table.set_array(state_calculation[0])
                current_table.set_vertical_headers(state_calculation[1])
                self.__step_number += 1


        else:
            print("Empty table")
        print("Out-----------")

    @QtCore.pyqtSlot(int, int)
    def apply_table_data(self, var_x, var_s,):
        self.__variable_count = var_x
        self.__verb_count = var_s
        self.__step_number = 0
        for table in self.__table_list:
            self.__lay.removeWidget(table)
            table.close()

        for label in self.__label_list:
            self.__lay.removeWidget(label)

        self.__table_list.clear()
        self.__label_list.clear()
        self.__step_number = 0
        self.__create_table("First", var_x,var_s)

