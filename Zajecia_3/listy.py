a = 12
print(a * a)
b = 32
print(a * b)
l = [3, 4, 1, 2]

print(l[0])
l[3] = 12
print(l[2])
print(l)
l.append(42)
print(l)
print(l[5])
print(len(l))
l.append(-3)
print(len(l))
print(l)

for i in range(len(l)):
    print(i, l[i])

for i in range(len(l)):
    print(i)


for e in l:
    print(e)

for i in range(5):
    print(i)

for i in range(0):
    print(i)

for i in range(10, 16):
    print(i)

for i in range(2,9,3):
    print(i)


for i in range(10):
    if i == 6:
        continue
    print(i)

for i in range(10):
    if i == 6:
        break
    print(i)

