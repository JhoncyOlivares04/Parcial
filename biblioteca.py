libro_1 = {'nombre': 'Harry Potter y la piedra filsofal', 'autor': 'J.k Rowling', 'codigo': 'HPJK1997', 'año': 1997, 'precio': 25000, 'costo': 9000, 'cantidad': 200}
libro_2 = {'nombre': 'Juegos del Hambre', 'autor': 'Suzanne Collins', 'codigo': 'JHSC2008', 'año': 2008, 'precio': 27000, 'costo': 12000, 'cantidad': 20}
libro_3 = {'nombre': 'El Hobit', 'autor': 'J.R.R. Tolkien', 'codigo': 'EHJR1937', 'año': 1937, 'precio': 35000, 'costo': 15000, 'cantidad': 100}
libro_4 = {'nombre': 'Hamlet', 'autor': 'William Shakespeare', 'codigo': 'HWS1589', 'año': 1589, 'precio': 26000, 'costo': 13000, 'cantidad': 20}

libros = [libro_1, libro_2, libro_3, libro_4]

mejor_libro = None
ganancia_maxima = 0

for libro in libros:
    cantidad = libro['cantidad']
    precio = libro['precio']
    costo = libro['costo']
    ganancia = precio - costo
    
    if cantidad >= 100 and ganancia > 14000:
        if cantidad > 800:
            precio = precio * 1.1
        
        ganancia_neta = (precio - costo) * cantidad
        
        if ganancia_neta > ganancia_maxima:
            ganancia_maxima = ganancia_neta
            mejor_libro = libro

if mejor_libro:
    print("El mejor libro para ser vendido es:", mejor_libro['nombre'], "de", mejor_libro['autor'], "con código", mejor_libro['codigo'], "publicado en", mejor_libro['año'], "y precio de", mejor_libro['precio'], "pesos.")
else:
    print("Ninguno de los libros es la mejor opción para ser vendido.")
