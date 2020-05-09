# 15
liste = [17, 38, 10, 25, 72]
liste.sort()
liste.append(12)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[1:3])
print(liste[:2])
print(liste[2:])
print(set(liste))

# 16
chaine = "abcdefghijklmnopqrstuvwxyz" [::-1]
print(chaine)

# 17
chaine = str(input("Enter word : "))
if chaine == chaine[::-1]:
    print("This is a palindrome")
else:
    print(chaine[::-1])
