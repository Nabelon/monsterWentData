import struct
import json
import random
def main():
    oldDic = json.load(open("monsterEasy.json")) 
    
    for i in oldDic.keys():
        s = str(i)
        print s
        statsDis = float(oldDic[s]["baseStats"]["mAtk"] + oldDic[s]["baseStats"]["hp"] + oldDic[s]["baseStats"]["atk"] + oldDic[s]["baseStats"]["armor"] + oldDic[s]["baseStats"]["speed"] + oldDic[s]["baseStats"]["mRes"]) 
        statsTotal = float(oldDic[s]["baseStats"]["total"])
        oldDic[s]["baseStats"]["atk"] = int(float(oldDic[s]["baseStats"]["atk"]) / statsDis * statsTotal)
        oldDic[s]["baseStats"]["mAtk"] = int(float(oldDic[s]["baseStats"]["mAtk"]) / statsDis * statsTotal)
        oldDic[s]["baseStats"]["mRes"] = int(float(oldDic[s]["baseStats"]["mRes"]) / statsDis * statsTotal)
        oldDic[s]["baseStats"]["armor"] = int(float(oldDic[s]["baseStats"]["armor"]) / statsDis * statsTotal)
        oldDic[s]["baseStats"]["hp"] = int(float(oldDic[s]["baseStats"]["hp"]) / statsDis * statsTotal)
        oldDic[s]["baseStats"]["speed"] = int(float(oldDic[s]["baseStats"]["speed"]) / statsDis * statsTotal)
        del oldDic[s]["baseStats"]["total"]
        
        
    with open("monster.json", 'w') as f:
            json.dump({int(x):oldDic[x] for x in oldDic.keys()}, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
