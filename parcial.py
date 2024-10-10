productos = [ 
{'idproducto':1,'nombreProducto':'Té de frutos rojos','idProveedor':'1','idCategoria':'1','cantidadPorUnidad':'10 cajas x 20 bolsas','preciounidad':18,'unidadesEnExistencia':'39','unidadesEnPedido':'0','nivelNuevoPedido':'10','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':2,'nombreProducto':'Cerveza tibetana Barley','idProveedor':'1','idCategoria':'1','cantidadPorUnidad':'24 bot. 12 l','preciounidad':19,'unidadesEnExistencia':'17','unidadesEnPedido':'40','nivelNuevoPedido':'25','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':3,'nombreProducto':'Sirope de regaliz','idProveedor':'1','idCategoria':'2','cantidadPorUnidad':'12 bot. 550 ml','preciounidad':10,'unidadesEnExistencia':'13','unidadesEnPedido':'70','nivelNuevoPedido':'25','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':4,'nombreProducto':'Especias Cajun del chef Anton','idProveedor':'2','idCategoria':'2','cantidadPorUnidad':'48 frascos 6 l','preciounidad':22,'unidadesEnExistencia':'53','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':5,'nombreProducto':'Mezcla Gumbo del chef Anton','idProveedor':'2','idCategoria':'2','cantidadPorUnidad':'36 cajas','preciounidad':21,'unidadesEnExistencia':'0','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'1','categoriaProducto':'Categoria D'},
{'idproducto':6,'nombreProducto':'Mermelada de grosellas de la abuela','idProveedor':'3','idCategoria':'2','cantidadPorUnidad':'12 frascos 8 l','preciounidad':25,'unidadesEnExistencia':'120','unidadesEnPedido':'0','nivelNuevoPedido':'25','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':7,'nombreProducto':'Peras secas org','idProveedor':'3','idCategoria':'7','cantidadPorUnidad':'12 paq. 1 kg','preciounidad':30,'unidadesEnExistencia':'15','unidadesEnPedido':'0','nivelNuevoPedido':'10','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':8,'nombreProducto':'Salsa de ar','idProveedor':'3','idCategoria':'2','cantidadPorUnidad':'12 frascos 12 l','preciounidad':40,'unidadesEnExistencia':'6','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':9,'nombreProducto':'Buey Mishi Kobe','idProveedor':'4','idCategoria':'6','cantidadPorUnidad':'18 paq. 500 g','preciounidad':97,'unidadesEnExistencia':'29','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'1','categoriaProducto':'Categoria D'},
{'idproducto':10,'nombreProducto':'Pez espada','idProveedor':'4','idCategoria':'8','cantidadPorUnidad':'12 frascos 200 ml','preciounidad':31,'unidadesEnExistencia':'31','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':11,'nombreProducto':'Queso Cabrales','idProveedor':'5','idCategoria':'4','cantidadPorUnidad':'paq. 1 kg','preciounidad':21,'unidadesEnExistencia':'22','unidadesEnPedido':'30','nivelNuevoPedido':'30','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':12,'nombreProducto':'Queso Manchego La Pastora','idProveedor':'5','idCategoria':'4','cantidadPorUnidad':'10 paq. 500 g','preciounidad':38,'unidadesEnExistencia':'86','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':13,'nombreProducto':'Algas Konbu','idProveedor':'6','idCategoria':'8','cantidadPorUnidad':'caja 2 kg','preciounidad':6,'unidadesEnExistencia':'24','unidadesEnPedido':'0','nivelNuevoPedido':'5','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':14,'nombreProducto':'Cuajada de jud','idProveedor':'6','idCategoria':'7','cantidadPorUnidad':'40 paq. 100 g','preciounidad':23,'unidadesEnExistencia':'35','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':15,'nombreProducto':'Salsa de soja baja en sodio','idProveedor':'6','idCategoria':'2','cantidadPorUnidad':'24 bot. 250 ml','preciounidad':16,'unidadesEnExistencia':'39','unidadesEnPedido':'0','nivelNuevoPedido':'5','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':16,'nombreProducto':'Postre de merengue Pavlova','idProveedor':'7','idCategoria':'3','cantidadPorUnidad':'32 cajas 500 g','preciounidad':17,'unidadesEnExistencia':'29','unidadesEnPedido':'0','nivelNuevoPedido':'10','suspendido':'0','categoriaProducto':'Categoria D'},
{'idproducto':17,'nombreProducto':'Cordero Alice Springs','idProveedor':'7','idCategoria':'6','cantidadPorUnidad':'20 latas 1 kg','preciounidad':39,'unidadesEnExistencia':'0','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'1','categoriaProducto':'Categoria D'},
{'idproducto':18,'nombreProducto':'Langostinos tigre Carnarvon','idProveedor':'7','idCategoria':'8','cantidadPorUnidad':'paq. 16 kg','preciounidad':63,'unidadesEnExistencia':'42','unidadesEnPedido':'0','nivelNuevoPedido':'0','suspendido':'0','categoriaProducto':'Categoria D'}]

def busqueda(lista):
    if len(lista)<=1:
        return lista
    else:
        pivot=lista[len(lista)//2]
        izquierda = [x for x in lista if x['preciounidad'] < pivot['preciounidad']]
        medio = [x for x in lista if x['preciounidad'] == pivot['preciounidad']]
        derecha = [x for x in lista if x['preciounidad'] > pivot['preciounidad']]
    return busqueda(derecha) + medio + busqueda(izquierda)
def ordenar_n_productos_costosos(productos, n):
    productos_ordenados = busqueda(productos)
    return productos_ordenados[:n]
print(ordenar_n_productos_costosos(productos,6))




