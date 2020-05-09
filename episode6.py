import re
try:
    f = open('./episode_6/ep6.txt', "r")
    f.seek(0)
    first_char = f.read(1)
    if not first_char:
        print("file is empty")
    else:
        f.seek(0)
        for x in f:
            temp = re.findall('\d+', x)
            res = list(map(int, temp))
            if res[0] < res[1]:
                print("[oui] la première valeur : ", res[0], "est inferieur à la deuxième valeur :", res[1])
            else:
                print("[non] la première valeur : ", res[0], "est superieur à la deuxième valeur :", res[1])

    f.close()
except FileNotFoundError:
    print('File does not exist')
