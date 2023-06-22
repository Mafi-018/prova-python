#Joao Pedro Mafi Intervalo

#primeiro  criei um input para a pessoa colocar o numero que ela quiser
numero= float(input("Digite um numero entre 0 a 100: "))

#depois usei o if e o elif para mostrar na onde pode encontrar o numero que pessoa escolheu 
if numero >= 0 and numero <= 25:
    print("seu numero se encontra entre 0 a 25 ")
elif numero >= 25 and numero <= 50:
    print("seu numero se encontra entre 25 a 50")
elif numero >= 50 and numero <= 75:
    print("seu numero se encontra entre 50 a 75")
elif numero >= 75 and numero <= 100:
    print("seu numero se encontra entre 75 a 100")