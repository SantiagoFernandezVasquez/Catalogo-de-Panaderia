#Listas de categorias con sus respectivos productos y promociones
Panes = {
    "Pan de Bono": 700,
    "Pan de Queso": 800,
    "Pan Cascarita": 500,
    "Pan de Yuca": 800,
    "Calentano": 700,
    "Rollito de Sal": 900,
    "Pan Integral": 700,
    "Pan relleno de Arequipe": 1150,
    "Pan con Salchicha": 1300,
    "Pan recubierto de Chocolate": 1200}
Pasteles = {
    "Pastel de Vainilla": 5000,
    "Pastel de Chocolate": 5500,
    "Pastel de bodas": 10000,
    "Glaseado de Vainilla": 3000,
    "Glaseado de Chocolate": 3500,
    "Pastel de Arequipe": 5700,
    "Pastel de Oreo": 7000,
    "Postre de Limon": 4300,
    "Postre de Vainilla": 4000,
    "Postre de Tres Leches": 4500}
Bebida = {
    "Coca-Cola": 3000,
    "Pepsi": 2900,
    "Red-Bull": 4000,
    "Gatorade": 3700,
    "Budweiser": 3200,
    "Hit": 2500,
    "Pony-Malta": 2300,
    "Sprite": 3200,
    "Monster": 3000,
    "Tropicana": 2400,
    "-Promociones-": "Algunas promociones de la seccion de Bebidas",
    "1 Pan con Salchicha y 1 Pony Malta": 3000,
    "1 Postre de Oreo y 1 Budweiser": 9000}
Promociones = {
    "6 Panes Integrales": 4000,
    "5 Panes recubiertos de Chocolate": 5500,
    "3 Pasteles de Vainilla": 13000,
    "4 Postres de Oreo": 25000,
    "1 Pan con Salchicha y 1 Pony Malta": 3000,
    "1 Postre de Oreo y 1 Budweiser": 9000}

productos_por_categoria = {
    "Panaderia": Panes,
    "Pasteleria": Pasteles,
    "Bebidas": Bebida,
    "Apartado de promociones": Promociones} 

#Bienvenida al Usuario
print("Bienvenido Usuario a la Panaderia Digital de Campusland")
print()
#Menu
print("Este es el menu de seleccion de productos")
for i,categoria in enumerate(productos_por_categoria, start=0):
    print(f" {i+1}. {categoria}")

#Aparecen las categorias al Usuario
print()
escoger_categoria = int(input("Escriba el numero de la seccion a la cual quiere acceder: "))

#Hacemos un bucle con While por si el usuario se equivoque al escoger un producto o cantidad
while True:
    categoria_seleccionada = list(productos_por_categoria.keys())[escoger_categoria - 1]
    productos_categoria_seleccionada = productos_por_categoria[categoria_seleccionada]

    print(f"\nProductos disponibles en la categoria '{categoria_seleccionada}':")
    for i, (producto, precio) in enumerate(productos_categoria_seleccionada.items(), start=1):
        print(f" {i}. {producto} - ${precio}")

    #Creamos un carrito virtual
    carrito_virtual = {}

    #Seleccionar el articulo y la cantidad
    productos = int(input("\nSeleccione el producto que desea comprar: "))

    producto_seleccionado = list(productos_categoria_seleccionada.keys())[productos - 1]
    precio_producto_seleccionado = productos_categoria_seleccionada[producto_seleccionado]

    producto in productos_categoria_seleccionada
    cantidad = int(input(f"Ingrese la cantidad de: {producto_seleccionado}: "))

    carrito_virtual[producto_seleccionado] = cantidad
    total = sum(productos_categoria_seleccionada[producto_seleccionado] * cantidad for producto_seleccionado, cantidad in carrito_virtual.items()) 
    
    print(f"\nTotal a pagar: ${total}")
#print (precio x cantidad)
    #Confirmacion de usuario si realmente desea comprar el articulo
    respuesta = input("¿Esta es una confirmacion para la compra, esta todo listo? (Si o No): ")

    if respuesta.lower() == "si":
        print("Perfecto, continuemos con el pago del producto")
        break
    else:
        print("Esta bien, puedes seleccionar otro articulo de la lista si deseas")

#Empezar el proceso de pago por el producto
dinero = int(input("Ingrese la cantidad de dinero que posee: "))

vueltos = dinero - precio_producto_seleccionado
if dinero >= precio_producto_seleccionado:
    print(f"Usuario usted compro el producto: {producto_seleccionado} con un valor de {total}, sus vueltos son: ${vueltos}, gracias por su compra.")
else:
    print(f"Usuario el producto que desea comprar {producto_seleccionado} con un valor de {total}, le falta un total de ${-vueltos}")
