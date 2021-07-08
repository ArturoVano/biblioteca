#Programa MODIFICADO del que estaba en el ejercicio de python del examen:

def listarLibro(bib): #Simple bucle que muestra las llaves y sus valores del diccionario pasado como parámetro.
    print("\n Biblioteca actual:")
    for i in bib:
        print("ISBN:", i, "Titulo:",bib[i])
    print("\n")

def addModBook(bib): #Para añadir o modificar libros

    print("Introduce un ISBN:")
    isbn = input()
    if isbn in bib:
        
        correcto = False #Variable para asegurar que el usuario solo tiene dos respuestas para avanzar.      
        while correcto != True:
            print("El ISBN ya se encuentra en el diccionario, ¿Quieres modificarlo?")
            try: # Controlamos las exepciones en caso de no introducir un entero
                resp = int(input("1.Si, 2.No "))
                if resp == 1:

                    new =input("Nuevo libro: ")
                    bib[isbn] = new
                    correcto = True #Para que no repita el bucle
                elif resp == 2:

                    print("Ok, Adiós")
                    correcto = True #Para que no repita el bucle
                else:
                    print("Valor no válido, es o 0(no) o 1(si). Te lo vuelvo a preguntar ")                   

            except ValueError:
                print("Valores incorrectos. Te lo vuelvo a preguntar ")
                
                
    else:
        book = input("No hay libro con ese ISBN, introduce el libro: ")
        bib[isbn] = book #Nueva llave y valor en el diccionario
    
    return bib

def borrarLibro(bib):

    isbn = input("Introduce el ISBN del libro que deseas borrar: ")
    if isbn in bib:

        correcto = False        
        while correcto != True:
            print("¿Seguro que deseas eliminarlo? ")
            try:
                resp = int(input("1.Si, 2.No "))
                if resp == 1:
                    
                    bib.pop(isbn)
                    print("Eliminado con éxito")
                    correcto = True #Para que no repita el bucle
                elif resp == 2:

                    print("Ok, adiós")
                    correcto = True #Para que no repita el bucle
                else:
                    print("Valor no válido, es o 2(no) o 1(si). Te lo vuelvo a preguntar ")                  

            except ValueError:
                print("Valores incorrectos. Te lo vuelvo a preguntar ")

    else:
        print("El isbn", isbn, "no existe en este diccionariom añadelo antes de borrarlo \n")

    return bib


biblioteca ={"3432dfs4" : "La casa de Bernarda Alba",
            "45623hf4" : "Luces de Bohemia",
            "fa3893": "El príncipe de la niebla" }

biblioteca = addModBook(biblioteca)
listarLibro(biblioteca)
biblioteca = borrarLibro(biblioteca)
listarLibro(biblioteca)