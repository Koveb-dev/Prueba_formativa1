
import textwrap
import time
import os

descuento_salud = 70000
descuento_afp = 120000

empleado_datos =[]
matriz_empleados = []
opciones = (1,2,3,4)
while True:
    print('Bienvenido a la app sueldos de trabajadores!')
    time.sleep(1)
    os.system('cls')
    while True:
        print('Menú\n\t1. Registrar trabajador\n\t2. Listar los todos de los trabajadores\n\t3. Imprimir planilla de sueldos\n\t4. Salir de la App')
        try:
            opc = int(input('Ingrese una opción: '))
            if opc in opciones:
                break
            else:
                print('ERROR! debe ingresar una opcion valida, opciones validas(1,2,3,4)!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar números enteros!')
    
    if opc == 1:
        print('Registrar trabajador!')
        time.sleep(1)
        os.system('cls')
        while True:
            nombre_empleado = str(input('Ingrese el nombre del trabajador: '))
            if len(nombre_empleado.strip()) >= 3:
                print('Nombre registrado correctamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! debe ingresar un nombre contenga al menos 3 letras!')
            time.sleep(1)
            os.system('cls')
        
        while True:
            apellido = str(input('Ingrese el apellido del trabajador: '))
            if len(apellido.strip()) >= 3:
                print('Apellido registrado correctamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! debe ingresar un apellido que contenga al menos 3 letras!')
            time.sleep(1)
            os.system('cls')
        
        while True:
            cargo = str(input('Ingrese el cargo del trabajador: '))
            if cargo.lower() in ("ceo","desarrollador","analista"):
                print('Cargo registrado correctamente')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! debe ingresar un cargo valido, cargos validos a ingresar(ceo|desarrollador|analista)!')
        while True:
            try:
                sueldo_bruto = int(input('Ingrese el sueldo bruto del trabajador: '))
                if sueldo_bruto >= 500000 and sueldo_bruto <= 99999999:
                    print('Sueldo bruto registrado correctamente!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print('ERROR! debe ingresar un sueldo bruto que este dentro del rango 500.000 a 99.999.999!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar números enteros!')
        
        sueldo_liq = sueldo_bruto  - (descuento_afp+descuento_salud)
        empleado_datos = [nombre_empleado,apellido,cargo,sueldo_bruto,sueldo_liq]
        matriz_empleados.append(empleado_datos)
        print(matriz_empleados)
        time.sleep(1)
        print('TRABAJADOR REGISTRADO!')

    elif opc == 2:
        if len(matriz_empleados) >= 1:
            while True: 
                for x in range(len(matriz_empleados)):
                    print(f"Empleados\n\t","{x}",matriz_empleados)
                mensaje = str(input('Deseas salir?("SI":SALIR "NO": REDIRIGIR)'))
                if mensaje.upper() in ("SI","NO"):
                    if mensaje == "SI":
                        break
                    else:
                        print('Redirigiendo.')
                    time.sleep(1)
                    os.system('cls')
                else:
                    print('ERROR! debe ingresar una opcion valida, opciones validas("SI" O "NO")!')
                time.sleep(1)
                os.system('cls')

    elif opc == 3:
        with open("sueldos_emp.txt","w",newline="") as archivo: 
            escritor = textwrap.writer(archivo)
    else:
        for x in range(1,4):
            print('Saliendo de la app',('.'*x))
            time.sleep(1)
            os.system('cls')
        break


