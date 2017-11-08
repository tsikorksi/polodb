"""
This file will take and compare the data in coredb.txt
"""
import Encrypt as encrypt


def split(test):
    final_array = []
    for i in range(0, len(test)):
        temp = test[i]
        return_array = []

        for j in range(0, len(temp)):
            if temp[j] == ".":
                pass
            else:
                return_array.append(temp[j])
        final_array.append(''.join(return_array))
    # formatting(final_array)
    print(final_array)
    return final_array


def base():
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        data = split(data)
        print(data)
        data = encrypt.shift_decode(data, 5)
        return data


split(["aa.aa.aa.aa.aa", "bb.bb.bb.bb.bb"])
