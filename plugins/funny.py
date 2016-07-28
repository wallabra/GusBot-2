import json

from random import choice
from plugincon import bot_command, easy_bot_command, get_message_target, get_bot_nickname, reload_all_plugins


@easy_bot_command("hack")
def hack(message, raw):
	if not raw:
		hackdata = json.load(open("hackstrings.json"))
		
		hack_subjects = hackdata["subjects"]
		hack_targets = hackdata["targets"]
		hack_means = hackdata["means"]
		hack_means_ingredients = hackdata["meaning"]
		
		hack_subjects[None] = hack_subjects["NullItemOk?"]
		hack_targets[None] = hack_targets["NullItemOk?"]
		hack_means[None] = hack_means["NullItemOk?"]
		hack_means_ingredients[None] = hack_means_ingredients["NullItemOk?"]
	
		if len(message["arguments"]) < 2 or message["arguments"][1] not in hack_subjects.keys():
			hack_key = None
			
		else:
			hack_key = message["arguments"][1]
			
		return [(choice(hack_subjects[hack_key]) + choice(hack_means[hack_key])).format(hmi=choice(hack_means_ingredients[hack_key]), target=choice(hack_targets[hack_key]))]
	
@easy_bot_command("move")
def wheels(message, raw):
	if not raw:
		return ["Wheelin' everywhere! Woohoo! This is so cool!", "Thanks for implementing my wheels! :D", "Ow!... didn't you implement bumpers yet?"]
		
@easy_bot_command("hacklist")
def hacking_list(message, raw):
	if not raw:
		hackdata = json.load(open("hackstrings.json"))
		
		hack_subjects = hackdata["subjects"]
		hack_subjects.__delitem__("NullItemOk?")
	
		return ["Hack subjects available: " + "; ".join(filter(lambda x: x != None, hack_subjects.keys()))]

@easy_bot_command("imsad")
def im_sad(message, raw):
	if raw:
		return
		
	return ["\x01ACTION hugs {}\x01".format(message["nickname"])]
	
@easy_bot_command(u"jeparlefran\u00e7ais".encode("utf-8"))
def french_sad(message, raw):
	if raw:
		return
		
	return [
		u"Le utiliqu\u00e9 le traducteur.... caham, sorry, I wish I could learn French. :(".encode("utf-8"),
		"Well, I could speak only Portuguese, since my programmer, but...",
		"\x01ACTION sits in a corner, frowning\x01"
	]
	
@easy_bot_command(u"jeteachfran\u00e7ais".encode("utf-8"))
def french_learning(message, raw):
	if raw:
		return
		
	return ["\x01ACTION hugs {}\x01".format(message["nickname"]), "Seriously?! Well, use ||teachfrench <word in English> <word in French>. It won't use conjugation, but it's the best I can do. :)"]