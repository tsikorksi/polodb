"""
Generates random data for analysis
"""
import random
import encrypt


def random_write():
    """
    takes user input as to number of generated values
    saves generated data to DB
    :return:
    """
    # gets user input as to number of values to be generated
    count = int(input("Data points?"))
    # opens DB
    coredb = open("data" + "/coredb.txt", "a")
    for i in range(0, count):
        output_str = ''
        output_array = []
        # runs generation
        arr = random_gen()
        for j in range(0, len(arr)):
            output_array.append(arr[j])
        for k in range(0, len(output_array)):
            output_str += ''.join(encrypt.shift_encode(''.join(output_array[k]), 5))
            output_str += '.'
        # print(output_str)
        coredb.write(output_str)
        coredb.write('\n')


def random_gen():
    """
    selects data to be randomly generated
    :return:
    """
    players = ["tad", "eric", "john", "simon", 'erica', 'samantha']
    venues = ["epsom", "guards"]
    ponies = ["dora", "simpatico", "elana", "horace", "dagny", "heel", "india"]
    # selects values to add to output array, randomly
    arr = [players[random.randint(0, 3)], venues[random.randint(0, 1)], ponies[random.randint(0, 6)],
           str(random.randint(1, 8)), str(random.randint(0, 3))]
    return arr


random_write()
