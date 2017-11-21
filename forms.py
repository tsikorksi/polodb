"""
This file will take and compare the data in coredb.txt
"""
import encrypt
import math


class InternalMethods:
    """
    all the functions needed for internal processing of forms
    """

    @staticmethod
    def bubble_sort(arr):
        """
        bubble sort
        :param arr: list
        :return arr: list
        """
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def split(input_str):
        """
        this function is haunted
        this function has been exorcised, carry on citizen

        splits data from DB into strings for processing
        :return:
        """
        final_array = []
        mid_str = ''
        for i in range(0, len(input_str)):
            # takes encrypted or unencrypted strings
            if input_str[i] == "." or input_str[i] == ')':
                final_array.append(mid_str)
                mid_str = ''
            else:
                mid_str += input_str[i]
        return final_array

    @staticmethod
    def data_decode():
        """
        reads and decrypts data from DB
        :return:
        """
        output_data = []
        with open("data" + "/coredb.txt") as f:
            data = f.read().splitlines()
            # print(data)
            for i in range(0, len(data)):
                output_data.append(InternalMethods.split(encrypt.shift_decode(data[i].lower(), 5)))
        # print(output_data)
        return output_data

    @staticmethod
    def maths(values, mean):
        """
        calculates median, largest value , smallest value and standard deviation
        :param values:
        :param mean:
        :return:
        """
        std_values = []
        # median calculation
        med = (len(values) - 1) / 2
        if med.is_integer() is False:
            median = (values[int(med + 0.5)] + values[int(med - 0.5)]) / 2
        else:
            median = values[int(med)]
        # highest value calculation
        max_val = values[len(values) - 1]
        # lowest value calculation
        min_val = values[0]
        # standard deviation calculation
        for i in range(0, len(values)):
            std_values.append(values[i] ** 2)
        half_way = (sum(std_values)) / (len(values))
        std_dev = math.sqrt((half_way - (mean ** 2)))
        # print(mean, median, max_val, min_val, std_dev)
        return median, max_val, min_val, std_dev


def single_variable_stats(variable, flag):
    """
    gets statistics for single variable that is used in data_menu.html
    :param: str
    :return:
    """
    error = False
    values = []
    sum_val, count = 0, 0
    input_array = InternalMethods.data_decode()
    # mean calculation
    for i in range(0, len(input_array)):
        if input_array[i][flag] == variable:
            count += 1
            values.append(int(input_array[i][3]))
            sum_val += int(input_array[i][3])
    # checks if no values are returned
    try:
        mean = sum_val/count
    except ZeroDivisionError:
        error = True
        mean, median, max_val, min_val, std_dev = 0, 0, 0, 0, 0
        return mean, median, max_val, min_val, std_dev, error
    # sort
    InternalMethods.bubble_sort(values)
    # runs maths calc
    median, max_val, min_val, std_dev = InternalMethods.maths(values, mean)
    # print(mean, median, max_val, min_val, std_dev, error)
    return mean, median, max_val, min_val, std_dev, error


def double_variable_stats(player, variable, flag):
    """
    used in comparison in data_menu.html
    :param player:
    :param variable:
    :param flag:
    :return:
    """
    count, sum_val = 0, 0
    error = False
    values, scores = [], []
    input_array = InternalMethods.data_decode()
    # print(input_array)
    # selects positions for scores where the player and variable are True
    for i in range(0, len(input_array)):
            if input_array[i][0] == player:
                values.append(i)
    # mean calculation
    for i in range(0, len(input_array)):
        if i in values and input_array[i][flag] == variable:
            count += 1
            scores.append(int(input_array[i][3]))
            sum_val += int(input_array[i][3])
    # print(scores)
    # error handling
    try:
        mean = sum_val/count
    except ZeroDivisionError:
        error = True
        mean, median, max_val, min_val, std_dev = 0, 0, 0, 0, 0
        return mean, median, max_val, min_val, std_dev, error
    # sort
    InternalMethods.bubble_sort(scores)
    # maths
    median, max_val, min_val, std_dev = InternalMethods.maths(scores, mean)
    # print(mean, median, max_val, min_val, std_dev, error)
    return mean, median, max_val, min_val, std_dev, error
