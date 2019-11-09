# 1.  Imate dictionary sa items:
# "banana": 4,
# "apple": 2,
# "orange": 1.5,
# "pear": 3
# Korisniku trazite da unese jos voca ili povrca I njihove cijene. Zadatak je racunanje za
# voce/povrce  koje korisnik zeli da kupi. Prvo unosi namirnicu, onda unosi koliko
# kilograma zeli da kupi. Vratiti poruku: Kupili ste STA JE KUPIO. Vas ukupan racun je
# SUMA.
# O cemu je potrebno voditi racuna??


f_and_v = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
wished_number_of_new_f_and_v = input("Koliko namirnica zelis da dodas?")
for i in range(0, int(wished_number_of_new_f_and_v)):
    add_f_or_v = input("Dodaj namirnicu: ")
    if not add_f_or_v in f_and_v:
        add_price = input("Cijena dodate namirnice: ")
        f_and_v[add_f_or_v] = float(add_price)
    else:
        while add_f_or_v in f_and_v:
            print("Vec imamo tu namirnicu, daj neku drugu.")
            add_f_or_v = input("Dodaj namirnicu: ")
            if not add_f_or_v in f_and_v:
                add_price = input("Cijena dodate namirnice: ")
        f_and_v[add_f_or_v] = float(add_price)

wished_f_or_v = input("Zeljena namirnica: ")
wished_kg = input("Zeljena kolicina: ")
total_price = f_and_v[wished_f_or_v] * float(wished_kg)

print(f"Kupili ste {wished_f_or_v}. Vas ukupan racun je {float(total_price)}.")