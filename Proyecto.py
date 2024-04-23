#### MATRICES PARA ALMACENAR ####

usuarios = []
paquetes = []
facturas = []
guias = []
cuentaE = []
sesionActual = []
pqtActuales = []

##guardar txt##

def guardarTXT (archivo, texto):
	file = open (archivo, "w")
	file.write (texto)
	file.close

def guardarTXTAnadir (archivo, texto):
	file = open (archivo, "a")
	file.write (texto+"\n")
	file.close

def guardarMatriz (matriz):
	textoGuardar = ""

	for fila in range(len(matriz)):
		for columna in range(len(matriz [fila])):
			textoGuardar = textoGuardar + matriz [fila][columna]

			if columna < len(matriz [fila] )-1:
				textoGuardar = textoGuardar + ","

		textoGuardar = textoGuardar + "\n"

	return textoGuardar

def cargarArchivo (nombreArchivo):
	matrizArch = []

	try:
		file = open (nombreArchivo, "r")
		lineas = file.readlines ()

		for linea in lineas:
			linea = linea.replace ("\n", "")

			arreglo = linea.split (",")
			matrizArch.append (arreglo)

	except:
		print ("", end="")

	return matrizArch

####Registrar Cuenta de Usuario####

def registrarUsuario (matriz):
	correo = input("Ingrese su correo electrónico: ")
	nombreCo = input("Ingrese el nombre del comercio: ")
	tel = input("Digite el numero telefonico del comercio: ")
	nombreDueno = input("Ingrese su nombre: ")
	ubi = input("Ingrese la ubicación del local: ")
	ced = input("Ingrese cedula: ")

	cuentaU = [correo, nombreCo, tel, nombreDueno, ubi, ced]

	matriz.append (cuentaU)

	print ("\nUsuario registrado con exito!")

    ##GUARDAR##

	textoGuardar = guardarMatriz (matriz)
	guardarTXT ("Usuarios.txt", textoGuardar)
	return matriz

## Registrar Factura ##

def factura (matriz):

	tipoCedula = input("Ingrese el tipo de cédula (Física o Jurídica): ")
	numCedula = input("Ingrese el número de cédula: ")
	nombre = input("Ingrese el nombre registrado: ")
	telefono = input("Ingrese el teléfono: ")
	correo = input("Ingrese el correo electrónico: ")
	provincia = input("Ingrese la provincia: ")
	canton = input("Ingrese el cantón: ")
	distrito = input("Ingrese el distrito: ")

	papel = [tipoCedula, numCedula, nombre, telefono, correo, provincia, canton, distrito]

	matriz.append (papel)

	print ("\nFactura registrada con exito!")

	##GUARDAR##

	textoGuardar = guardarMatriz (matriz)
	guardarTXT ("Facturas.txt", textoGuardar)
	return matriz

#### Crear PAQUETE ####

def paquete (matriz, sesionA, documento):
	dest = input("Ingrese el nombre del destinatario: ")
	telf = input("Ingrese el telefono del destinatario: ")
	ced = input("Ingrese el numero de cedula del destinatario: ")
	pes = input("Ingrese el peso del paquete: ")
	cobro = (input("Ingrese la opcion de compra contra entrega [Monto a cobrar ¢1500]: "))

	infor = [dest, telf, ced, pes, cobro]

	matriz.append (infor)
	sesionA = infor

	print ("\nPaquete creado exitosamente!")

	##GUARDAR##

	textoGuardar = guardarMatriz (matriz)
	guardarTXT ("Paquetes.txt", textoGuardar)

	textoGuardar = guardarMatriz (matriz)
	guardarTXTAnadir (documento, str(infor))
	return matriz
	return sesion

### BUSCAR CUENTA ###

