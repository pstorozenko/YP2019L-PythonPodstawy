print("=" * 20)
print("Dzień dobry")
print("=" * 20)

x = 44
print(x)
print(x / 5)
print(x // 5)
print(x % 5)

l = ["Ala", "ma", "kota"]

for e in l:
    print(e)

for i in range(len(l)):
    print(i, l[i])

for i, e in enumerate(l):
    print(i, e)

l2 = ["Dziś", "koniec", "zajęć"]

for i in range(len(l)):
    print(l[i], l2[i])

for e1, e2 in zip(l,l2):
    print(e1, e2)

for i in range(51):
    if i >= 10:
        print(i)
    
for i in range(10, 51):
    print(i)

for i in range(10, 51, 15):
    print(i)

a = [3, 4]
print(type(a))

from math import pi
print(pi)
print("Obiekt a zawiera " + str(a))
print(f"Obiekt a zawiera {a}")
print(f"Liczba pi wynosi {pi:.4f}") # f-string
s = "Siema"
print(s.upper)
print(s.upper())
print("=" * 20)
l = ["Ala", "ma", "kota"]
l2 = ["Dziś", "koniec", "zajęć"]
for e in l + l2:
    if len(e) > 2:
        print(e)
print("=" * 20)
for e in l, l2:
    if len(e) > 2:
        print(e)
