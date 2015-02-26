#from pattern.web import *
#w = Wikipedia()
#jupitor = w.search('Jupiter')
#txt = jupitor.string
#print txt

def replacer(textr):
	'''takes a string about jupiter and replaces selected nouns with goofy space nouns'''
	textr = textr.replace('jupiter', 'zorgx')
	textr = textr.replace('mars', 'fafnar')
	textr = textr.replace('ganymede', 'elts')
	textr = textr.replace('galileo galilei', 'mantar shreegnat')
	textr = textr.replace('galilean', 'shreegatian')
	textr = textr.replace('neptune', 'zimp')
	textr = textr.replace('saturn', 'kreej')
	textr = textr.replace('uranus', 'vlimped')
	textr = textr.replace('romans', 'slaughtering rat people')
	textr = textr.replace('great red spot', 'enormous terrifying eyeball')
	textr = textr.replace('earth', 'minxk')
	textr = textr.replace('solar', 'zhrdekite')
	textr = textr.replace('venus', 'zslik')
	textr = textr.replace('the moon', 'blep')
	textr = textr.replace('the sun', 'zhrdek')
	textr = textr.replace('the sun\'s', 'zhrdek\'s')
	textr = textr.replace('hydro', 'dagstan')
	textr = textr.replace('helium', 'roemium')
	textr = textr.replace('km', 'zlemoks')
	textr = textr.replace('g/cm3', 'somps')
	textr = textr.replace('terrestrial', 'minxkian')
	textr = textr.replace('methane', 'ulat')
	textr = textr.replace('water', 'blisk')
	textr = textr.replace('ammonia', 'borbonia')
	textr = textr.replace('silicon-based', 'tantaneous')
	textr = textr.replace('carbon', 'yron')
	textr = textr.replace('ethane', 'fojrane')
	textr = textr.replace('sulf', 'hlig')
	textr = textr.replace('neon', 'zoon')
	textr = textr.replace('oxygen', 'moryligen')
	textr = textr.replace('phosphine', 'boitine')
	textr = textr.replace('benzene', 'zorbene')

	return textr


def simpleMarkov(textr): #later add prefix order as another parameter
	'''creates a Markov dictionary from the input textr and returns a Markov-generated sentence'''
	import random
	from random import randint
	textr = textr.lower()
	textr = replacer(textr)		#fictionalize proper names!

	thing0 = textr.split()
	thing = []
	for i in range(len(thing0)):	#create new word list without punctuation
		elem = thing0[i]
		if elem[-1] == '.':
			elem = elem[0:-1]
			thing.append(elem)		
		else:
			thing.append(elem)


	'''creates a dictionary'''
	MDict = {}
	for i in range(len(thing)-2):
		wordPair = (thing[i], thing[i + 1])	
		newKey = ' '.join(wordPair)		#convert word pair to string 
		if newKey in MDict.keys():
			nextWord = MDict[newKey]	#current value for newKey
			nextWord.append(thing[i + 2])	#add new possible next word
			MDict[newKey] = nextWord		#list of possibles = new value
		else:
			MDict[newKey] = [thing[i+2]]	#assign possible next word

	besh = (thing[-2], thing[-1])
	MDict[' '.join(besh)] = ''			#last key codes for nothing

	'''finds a random starting word and generates a chain'''
	firstindx = randint(0, len(thing) - 2)	#generate random first 2 words
	next = ' '.join((thing[firstindx], thing[firstindx + 1]))
	output = next 						#first 2 words begin output string
	for i in range(30):
		if next == thing[-1] + ' ':
			break				#if it doesn't code for anything stop the loop
		if type(MDict[next]) is list:
			var = MDict[next]
			randomNum = randint(0, len(MDict[next])) - 1 
			newSecondWord = var[randomNum] #one word from list of possibles
			output += " " + newSecondWord
		else:
			newSecondWord = MDict[next]
			output += " " + newSecondWord
		
		temp = next.split()					#split to use only 2nd word
		next = temp[1] + ' ' + newSecondWord	#next key is next 2 words in text



	return output