def buscarCuenta (matriz, cuenta):

	cedula = input ("Ingrese su cedula: ")
	cuentaEncontrada = []

	for fila in range(len(matriz)):

		if cedula == matriz[fila][5]:
			cuentaEncontrada = (matriz [fila])
			cuenta.append (cuentaEncontrada)
			print (cuentaEncontrada)
			print ("\nCUENTA ENCONTRADA!\n\n")
			print ("**** BIENVENID@ A SU CUENTA ",cuentaEncontrada[3], "DE ", cuentaEncontrada[1], "****")

	if (len(cuentaEncontrada) == 0):
		print ("Usario NO existe, cree uno")
		cuenta = cuentaEncontrada

	return matriz
	return cuenta

### GENERAR GUIA ###

def crearGuia (matrizCod, matrizComer, matrizPqt):

	numeroG = (len(matrizCod)) + 1
	nGuia = str(f"GUIAPQT{numeroG}")

	for fila in range(len(matrizComer)):
		nomCom = matrizComer[fila][1]
		telCom = matrizComer[fila][2]

	for fila in range(len(matrizPqt)):
		nomdest = matrizPqt[fila][0]
		teldest = matrizPqt[fila][1]


		estado = ("Creado")

	guia = [nGuia, nomCom, telCom, nomdest, teldest, estado]

	matrizCod.append (guia)

	print ("Su numero de GUIA es: ", nGuia)

	##GUARDAR##

	textoGuardar = guardarMatriz (matrizCod)
	guardarTXT ("Guias.txt", textoGuardar)

	return matrizPqt

def rastrearPaquete (matriz):

	cant = []

	numeroGuia = input ("Ingrese el numero de guia: ")

	for fila in range(len(matriz)):

		num = matriz[fila][0]

		if numeroGuia == num:
			print ("El estado del paquete es: ", matriz [fila][5])

			cant = (matriz [fila])

	if (len(cant)== 0):
		print ("Numero de Guia NO encontrado, intente de nuevo")

	return (matriz)

def cambiarEstado (matriz):

	estadoActual = []

	numeroGuia = input ("Ingrese el numero de guia: ")

	for fila in range (len(matriz)):
		if numeroGuia == matriz [fila][0]:
			estadoActual = matriz [fila]
			print ("Estado actual del paquete: ", estadoActual[5])
			print ("\nIngrese el nuevo estado:")
			estadoNuevo = input ("Ingrese estado: ")
			estadoActual[5] = estadoNuevo

			matriz[fila] = estadoActual

			##GUARDAR##

			textoGuardar = guardarMatriz (matriz)
			guardarTXT ("Guias.txt", textoGuardar)
			print ("***Estado Actualizado***")
			break

	if (len(estadoActual)== 0):
		print ("Numero de guia NO encontrado, intente nuevamente")
	return matriz

def verFactura (matriz):

	facturaVer = input ("Ingrese numero de cedula: ")
	fac = []

	for fila in range(len(matriz)):

		if facturaVer == matriz [fila][1]:
			fac = matriz[fila]

			matriz.append (fac)

			print ("\n____________________________\nFACTURA\n\nTipo de Cedula: ", fac[0], "\nCedula: ", fac[1], "\nNombre: ",fac[2], "\nTelefono: ",fac[3], "\nCorreo: ",fac[4], "\nUbicacion: ", fac[5], ",", fac[6], ",", fac[7],".\n____________________________")

	if (len(fac) == 0):
		print ("No se encontro la factura")

	return ("")

def verGuias (matriz):

	facturaVer = input ("Ingrese numero de GUIA: ")
	fac = []

	for fila in range(len(matriz)):

		if facturaVer == matriz [fila][0]:
			fac = (matriz [fila])

			matriz.append (fac)

			print ("\n____________________________\nGUIA\n\nNumero de Guia: ", fac[0], "\nNombre REMITENTE: ", fac[1], "\nTelefono REMITENTE: ",fac[2], "\nNombre DESTINATARIO: ",fac[3], "\nTelefeno DESTINATARIO: ",fac[4], "\nEstado Paquete: ", fac[5], "\n____________________________")

	if (len(fac) == 0):
		print ("No se encontro la guia")

	return ("")

