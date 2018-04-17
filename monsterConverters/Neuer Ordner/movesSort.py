import struct
import json
import random
def main():
    oldDic = json.load(open("movesData.json")) 
    for i in oldDic.keys():
        if oldDic[i]["pp"] < 16:
            oldDic[i]["cooldown"] = 1 if oldDic[i]["pp"] > 9 else 3
        del oldDic[i]["pp"]
    with open("movesSorted.json", 'w') as f:
            json.dump(oldDic, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
