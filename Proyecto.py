### Definir Funciones ###

# Lista para almacenar la información de los usuarios y paquetes
usuarios = []
paquetes = []

### Crear Cuenta de Usuario ###

def registro_de_usuario():
    correo = input("Ingrese su correo electrónico: ")
    Nombre_Co = input("Ingrese el nombre del comercio: ")
    telefono = input("Digite el numero telefonico del comercio: ")
    Nombre_Dueño = input("Ingrese su nombre: ")
    Ubicacion = input("Ingrese la ubicación del local: ")
    ced = input("Ingrese cedula: ")

    usuario = {
        "cedula": ced,
        "correo": correo,
        "Nombre_Co": Nombre_Co,
        "telefono": telefono,
        "Nombre_Dueño": Nombre_Dueño,
        "Ubicacion": Ubicacion
    }
    usuarios.append(usuario)

    print("Usuario registrado con exito")

    with open("User" + ced + ".txt", "w") as file:
        file.write(f"El nombre del Comercio es: {Nombre_Co}\n")
        file.write(f"El nombre del dueño es: {Nombre_Dueño}\n")
        file.write(f"El correo del dueño es: {correo}\n")
        file.write(f"El telefono del dueño es: {telefono}\n")
        file.write(f"La ubicacion es: {Ubicacion}\n")
        file.write(f"{ced}\n")

### Crear Factura Electronica ###

def factura(ced):
    tipo_cedula = input("Ingrese el tipo de cédula (Física o Jurídica): ")
    num_cedula = input("Ingrese el número de cédula: ")
    nombre = input("Ingrese el nombre registrado: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    provincia = input("Ingrese la provincia: ")
    canton = input("Ingrese el cantón: ")
    distrito = input("Ingrese el distrito: ")
    
    print("Factura Registrada")

    file=open ("Fact" + ced + ".txt", "w") 
    file.write(f"Tipo de Cedula: {tipo_cedula}\n")
    file.write(f"Numero de Cedula: {num_cedula}\n")
    file.write(f"Nombre: {nombre}\n")
    file.write(f"Tel: {telefono}\n")
    file.write(f"E-Mail: {correo}\n")
    file.write(f"Localizacion: {provincia}, {canton}, {distrito}\n")

### Crear Paquete ###

def paquete(ced):
    dest = input("Ingrese el nombre del destinatario: ")
    telf = input("Ingrese el telefono del destinatario: ")
    ceddes = input("Ingrese el numero de cedula del destinatario: ")
    pes = float(input("Ingrese el peso del paquete: "))
    cobro = float(input("Ingrese la opcion de compra contra entrega [Monto a cobrar ¢1500]: "))
    numpq = input("Este es el paquete #? que envio: ")

    nuevo_paquete = {
        "codigo": ced + numpq,
        "estado": "Creado",
        "destinatario": dest,
        "telefono_dest": telf,
        "cedula_dest": ceddes,
        "peso": pes,
        "costo": cobro
    }
    paquetes.append(nuevo_paquete)

    

    file=open("PQT" + ced + numpq + ".txt", "w")
    file.write(f"Destinatario: {dest}\n")
    file.write(f"Tel: {telf}\n")
    file.write(f"Cedula Destinatario: {ceddes}\n")
    file.write(f"Peso en KG: {pes}\n")
    file.write(f"Costo: {cobro}\n")

    print ("Su codigo de paquete sera igual a: ", ced+numpq)

    print("Paquete creado y registrado con éxito.")

    

### Funciones de Rastreo y Actualización de Estado ###

def actualizar_estado_paquete(codigo, nuevo_estado):
    for paquete in paquetes:
        if paquete['codigo'] == codigo:
            paquete['estado'] = input("Ingrese el nuevo estado (Creado, Recolectado, Entrega Fallida, Entregado): ")
            nuevo_estado = paquete['estado']
            return f"El estado del paquete {codigo} ha sido actualizado a: {nuevo_estado}"
    return "Código de paquete no encontrado."

def rastrear_paquete(codigo):
    for paquete in paquetes:
        if paquete['codigo'] == codigo:
            return f"El estado de su paquete {codigo} es: {paquete['estado']}"
    return "Código de paquete no encontrado."

def generar_numero_guias(datos):
    

    remitente = input("Ingrese el nombre del remitente: ")
    destinatario2 = input("Ingrese el nombre del destinatario: ")
    contenido = input("Ingrese la descripción del contenido del paquete: ")
    numero_seguimiento = input("Ingrese numero  de seguimiento (cedula+01): ")


    print("**INFORMACIÓN DEL PAQUETE**")
    print("Remitente:", remitente)
    print("Destinatario:", destinatario)
    print("Contenido:", contenido)
    print("Número de Seguimiento:", numero_seguimiento)

### Mostrar Menu al Usuario ###

print("►►►► Bienvenido al Programa de Mensajeria Fidelitas ◄◄◄◄\n")
print("▬▬▬▬ MENU ▬▬▬▬\n")
print("Opciones:")
print("1. Crear cuenta de usuario")
print("2. Entrar a cuenta")
print("3. Salir\n")

while True:
    opc = int(input("Ingrese la opcion: "))

    if opc == 1:
        registro_de_usuario()

    elif opc == 2:
        ced = input("Ingrese numero de Cedula: ")
        usuario_encontrado = any(usuario['cedula'] == ced for usuario in usuarios)
        
        if usuario_encontrado:
            print("Bienvenido, escoja lo que desea hacer: ")
            print("1. Verificar estado de paquete: ")
            print("2. Crear nuevo paquete: ")
            print("3. Cambiar estado de paquete")
            print("4. Salir")

            dec = int(input("Decision: "))

            if dec == 1:
                codigo_paquete = input("Ingrese el código de su paquete: ")
                print(rastrear_paquete(codigo_paquete))

            elif dec == 2:
                paquete(ced)
                generar_numero_guias()
                fact = int(input("Si desea factura, presione 1, sino 2: "))
                if fact == 1:
                    factura(ced)

            elif dec == 3:
                codigo_paquete = input("Ingrese el código de su paquete: ")
                nuevo_estado = "Creado"
                print (actualizar_estado_paquete(codigo_paquete, nuevo_estado))

            elif dec == 4:
                break

        else:
            print("El usuario NO fue encontrado, cree uno")

    elif opc == 3:
        break

print ("Gracias por usar el servicio, vuelva pronto")
        else:
            print("El usuario NO fue encontrado, cree uno")

    elif opc == 3:
        break
