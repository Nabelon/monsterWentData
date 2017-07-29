import struct
import json
import random
def main():
    newDic = {};
    oldDic = json.load(open("monster.json")) 
    for i in range(1,38):
        s = str(i)
        print s
        mDic = oldDic[s]["baseStats"]
        newDic['{0:05d}'.format(i)] = mDic["mAtk"]+mDic["hp"]+mDic["atk"]+mDic["armor"]+mDic["speed"]+mDic["mRes"]
    with open("monsterStatsAvg.json", 'w') as f:
            json.dump(newDic, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
