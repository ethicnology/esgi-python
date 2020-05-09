import math
import sys

# Premier BreakPoint
# 1
temps = 6.892
distance = 19.7
print("vitesse = {}".format(temps / distance))

# 2
time = float(input("Enter time : "))
travel = float(input("Enter distance : "))
print("vitesse = {}".format(time / travel))

# 3
floatter = float(input("Enter a float : "))
if floatter >= 0:
    print(math.sqrt(floatter))
else:
    raise Exception('ERROR')

# 4
word1 = str(input("word 1 : "))
word2 = str(input("word 2 : "))
print(min(word1, word2))

# 5
pSeuil = 2.3
vSeuil = 7.41
pressure = float(input("Enter pressure : "))
volume = float(input("Enter volume : "))
if pressure > pSeuil and volume > vSeuil:
    sys.exit()
elif pressure > pSeuil:
    volume = float(input("Please increase volume : "))
elif volume > vSeuil:
    volume = float(input("Please decrease volume : "))
else:
    print("Tout va bien frr")
