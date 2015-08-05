#################      KEY      ########################
# A group of octothorpres (#############) signifies the end of a main descision
# A comment saying (#END OF THIS PATH) signifies the end of a subdescision
# any code between two #FACTOR# marks, a factor may or may not have an effect

#Introduction of the game
print "-----------------------------------------------------"
print "The Bagel Project Interactive Game"
print "-----------------------------------------------------"
print "for multiple option questions, enter the number of the response you prefer"
print "HINT: Choosing one of the options will make for a more interesting story"



#First Main Descision: Whether or not to go to lab
print "\n\nIt's time to wake up!!!  Are you planning on going to lab today?"
lab_today = raw_input("> ").lower()

if lab_today == "yes":
	print "\nThen lets get ready!"
	print "\n"
	print "." * 10#END OF THIS PATH
elif lab_today == "no":
	print "\nYes you are.  It's Day 1.  Those E. Coli aren't gonna transform themselves."
	print "\n"
	print "." * 10
	lazy = True#END OF THIS PATH
else:
	print "\nThat's a dumb answer.  I'll just assume you said yes.  "
	print "\n"
	print "." * 10#END OF THIS PATH
#############



#Second Main Descision: What to do before the others get there
print "\nYou get to lab, and darn! You're early.  Nobody's there yet.  What do you do to pass the time?"
print "1. Work on Foldit"
print "2. Leave and come back later"
print "3. Check out the lab"
print "4. Watch youtube videos of cats."
pass_time = raw_input("> ")

if pass_time == "1":
	print "\nGood for you."
	print "While you're working on Foldit, you accidentally mutate half the enzyme to Tryptophan.  High energy levels are known to cause explosions.  The energy level is so astronaomically high, that to even consider ordering it would be an abomination.  What do you do?"
	print "1. Order it"
	print "2. Undo the mutation"
	print "3. Order it but blame it on the YSP kids"
	tryp_what_do = raw_input("> ")

	if tryp_what_do == "1":
		print "\nThere is an explosion at the Transcriptic factory.  The police are searching for suspects.  Better lay low for now."
		guilty = True#END OF THIS PATH
	elif tryp_what_do == "2":
		print "\nGood, idea.  Better to play it safe."#END OF THIS PATH
	elif tryp_what_do == "3":
		print "\nThat's risky.  There is an explosion at the Transcriptic factory.  The police are searching for suspects.  Better lay low for know."
		guilty = True
		blame = True#END OF THIS PATH
	else:
		print "\nSure, I guess, that's another viable option"#END OF THIS PATH

elif pass_time == "2":
	print "\nWhere do you go?"
	where_go = raw_input("> ")

	print "\nWhile you're at %s, you see an innocent 4-nitrophenyl B-d-glucopyranoside being attacked by a Beta-Glucosidase.  What do you do?" % where_go
	print "1. Intervene and take the enzymes IPTG, rendering it innefective."
	print "2. Keep to yourself"
	print "3. Cheer on the Beta-Glucosidase, because you are racist against substrate."
	attack_what_do = raw_input("> ")

	if attack_what_do == "1":
		print "\nYou successfully stopped the enzyme"
		print '"Why don\'t you pick on someone your own chemical composition" you say.'
		print "You make your way back to the lab after making sure the substrate was okay and in good hands.  Another job well done."
		brave = True#END OF THIS PATH
	elif attack_what_do == "2":
		print '"\nWe don\'t allow yer\' kind here.  This here %s is fer products only" says the enzyme.  "Why don\'t you head on over to the substrate bar, before I give you a reason to stay."' % where_go
		print "You just sit there and watch it happen.  You feel bad, but feel like there's nothing you can do about it."
		print "\nYou eventually make your way back to the lab"
		coward = True#END OF THIS PATH
	elif attack_what_do == "3":
		print "\nHow dare you.  Just because someone isn't product, doesn't mean they're any less of a chemical.  People like you make me sick."
		print "\nYou make your way back to the lab"
		racist = True#END OF THIS PATH
	else:
		print "Maybe thats a better idea"
		print "You eventually head back to the lab"#END OF THIS PATH

elif pass_time == "3":
	print ""

elif pass_time == "4":
	print ""

else:
	print ""

#############
