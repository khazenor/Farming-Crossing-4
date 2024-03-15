from src import const

nameKey = 'nameKey'
textureKey = 'textureKey'

tradesKey = 'tradesKey'
villagerGiveItemsKey = 'villagerGiveItemsKey'
villagerGiveNumKey = 'villagerGiveNumKey'
playerGiveItemsKey = 'playerGiveItemsKey'
playerGiveNumKey = 'playerGiveNumKey'

villagers = [
	{ # Ren
		nameKey: "Ren",
		textureKey: "woodpecker",
		tradesKey: [
			{
				villagerGiveItemsKey: ["framedblocks:framed_cube"],
				villagerGiveNumKey: 64
			}
		]
	},
  { # Sam
    nameKey: "Sam",
    textureKey: "eagle",
    tradesKey: [
      {
        playerGiveItemsKey: [
          "aquaculture:catfish",
          "aquaculture:capitaine",
          "aquaculture:tuna",
          "aquaculture:arrau_turtle",
          "aquaculture:starshell_turtle"
				],
        villagerGiveNumKey: 20
			}
		]
	},
	{ # Jess
		nameKey: "Jess",
		textureKey: "beaver"
	}
]