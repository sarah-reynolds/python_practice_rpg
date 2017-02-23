from character import Character
import time

class Murloc(Character):
	def __init__(self):
		Character.__init__(self, "Murloc", 6, 2)

	def attack(self,hero):
		print "%s attacks %s with %d power." % (self.name, hero.name, self.power)
		hero.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s. %s now has %d health." % (self.name, self.power, hero.name, hero.name, hero.health)

class Dragon(Character):
	def __init__(self):
		Character.__init__(self, "Dragon", 10, 10)

	def attack(self,hero):
		print "%s attacks %s with %d power." % (self.name, hero.name, self.power)
		hero.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s. %s now has %d health." % (self.name, self.power, hero.name, hero.name, hero.health)