def estadisticas(documento):
	matriz = []

	file = open (documento, "r")
	lineas = file.readlines ()

	for linea in lineas:
		linea = linea.replace ("\n", "")
		linea = linea.replace ("[", "")
		linea = linea.replace ("]", "")
		linea = linea.replace ("'", "")
		linea = linea.replace (" ", "")

		arreglo = linea.split (",")
		matriz.append (arreglo)

	montoT = 0

	for fila in range(len(matriz)):
		monto = matriz [fila][4]
		monto = int(monto)
		montoT = montoT + monto

	print ("El total de monto gastado en paquetes: ", montoT)


### MENU A MOSTRAR ###

usuarios = cargarArchivo ("Usuarios.txt")
paquetes = cargarArchivo ("Paquetes.txt")
facturas = cargarArchivo ("Facturas.txt")
guias = cargarArchivo ("Guias.txt")

opc = 0

while opc != 3:

	print("►►►► Bienvenido al Programa de Mensajeria Fidelitas ◄◄◄◄\n")
	print("▬▬▬▬ MENU ▬▬▬▬\n")
	print("Opciones:")
	print("1. Crear cuenta de usuario")
	print("2. Entrar a cuenta")
	print("3. Salir\n")

	opc = int(input("Ingrese una opcion: "))

	if opc == 1:

		registrarUsuario (usuarios)

	if opc == 2:

		buscarCuenta (usuarios, cuentaE)

		if (len(cuentaE)) > 0:

			sesionActual = cuentaE[0][5]
			nomDoc = sesionActual+".txt"

			file = open (nomDoc, "a")
			file.close

			cuentaE = []

			seleccion = 0

			while seleccion != 7:

				print ("MENU\n\nQue accion desea realizar?\n\n1.Crear paquete\n2.Rastrear paquete\n3.Cambiar estado de paquete\n4.Ver factura\n5.Ver guia\n6.Ver estadisticas\n7.Salir")

				seleccion = int(input("\n\nIngrese una opcion: "))

				if seleccion == 1:
					paquete (paquetes, sesionActual, nomDoc)
					crearGuia (guias, usuarios, paquetes)

					print ("\nSi desea factura electronica, ingrese 1, si no, ingrese 2: ")
					dec = int(input("Ingrese la decision: "))

					if dec == 1:
						factura (facturas)

					else:
						print ("Continue")

				if seleccion == 2:

					rastrearPaquete (guias)

				if seleccion == 3:

					cambiarEstado (guias)

				if seleccion == 4:

					verFactura (facturas)

				if seleccion == 5:

					verGuias (guias)

				if seleccion == 6:
					print ("MENU")
					print ("Seleccione, que estadistica desea visualizar?\n1.Cantidad de envios\n2.Lista de paquetes enviados\n3.Monto de Cobro\n4.Cantidad de paquetes por numero de telefono\n5.Cantidad de paquetes por cedula\n6.Salir")
					
					tot = 0

					file = open (nomDoc, "r")

					lineas = file.readlines ()

					sel = int(input("Escoja una opcion: "))

					if sel == 1:
						for linea in lineas:
							tot = tot+1

						print ("El total de envios es: ",tot)

					if sel == 2:
						print ("La lista de envios es: ")
						for linea in lineas:
							print (linea,"\n")

					if sel == 3:
						estadisticas(nomDoc)

					if sel == 5:
						cedVer = input ("Ingrese cedula: ")
						totExcl = 0
						for linea in lineas:
							if cedVer in linea:
								totExcl = totExcl + 1

						print ("El total por esa cedula es: ",totExcl)

					if sel == 4:
						telVer = input ("Ingrese telefono: ")
						totExcl = 0
						for linea in lineas:
							if telVer in linea:
								totExcl = totExcl + 1

						print ("El total por ese telefono es: ",totExcl)

					
				if seleccion == 7:
					print ("De vuelta al MENU PRINCIPAL\n\n")

	sesionActual = []
	pqtActuales = []

		



print ("Gracias por usar el programa, hasta luego!")
