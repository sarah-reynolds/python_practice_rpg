from character import Character
import time
import os

class Murloc(Character):
	def __init__(self):
		Character.__init__(self, "Murloc", 5, 2)

	def attack(self,hero):
		print "%s attacks %s with %d power." % (self.name, hero.name, self.power)
		os.system("say --voice=Maged 'mrglgrgle'")
		hero.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s." % (self.name, self.power, hero.name)
		time.sleep(1.5)
		print "%s's health: %d  |  %s's health: %d" % (self.name, self.health, hero.name, hero.health)
		if hero.alive() != True:
			print "You died."

class Dragon(Character):
	def __init__(self):
		Character.__init__(self, "Dragon", 10, 10)

	def attack(self,hero):
		print "%s attacks %s with %d power." % (self.name, hero.name, self.power)
		os.system("say --voice=Maged 'mrglgrgle'")
		hero.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s." % (self.name, self.power, hero.name)
		time.sleep(1.5)
		print "%s's health: %d  |  %s's health: %d" % (self.name, self.health, hero.name, hero.health)
		if hero.alive() != True:
			print "You died."