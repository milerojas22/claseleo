tmeses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero = int(input("que mes quiere encontrar: "))

def encontar (tmeses, numero): # 13
    if numero <= len(tmeses):
        for n, value in enumerate(tmeses, 1):
            if n==numero:
                print(value)
                break
    else:
        print("Mes invalido")

while numero >= 1: 
    encontar(tmeses, numero)
    numero = int(input("que mes quiere encontrar: "))