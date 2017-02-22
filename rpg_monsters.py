class Goblin(object):
	def __init__(self):
		self.name = "Goblin"
		self.health = 6
		self.power = 2

	def alive(self):
		return self.health > 0

	def take_damage(self,points_of_damage):
		self.health -= points_of_damage

	def attack(self,hero):
		print "%s attacks %s" % (self.name, hero.name)
		hero.take_damage(self.power)
