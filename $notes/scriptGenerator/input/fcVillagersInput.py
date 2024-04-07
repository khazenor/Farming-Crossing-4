from src import const

nameKey = 'nameKey'
textureKey = 'textureKey'

tradesKey = 'tradesKey'
springTradesKey = 'spring'
summerTradesKey = 'summer'
fallTradesKey = 'fall'
winterTradesKey = 'winter'
villagerItems = 'villagerItems'
villagerNum = 'villagerNum'
playerItems = 'playerItems'
playerNum = 'playerNum'

villagers = [
	{ # Ren
		nameKey: "Ren",
		textureKey: "woodpecker",
		tradesKey: [
			{
				villagerItems: ["framedblocks:framed_cube"],
				villagerNum: 64
			},
      {
        villagerItems: ["wands:diamond_wand", "constructionwand:diamond_wand"],
        playerNum: 64
			},
      { # tools
        villagerItems: [
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
        playerNum: 6
			},
      { # decorations
        villagerItems: [
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
		],
    springTradesKey: [
      {
        villagerItems: [
          'luphieclutteredmod:luphie_general_store_cabinet',
          'luphieclutteredmod:luphie_mermaid_dresser',
          'luphieclutteredmod:luphie_bunny_book_ends',
          'luphieclutteredmod:luphie_pastel_chair',
          'luphieclutteredmod:luphie_pastel_table',
          'luphieclutteredmod:luphie_rose_endtable',
          'luphieclutteredmod:luphie_pastel_block_bookshelf',
          'luphieclutteredmod:luphie_hoppin_park_lantern',
          'luphieclutteredmod:luphie_pastel_traditional_table',
          'luphieclutteredmod:luphie_pastel_wardrobe'
        ],
        playerNum: 6
      }
    ],
    summerTradesKey: [
      {
        villagerItems: [
          'luphieclutteredmod:luphie_lunar_observatory_small_table',
          'luphieclutteredmod:luphie_nightstand',
          'luphieclutteredmod:luphie_greener_nightstand',
          'luphieclutteredmod:luphie_cluttered_green_desk',
          'luphieclutteredmod:luphie_green_desk',
          'luphieclutteredmod:luphie_imperial_table',
          'luphieclutteredmod:luphie_wedding_arch',
          'luphieclutteredmod:luphie_retro_cafe_shelf',
          'luphieclutteredmod:luphie_retro_cafe_shelf_stained_glass',
          'luphieclutteredmod:luphie_rovers_stool',
          'luphieclutteredmod:luphie_apple_chair'
        ],
        playerNum: 6
      }
    ],
    fallTradesKey: [
      {
        villagerItems: [
          'luphieclutteredmod:luphie_lunar_observatory_table',
          'luphieclutteredmod:luphie_steampunk_globe',
          'luphieclutteredmod:luphie_unliving_chair',
          'luphieclutteredmod:luphie_brown_desk',
          'luphieclutteredmod:luphie_button_stool',
          'luphieclutteredmod:blue_birdhouse',
          'luphieclutteredmod:red_birdhouse',
          'luphieclutteredmod:unpainted_birdhouse'
        ],
        playerNum: 6
      }
    ],
    winterTradesKey: [
      {
        villagerItems: [
          'luphieclutteredmod:luphie_card_index',
          'luphieclutteredmod:luphie_china_cabinet',
          'luphieclutteredmod:luphie_gothic_rose_endtable',
          'luphieclutteredmod:luphie_table_with_cloth',
          'luphieclutteredmod:luphie_vial_stand',
          'luphieclutteredmod:luphie_cluttered_desk',
          'luphieclutteredmod:luphie_havana_cabinet',
          'luphieclutteredmod:luphie_cluttered_havana_cabinet'
        ],
        playerNum: 6
      }
    ]
	},
  { # Sam
    nameKey: "Sam",
    textureKey: "eagle",
    tradesKey: [
      { # sushi
        villagerItems: [
          "pamhc2foodextended:sushiitem",
          "aquaculture:sushi",
          "pamhc2foodextended:californiarollitem",
          "farmersdelight:salmon_roll",
          "farmersdelight:cod_roll",
          "farmersdelight:kelp_roll_slice",
          "aquaculturedelight:raw_fish_fillet_roll"
				],
        playerNum: 2
			},
      {
				villagerItems: ['moa_decor_cookery:sushi'],
        playerNum: 8
			},
      {
				villagerItems: ['farmersdelight:rice_roll_medley_block'],
        playerNum: 6
			},
			{ villagerItems: ['aquaculture:algae'] },
      {
        villagerItems: ['aquaculture:lockbox'],
        playerNum: 4
			},
      {
        villagerItems: ['aquaculture:treasure_chest'],
        playerNum: 8
			},
      {
        villagerItems: ['minecraft:trident'],
        playerNum: 6
			},
      {
        villagerItems: ['aquaculture:neptunium_ingot'],
        playerNum: 64
			}
		],
    springTradesKey: [
      { playerItems: ['aquaculture:bluegill'], villagerNum: 2},
      { # 3
        playerItems: [
          'aquaculture:perch',
          'aquaculture:minnow'
        ],
        villagerNum: 3
      },
      { # 4
        playerItems: [
          'aquaculture:smallmouth_bass',
          'aquaculture:brown_trout',
          'aquaculture:carp'
        ],
        villagerNum: 4
      },
      {
        playerItems: [
          'aquaculture:gar',
          'aquaculture:muskellunge'
        ],
        villagerNum: 5
      },
      { playerItems: ['aquaculture:catfish'], villagerNum: 12 }
    ],
    summerTradesKey: [
      { playerItems: ['aquaculture:piranha'], villagerNum: 2 },
      { playerItems: ['aquaculture:tambaqui'], villagerNum: 5},
      {
        playerItems: [
          'aquaculture:capitaine',
          'aquaculture:arapaima'
        ],
        villagerNum: 12
      }
    ],
    fallTradesKey: [
      {
        playerItems: [
          'aquaculture:brown_shrooma',
          'aquaculture:red_shrooma'
        ]
      },
      { playerItems: ['aquaculture:synodontis'], villagerNum: 2 },
      { playerItems: ['aquaculture:boulti'], villagerNum: 4 },
      { playerItems: ['aquaculture:bayad'], villagerNum: 5 },
      { playerItems: ['aquaculture:arrau_turtle'], villagerNum: 12}
    ],
    winterTradesKey: [
      { playerItems: ['aquaculture:atlantic_herring'], villagerNum: 2 },
      { playerItems: ['aquaculture:blackfish'], villagerNum: 3 },
      { playerItems: ['aquaculture:pollock'], villagerNum: 4 },
      {
        playerItems: [
          'aquaculture:atlantic_cod',
          'aquaculture:pacific_halibut',
          'aquaculture:atlantic_halibut',
          'aquaculture:pink_salmon',
          'aquaculture:rainbow_trout',
          'aquaculture:red_grouper'
        ],
        villagerNum: 5
      },
      { playerItems: ['aquaculture:tuna'], villagerNum: 12}
    ]
	},
  { # Andre
		nameKey: "Andre",
    textureKey: "dog",
    tradesKey: [
      {
        villagerItems: [
          'minecraft:saddle',
          "minecraft:spyglass"
        ],
        playerNum: 4
			},
      {
        villagerItems: [
          'farmingforblockheads:chicken_nest',
          'farmingforblockheads:feeding_trough'
        ],
        playerNum: 2
			},
      {
        villagerItems: ['waystones:warp_plate'],
        villagerNum: 2,
        playerNum: 8
      },
      {
        villagerItems: [
          'waystones:waystone',
          "waystones:sandy_waystone",
          "waystones:mossy_waystone",
          "waystones:warp_stone"
        ],
        playerNum: 16
			},
      {
        villagerItems: ["mobcapturingtool:mob_capturing_tool"],
        playerNum: 16
			},
      { villagerItems: ["naturescompass:naturescompass"] },
      {
        villagerItems: [
          "exoticbirds:bird_book",
          "exoticbirds:egg_identifier",
          "exoticbirds:egg_incubator",
          "exoticbirds:roost_box",
          "exoticbirds:pigeon_backpack",
        ],
        playerNum: 4
			}
		],
    springTradesKey: [
      {
        villagerItems: [
          'moa_decor_toys:vaca',
          'moa_decor_toys:gatobritanico',
          'moa_decor_toys:gatosiames',
          'moa_decor_toys:lorocian',
          'moa_decor_toys:loroverde'
        ],
        playerNum: 6
      }
    ],
    summerTradesKey: [
      {
        villagerItems: [
          'moa_decor_toys:gallina',
          'moa_decor_toys:gatojellie',
          'moa_decor_toys:gatonegro',
          'moa_decor_toys:gatotuxedo',
          'moa_decor_toys:loroazul',
          'moa_decor_toys:lororojo'
        ],
        playerNum: 6
      }
    ],
    fallTradesKey: [
      {
        villagerItems: [
          'moa_decor_toys:gatoatigrado',
          'moa_decor_toys:gatocalico',
          'moa_decor_toys:gatopersa',
          'moa_decor_toys:gatotabby',
          'moa_decor_toys:lorogris'
        ],
        playerNum: 6
      }
    ],
    winterTradesKey: [
      {
        villagerItems: [
          'moa_decor_toys:zorroblanco',
          'moa_decor_toys:lobo',
          'moa_decor_toys:osopolar',
          'moa_decor_toys:gatoblanco',
          'moa_decor_toys:gatoragdoll'
        ],
        playerNum: 6
      }
    ]
	},
  { # Laly
		nameKey: "Laly",
    textureKey: "merekat",
    tradesKey: [
      { villagerItems: ["minecraft:iron_ingot"] },
      {
        villagerItems: ["minecraft:netherite_scrap"],
        playerNum: 64
			},
      {
        playerItems: [
          "minecraft:redstone",
          "minecraft:raw_copper",
          "create:raw_zinc"
        ],
        playerNum: 64
			}
		],
    springTradesKey: [
      { # 3
        playerItems: [
          'gemsnjewels:tourmaline',
          'gemsnjewels:spinel',
          'gemsnjewels:morganite',
          'gemsnjewels:kunzite'
        ],
        villagerNum: 3
      },
      { # 6
        playerItems: [
          'gemsnjewels:sable_amethyst',
          'gemsnjewels:opal'
        ],
        villagerNum: 6
      }
    ],
    summerTradesKey: [
      { # 3
        playerItems: [
          'gemsnjewels:garnet',
          'gemsnjewels:peridot',
          'gemsnjewels:black_opal',
          'gemsnjewels:jade'
        ],
        villagerNum: 3
      },
      { # 6
        playerItems: [
          'gemsnjewels:dusk_emerald',
          'gemsnjewels:opal'
        ],
        villagerNum: 6
      }
    ],
    fallTradesKey: [
      { # 3
        playerItems: [
          'gemsnjewels:topaz',
          'gemsnjewels:citrine',
          'gemsnjewels:ametrine',
          'gemsnjewels:iolite'
        ],
        villagerNum: 3
      },
      { # 6
        playerItems: [
          'gemsnjewels:pale_diamond',
          'gemsnjewels:ruby'
        ],
        villagerNum: 6
      }
    ],
    winterTradesKey: [
      { # 3
        playerItems: [
          'gemsnjewels:aquamarine',
          'gemsnjewels:zircon',
          'gemsnjewels:alexandrite',
          'gemsnjewels:tanzanite'
        ],
        villagerNum: 3
      },
      { # 6
        playerItems: [
          'gemsnjewels:pale_diamond',
          'gemsnjewels:sapphire'
        ],
        villagerNum: 6
      }
    ]
	},
  { # Pamela
		nameKey: "Pamela",
    textureKey: "rabbit",
		tradesKey: [
      {
        villagerItems: ["minecraft:egg"],
        villagerNum: 16
			},
      {
        villagerItems: ["bakery:yeast"],
        villagerNum: 8
			},
      {
        villagerItems: ["minecraft:honey_bottle"],
        playerNum: 2
			},
      { # containers
        villagerItems: [
          "bakery:jar",
          "vinery:wine_bottle",
          "bakery:tray"
        ],
        villagerNum: 64
			},
      {
        villagerItems: [
          "farmingforblockheads:green_fertilizer",
          "farmingforblockheads:red_fertilizer",
          "farmingforblockheads:yellow_fertilizer"
				]
			}
		],
    springTradesKey: [
      {
        villagerItems: [
          'pamhc2foodcore:carrotmuffinitem',
          'pamhc2foodextended:hamandpineapplepizzaitem',
          'pamhc2foodextended:apricotglazedporkitem',
          'pamhc2foodextended:avocadoburritoitem',
          'pamhc2foodextended:lemondrizzlecakeitem',
          'pamhc2foodextended:mangochutneyitem',
          'pamhc2foodextended:strawberryrhubarbpieitem',
          'pamhc2foodextended:grapefruitpieitem'
        ],
        playerNum: 4
      }
    ],
    summerTradesKey: [
      {
        villagerItems: [
          'pamhc2foodcore:glowberrymuffinitem',
          'pamhc2foodcore:sweetberryyogurtitem',
          'pamhc2foodcore:melonpopsicleitem',
          'pamhc2foodextended:cherryicecreamitem',
          'pamhc2foodextended:cornonthecobitem',
          'pamhc2foodextended:friedpecanokraitem',
          'pamhc2foodextended:summersquashwithradishitem',
          'pamhc2foodextended:tomatoherbchickenitem',
          'pamhc2foodextended:cantaloupejellysandwichitem'
        ],
        playerNum: 4
      }
    ],
    fallTradesKey: [
      {
        villagerItems: [
          'pamhc2foodcore:pumpkinbreaditem',
          'pamhc2foodcore:applesauceitem',
          'pamhc2foodextended:cranberrysauceitem',
          'pamhc2foodextended:baconwrappeddatesitem',
          'pamhc2foodextended:figbaritem',
          'pamhc2foodextended:poachedpearitem',
          'pamhc2foodextended:pumpkinoatsconesitem',
          'pamhc2foodextended:stuffedpepperitem',
          'pamhc2foodextended:grapepieitem'
        ],
        playerNum: 4
      }
    ],
    winterTradesKey: [
      {
        villagerItems: [
          'pamhc2foodcore:pickledbeetsitem',
          'pamhc2foodextended:banananutbreaditem',
          'pamhc2foodextended:beetburgeritem',
          'pamhc2foodextended:creamedbroccolisoupitem',
          'pamhc2foodextended:ovenroastedcaulifloweritem',
          'pamhc2foodextended:spinachpieitem',
          'pamhc2foodextended:sunflowerbroccolisaladitem',
          'pamhc2foodextended:orangegingerbeefitem',
          'pamhc2foodextended:cornedbeefandcabbageitem'
        ],
        playerNum: 4
      }
    ]
	},
	{ # Yukkie
    nameKey: "Yukkie",
    textureKey: "bat",
    tradesKey: [
      {
        playerItems: ["minecraft:enchanted_golden_apple"],
        villagerNum: 64
			}, {
        playerItems: [
					"bakery:sweetberry_cupcake",
					"vinery:cherry_wine",
					"beachparty:sweetberries_cocktail",
					"beachparty:icecream_melon",
					"farmersdelight:glow_berry_custard",
          "farmersdelight:apple_pie",
					"delightful:salmonberry_ice_cream",
					"delightful:cantaloupe_popsicle"
				],
        villagerNum: 2
			},
      { # Juices and Jellies
        playerItems: [
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
        playerNum: 3
			},
      { # Smoothies
        playerItems: [
          "pamhc2foodextended:grapesmoothieitem",
          "pamhc2foodextended:greengrapesmoothieitem",
          "pamhc2foodextended:kiwismoothieitem",
          "pamhc2foodextended:pineapplesmoothieitem",
          "pamhc2foodextended:cherrysmoothieitem",
          "pamhc2foodextended:orangesmoothieitem"
				],
        playerNum: 2
			},
      { # Pies and Jellied Toast
        playerItems: [
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
        playerItems: [
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
        villagerNum: 2
			}
		],
    springTradesKey: [
      { playerItems: ['bakery:strawberry'], playerNum: 64 }
    ],
    summerTradesKey: [
      { playerItems: ['vinery:cherry'], playerNum: 64 }
    ],
    fallTradesKey: [
      {
        playerItems: [
          'vinery:red_grape',
          'vinery:white_grape',
          'vinery:savanna_grapes_red',
          'vinery:savanna_grapes_white',
          'vinery:taiga_grapes_red',
          'vinery:taiga_grapes_white',
          'vinery:jungle_grapes_red',
          'vinery:jungle_grapes_white'
        ],
        playerNum: 64
      }
    ],
    winterTradesKey: [
      { playerItems: ['pamhc2trees:orangeitem'], playerNum: 64 }
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