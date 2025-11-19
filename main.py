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
