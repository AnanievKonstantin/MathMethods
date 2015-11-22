import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from MathMethods import Table, Model, Control_panel


class Controller(QApplication):

    def __init__(self,parent=None):

        QApplication.__init__(self, sys.argv)

        self.__lay = QVBoxLayout()
        self.__window = QWidget()

        self.__table_widget = QWidget()
        self.__table_lay = QVBoxLayout()

        self.__scroll = QScrollArea()


        self.__window.setWindowTitle("MM")

        self.__mode_calculation = "max"
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

        label = QLabel(name)
        self.__table_lay.addWidget(label)

        table = Table.Table(var_x, var_s)
        self.__table_lay.addWidget(table)
        self.__table_list.append(table)
        self.__label_list.append(label)

        return table

    def __build_window(self):

        self.__window.setLayout(self.__lay)
        self.__lay.addWidget(self.__control_panel)

        self.__table_widget.setLayout(self.__table_lay)

        self.__scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll.setWidgetResizable(True)
        self.__scroll.setWidget(self.__table_widget)

        self.__lay.addWidget(self.__scroll)



    def __to_scatter__action(self):
        """
        Установит отклик на сигналы от панели управления
        :return:
        """
        self.__control_panel.connect(self.__control_panel, SIGNAL("apply_signal(int,int)"),
                                      self, SLOT("apply_table_data(int,int)"))

        self.__control_panel.connect(self.__control_panel, SIGNAL("calc_signal()"),
                                      self, SLOT("calculate()"))

    @pyqtSlot()
    def calculate(self):

        print("IN-----------")

        is_end = False
        current_table_index = 0
        state_calculation = tuple()
        current_table = None

        if len(self.__table_list) != 0:
            while(not(is_end)):
                print("___________________________Iteration____________________Start")
                if self.__step_number > 30:
                    break
                table_to_calc = self.__table_list[current_table_index]
                current_table_index +=1

                state_calculation = self.__model.calculate_simplex_method(table_to_calc.get_array(),
                                                                          table_to_calc.get_vertical_headers(),self.__mode_calculation)

                is_end = state_calculation[2]
                current_table = self.__create_table("Step: "+str(self.__step_number),
                                                    self.__variable_count,
                                                    self.__verb_count)
                current_table.set_array(state_calculation[0])
                current_table.set_vertical_headers(state_calculation[1])
                self.__step_number += 1

                print("State: ", state_calculation)

                print("___________________________Iteration____________________END")
        else:
            print("Empty table")

        print("Out-----------")

    @pyqtSlot(int,int)
    def apply_table_data(self, var_x: int, var_s: int):

        self.__variable_count = var_x
        self.__verb_count = var_s
        self.__step_number = 0
        self.__mode_calculation = self.__control_panel.get_mode()

        for table in self.__table_list:
            self.__table_lay.removeWidget(table)
            table.close()

        for label in self.__label_list:
            self.__table_lay.removeWidget(label)
            label.close()

        self.__table_list.clear()
        self.__label_list.clear()
        self.__step_number = 0
        self.__create_table("First", var_x,var_s)

