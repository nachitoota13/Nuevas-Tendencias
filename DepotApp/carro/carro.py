class carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            self.session["carro"]={}
            self.carro=self.session["carro"]
        else:
            self.carro=carro

def agregar (self, articulo):
    id=str(articulo.id)
    if id not in self.carro.keys():
        self.carro[id]={
            "articulo_id":articulo.id,
            "nombre":articulo.Nombre,
            "precio":str(articulo.precio),
            "cantidad":1,
            "imagen":articulo.imagen.url
        }
    else:
        self.carro[id]["cantidad"]+=1
        self.carro[id]["precio"]=self.carro[id]["cantidad"]*articulo.precio
    self.guardarCarro()

def guardarCarro(self):
    self.session["carro"]=self.carro
    self.session.modified=True

def eliminar(self,articulo):
    articulo.id=str(articulo.id)
    if articulo.id in self.carro:
        del self.carro[articulo.id]
        self.guardarCarro()

def restar(self,articulo):
    for key, value in self.carro.items():
        if key==str(articulo.id):
            value["cantidad"]=value["cantidad"]-1
            if value["cantidad"]==0:
                self.eliminar(articulo)
            break
    self.guardarCarro()

def limpiarCarro(self):
    carro=self.session["carro"]={}
    self.session.modified=True
