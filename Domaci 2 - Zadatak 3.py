# Potrebno je napraviti dictionary sa username I password. Korisnik unosi svoj username I
# password I loguje se. Razmisliti sta je sve potrebno, poruke, if uslovi.. Zadatak raditi sa
# funkcijom kojoj se prosledjuju argumenti.


user = input("Molimo vas unesite vas username: ")
password = input("Molimo vas unesite vas password: ")
my_dict = {"Username": "vasilije", "Password": "1234"}

def checkuser(Sifra, Korisnik):
    if Sifra == my_dict.get("Password") and Korisnik == my_dict.get("Username"):
        print("Logovali ste se uspjesno! ")
    else:
        print("Pogresno ste unijeli podatke! ")

checkuser(password,user)



