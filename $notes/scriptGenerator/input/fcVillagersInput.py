from src import const

nameKey = 'nameKey'
textureKey = 'textureKey'

tradesKey = 'tradesKey'
villagerGiveItemsKey = 'villagerGiveItemsKey'
villagerGiveNumKey = 'villagerGiveNumKey'
playerGiveItemKey = 'playerGiveItemKey'
playerGiveNumKey = 'playerGiveNumKey'

villagers = [
	{ # Ren
		nameKey: "Ren",
		textureKey: "woodpecker",
		tradesKey: [
			{
				villagerGiveItemsKey: ["framedblocks:framed_cube"],
				villagerGiveNumKey: 64,
				playerGiveItemKey: const.priceItem
			}
		]
	},
	{ # Jess
		nameKey: "Jess",
		textureKey: "beaver"
	}
]