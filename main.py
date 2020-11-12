#!/bin/python3
# -*- coding: utf-8 -*-

from core.horloge import Horloge

def main():
	timer = Horloge(23, 59, 54)

	print("Démarrage de l'objet \"{}\" avec comme paramètre:\n".format(timer.name))
	print("\t{} Heures".format(timer.get("hours")))
	print("\t{} Minutes".format(timer.get("minutes")))
	print("\t{} Seconds".format(timer.get("seconds")))

	input("\npress [ ENTER ] to start ...")

	timer.start()

if(__name__ == "__main__"):
	main()
