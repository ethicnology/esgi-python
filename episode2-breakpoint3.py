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

# 18
string = str(input("variable : "))
if(re.search(r"^[^@]+@[^@]+\.[^@]+$",string)):  
    print("ok")
    
# 19
something = []
print(something)
otherthing = ["0.0", "0.0", "0.0", "0.0", "0.0",]
print(otherthing)

# 20
for i in range(0,3):
    print(i)
for i in range(4,7):
    print(i)
for i in range(2,8+1):
    if( i%2  == 0 ):
        print(i)

chose = [i+1 for i in range(5)]
print(chose)
find = [3,6]
for i in find :
    exist = False
    for y in chose:
        if i == y:
            exist = True
    if exist == True:
        print(i , " exist in chose")
    else:
        print(i , " don't exist in chose")
        
# 21
with open("file.txt","w") as f21:
    something = int(input("nb string : "))
    for x in range(something):
        temp = str(input("Mot : "))
        f21.write(temp)
        f21.write("\n")
        
# 22
import re
with open("file1.txt","w") as f22
    for line in f22:
        if(re.search(r"^[^@]+@[^@]+\.[^@]+$", str(line))):
            print(line)
            
# 23
def wordCounter(something):
    count = dict()
    words = something.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
print(wordCounter("Le projet svp"))

# 24
import sys
try:
    r = int(sys.argv[1])
    pi = 3.1415926535897931
    V= 4.0/3.0*pi* r**3
    print('The volume of the sphere is: ',V," pour un ranyon de ",r)
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

# 25
def somme(a, b, c) :
    return print((a+b+c))

my_tuple = (1, 2, 1)
somme(my_tuple[0], my_tuple[1], my_tuple[2])
