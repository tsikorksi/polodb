"""
Generates random data for analysis
"""
import random
import encrypt


def random_write():
    count = int(input(""))
    coredb = open("data" + "/coredb.txt", "a")
    for i in range(0, count):
        arr = random_gen()
        for j in range(0, len(arr)):
            coredb.write(encrypt.shift_encode(arr[i],  5))
            coredb.write(".")
        coredb.write('\n')


def random_gen():
    players = ["Tad", "Eric", "John", "Simon"]
    venues = ["Epsom", "Guards"]
    ponies = ["Dora", "Simpatico", "Elana", "Horace", "Dagny", "Heel", "India"]
    arr = [players[random.randint(0, 3)], venues[random.randint(0, 1)], ponies[random.randint(0, 6)],
           random.randint(1, 8), random.randint(0, 3)]
    return arr


random_write()
