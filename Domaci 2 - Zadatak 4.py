# Napisati kod pomocu kojeg 2 stringa: "PyNaTive" I “PrOgrAMmiNg” formatiramo tako
# sto prvo upisujemo mala slova pa onda velika, odnosno dobijamo yaivePNT.


str1 = "PyNaTive"
str2 = "PrOgrAMmiNG"

lower = []
upper = []

for elem in str1:
    if elem.islower():
        lower.append(elem)

for elem in str1:
    if elem.isupper():
        upper.append(elem)

listtostring = ''.join([str(elem) for elem in lower + upper])

for elem in str2:
   if elem.islower():
       lower.append(elem)
for elem in str2:
   if elem.isupper():
       upper.append(elem)
listtostring = ''.join([str(elem) for elem in lower + upper])
print(listtostring)
