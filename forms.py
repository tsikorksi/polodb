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
        if input_str[i] == ".":
            final_array.append(mid_str)
            mid_str = ''
        else:
            mid_str += input_str[i]
    return final_array


def data_decode():
    """
    probably wont be needed
    :return:
    """
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        for i in range(0, len(data)):
            data.append(encrypt.shift_decode(data[i], 5))
        return data


def data_encode():
    """
    probably wont be needed
    :return:
    """
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        for i in range(0, len(data)):
            data.append(encrypt.shift_decode(data[i], 5))
        return data


def main_stats():
    """
    needs work, doesnt work yet
    :return:
    """
    input_data = []
    mid_data = []
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        print(data)
    for i in range(0, len(data)):
        mid_data.append(split(data[i]))
        for j in range(0, len(mid_data[i])):
            input_data.append(encrypt.shift_decode(mid_data[i][j], 5))
        print(mid_data)
    print(input_data)

main_stats()
