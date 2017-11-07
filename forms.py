"""
This file will take and compare the data in coredb.txt
"""


def base():
    with open("data" + "/coredb.txt") as f:
        data = f.read().splitlines()
        return data


base()
