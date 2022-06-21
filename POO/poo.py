import datetime 
class Reloj:
	hora = datetime.datetime.now()
	def __init__ (self,nombre,precio):
		self.nombre = nombre
		self.precio = precio

	def marca(self):
		print('mi Reloj es '+self.nombre)

	def tipo(self, x):
		if self.nombre == 'rolex': 
			if x == 'submarin':
				self.precio = self.precio + 10000
				print('tu rolex es mas caro' + str(self.precio))
			else : 
				print('tu rolex es de lo baratos')
		else: 
			print('solo se de rolex')




r1= Reloj('rolex',10000)
r2= Reloj('tissot',10000)
r3= Reloj('rolex',5)

r1.tipo('submarin')
r2.tipo('r540')
r3.tipo('datejust')

r1.damelahora()
r2.damelahora()
