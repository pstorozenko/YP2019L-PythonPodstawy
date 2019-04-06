l = [6, 5, 1, 42]
print(l)
l[2] = 43
print(l)

t = (6, 5, 1, 42)
print(t)
# t[2] = 43
print(t[2])

print(5 in l)

print(5 in t)

print("Wypisywanie listy")
for e in l:
    print(e)

print("Wypisywanie krotki")
for e in t:
    print(e)

s = {6, 5, 1, 42}
print(s)
# print(s[0])
s.add(12)
print(s)

# Wypisywanie elementów zbioru
for e in s:
    print(e)

print(43 in s)
# usuwam jedynkę
s.remove(1)
print(s)

print(l)
l.pop(3) # usuwanie po indeksie
print(l)
l.append(43)
print(l)
l.remove(43)
print(l)

### Słowniki
d = {}
d["Piotr"] = 23
d['Ula'] = 24
d['Janek'] = 26
d["Asia"] = 21
print(d)

print(d["Janek"])

if "Jarek" in d:
    print(d["Jarek"])

d[42] = 42
print(d)
d[t] = "krotka"
print(d)
# d[l] = "lista"
# print(d)

print("Wyświetlanie słownika")
for e in d:
    print(e, d[e])