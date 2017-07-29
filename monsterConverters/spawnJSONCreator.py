import struct
import json

def main():
    monsters = json.load(open("monsterSpawnData.json"))
    spawnPlaces = json.load(open("encounters.json"))  
    print "deleting old data"
    spawnPlaces[0] = {}
    print "adding pokes"
    for i in range(1,56):
        print "next: %d" % i
        if str(i) in monsters.keys(): #pokedex is not full :/
            monster = monsters[str(i)]
            for q in monster["landuse"]:
                if q not in spawnPlaces[0]:
                    spawnPlaces[0][q] = {}
                for j in monster["time"]:
                    if j not in spawnPlaces[0][q]:
                        spawnPlaces[0][q][j] = {}
                    for p in monster["weather"]:
                        if p not in spawnPlaces[0][q][j]:
                            spawnPlaces[0][q][j][p] = []
                        spawnPlaces[0][q][j][p].append(str(i))
    with open("encounters.json", 'w') as f:
            json.dump(spawnPlaces, f, indent=2)
if __name__ == '__main__':
    main()
