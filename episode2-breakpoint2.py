
# Deuxième BreakPoint
# 6
email = str(input("Enter email : "))
arobase = 0
for char in email:
    if char == "@":
        arobase += 1
if email[-4:] == ".com" and arobase == 1:
    print("Email correct")
else:
    raise Exception("Email need one @ and finish by .com")

# 7
for i in range(0, 10):
    print("Implémentons des algorithmes intéressants")

# 8 et 12
word = "Pouvons nous étudier des algorithmes?"
for letter in word:
    print(letter)

# 9
a = 0
b = 10
while a < b:
    a += 1

# 10
a = 0
b = 10
while b != 0:
    b -= 1

# 11
while True:
    try:
        n = int(input("Entrez un nombre entre 1 et 10 : "))
        if 1 <= n <= 10:
            print(n)
            break
    except ValueError:
        continue

# 13
for i in range(0, 15):
    if i % 3 == 0:
        print(i)

# 14
n = 15
i = 0
while i != n:
    for i in range(0, n):
        if i % 2 == 0:
            print(i)
        i += 1
