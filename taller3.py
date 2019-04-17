lista=[]
total=0
for n in range(10):
    
    numero =int(input('ingrese un numero: '))
    lista.append(numero)
    total = total + numero

media = total/10
print(lista)
print('la suma de los numeros es: ',total)
print('la media de los numeros es: ',media)
