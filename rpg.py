from rpg_hero import Hero
from rpg_monsters import Murloc, Dragon
from random import randint
from rpg_load import load_game
import time
import sys
import character
hero = Hero()
# load_game = load_game()
enemies = [Murloc(),Dragon()]

# list_of_all_enemy_classes = ['vampire','ghost','zombie']
# how_many_enemies = raw_input()
# for i in range(0,how_many_enemies)


load_game.game_start()

for enemy in enemies:
	# print vars(enemy)
	while hero.alive() and enemy.alive():
		print "An evil %s approaches. What will you do?" % enemy.name
		time.sleep(1)
		print "1. Fight %s" % enemy.name
		time.sleep(1)
		print "2. Run away"
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
			print "Roll for luck to see if you escape. 5+ to make it away safely, under 5 the enemy attacks as you escape."
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
			time.sleep(0.3)
			if luck_roll > 5:
				time.sleep(1.5)
				print "You escaped safely!"
				time.sleep(1.5)
			else:
				print "The %s attacks you as you escape!" % enemy.name
				time.sleep(1.5)
				enemy.attack(hero)
				time.sleep(1.5)
				if hero.alive():
					print "Although %s hurt you, you managed to escape." % enemy.name
				else:
					print "%s killed you as you tried to escape. Game over."
			break
		else:
			print "Invalid choice %s" % input
		if enemy.alive():
			hero.health -= enemy.power
	
