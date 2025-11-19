import random

jatekos_szamai = []
gep_szamai = []
print("Ötös lottó")

# Játékos
while len(jatekos_szamai) < 5:
    szam = int(input(f"Kérem a(z) {len(jatekos_szamai) + 1}. számot! (1-90) "))
    if szam in range(1, 91):
        jatekos_szamai.append(szam)
    elif szam not in range(1, 91): 
        print("Megfelelő számot adj meg!")

# Gép

while len(gep_szamai) < 5:
    szam = random.randint(1, 90)
    gep_szamai.append(szam)

# print(jatekos_szamai)
# print(gep_szamai)

talalat = 0
for jatekos in jatekos_szamai:
    for gep in gep_szamai:
        if jatekos == gep:
            talalat += 1

print("------------")
print(f"Találatok száma: {talalat}")
print("------------")
print(f"A gép ezeket a számokat sorsolta: {gep_szamai}")