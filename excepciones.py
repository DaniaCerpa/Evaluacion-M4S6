usuarios = {"001": "Marca", "002": "Mónica", "003": "Jacob"}


#Se establece un valor "vacio" inicialmente para el id del usuario. Este se modificar luego dento de la ejecucion del while.
id_usuario = ""

while id_usuario not in usuarios:
    try:
        id_usuario = input("Ingrese el ID del usuario que quiere buscar: ")
        
        #Intentamos convertir el dato ingresado a un numero entero, si no es posible lanzara ValueError
        id_numero = int(id_usuario)
        
        #Volvemos a convertir el dato en string para lograr el mismo formato que las demas claves en el diccionario con la funcion zfill()
        id_usuario = str(id_numero).zfill(3)
        
        resultado = usuarios[id_usuario]
        
        print(resultado)
        
    except ValueError:
        print("El ID solicitado no es de un tipo valido. Porfavor ingrasa un numero")
        
    except KeyError:
        print(f"La clave {id_usuario} no está en el diccionario. Añadiendo clave...'")
        
        #Se agrega nueva clave-valor al diccionario
        usuarios[id_usuario] = "Ninguno"
        print(usuarios)
    
