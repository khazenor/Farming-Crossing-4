from list import collectionQuests as cqList

newCollection = [
	'simplehats:acornhat',
	'simplehats:aegishat',
	'simplehats:alienphil',
	'simplehats:amalgalichhat',
	'simplehats:angrymask',
	'simplehats:antlers',
	'simplehats:apple',
	'simplehats:artsy',
	'simplehats:artsy_doll',
	'simplehats:azumanga_hat',
	'simplehats:babydolphin',
	'simplehats:babyturtle',
	'simplehats:bandana',
	'simplehats:bandanargb',
	'simplehats:baseballeaster',
	'simplehats:baseballhat',
	'simplehats:baseballhatfestive',
	'simplehats:baseballhatjuly',
	'simplehats:baseballhatrgb',
	'simplehats:batwinghat',
	'simplehats:beanie',
	'simplehats:beanieeaster',
	'simplehats:beaniefestive',
	'simplehats:beaniejuly',
	'simplehats:beaniergb',
	'simplehats:beaniespooky',
	'simplehats:beehat',
	'simplehats:beret_ribbon',
	'simplehats:bicorne',
	'simplehats:bigbrain',
	'simplehats:bigcrown',
	'simplehats:bigeyes',
	'simplehats:bigribbon',
	'simplehats:bigstevehead',
	'simplehats:bluefireeye',
	'simplehats:bowler',
	'simplehats:breadhat',
	'simplehats:brownbrick',
	'simplehats:bucket',
	'simplehats:bunnyhat',
	'simplehats:burgerhat',
	'simplehats:burning_m_bison',
	'simplehats:caddycap',
	'simplehats:camera',
	'simplehats:camerabeard',
	'simplehats:candleonhead',
	'simplehats:candycane',
	'simplehats:carrotonstick',
	'simplehats:cartoonegg',
	'simplehats:chalk_stick',
	'simplehats:cheeseslice',
	'simplehats:chefshat',
	'simplehats:chi_ears',
	'simplehats:chickenhead',
	'simplehats:chickenonhead',
	'simplehats:christmascakehat',
	'simplehats:christmastree',
	'simplehats:circular_glasses',
	'simplehats:clockface',
	'simplehats:cowboy',
	'simplehats:cowboyrgb',
	'simplehats:crabonhead',
	'simplehats:crown',
	'simplehats:cucumbereyemask',
	'simplehats:cuphead',
	'simplehats:cyclopseye',
	'simplehats:dairyqueen',
	'simplehats:dangereqsue',
	'simplehats:dangeresquejuly',
	'simplehats:dejiko',
	'simplehats:demoneyes',
	'simplehats:demonhorns',
	'simplehats:digger',
	'simplehats:dimmahat',
	'simplehats:discoball',
	'simplehats:disguise',
	'simplehats:doctorhat',
	'simplehats:dorkglassesandteeth',
	'simplehats:doubletake',
	'simplehats:dragonhead',
	'simplehats:dragonskull',
	'simplehats:dragonskullender',
	'simplehats:drinkinhat',
	'simplehats:dumhat',
	'simplehats:dwarfminerbeard',
	'simplehats:easterhead',
	'simplehats:egghead',
	'simplehats:eggonhead',
	'simplehats:elfhat',
	'simplehats:explorerhat',
	'simplehats:eyepatch',
	'simplehats:fakeblight',
	'simplehats:fakefire',
	'simplehats:farmerbrim',
	'simplehats:festiveantlers',
	'simplehats:festiveribbon',
	'simplehats:fez',
	'simplehats:finnhood',
	'simplehats:fireworks',
	'simplehats:fishing_hat',
	'simplehats:fishonhead',
	'simplehats:flagjuly',
	'simplehats:flies',
	'simplehats:floatinghearts',
	'simplehats:floatingstar',
	'simplehats:flowercrown',
	'simplehats:floweronhead',
	'simplehats:foxhat',
	'simplehats:fro',
	'simplehats:frozenhead',
	'simplehats:fullironhelm',
	'simplehats:ghostmask',
	'simplehats:goggles',
	'simplehats:grandmadisguise',
	'simplehats:greenbirb',
	'simplehats:grinchhat',
	'simplehats:halo',
	'simplehats:hatbag_common',
	'simplehats:hatbag_easter',
	'simplehats:hatbag_epic',
	'simplehats:hatbag_festive',
	'simplehats:hatbag_halloween',
	'simplehats:hatbag_rare',
	'simplehats:hatbag_summer',
	'simplehats:hatbag_uncommon',
	'simplehats:hatdisplay',
	'simplehats:haticon',
	'simplehats:hatscraps_common',
	'simplehats:hatscraps_easter',
	'simplehats:hatscraps_festive',
	'simplehats:hatscraps_halloween',
	'simplehats:hatscraps_rare',
	'simplehats:hatscraps_summer',
	'simplehats:hatscraps_uncommon',
	'simplehats:headbolts',
	'simplehats:headphonesblue',
	'simplehats:headshot',
	'simplehats:hockeymask',
	'simplehats:holyhead',
	'simplehats:horsemask',
	'simplehats:hosthat',
	'simplehats:icedragonskull',
	'simplehats:jackohat',
	'simplehats:jesterhat',
	'simplehats:julydouble',
	'simplehats:kirbymouthful',
	'simplehats:largehorns',
	'simplehats:lightning_eyes',
	'simplehats:lilbow',
	'simplehats:longfoxears',
	'simplehats:madscientist',
	'simplehats:magikarp',
	'simplehats:megamanhat',
	'simplehats:milady_doll',
	'simplehats:mistletoe',
	'simplehats:mohawk',
	'simplehats:monkeyking',
	'simplehats:monocle',
	'simplehats:moreeyes',
	'simplehats:murdered',
	'simplehats:nekoears',
	'simplehats:nyan_doll',
	'simplehats:orange_hat',
	'simplehats:palmtree',
	'simplehats:paperbag',
	'simplehats:partyhat',
	'simplehats:paypay',
	'simplehats:penguinbaby',
	'simplehats:penguinhat',
	'simplehats:peppino',
	'simplehats:pighead',
	'simplehats:pinhead',
	'simplehats:plaguedoctor',
	'simplehats:pog',
	'simplehats:pohatoe',
	'simplehats:policebucket',
	'simplehats:policesiren',
	'simplehats:pom_moog',
	'simplehats:poofballhat',
	'simplehats:poofballrgb',
	'simplehats:popehat',
	'simplehats:potionhead',
	'simplehats:presentsstack',
	'simplehats:propelhat',
	'simplehats:puchiko',
	'simplehats:questbook',
	'simplehats:rabbitears',
	'simplehats:rabbitonhead',
	'simplehats:rabi_en_rose',
	'simplehats:rainboworbiters',
	'simplehats:raincloud',
	'simplehats:ranahat',
	'simplehats:redeyes',
	'simplehats:rednose',
	'simplehats:redstache',
	'simplehats:rgbbigribbon',
	'simplehats:rgbbowler',
	'simplehats:rgbdragonskull',
	'simplehats:rgbdrinkinhat',
	'simplehats:rgbeasterhead',
	'simplehats:rgbfullhelm',
	'simplehats:rgbpartyhat',
	'simplehats:rgbsmallbowler',
	'simplehats:rgbsunglasses',
	'simplehats:rgbtoptophathat',
	'simplehats:rgbushanka',
	'simplehats:rock',
	'simplehats:rubbernipple',
	'simplehats:sandcastle',
	'simplehats:santaclaus',
	'simplehats:sausage',
	'simplehats:scouter',
	'simplehats:seaweedhat',
	'simplehats:shakehat',
	'simplehats:sheep',
	'simplehats:shrekears',
	'simplehats:shroomcap',
	'simplehats:simsgem',
	'simplehats:sleepeyemask',
	'simplehats:smokingpipe',
	'simplehats:snowmanbaby',
	'simplehats:sombrero',
	'simplehats:sonichood',
	'simplehats:spadesoldier',
	'simplehats:special',
	'simplehats:spiderweb',
	'simplehats:sport_sunglasses',
	'simplehats:springer',
	'simplehats:sprout',
	'simplehats:spyzombie',
	'simplehats:stackofeggs',
	'simplehats:strawberry_hat',
	'simplehats:stress',
	'simplehats:summerhat',
	'simplehats:sunglasses',
	'simplehats:sunglassesbig',
	'simplehats:supersandhat',
	'simplehats:swimmer',
	'simplehats:teddy_bear',
	'simplehats:the_noise',
	'simplehats:tinkerhat',
	'simplehats:topcathat',
	'simplehats:tophat',
	'simplehats:toptophathat',
	'simplehats:toy_story_alien',
	'simplehats:triangleshades',
	'simplehats:tricorne',
	'simplehats:tvhead',
	'simplehats:twilight_doll',
	'simplehats:unicornhorn',
	'simplehats:ushanka',
	'simplehats:vikinghatbeard',
	'simplehats:villagernose',
	'simplehats:winghat',
	'simplehats:worms_mine',
	'simplehats:zigzagwitchhat'
]
def findMissingCollection():
	currentCollection = cqList.allHats
	missingCollection = []
	for collectionItem in newCollection:
		if collectionItem not in currentCollection:
			missingCollection.append(collectionItem)
	print(missingCollection)

if __name__ == "__main__":
	findMissingCollection()
