class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")  # Cambié esto

        # Inicializa carrito vacío si no existe
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito




    def agregar_carrito(self, producto):
        id = str(producto.id)  # Corrección de 'srt' a 'str'
        if id not in self.carrito.keys():  # Cambié .key() a .keys()
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "descripcion": producto.descripcion,
                "precio": str(producto.precio),  # Asegúrate que el precio sea un número
                "imagen": producto.imagen.url,  # Asegúrate que la imagen se maneje correctamente
                "cantidad": 1,  # Inicializa cantidad
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    self.guardar_carrito()
                    break

    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito  # Guarda el carrito en la sesión
        self.session.modified = True



    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        for key, value in self.carrito.items():
            if key ==str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                else:
                    self.guardar_carrito()
                break
            else:
                print("El Producto no existe en el carrito.")


    def sumar(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value["cantidad"] += 1  # Incrementar la cantidad en 1
                self.guardar_carrito()  # Guardar los cambios en la sesión
                break
        else:
            print("El Producto no existe en el carrito.")
            

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


    