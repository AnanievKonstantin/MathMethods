from PyQt4 import QtGui, QtCore
from tabulate import tabulate
import numpy as num


class Model(QtCore.QObject):

    calculationSuccess = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        pass

    def calculate_simplex_method(self, array):

        print("start: calculate_simplex_method")
        mainCol = self.__find_main_column(array);
        mainRow = self.__find_main_row(array, mainCol);
        new_array = self.__rect_method(mainCol, mainRow, array)
        end_flag = self.__isEnd(new_array)
        vertex_table_header = self.__create_vertex_header(mainCol, mainRow,array)
        print("end: calculate_simplex_method")

        return new_array,vertex_table_header, end_flag

    def __find_main_column(self, array: num.ndarray) -> int:
        """
        Получить индекс базового столбца
        :param array: num.ndarray
        :return: int
        """

        # this line copy last line of array
        F_line = array[array.shape[0]-1]
        F_line = F_line[0:len(F_line)-1]
        # print(F_line)
        absolute_array = num.absolute(F_line)
        max_absolute_value = num.max(absolute_array)

        # position = num.where(absolute_array == max_absolute_value)

        position = list(absolute_array).index(max_absolute_value)

        # print(position)

        return position


    def __find_main_row(self, array: num.ndarray, main_column: int) ->int:
        """
        Find index of main row
        :param array: Array from table
        :type array: num.ndarray
        :param main_column
        :type main_column: int
        :return: index of main row
        :rtype: int
        """
        #print("Start __find_main_row")
        # print(array)

        min_array = num.ndarray
        #print(array.shape)

        for i in range(array.shape[0] - 1):
            # print(array[i][0] / array[i][main_column])
            # array[i][array.shape[1]] = array[i][0] / array[i][main_column]
            if array[i][main_column] <= 0:
                array[i][array.shape[1] - 1] = 0
            else:
                array[i][array.shape[1] - 1] = array[i][0] / array[i][main_column]
            # print(array[i][0], array[i][array.shape[1] - 1], sep=" ")

        list_min = num.zeros((array.shape[0] - 1))

        for i in range(array.shape[0] - 1):
            list_min[i] = array[i][array.shape[1] - 1]

        # print("Min list: ",list_min)

        list_min = num.extract(list_min>0,list_min)
        min_value = num.amin(list_min)
        index_main_row = num.argmin(list_min)

        # print("Value: ",min_value)
        # print("Index: ",index_main_row)


        # min_relation = min(list_min);
        #
        # # print("Min at:",list_min.index(min_relation))
        #
        # index_main_row = list_min.index(min_relation)
        #
        # # print(tabulate(array))
        # print("Index: ",index_main_row)
        # print("End __find_main_row")
        return index_main_row

    def __rect_method(self, col: int, row: int, array: num.ndarray) -> num.ndarray:
        """
        Square recalculation tables
        :param col: main column
        :param row: main row
        :param array: data feom table
        :return: array after square recalculation

        """
        # print("before: ", tabulate(array))
        #print("Main i: ", row)
        #print("Main j: ", col)

        den = array[row][col]
        for j in range(array.shape[1] - 1):
            array[row][j] /= den

        for i in range(array.shape[0]):
            if i == row:
                continue

            k = array[i][col]
            for j in range(array.shape[1] - 1):
                array[i][j] -= k*array[row][j]

        #print(tabulate(array))
        return array

    def __isEnd(self,array: num.ndarray):
        """
        Performs a check on end conditions calculation
        :param array:
        :return: bool value  - true if process is ended
        """
        F_line = array[array.shape[0]-1]
        F_line = F_line[0:len(F_line)-1]

        # minus_array = num.where(F_line < 0)

        print(num.min(F_line))

        if num.min(F_line) < 0:
            return True
        else:
            return False

    def __create_vertex_header(self,col: int,row: int,array: num.ndarray) -> str:
        """
        Создает вертикальный заголовок катблицы
        :param row:
        :param col:
        :return:
        """
        print("Col: ",col)
        print("Row: ",row)

        header = ["S"+str(x+(array.shape[0])) for x in range(array.shape[0]-1)]
        print(header)
        header[row] = "X"+str(col)
        print(header)

        return header