import json
import re
import math
import os

class blockdata:
    def __init__(self):
        self.blockNumber = addressData()

class addressData:
    def __init__(self):
        self.address = mnData()

class mnData:
    def __init__(self, collat, amt):
        self.collateral = collat
        self.amount = amt



def read_data():
    output = {}
    outer = {}
    inner = {}
    for dirpath, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".json"):
                with open(filename, 'r') as file:
                    data = file.read()
                    obj = json.loads(data)
                    fullName = re.split('_', file.name)
                    blockNumber = fullName[1].split(".json")
                    for i in obj:
                        inner["collateral"] = convert(i["collateral"])
                        inner["amount"] = 50
                        outer[i["owner"]] = json.dumps(inner)
                        output[blockNumber[0]] = json.dumps(outer)

    print(output)


def convert(num):
    p = (f'{num:f}')
    print(p)
    return p



if __name__ == '__main__':
    read_data()
