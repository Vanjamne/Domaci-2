# Potrebno je da korisnik unese 2 liste sa istim brojem elemenata. Za svaki broj koji je u
# listi pronaci kvadrat tog broja, prikazati odvojeno, a onda prikazati parne brojeve iz tih
# kvadriranih brojeva. Odraditi sa list comph. I sa For loop


Q1 = input("Unesite broj elemenata za prvu listu:")
List1 = []
List2 = []
Square = []
Even = []
Odd = []
for i in range(0, int(Q1)):
    elem = input("Unesite element:")
    if elem.isdigit():
        List1.append(elem)
    else:
        print("Element mora biti broj!")
Q2 = input("Unesite broj elemenata za drugu listu:")
for i in range(0,int(Q2)):
    elem = input("Unesite element:")
    if elem.isdigit():
        List2.append(elem)
    else:
        continue

if len(List1) != len(List2):
    print("Greska.Broj elemenata listi mora biti identican!")

for elem in List1:
    print(elem)
    if elem.isnumeric():
        Square.append(int(elem)**2)
        print(Square)
for i in Square:
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print(f" Unijeli ste elemente {List1},parni brojevi su {Even}, ")







