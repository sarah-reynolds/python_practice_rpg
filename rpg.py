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
def spinning_cursor():
	while True:
		for cursor in '2746103958':
			yield cursor
spinner = spinning_cursor()

load_game.game_start(hero)

for enemy in enemies:
	# print vars(enemy)
	while hero.alive() and enemy.alive():
		print "An evil %s approaches. What will you do?" % enemy.name
		time.sleep(1.5)
		print "1. Fight %s" % enemy.name
		time.sleep(1)
		print "2. Run away"
		print "> ",
		input = int(raw_input())
		if input == 1:
			# enemy.health -= hero.power
				
			hero.attack(enemy)
			while hero.alive() and enemy.alive():
				print "Roll to see who strikes next! Over 5, it's your turn.",
				print "> ",
				input = raw_input()
				for _ in range(10):
					sys.stdout.write(spinner.next())
					sys.stdout.flush()
					time.sleep(0.1)
					sys.stdout.write('\b')
				fight_luck = (randint(0,9))
				print fight_luck
				time.sleep(0.3)
				print "You rolled a "+str(fight_luck)
				time.sleep(1)
				if fight_luck > 5:
					hero.attack(enemy)
				else:
					enemy.attack(hero)
			# if hero.alive():
			# 	if enemy.alive():
			# 		hero.attack(enemy)
			# 	print "%s is dead! You win!" % enemy.name
			# 	break
			# else:
			# 	print "You were defeated by the ferocious %s. Game over!" % enemy.name
			# 	break
		elif input == 2:
			hero.run_away(enemy)

			break
		else:
			print "Invalid choice %s" % input
		if enemy.alive():
			hero.health -= enemy.power
	
