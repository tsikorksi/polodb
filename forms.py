"""
This file will take and compare the data in coredb.txt
"""
# "aa.aa.aa.aa.aa", "bb.bb.bb.bb.bb"
import encrypt as encrypt


def split(input_array):
    final_array = []
    for i in range(0, len(input_array)):
        temp = input_array[i]
        return_array = []
        # print(temp)
        for j in range(0, len(temp)):
            if temp[j] == ".":
                print(return_array)
                final_array.append(return_array)
                del return_array[:]
            else:
                return_array.append(temp[j])

    # formatting(final_array)
    # print(final_array)
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
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        for i in range(0, len(data)):
            data.append(encrypt.shift_decode(data[i], 5))
        return data


split(["aa.aa.aa.aa.aa", "bb.bb.bb.bb.bb"])
