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
			},
      {
        villagerGiveItemsKey: ["wands:diamond_wand"],
        playerGiveNumKey: 64
			},
      { # tools
        villagerGiveItemsKey: [
          "chipped:botanist_workbench",
          "chipped:glassblower",
          "chipped:carpenters_table",
          "chipped:loom_table",
          "chipped:mason_table",
          "chipped:alchemy_bench",
          "chipped:tinkering_table",
          "moa_decor_cookery:barril",
          "moa_decor_cookery:barrica",
          "quark:trowel",
          "meadow:woodcutter",
          "meadow:wooden_cauldron"
				],
        playerGiveNumKey: 6
			},
      { # decorations
        villagerGiveItemsKey: [
          "beautify:hanging_pot",
          "vinery:storage_pot",
          "vinery:flower_box",
          "vinery:flower_pot",
          "vinery:wine_box",
          "candlelight:drawer",
          "candlelight:cabinet",
          "candlelight:sideboard",
          "candlelight:chair",
          "candlelight:sofa",
          "candlelight:table",
          "candlelight:lamp",
          "candlelight:side_table",
          "moa_decor_garden_:macetero_m",
          "meadow:wheelbarrow",
          "meadow:fire_log",
          "meadow:flower_pot_big",
          "meadow:wooden_flower_pot",
          "meadow:flower_box",
          "meadow:wooden_bucket"
				]
			}
		]
	},
  { # Sam
    nameKey: "Sam",
    textureKey: "eagle",
    tradesKey: [
      { # rare fish sells
        playerGiveItemsKey: [
          "aquaculture:catfish",
          "aquaculture:capitaine",
          "aquaculture:tuna",
          "aquaculture:arrau_turtle",
          "aquaculture:starshell_turtle"
				],
        villagerGiveNumKey: 20
			},
      { # sushi
        villagerGiveItemsKey: [
          "pamhc2foodextended:sushiitem",
          "aquaculture:sushi",
          "pamhc2foodextended:californiarollitem",
          "farmersdelight:salmon_roll",
          "farmersdelight:cod_roll",
          "farmersdelight:kelp_roll_slice",
          "aquaculturedelight:raw_fish_fillet_roll"
				]
			},
      {
				villagerGiveItemsKey: ['moa_decor_cookery:sushi'],
        playerGiveNumKey: 4
			},
      {
				villagerGiveItemsKey: ['farmersdelight:rice_roll_medley_block'],
        playerGiveNumKey: 6
			},
			{ villagerGiveItemsKey: ['aquaculture:algae'] },
      {
        villagerGiveItemsKey: ['aquaculture:lockbox'],
        playerGiveNumKey: 4
			},
      {
        villagerGiveItemsKey: ['aquaculture:treasure_chest'],
        playerGiveNumKey: 8
			},
      {
        villagerGiveItemsKey: ['minecraft:trident'],
        playerGiveNumKey: 6
			},
      {
        villagerGiveItemsKey: ['aquaculture:neptunium_ingot'],
        playerGiveNumKey: 64
			}
		]
	},
  { # Andre
		nameKey: "Andre",
    textureKey: "dog",
    tradesKey: [
      {
        villagerGiveItemsKey: [
          'minecraft:saddle',
          "minecraft:spyglass"
        ],
        playerGiveNumKey: 4
			},
      {
        villagerGiveItemsKey: [
          'farmingforblockheads:chicken_nest',
          'farmingforblockheads:feeding_trough'
        ],
        playerGiveNumKey: 2
			},
      {
        villagerGiveItemsKey: [
          'waystones:waystone',
          "waystones:sandy_waystone",
          "waystones:mossy_waystone",
          "waystones:warp_stone"
        ],
        playerGiveNumKey: 16
			},
      {
        villagerGiveItemsKey: ["mobcapturingtool:mob_capturing_tool"],
        playerGiveNumKey: 32
			},
      { villagerGiveItemsKey: ["naturescompass:naturescompass"] },
      {
        villagerGiveItemsKey: [
          "exoticbirds:bird_book",
          "exoticbirds:egg_identifier",
          "exoticbirds:egg_incubator",
          "exoticbirds:roost_box",
          "exoticbirds:pigeon_backpack",
        ],
        playerGiveNumKey: 4
			}
		]
	},
  { # Laly
		nameKey: "Laly",
    textureKey: "merekat",
    tradesKey: [
      { # Gem sells
        playerGiveItemsKey: [
          "gemsnjewels:dusk_emerald",
          "gemsnjewels:opal",
          "gemsnjewels:pale_diamond",
          "gemsnjewels:ruby",
          "gemsnjewels:sable_amethyst",
          "gemsnjewels:sapphire"
				],
        villagerGiveNumKey: 10
			},
      { villagerGiveItemsKey: ["minecraft:iron_ingot"] },
      {
        villagerGiveItemsKey: ["minecraft:netherite_scrap"],
        playerGiveNumKey: 64
			},
      {
        playerGiveItemsKey: [
          "minecraft:redstone",
          "minecraft:raw_copper",
          "create:raw_zinc"
        ],
        playerGiveNumKey: 64
			}
		]
	},
  { # Pamela
		nameKey: "Pamela",
    textureKey: "rabbit",
		tradesKey: [
      {
        villagerGiveItemsKey: ["minecraft:egg"],
        villagerGiveNumKey: 16
			},
      {
        villagerGiveItemsKey: ["bakery:yeast"],
        villagerGiveNumKey: 8
			},
      {
        villagerGiveItemsKey: ["minecraft:honey_bottle"],
        playerGiveNumKey: 2
			},
      { # containers
        villagerGiveItemsKey: [
          "bakery:jar",
          "vinery:wine_bottle",
          "bakery:tray"
        ],
        villagerGiveNumKey: 16
			},
      {
        villagerGiveItemsKey: [
          "farmingforblockheads:green_fertilizer",
          "farmingforblockheads:red_fertilizer",
          "farmingforblockheads:yellow_fertilizer"
				]
			}
		]
	},
	{ # Yukkie
    nameKey: "Yukkie",
    textureKey: "bat",
    tradesKey: [
      {
        playerGiveItemsKey: ["minecraft:enchanted_golden_apple"],
        villagerGiveNumKey: 64
			}, {
        playerGiveItemsKey: [
					"bakery:sweetberry_cupcake",
					"vinery:cherry_wine",
					"beachparty:sweetberries_cocktail",
					"beachparty:icecream_melon",
					"farmersdelight:glow_berry_custard",
          "farmersdelight:apple_pie",
					"delightful:salmonberry_ice_cream",
					"delightful:cantaloupe_popsicle"
				],
        villagerGiveNumKey: 2
			},
      { # Juices and Jellies
        playerGiveItemsKey: [
          "pamhc2foodextended:blackberryjuiceitem",
          "pamhc2foodextended:blueberryjuiceitem",
          "pamhc2foodextended:cactusfruitjuiceitem",
          "pamhc2foodextended:candleberryjuiceitem",
          "pamhc2foodextended:cranberryjuiceitem",
          "pamhc2foodextended:elderberryjuiceitem",
          "pamhc2foodextended:huckleberryjellyitem",
          "pamhc2foodextended:juniperberryjellyitem",
          "pamhc2foodextended:mulberryjellyitem",
          "pamhc2foodextended:raspberryjellyitem",
          "pamhc2foodextended:strawberryjellyitem",
          "pamhc2foodextended:cantaloupejellyitem"
				],
        playerGiveNumKey: 3
			},
      { # Smoothies
        playerGiveItemsKey: [
          "pamhc2foodextended:grapesmoothieitem",
          "pamhc2foodextended:greengrapesmoothieitem",
          "pamhc2foodextended:kiwismoothieitem",
          "pamhc2foodextended:pineapplesmoothieitem",
          "pamhc2foodextended:cherrysmoothieitem",
          "pamhc2foodextended:orangesmoothieitem"
				],
        playerGiveNumKey: 2
			},
      { # Pies and Jellied Toast
        playerGiveItemsKey: [
          "pamhc2foodextended:peachpieitem",
          "pamhc2foodextended:pearpieitem",
          "pamhc2foodextended:plumpieitem",
          "pamhc2foodextended:pawpawpieitem",
          "pamhc2foodextended:soursoppieitem",
          "pamhc2foodextended:apricotpieitem",
          "pamhc2foodextended:bananajellytoastitem",
          "pamhc2foodextended:datejellytoastitem",
          "pamhc2foodextended:dragonfruitjellytoastitem",
          "pamhc2foodextended:figjellytoastitem",
          "pamhc2foodextended:grapefruitjellytoastitem",
          "pamhc2foodextended:mangojellytoastitem"
				]
			},
      { # Jelly Sandwich
        playerGiveItemsKey: [
          "pamhc2foodextended:papayayogurtitem",
          "pamhc2foodextended:persimmonyogurtitem",
          "pamhc2foodextended:pomegranateyogurtitem",
          "pamhc2foodextended:starfruityogurtitem",
          "pamhc2foodextended:breadfruityogurtitem",
          "pamhc2foodextended:jackfruityogurtitem",
          "pamhc2foodextended:guavajellysandwichitem",
          "pamhc2foodextended:lycheejellysandwichitem",
          "pamhc2foodextended:passionfruitjellysandwichitem",
          "pamhc2foodextended:rambutanjellysandwichitem",
          "pamhc2foodextended:tamarindjellysandwichitem",
          "pamhc2foodextended:gooseberryjellysandwichitem",
          "pamhc2foodextended:durianjellysandwichitem",
          "pamhc2foodextended:lemonjellysandwichitem",
          "pamhc2foodextended:limejellysandwichitem",
				],
        villagerGiveNumKey: 2
			}
		]
	},
	{ # Jess
		nameKey: "Jess",
		textureKey: "beaver"
	},
  { # Bernina
    nameKey: "Bernina",
    textureKey: "bernina"
	},
  { # Elna
    nameKey: "Elna",
    textureKey: "elna"
	}
]