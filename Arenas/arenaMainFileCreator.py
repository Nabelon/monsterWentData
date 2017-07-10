import struct
import json
import random
def main():
    newDic = {};
    arenaFileNames = ["arena0","arena1"];
    for i in range(0,len(arenaFileNames)):
        s = str(i)
        print s
        arenaDic = json.load(open(arenaFileNames[i] + ".json")) 
        arenaTmpDic = {};
        arenaTmpDic["size"] = len(arenaDic["trainers"])
        arenaTmpDic["name"] = arenaDic["name"]
        arenaTmpDic["requirement"] = arenaDic["requirement"];
        arenaTmpDic["fileName"] = arenaFileNames[i]
        newDic[str(arenaDic["id"])] = arenaTmpDic
        
    with open("arenas.json", 'w') as f:
            json.dump(newDic, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
