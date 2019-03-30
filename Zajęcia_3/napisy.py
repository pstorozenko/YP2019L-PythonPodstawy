s = "Dzien dobry"  # równie dobrze może być 'Dzien dobry' 
print(s)

for c in s:
    print(c)

print(s[4])

print(s.upper())
print(s.lower())

print(s.find('obry'))
# Jeżeli jest fraza to zostanie zwrócony indeks początku frazy w napisie
print(s.find('wieczor'))
# Jeżeli nie to zostanie zwrócone -1

print(s == "Dzien dobry")

s2 = "DziEn Dobry"
print(s.lower() == s2.lower())

print(s)
print(s.startswith("dzien"))
print(s.lower().startswith("dzien"))

print(s.endswith("bry"))


dlugi_napis = "Ala ma kota"
if dlugi_napis.find("kot") != -1:
    print("W zdaniu")
    print(dlugi_napis)
    print("wystepuje slowo kot")