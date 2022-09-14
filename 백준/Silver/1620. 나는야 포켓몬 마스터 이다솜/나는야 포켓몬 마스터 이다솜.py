'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
Raichu
25
3
Pidgey
Kakuna
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
idx = 0
for _ in range(n):
    idx += 1
    dic[idx] = input().rstrip()
# print(dic)
dicstr = {v : k for k, v in dic.items()}
# print(dicstr)
for _ in range(m):
    word = input().rstrip()
    if word.isdigit() :
        print(dic[int(word)])
    else:
        print(dicstr[word])