#Modules
import random
#Defined Factors (Factors have to be predefined, but turned off, if they are to work)
lazy = False
guilty = False
bad_liar = False
brave = False
coward = False
racist = False
indecisive = False
eureka = False
amnesia = False
broke = False
end = False
cautious = False
#################      KEY      ########################
# A group of octothorpres (#############) signifies the end of a main descision
# A comment saying (#END OF THIS PATH) signifies the end of a subdescision
# any code between two #FACTOR# marks, a factor may or may not have an effect depending of factors
# any code between two #interphase# marks is in the interphase between two main descisions and only comes into play for certain cenarios, not all

#Introduction of the game
print "\n\n"
print "------------------------------------"
print "The Bagel Project Interactive Game"
print "------------------------------------"
print "\n"
print "At any point, type HELP for help"
#HELP STUFF
#print "for multiple option questions, enter the number of the response you prefer"
#print "HINT: Choosing one of the options will make for a more interesting story"

print "\n\nWhat is your name?"
name = raw_input("> ")
print "Are you ready to begin %s?" % name
ready_begin = raw_input("> ").lower()
#This makes it so that if Ryan is playing, Alex is the overseer
if name.lower() == "ryan":
	overseer = "Alex"
else:
	overseer = "Ryan"

if ready_begin == "no":
	print "\nWell that's too bad!"
if ready_begin != "yes" and ready_begin != "no":
	print "\nI'll just assume that means yes."


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
		print "\nGood, idea.  Better to play it safe."
		cautious = True#END OF THIS PATH
	elif tryp_what_do == "3":
		print "\nThat's risky.  There is an explosion at the Transcriptic factory.  The police are searching for suspects.  Better lay low for know."
		guilty = True
		bad_liar = True#END OF THIS PATH
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
		indecisive = True
		print "You eventually head back to the lab"#END OF THIS PATH

elif pass_time == "3":
	print "\nYou take a stroll through the lab.  Suddenly, you come to a realization!  It's so simple!  How to perfectly engineer an enzyme to do whatever you want!  What do you do?"
	eureka = True
	print "1. Do a happy dance!"
	print '2. Shout "Eureka!"'
	print "3. Make it rain with pre-cut tube seals"
	print "4. All of the above"
	eureka_what_do = raw_input("> ")

	if eureka_what_do == "1" or eureka_what_do == "4":
		print "\nWhile doing your happy dance, you proceed to knock over a bottle of TB which falls on your head, knocking you unconscious."
		prob_amnesia = random.uniform(1, 10)
		if prob_amnesia >= 5:
			print "You wake up quickly.  Thank god you remember your eureka moment!  Whew, that was a close one"
		else:
			eureka = False
			amnesia = True#END OF PATH
	elif eureka_what_do == "2":
		print "\nThe iGEM team tells you to shut up but you dont care!  You have just solved all of their problems for them!  I'm sure they'll be thrilled to find out that all of their hard work has been for nothing."
		#END OF PATH
	elif eureka_what_do == "3":
		print "\nYou start making it rain.  Unfortunately, you faint at the sight of blood and the tube seals are giving you paper cuts."
		print "You pass out..."
		if prob_amnesia >= 5:
			print "You wake up quickly.  Thank god you remember your eureka moment!  Whew, that was a close one"
		else:
			eureka = False
			amnesia = True#END OF PATH
	else:
		print "You ovbiously don't seem very excited.  I guess you dont need to know the secret to enzyme engineering"
		print "\nForgetting......"
		eureka = False
elif pass_time == "4":
	print "\nGood choice"
	print "." * 10#END OF PATH

else:
	print "\nI guess that's one way to pass the time...."

#############

#Interphase#
if pass_time == "2":
	print "\nOn your way back to the lab, a mugger holds you at gunpoint."
	if brave == True:
		print "You bravely punch the gun out of his hand and knock him out cold.  Then you call the cops, steal HIS money, and continue making your way back to the lab."
	elif coward == True:
		print '"Don\'t hurt me!" you cry.  "Just take my money and go!"  The mugger takes your money and runs.  You dust yourself off, and continue making your way back to the lab.'
		broke = True
	elif racist == True:
		print '"You can\'t mug me!" you say.  "You\'re just a substrate!"'
		print "The mugger, annoyed with your prejudice, mugs you anyway, and stabs you for good measure."
		print 'With your last dying breath, you scream "PRODUCT POWER!"'
		end = True
	elif indecisive == True:
		print "While you're trying to figure out what to do, the mugger takes all your money."
		broke == True
#Interphase#

#if guilty == True:
	#Cops come in looking for culprit by interrogating
	#25% chance they find out its you
	#75% chance if badliar is True
#FACTOR#


#Third main descision: Foldit Meeting, lab mates arrive
#FACTOR#
if amnesia == True:
	print '\n"Hello?  HELLO?  %s, ARE YOU AWAKE?"' % name.capitalize()
	print "You slowly start to get up..."
	print "Your head hurts"
	print "What happened?"
	print "You feel like you forgot something..."
	print '\n"Are you okay?" asks %s.  "It looks like you passed out."' % overseer
	if eureka_what_do == "1" or eureka_what_do == "4":
		print '"Yeah, I\'m fine" you say.'
		print '"Well it looks like you spilled TB all over the place." he says.'
		print '"After you clean this up, come over to the intern room.  Were having a meeting."'
	if eureka_what_do == "3":
		print "You must have hit your head on a table or something"
		print '"Yeah, I\'m fine" you say.'
		print '"That\'s good, come over to the intern room.  Were having a meeting."'
#FACTOR#
print "\nAll the interns start filing in."
print '"So there\'s some interesting news." %s says.' % overseer
print '"This morning, there was an explosion at the Transcriptic factory.  Apparently, someone tried to order a mutant that was half tryptophan, and the energy level was so ridiculously high, that the transcriptic computers exploded"  Continues %s.' % overseer
print '"Thankfully, no one was hurt although the people at Transcriptic are upset.  They plan to press charges against anyone who caused this catastrophe"'
if guilty == True:
	print "\nYou start to sweat a little..."
print '\n"They have traced the order from this lab"'
if guilty == True:
	print "\nYou start to sweat a lot..."
	print '"%s, are you okay?" asks %s' % (name, overseer)







#ENDING
if end == True:
	pay_again = raw_input("\n\nWould you like to play again?\n> ").lower()
	#if play_again == "yes":
		#Figure out how the fuck to start over
