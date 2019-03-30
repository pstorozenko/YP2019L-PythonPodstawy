i = 0

while i < 5:
    print("Czesc")
    i = i + 1

odp = input("Podaj dobrą odpowedź: ")

while odp != "42":
    odp = input("Podaj DOBRĄ odpowiedź: ")

s = "Brawo to była dobra odpowiedź"
print(s)
print(s.upper())