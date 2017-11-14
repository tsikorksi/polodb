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
        arr = random_gen()
        for j in range(0, len(arr)):
            print(arr[j])
            mid = str(arr[j])
            output_str += encrypt.shift_encode(mid, 5)
            output_str += '.'
        print(output_str)
        coredb.write(output_str)
        coredb.write('\n')


def random_gen():
    players = ["Tad", "Eric", "John", "Simon"]
    venues = ["Epsom", "Guards"]
    ponies = ["Dora", "Simpatico", "Elana", "Horace", "Dagny", "Heel", "India"]
    arr = [str(players[random.randint(0, 3)]), str(venues[random.randint(0, 1)]), str(ponies[random.randint(0, 6)]),
           str(random.randint(1, 8)), str(random.randint(0, 3))]
    return arr


random_write()
