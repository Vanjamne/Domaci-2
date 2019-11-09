#  Korisnik ponovo popunjava listu kao u prvom zadatku (brojeve). Ukoliko je element veci
# od 2 I djeljiv je sa 3 dodati ga u listu divide_by_3. Ako je element veci od 2 I djeljiv sa 2
# dodati ga u listu divide_by_2. Spojiti te 2 liste I prikazati jedinstvene elemente.


divide_by_3 = []
divide_by_2 = []

for i in range(1, 6):
    elem = input("Unesite element prve liste:")
    if elem.isdigit():
        if int(elem) > 2 and int(elem) % 3 == 0:
            divide_by_3.append(elem)
    else:
        print("Element mora biti broj!")

for i in range(1, 6):
    elem = input("Unesite element druge liste:")
    if elem.isdigit():
        if int(elem) > 2 and int(elem) % 2 == 0:
            divide_by_2.append(elem)
    else:
        print("Element mora biti broj!")

divide_list = divide_by_3 + divide_by_2

print(f"Lista elemenata koji su djeljivi sa 2 i 3 je {divide_list}")
