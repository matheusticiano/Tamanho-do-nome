nome = input("Digite seu nome :")
tnome = len(nome)
if tnome <= 4  :
    print(f"{nome} é um nome curto !")
elif tnome >= 5 and tnome <= 6 :
    print(f"{nome} é um nome normal !")
else :
    print(f"{nome} é um nome grande !")
