# Ćwiczenia na wszystko

## Python

1. Zapytaj użytkownika ile ma lat i napisz mu ile będzie miał w 2040 roku. Pamiętaj o zamianie na liczbę `int(tekst)`.
2. Policz średnią prędkość z jaką jechał na rowerze Jaś jeżeli przebył drogę z domu do sklepu w 10 min i z powrotem w 8 min, a sklep był odległy od 2km od domu. Wynik podaj zarówno w m/s jak i km/h.

## Listy i pętle

Mając listy:

```python
l1 = [2, 3, 41, 12 ,-23]
l2 = [-4, 5, 1, 23, 23]
```

1. Wylicz sumę listy `l1`.
2. Stwórz listę, która na kolejnych elementach będzie miała różnicę między i-tymi elementami `l1` i `l2` czyli `6 -2 40 11 -46`.
3. Program, który wypisze na ekran liczby podzielne przez 7 w zakresie od 10 do 50.
4. Wypisze wszystkie liczby podzielne przez 3 z listy `l1` i `l2`.

## Napisy

```python
napis1 = "Ala ma kota!"
```

1. Sprawdź czy imię Ala kończy się na a.
2. Sprawdź czy `napis1` zaczyna się z wielkiej litery.
3. Wyświetl użytkownikowi `napis1`, a następnie poproś go o przepisanie tegoż napisu wielkimi literami. Sprawdź czy użytkownik nie popełnił błędu.
4. Wyświetl co drugą literkę z `napis1`.
5. Wyświetl `napis1` od tyłu.

## Kolekcje

```python
slownik = {
    "rower" : "jedno- lub wielośladowy pojazd drogowy napędzany siłą mięśni poruszających się nim osób za pomocą przekładni mechanicznej, wprawianej w ruch (najczęściej) nogami.",
    "samochód" : "pojazd silnikowy służący do przewozu osób lub ładunków.",
    "samolot" : "załogowy bądź bezzałogowy statek powietrzny cięższy od powietrza (aerodyna), utrzymujący się w powietrzu dzięki wytwarzanej sile nośnej za pomocą nieruchomych, w danych warunkach względem statku, skrzydeł.",
    "żaglowiec" : "statek wodny o napędzie żaglowym. Jednostka pływająca, której jedynym lub podstawowym czynnikiem napędowym jest jeden lub więcej żagli."

}
napis2 = """
Litwo! Ojczyzno moja! ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno Święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
"""
```

1. Wypisz użytkownikowi znane Ci hasła (hasła ze słownika `slownik`), tylko hasła, bez znaczeń. Następnie zapytaj na temat którego hasła chciałby się więcej dowiedzieć. Wyświetl mu to hasło, bądź poinformuj, że go nie znasz.
2. Policz ile jakich liter występuje w `napis2`.

## Funkcje

Przerób rozwiązania z poprzednich zadań tak aby były funkcjami przyjmującymi odpowiednio napis, słownik, listę.