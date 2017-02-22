import time

class Hero(object):
	def __init__(self):
		self.name = "Incognito"
		self.health = 10
		self.power = 5

	def alive(self):
		return self.health > 0

	def attack(self, enemy):
		print "%s attacks %s with %d power." % (self.name, enemy.name, self.power)
		enemy.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s. %s now has %d health." % (self.name, self.power, enemy.name, enemy.name, enemy.health)
		time.sleep(1.5)
