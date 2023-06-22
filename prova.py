# Joao Pedro Mafi Domingo de manhã

horario = input("Digite um horário: ")

# primeiro separei as horas em minutos
horas, minutos = map(int, horario.split(':'))

# depois calculei a diferença usando como referência 8 horas pois era o horario que se pede
atraso_horas = horas - 8
atraso_minutos = minutos

#  depois verifiquei se há atraso ou adiantamento
if atraso_horas > 0:
    print("Você está", atraso_horas, "horas e", atraso_minutos, "minutos atrasado(a).")
elif atraso_horas < 0:
    print("Você está", abs(atraso_horas), "horas e", atraso_minutos, "minutos adiantado(a).")
elif atraso_minutos > 0:
    print("Você está", atraso_minutos, "minutos atrasado(a).")
elif atraso_minutos < 0:
    print("Você está", abs(atraso_minutos), "minutos adiantado(a).")
else:
    print("Você está pontual.")
