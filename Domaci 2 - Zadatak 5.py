# Napisati funkciju kojoj se prosledjuje korisnikov input. Potrebno je vratiti poruku sa
# prebrojanim slovima,brojevima I ostalim karakterima (other). String za provjeru
# "P@#yn26at^&i5ve"

user = input("Unesite string: ")

def a(user):
   integer = []
   alpha = []
   other = []
   for elem in user:
        if elem.isdigit():
           integer.append(elem)
        elif elem.isalnum():
           alpha.append(elem)
        else:
           other.append(elem)
   print(f"Broj brojeva u stringu je: {len(integer)}, broj slova u stringu je: {len(alpha)}, "
         f"broj ostalih elemenata u stringu je: {len(other)}")
a(user)