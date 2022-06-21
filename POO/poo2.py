import datetime 
class Reloj:
	hora = datetime.datetime.now()

class Rolex(Reloj):
	marca = 'rolex'
	


r1= Reloj()

r2 = Rolex()

print(r2.hora)

