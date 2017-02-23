class Character(object):
	def __init__(self, name, health, power):
		self.name = name
		self.health = health
		self.power = power

	def alive(self):
		return self.health > 0

	def take_damage(self,points_of_damage):
		self.health -= points_of_damage