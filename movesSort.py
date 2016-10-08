import struct
import json
import random
def main():
    newDic = {};
    oldDic = json.load(open("movesData.json")) 
    for i in range(1,113):
        s = str(i)
        if oldDic[s]["type"] in newDic.keys():
            newDic[oldDic[s]["type"]].append(oldDic[s]["name"] + " Id:" + s + " Str:" + str(oldDic[s]["dmg"]) + " Acc:" + str(oldDic[s]["acc"]))
        else:
            m = []
            m.append(oldDic[s]["name"] + " Id:" + s + " Str:" + str(oldDic[s]["dmg"]) + " Acc:" + str(oldDic[s]["acc"]))
            newDic[oldDic[s]["type"]] = m
    with open("movesSorted.json", 'w') as f:
            json.dump(newDic, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
