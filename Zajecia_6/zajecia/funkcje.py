def dziwny_kwadrat(x):
    a = x * x + 2 * x
    return a

def druga_funkcja(x, y):
    return x * x + y * y

print(dziwny_kwadrat(10))

# zmienna = input("Podaj liczbę: ")
# zmienna = int(zmienna)
# print(dziwny_kwadrat(zmienna))


a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
a = int(a)
b = int(b)
print(druga_funkcja(a, b))