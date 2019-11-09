#  Korisnik unosi pocetak i kraj range-a. U listi se popunjavaju brojevi u tom range-u.
# Korisniku prikazati listu koju je odredio I tu listu sa kvadriranim elementima. Ukoliko je
# range veci od 100 prikazati prvih 10 elemenata pa ... I onda jos 10 poslednjih elemenata.

q1 = int(input("Unesite prvi broj:"))
q2 = int(input("Unesite drugi broj:"))

List1 =[]
square = []

for e in range(q1,q2):
    List1.append(e)
for e in range(q1,q2):
    square.append(e**2)
for e in List1:
    if e > 100:
         print(f"Vasa lista je {List1}, a kvadrirana lista je {square}, prvih 10 elemenata su {List1[:10]}"
               f",a zadnjih 10 elemenata su {List1[-10:]}")

else:
     print(f"Vasa lista je {List1}, a kvadrirana lista je {square}")


