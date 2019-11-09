# 11. Korisnik unosi elemente za 2 liste. Potrebno je da unese 5 elemenata za po jednu listu.
# # Ukoliko se u listama nalaze isti elementi, dodati ih u listu I prikazati korisniku. Ako nema
# # istih elemenata vratiti neku poruku.



List1 = []
List2 = []
List3 = []
for i in range(1, 6):
    elem = input("Unesite element prve liste:")
    if elem.isdigit():
        List1.append(elem)
    else:
        print("Element mora biti broj!")

for i in range(1, 6):
    elem = input("Unesite element druge liste:")
    if elem.isdigit():
        List2.append(elem)
    else:
        print("Element mora biti broj!")

for elem in List1:
    if elem in List2:
        List3.append(elem)
    else:
        print("Nema istih elemenata!")

print(f"Elementi vase prve liste su {List1}")
print(f"Elementi vase druge liste su {List2}")
print(f"Isti elementi su: {List3}")

