'''
TroyMartian : 최소 3개 안테나, 최대 4개 눈
VladSaturnian : 최대 6개 안테나, 최소 2개 눈
GraemeMercurian : 최대 2개 안테나, 최대 3개 눈

<input>
first line : antenna
seconde line : eyes
'''

first = int(input()) # antenna
seconde = int(input()) # eyes

if first >= 3 and seconde <= 4:
    print("TroyMartian")
if first <= 6 and seconde >= 2:
    print("VladSaturnian")
if first <= 2 and seconde <= 3:
    print("GraemeMercurian")