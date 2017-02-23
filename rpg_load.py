import time
import sys
import os
from rpg_hero import Hero
from random import randint
def spinning_cursor():
	while True:
		for cursor in '2746103958':
			yield cursor
spinner = spinning_cursor()

class load_game(object):
	@staticmethod
	def game_start(hero):
		print "Enter your name"
		print ">",
		hero.name = raw_input()
		os.system("say --voice=Maged 'Hello' "+hero.name+"'! Good luck!'")
		time.sleep(0.5)
		print "Roll for health",
		print ">",
		raw_input()
		for _ in range(20):
			sys.stdout.write(spinner.next())
			sys.stdout.flush()
			time.sleep(0.1)
			sys.stdout.write('\b')
		hero.health = (randint(1,9))
		print "Your health is "+str(hero.health)
		
		# time.sleep(0.5)
		# print "Roll for power"
		# print ">"
		# hero.power = (randint(0,9))
		# print "Your power is "+str(hero.power)
		# time.sleep(0.5)
		# print "Roll for luck"
		# print ">"
		# hero.luck = (randint(0,9))
		# print "Your luck is "+str(hero.luck)
		# time.sleep(0.5)
		# print "Roll for shield"
		# print ">"
		# hero.shield = (randint(0,9))
		# print "Your shield is "+str(hero.shield)