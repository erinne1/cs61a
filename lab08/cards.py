from classes import *

standard_cards = [
	AICard('Yao Ming', 1400, 2000),
	AICard('Jia Jun, Bringer of Hearing Loss', 2100, 1200),
	AICard('Anthony', 1500, 1600),
	AICard('Shreyas, Fruit Flinger', 1000, 2200),
	AICard('Arnold, Skips Leg Day', 1600, 1500),
	AICard('Ryan, Bolter of Birds', 1600, 1800),
	AICard('Pranav, The Chosen Chef', 1300, 2100),
	AICard('James, Handler of Flames', 1900, 1400),
	AICard('Andy, Handy Dandy Cotton Candy', 2100, 1000),
	AICard('Daniel, The Korean Waffle', 2100, 1300),
	AICard('Sarah, Eternal Sleeper', 1500, 1900),
	AICard('Colleen the Conqueror', 1200, 1500),
	TutorCard('Hans, Compiler of Chaos', 1100, 2200),
	TutorCard('Matthew, Midnight Magician', 1600, 1300),
	TutorCard('Aldrin, Angelic Almond', 1700, 1700),
	TutorCard('Thomas the Tank (Engine)', 2000, 1100),
	TutorCard('λaryn, λord of λambdas', 1100, 2000),
	TutorCard('Richik, the Royal Ragnarok', 1700, 1600),
	TutorCard('Hailee, SoDoI Addict', 1600, 1700),
	TACard('Rachel, Master of Naps', 1200, 2200),
	TACard('Tyler, Lam(bda)', 1600, 1800),
	TACard('Cyrus, The Asleep', 1500, 1600),
	TACard('Christina, Cheese Chomper', 1500, 1600),
	TACard('Bryce, Fuzzy Fire Flinger', 2100, 1100),
	TACard('Anto, Spinner', 2300, 1000),
	InstructorCard('Jordan, The Just Ok', 6650, 6650),
	InstructorCard('Tim, Twin Terror of Twos', 7100, 6200),
	InstructorCard('Noor, Chaotic Wanderer', 0, 10000)
]

standard_deck = Deck(standard_cards)
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()
