from PyQt4 import QtGui, QtCore
from tabulate import tabulate
import numpy as num
import sys

class Model(QtCore.QObject):

    calculationSuccess = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        pass

    def calculate_simplex_method(self, array: num.ndarray, headers: list(), mode: str):

        mainCol = self.__find_main_column(array, headers, mode)
        mainRow = self.__find_main_row(array, mainCol, headers)

        new_array = self.__rect_method(mainCol, mainRow, array)
        end_flag = self.__isEnd(new_array, mode)
        print("End ?: ",end_flag)
        vertex_table_header = self.__create_vertex_header(mainCol, mainRow, array, headers)

        return new_array,vertex_table_header, end_flag

    def __find_main_column(self, array: num.ndarray, list_headers:list, mode: str) -> int:
        """
        Получить индекс базового столбца
        :param headers:
        :param array: num.ndarray
        :return: int
        """


        # this line copy last line of array
        F_line = array[array.shape[0]-1]

        #strip b,min, and additional variable column
        F_line = F_line[1:len(F_line) - array.shape[0]]

        #print("F-LINE: ",F_line)


        position = int()

        print("__find_main_column: F_Line: ",F_line)

        if mode == "max":
            min_value = num.min(F_line)
            position = list(F_line).index(min_value)
        elif mode == "min":
            max_value = num.max(F_line)
            position = list(F_line).index(max_value)

        # +1 так как таблица считается с B и после B идет X1
        #print("Main column: ", position+1)
        return position+1


    def __find_main_row(self, array: num.ndarray, main_column: int, headers: list) ->int:
        """
        Find index of main row
        :param array: Array from table
        :type array: num.ndarray
        :param main_column
        :type main_column: int
        :param headers
        :type headers: list
        :return: index of main row
        :rtype: int
        """

        #подсчитать отнашения

        print("headers: ", headers)
        print("Before: ",tabulate(array))
        print("main col: ",main_column)

        for i in range(array.shape[0] - 1):
            # if array[i][main_column] <= 0:
            #     array[i][array.shape[1] - 1] = 0
            #     print("<= 0",end=" ")
            #     continue
            if headers[i][0] == "X":
                array[i][array.shape[1] - 1] = 0
                #print("x",end=" ")
                continue
            else:
                array[i][array.shape[1] - 1] = abs(array[i][0] / array[i][main_column])
                #print("ok")

        #print("After: ",tabulate(array))

        list_min = num.zeros((array.shape[0] - 1))

        #записать значения из столбца min в list
        for i in range(array.shape[0] - 1):
            list_min[i] = array[i][array.shape[1] - 1]

        #print("Min list row before zero strip: ",list_min)

        #list_min = num.extract(list_min>0,list_min)

        for i in range(len(list_min)):
            if list_min[i] == 0:
                list_min[i] = sys.maxsize

        #print("Min list row after zero strip: ",list_min)
        #Условие завершениея вычислений
        if len(list_min) == 0:
            #print("zero list condition")
            return -1

        index_main_row = num.argmin(list_min)
        #print("main row: ",index_main_row)
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

    def __isEnd(self,array: num.ndarray, mode: str):
        """
        Performs a check on end conditions calculation
        :param array:
        :return: bool value  - true if process is ended
        """
        F_line = array[array.shape[0]-1]
        F_line = F_line[1:len(F_line)-array.shape[0]]

        # minus_array = num.where(F_line < 0)

        print("__isEnd: F_Line: ",F_line)

        if mode == "max":
            print("Check max condition ")
            some_element_less_zero = False
            for i in F_line:
                if i >= 0: continue
                else: some_element_less_zero = True

            if some_element_less_zero == False:
                return True
            else:
                return False

        elif mode == "min":
            print("Check min condition ")
            some_element_more_zero = False
            for i in F_line:
                if i <= 0: continue
                else:some_element_more_zero = True

            if some_element_more_zero == False:
                return True
            else:
                return False



    def __create_vertex_header(self,col: int,row: int,array: num.ndarray, old_headers: list) -> str:
        """
        Создает вертикальный заголовок катблицы
        :param row:
        :param col:
        :param old_headers
        :return:
        """
        # print("Col: ",col)
        # print("Row: ",row)
        #
        print("old_headers: ",old_headers)

        old_headers[row] = "X"+str(col)
        new_headers = old_headers

        print("new_headers: ",new_headers)
        return new_headers