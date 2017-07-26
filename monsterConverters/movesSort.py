import struct
import json
import random
def main():
    newDic = {};
    oldDic = json.load(open("movesData.json")) 
    for i in oldDic.keys():
        s = str(i)
        print s
        if oldDic[s]["type"] in newDic.keys():
            newDic[oldDic[s]["type"]].append(oldDic[s]["name"] + " Id:" + s + " Str:" + str(oldDic[s]["dmg"]) + " Acc:" + str(oldDic[s]["acc"]) + " cat: " + str(oldDic[s]["cat"]))
        else:
            m = []
            m.append(oldDic[s]["name"] + " Id:" + s + " Str:" + str(oldDic[s]["dmg"]) + " Acc:" + str(oldDic[s]["acc"]) + " cat: " + str(oldDic[s]["cat"]))
            newDic[oldDic[s]["type"]] = m
    with open("movesSorted.json", 'w') as f:
            json.dump(newDic, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
