#episode 5
import re
liste = ["\b\t80cm\t60cm\n" , "\b\t81cm\t51cm\n" , "\b\t105cm\t145cm\n" ]
print(liste)

for x in range(len(liste)) :
    tmp = re.findall(r'\d+', liste[x])
    res = list(map(int, tmp))
    if res[0] < res[1] :
        print(res[0])
