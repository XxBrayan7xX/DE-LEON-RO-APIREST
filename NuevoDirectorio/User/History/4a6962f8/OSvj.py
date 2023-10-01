cntPayasos = int(input("Introduce la cantidad de payasos: "))
cntMuniecas = int(input("Introduce la cantidad de muniecas: "))
pesoPayasos = cntPayasos*112
pesoMunieca = cntMuniecas*75
fletePayaso = float(pesoPayasos / 100 * 3)
fletemunieca = float(pesoMunieca/100*2)
print(f"El peso total del paquete es: {pesoMunieca+pesoPayasos}g.\nEl costo del flete por {cntPayasos} payasos: {fletePayaso}, el costo de fleye por {cntMuniecas} muniecas: {fletemunieca}\nEl precio TOTAL del flete es: {round(fletemunieca+fletePayaso,2)}")