# Vi ste profesor na fakultetu. Unosite ime I prezime studenata I broj bodova za
# kolokvijum1, kolokvijum2 I zavrsni ispit. (Max broj bodova po cjelini za kolokvijume j
# 20). Kada zavrsite upis svega, potrebno je izbaciti rezultate. STUDENT, broj bodova,
# ocjena, polozio ili ne.
# Ocjene se krecu: >90 – A, >80 – B, >70 – C, >60 – D,< 59 F.

name_and_surname = input("Unesite Ime i prezime studenta:")
kolokvijum1 = input("Unestite broj bodova za prvi kolokvijum:")
my_dict = {"STUDENT": name_and_surname}

if int(kolokvijum1) > 20:
    print("Broj bodova ne moze biti veci od 20!")
else:
    my_dict.update({"kolokvijum1": kolokvijum1})

kolokvijum2 = input("Unesite broj bodova za drugi kolokvijum:")
if int(kolokvijum2) > 20:
    print("Broj bodova ne moze biti veci od 20!")
else:
    my_dict.update({"Kolokvijum2": kolokvijum2})
Final_Exam = input("Unesite broj bodova za zavrsni ispit")
if int(Final_Exam) > 20:
    print("Broj bodova ne moze biti veci od 20!")
else:
    my_dict.update({"FinalExam": Final_Exam})
sum1 = int(kolokvijum1) + int(kolokvijum2) + int(Final_Exam)
print(sum1)
my_dict.update({"SUM": sum1})
if sum1 > 90:
    Grade = "A"
    polozio = "Da"
if sum1 > 80 and sum1 < 90:
    Grade = "B"
    polozio = "Da"
if sum1 > 70 and sum1 < 80:
    Grade = "D"
    polozio = "Da"
if sum1 > 60 and sum1 < 70:
    Grade = "D"
    polozio = "Da"
if sum1 <60:
    Grade = "F"
    polozio = "Ne"

my_dict.update({"Grade": Grade})
my_dict.update({"Status": polozio})

print(f'Student {my_dict.get("STUDENT")} ima ukupan broj bodova {my_dict.get("SUM")} '
      f',njegova ocjena je {my_dict.get("Grade")} i njegov status je {my_dict.get("Status")}')



