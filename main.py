import json
import re
import math


def read_data():
    output = {}
    with open('listmn_38412.json', 'r') as file:
        data = file.read()
        obj = json.loads(data)
        fullName = re.split('_', file.name)
        blockNumber = fullName[1].split(".json")
        for i in obj:
            # output[blockNumber] = json.dumps()
            # output["collateral"] = i["
            print(i["owner"])
            convert(i["collateral"])
            


def convert(num):
    p = (f'{num:f}')
    print(p)



if __name__ == '__main__':
    read_data()
