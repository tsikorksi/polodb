"""
Generates random data for analysis
"""
import random
import encrypt


def random_write():
    """
    this function is haunted
    :return:
    """
    count = int(input("Data points?"))
    coredb = open("data" + "/coredb.txt", "a")
    for i in range(0, count):
        output_str = ''
        output_array = []
        arr = random_gen()
        # print(arr)
        for j in range(0, len(arr)):
            # print(type(arr[j]))
            output_array.append(arr[j])
            # output_array.append('.')
        for k in range(0, len(output_array)):
            output_str += ''.join(encrypt.shift_encode(''.join(output_array[k]), 5))
            output_str += '.'
        # print(output_str)
        coredb.write(output_str)
        coredb.write('\n')


def random_gen():
    players = ["tad", "eric", "john", "simon", 'erica', 'samantha']
    venues = ["epsom", "guards"]
    ponies = ["dora", "simpatico", "elana", "horace", "dagny", "heel", "india"]
    arr = [players[random.randint(0, 3)], venues[random.randint(0, 1)], ponies[random.randint(0, 6)],
           str(random.randint(1, 8)), str(random.randint(0, 3))]
    return arr


random_write()
