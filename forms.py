"""
This file will take and compare the data in coredb.txt
"""
import encrypt
import math


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


def split(input_str):
    """
    this function is haunted
    this function has been exorcised, carry on citizen
    :return:
    """
    final_array = []
    mid_str = ''
    for i in range(0, len(input_str)):
        if input_str[i] == "." or input_str[i] == ')':
            final_array.append(mid_str)
            mid_str = ''
        else:
            mid_str += input_str[i]
    return final_array


def data_decode():
    """
    :return:
    """
    output_data = []
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        # print(data)
        for i in range(0, len(data)):
            output_data.append(split(encrypt.shift_decode(data[i].lower(), 5)))
    # print(output_data)
    return output_data


def maths(values, mean):
    """
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


def player_stats(player):
    """
    needs work, doesnt work yet
    :param: str
    :return:
    """
    error = False
    values = []
    sum_val, count = 0, 0
    input_array = data_decode()
    # mean calculation
    for i in range(0, len(input_array)):
        if input_array[i][0] == player:
            count += 1
            values.append(int(input_array[i][3]))
            sum_val += int(input_array[i][3])
    try:
        mean = sum_val/count
    except ZeroDivisionError:
        error = True
        mean, median, max_val, min_val, std_dev = 0, 0, 0, 0, 0
        return mean, median, max_val, min_val, std_dev, error
    # sort
    bubble_sort(values)
    # print(values)
    median, max_val, min_val, std_dev = maths(values, mean)
    return mean, median, max_val, min_val, std_dev, error
