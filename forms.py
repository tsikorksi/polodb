"""
This file will take and compare the data in coredb.txt
"""
import encrypt


def split(input_str):
    """
    this function is haunted
    this function has been exorcised, carry on citizen
    :return:
    """
    final_array = []
    mid_str = ''
    for i in range(0, len(input_str)):
        if input_str[i] == "." or input_str [i] == ')':
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
        for i in range(0, len(data)):
            # mid_data = []
            # mid_data.append(split(data[i]))
            output_data.append(split(encrypt.shift_decode(data[i], 5)))
        print(output_data)
    return output_data


def main_stats(name):
    """
    needs work, doesnt work yet
    :param: str
    :return:
    """
    input_array = data_decode()
