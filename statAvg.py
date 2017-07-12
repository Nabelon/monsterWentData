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
        newDic['{0:05d}'.format(i)] = mDic["special_attack"]+mDic["special_attack"]+mDic["hp"]+mDic["attack"]+mDic["defense"]+mDic["speed"]+mDic["special_defense"]
    with open("monsterStatsAvg.json", 'w') as f:
            json.dump(newDic, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
