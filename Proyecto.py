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