tnxt = 'Jupiter is the fifth planet from the Sun and it is the largest planet in the Solar System. It is a giant planet with a mass one-thousandth of that of the Sun, but is two and a half times that of all the other planets in the Solar System combined. Jupiter is a gas giant, along with Saturn. Uranus and Neptune are ice giants. Jupiter was known to astronomers of ancient times. The Romans named it after their god Jupiter. When viewed from Earth, Jupiter can reach an apparent magnitude of -2.94, bright enough to cast shadows, and making it on average the third-brightest object in the night sky after the Moon and Venus. Mars can briefly match Jupiter\'s brightness at certain points in its orbit. Jupiter is primarily composed of hydrogen with a quarter of its mass being helium, although helium only comprises about a tenth of the number of molecules. It may also have a rocky core of heavier elements, but like the other giant planets, Jupiter lacks a well-defined solid surface. Because of its rapid rotation, the planet\'s shape is that of an oblate spheroid it possesses a slight but noticeable bulge around the equator. The outer atmosphere is visibly segregated into several bands at different latitudes, resulting in turbulence and storms along their interacting boundaries. A prominent result is the Great Red Spot, a giant storm that is known to have existed since at least the 17th century when it was first seen by telescope. Surrounding Jupiter is a faint planetary ring system and a powerful magnetosphere. Jupiter has at least 67 moons, including the four large Galilean moons discovered by Galileo Galilei in 1610. Ganymede, the largest of these, has a diameter greater than that of the planet Mercury. Jupiter is composed primarily of gaseous and liquid matter. It is the largest of the four giant planets in the Solar System and hence its largest planet. It has a diameter of 142,984 km at its equator. The density of Jupiter, 1.326 g/cm3, is the second highest of the giant planets, but lower than those of any of the four terrestrial planets. Jupiter\'s upper atmosphere is composed of about 88-92% hydrogen and 8-12% helium by percent volume of gas molecules. Because a helium atom has about four times as much mass as a hydrogen atom, the composition changes when described as the proportion of mass contributed by different atoms. Thus, the atmosphere is approximately 75% hydrogen and 24% helium by mass, with the remaining one percent of the mass consisting of other elements. The interior contains denser materials, such that the distribution is roughly 71% hydrogen, 24% helium and 5% other elements by mass. The atmosphere contains trace amounts of methane, water vapor, ammonia, and silicon-based compounds. There are also traces of carbon, ethane, hydrogen sulfide, neon, oxygen, phosphine, and sulfur. The outermost layer of the atmosphere contains crystals of frozen ammonia. Through infrared and ultraviolet measurements, trace amounts of benzene and other hydrocarbons have also been found. The atmospheric proportions of hydrogen and helium are close to the theoretical composition of the primordial solar nebula. Neon in the upper atmosphere only consists of 20 parts per million by mass, which is about a tenth as abundant as in the Sun. Helium is also depleted, to about 80% of the Sun\'s helium composition. This depletion is a result of precipitation of these elements into the interior of the planet. Abundances of heavier inert gases in Jupiter\'s atmosphere are about two to three times that of the Sun. Jupiter\'s mass is 2.5 times that of all the other planets in the Solar System combined. This is so massive that its barycenter with the Sun lies above the Sun\'s surface at 1.068 solar radii from the Sun\'s center. Although this planet dwarfs the Earth with a diameter 11 times as great, it is considerably less dense. Jupiter\'s volume is that of about 1,321 Earths, yet the planet is only 318 times as massive. Jupiter\'s radius is about 1/10 the radius of the Sun, and its mass is 0.001 times the mass of the Sun, so the density of the two bodies is similar. A Jupiter mass is often used as a unit to describe masses of other objects, particularly extrasolar planets and brown dwarfs. So for example, the extrasolar planet HD 209458 b has a mass of 0.69 MJ, while Kappa Andromedae b has a mass of 12.8 MJ.'
print simpleMarkov(tnxt)