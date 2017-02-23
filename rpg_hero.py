import time
import sys
from character import Character
import os
from random import randint

class Hero(Character):
	def __init__(self):
		Character.__init__(self, "Hero", 6, 2)
		self.luck = 0
		self.shield = 0

	def attack(self, enemy):
		print "%s attacks %s with %d power." % (self.name, enemy.name, self.power)
		enemy.take_damage(self.power)
		time.sleep(1.5)
		print "%s has done %d damage to %s." % (self.name, self.power, enemy.name)
		time.sleep(1.5)
		print "%s's health: %d  |  %s's health: %d" % (self.name, self.health, enemy.name, enemy.health)
		if enemy.alive() != True:
			print "You win."

	def run_away(self, enemy):
		print "Roll for luck to see if you escape. 5+ to make it away safely, under 5 the enemy attacks as you escape.",
		print ">",
		raw_input()
		def spinning_cursor():
			while True:
				for cursor in '2746103958':
					yield cursor
		spinner = spinning_cursor()
		for _ in range(20):
			sys.stdout.write(spinner.next())
			sys.stdout.flush()
			time.sleep(0.1)
			sys.stdout.write('\b')
		luck_roll = (randint(0,9))
		print luck_roll
		time.sleep(0.3)
		print "You rolled a "+str(luck_roll)
		time.sleep(1.0)
		if luck_roll > 5:
			print "You escaped safely!"
			time.sleep(1.5)
		else:
			print "Not enough luck! The %s attacks as you escape!" % enemy.name
			time.sleep(1.5)
			enemy.attack(self)
			time.sleep(1.5)
			if hero.alive():
				print "Although %s attacked, you managed to escape." % enemy.name
			else:
				print "%s killed you as you tried to escape. Game over."
