import struct
import json
import random
def main():
    oldDic = json.load(open("monsterMovesLearn.json")) 
    moveData = json.load(open("movesData.json"))
    for i in oldDic.keys():
        s = str(i)
        print s
        for i in oldDic[s].keys():
            oldDic[s][i] = str(oldDic[s][i]) + " " + moveData[str(oldDic[s][i])]["name"]
        
        
    with open("movesLearnedWithNames.json", 'w') as f:
            json.dump({int(x):oldDic[x] for x in oldDic.keys()}, f, indent=2, sort_keys=True)
if __name__ == '__main__':
    main()
