from rpg_hero import Hero
from rpg_monsters import Goblin
hero = Hero()
enemies = [Goblin()]
import time

for enemy in enemies:
	# print vars(enemy)
	while hero.alive() and enemy.alive():
		print "An evil goblin approaches. What will you do?"
		time.sleep(1)
		print "1. Fight %s" % enemy.name
		time.sleep(1)
		print "2. Run away"
		time.sleep(1)
		print "> ",
		input = int(raw_input())
		if input == 1:
			# enemy.health -= hero.power
			hero.attack(enemy)
			if hero.alive():
				if enemy.alive():
					hero.attack(enemy)
				print "You won. The %s is defeated" % enemy.name
				break
			else:
				print "You were defeated by the ferocious %s" % enemy.name
				break
		elif input == 2:
			print "You take the coward's way and run to safety."
			break
		else:
			print "Invalid choice %s" % input
		if enemy.alive():
			hero.health -= enemy.power
	
