###PROYECTO
def registro_de_usuario():
    correo= input("Ingrese su correo electrónico:")
    Nombre_Co= input("Ingrese el nombre del comercio:")
    telefono= input("Digite el numero telefonico del comercio:")
    Nombre_Dueño= input("Ingrese su nombre:")
    Ubicacion = input("Ingrese la ubicación del local:")

    print("Usuario registrado con exito")
registro_de_usuario()

def registro_de_usuario():
    tipo_cedula = input("Ingrese el tipo de cédula (Física o Jurídica): ")
    num_cedula = input("Ingrese el número de cédula: ")
    nombre = input("Ingrese el nombre registrado: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    provincia = input("Ingrese la provincia: ")
    canton = input("Ingrese el cantón: ")
    distrito = input("Ingrese el distrito: ")
    
    print("Usuario registrado con éxito")
datos_usuario = registro_de_usuario()

print ("***PUNTO DE ENTREGA DEL PAQUETE***\n")

print ("Indique la siguiente informacion necesaria: \n")

def paquete():
	dest = input("Ingrese el nombre del destinatario: ")
	telf = input ("Ingrese el telefono del destinatario: ")
	ced = input ("Ingrese el numero de cedula del destinatario: ")
	pes = float(input("Ingrese el peso del paquete: "))
	cobro = float(input("Ingrese la opcion de compra contra entrega [Monto a cobrar ¢1500]: "))
	print ("")

print (paquete())

print ("**Informacion del paquete actualizada**")


def paqueteInfo():
	print ("Destinatario: ", dest)
	print ("Tel: ", telf)
	print ("ID: ", ced)
	print ("Peso: ", pes, "kg")
	print ("Total: Ø", cobro)
