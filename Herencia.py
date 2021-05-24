class Vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelera(self):
		self.acelera=True

	def frena(self):
		self.frena=True	

	def estado(self):
		print("Marca:", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha ", 
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)			
	class Moto(Vehiculos):
			hcaballito=""
		def caballito(self):
			self.hcaballito="Voy haciendo caballito"
		def estado(self):
			print("Marca:", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha ", 
				self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, "n", self.hcaballito)	
miMoto=Moto("Honde", "CBR")  
miMoto.caballito()
miMoto.estado()

