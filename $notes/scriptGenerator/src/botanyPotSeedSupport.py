from lib import botanyBots

seedKey = 'seed'
cropKey = 'crop'
blockKey = 'block'

seedSupports = [
	{
		seedKey: 'candlelight:lettuce_seeds',
		cropKey: 'candlelight:lettuce',
		blockKey: 'candlelight:lettuce_crop'
	},
	{
		seedKey: 'bakery:oat_seeds',
		cropKey: 'bakery:oat_crop',
		blockKey: 'bakery:oat'
	},
	{
		seedKey: 'bakery:strawberry_seeds',
		cropKey: 'bakery:strawberry',
		blockKey: 'bakery:strawberry_crop'
	},
	{
		seedKey: 'candlelight:tomato_seeds',
		cropKey: 'candlelight:tomato',
		blockKey: 'candlelight:tomato_crop'
	},
	{
		seedKey: 'delightful:cantaloupe_seeds',
		cropKey: 'delightful:cantaloupe',
		blockKey: 'delightful:cantaloupe'
	},
	{
		seedKey: 'nethervinery:crimson_grape_seeds',
		cropKey: 'nethervinery:crimson_grape',
		blockKey: 'nethervinery:crimson_grape_bush'
	},
	{
		seedKey: 'nethervinery:warped_grape_seeds',
		cropKey: 'nethervinery:warped_grape',
		blockKey: 'nethervinery:warped_grape_bush'
	},
	{
		seedKey: 'vinery:jungle_grape_seeds_red',
		cropKey: 'vinery:jungle_grapes_red',
		blockKey: 'vinery:jungle_grape_bush_red'
	},
	{
		seedKey: 'vinery:jungle_grape_seeds_white',
		cropKey: 'vinery:jungle_grapes_white',
		blockKey: 'vinery:jungle_grape_bush_white'
	},
	{
		seedKey: 'vinery:red_grape_seeds',
		cropKey: 'vinery:red_grape',
		blockKey: 'vinery:red_grape_bush'
	},
	{
		seedKey: 'vinery:savanna_grape_seeds_red',
		cropKey: 'vinery:savanna_grapes_red',
		blockKey: 'vinery:savanna_grape_bush_red'
	},
	{
		seedKey: 'vinery:savanna_grape_seeds_white',
		cropKey: 'vinery:savanna_grapes_white',
		blockKey: 'vinery:savanna_grape_bush_white'
	},
	{
		seedKey: 'vinery:taiga_grape_seeds_red',
		cropKey: 'vinery:taiga_grapes_red',
		blockKey: 'vinery:taiga_grape_bush_red'
	},
	{
		seedKey: 'vinery:taiga_grape_seeds_white',
		cropKey: 'vinery:taiga_grapes_white',
		blockKey: 'vinery:taiga_grape_bush_white'
	},
	{
		seedKey: 'vinery:white_grape_seeds',
		cropKey: 'vinery:white_grape',
		blockKey: 'vinery:white_grape_bush'
	}
]


def genBotanySeedSupport():
	for seedSupport in seedSupports:
		botanyBots.writeSeedJson(
			seedSupport[seedKey],
			seedSupport[cropKey],
			seedSupport[blockKey]
		)
