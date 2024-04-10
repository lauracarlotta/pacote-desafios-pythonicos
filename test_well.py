class Animal:
	def __init__(self, name, color, size):
		self.name = name
		self.color = color
		self.size = size
	def come_muito(self):
		return True


class Mamifero(Animal):
	def bebe_leite(self):
		return True


class Felinos(Mamifero):
	def bom_escalador(self):
		return True


class Canideos(Mamifero):
	pass

class Dog(Canideos):
	# def __init__(self, name):
	# 	self.name = name

	def late(self):
		return "Au au"

	def o_que_faz(self):
		return f'{self.name} {self.late()} demais'