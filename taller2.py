

def ingresar ():

    agenda={}

    print('Quiere agregar un contacto nuevo')
    print('1.Si o 2.No ')
    des = int(input("R: "))

    while des == 1:

        nombre = input ('Ingrese el nombre del contacto:  ')
        
        if nombre in agenda:

            print('NOMBRE YA INGRESADO, VUELVE A INTENTAR :)')

        else:
            telefono = input ('Ingrese el numero telefonico:  ')
            agenda.update({nombre:telefono})
            print('Quiere agregar un contacto nuevo')
            print('1.Si o 2.No ')
            des = int(input("R: "))
    print('Agenda:')
    for nombre in agenda:
        print(nombre, " : ",agenda[nombre])

ingresar()
    

    






