import time
from character import Character

class Hero(Character):
	def __init__(self):
		Character.__init__(self, "Hero", 6, 2)
		self.luck = 0
		self.shield = 0

	def attack(self, enemy):
		print "%s attacks %s with %d power." % (self.name, enemy.name, self.power)
		enemy.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s. %s now has %d health." % (self.name, self.power, enemy.name, enemy.name, enemy.health)
		time.sleep(1.5)
