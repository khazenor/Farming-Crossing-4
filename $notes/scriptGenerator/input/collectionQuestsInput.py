filenameKey = 'filename'
iconKey = 'icon'
nameKey = 'name'
dependencyIdKey = 'dependencyId'
increaseRateKey = 'increaseRate'

collectionNotificationKey = 'collectionNotification'

typeKey = 'type'
itemQuestTypeConst = 'itemQuestType'
observationQuestTypeConst = 'observationQuestType'

questGroupsKey = 'questGroups'
tasksKey = 'tasks'
observeKey = 'observe'
additionalRewardsKey = 'additionalRewards'

questlineGroupId = '5326E5A8132593FA'
questlines = [
  { # Animals
    filenameKey: 'animal_watching',
    nameKey: 'Animal Watching',
    iconKey: 'moa_decor_toys:lorocian',
    collectionNotificationKey: 'New animal observed!',
    increaseRateKey: 0.02,
    typeKey: observationQuestTypeConst,
    questGroupsKey: [
      { # General Water
        nameKey: 'General Water Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:squid_spawn_egg",
            nameKey: "Spot a squid",
            observeKey: "minecraft:squid"
          },
          {
            iconKey: "alexsmobs:spawn_egg_flying_fish",
            nameKey: "Spot a flying fish",
            observeKey: "alexsmobs:flying_fish"
          },
          {
            iconKey: "minecraft:dolphin_spawn_egg",
            nameKey: "Spot a dolphin",
            observeKey: "minecraft:dolphin"
          },
          {
            iconKey: "alexsmobs:spawn_egg_blobfish",
            nameKey: "Spot a blobfish",
            observeKey: "alexsmobs:blobfish"
          },
          {
            iconKey: "alexsmobs:spawn_egg_cachalot_whale",
            nameKey: "Spot a cachalot whale",
            observeKey: "alexsmobs:cachalot_whale"
          }
        ]
      },
      { # Warm Oceans
        nameKey: 'Warm Oceans Completion',
        iconKey: 'minecraft:fire_coral',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_mimic_octopus",
            nameKey: "Spot a mimic octopus",
            observeKey: "alexsmobs:mimic_octopus"
          },
          {
            iconKey: "alexsmobs:spawn_egg_mantis_shrimp",
            nameKey: "Spot a mantis shrimp",
            observeKey: "alexsmobs:mantis_shrimp"
          }
        ]
      },
      { # Beaches
        nameKey: 'Beaches Completion',
        iconKey: 'beachparty:beach_umbrella',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_lobster",
            nameKey: "Spot a lobster",
            observeKey: "alexsmobs:lobster"
          },
          {
            iconKey: "alexsmobs:spawn_egg_seagull",
            nameKey: "Spot a seagull",
            observeKey: "alexsmobs:seagull"
          },
          {
            iconKey: "alexsmobs:spawn_egg_seal",
            nameKey: "Spot a seal",
            observeKey: "alexsmobs:seal"
          },
          {
            iconKey: "exoticbirds:crane_spawn_egg",
            nameKey: "Spot a Crane",
            observeKey: "exoticbirds:crane"
          },
          {
            iconKey: "exoticbirds:gull_spawn_egg",
            nameKey: "Spot a Gull",
            observeKey: "exoticbirds:gull"
          },
          {
            iconKey: "exoticbirds:heron_spawn_egg",
            nameKey: "Spot a Heron",
            observeKey: "exoticbirds:heron"
          },
          {
            iconKey: "minecraft:turtle_spawn_egg",
            nameKey: "Spot a turtle",
            observeKey: "minecraft:turtle"
          },
          {
            iconKey: "exoticbirds:pelican_spawn_egg",
            nameKey: "Spot a Pelican",
            observeKey: "exoticbirds:pelican"
          },
          {
            iconKey: "beachparty:pelican_spawn_egg",
            nameKey: "Spot a Pelican",
            observeKey: "beachparty:pelican"
          }
        ]
      },
      { # River
        nameKey: 'River Completion',
        iconKey: 'beachparty:palm_sapling',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "exoticbirds:kingfisher_spawn_egg",
            nameKey: "Spot a Kingfisher",
            observeKey: "exoticbirds:kingfisher"
          },
          {
            iconKey: "exoticbirds:swan_spawn_egg",
            nameKey: "Spot a Swan",
            observeKey: "exoticbirds:swan"
          },
          {
            iconKey: "exoticbirds:flamingo_spawn_egg",
            nameKey: "Spot a Flamingo",
            observeKey: "exoticbirds:flamingo"
          },
          {
            iconKey: "exoticbirds:penguin_spawn_egg",
            nameKey: "Spot a Penguin",
            observeKey: "exoticbirds:penguin"
          },
          {
            iconKey: "alexsmobs:spawn_egg_platypus",
            nameKey: "Spot a platypus",
            observeKey: "alexsmobs:platypus"
          },
          {
            iconKey: "alexsmobs:spawn_egg_terrapin",
            nameKey: "Spot a terrapin",
            observeKey: "alexsmobs:terrapin"
          },
          {
            iconKey: "exoticbirds:booby_spawn_egg",
            nameKey: "Spot a Booby",
            observeKey: "exoticbirds:booby"
          },
          {
            iconKey: "exoticbirds:duck_spawn_egg",
            nameKey: "Spot a Duck",
            observeKey: "exoticbirds:duck"
          }
        ]
      },
      { # Frozen Ocean
        nameKey: 'Frozen Ocean Completion',
        iconKey: 'minecraft:ice',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_orca",
            nameKey: "Spot an orca",
            observeKey: "alexsmobs:orca"
          },
          {
            iconKey: "alexsmobs:spawn_egg_comb_jelly",
            nameKey: "Spot a comb jelly",
            observeKey: "alexsmobs:comb_jelly"
          }
        ]
      },
      { # Deepest Ocean
        nameKey: 'Deepest Ocean Completion',
        iconKey: 'minecraft:blue_ice',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_giant_squid",
            nameKey: "Spot a giant squid",
            observeKey: "alexsmobs:giant_squid"
          },
          {
            iconKey: "alexsmobs:spawn_egg_frilled_shark",
            nameKey: "Spot a frilled shark",
            observeKey: "alexsmobs:frilled_shark"
          }
        ]
      },
      { # Desert
        nameKey: 'Desert Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_rain_frog",
            nameKey: "Spot a rain frog",
            observeKey: "alexsmobs:rain_frog"
          },
          {
            iconKey: "alexsmobs:spawn_egg_triops",
            nameKey: "Spot a Triops",
            observeKey: "alexsmobs:triops"
          },
          {
            iconKey: "alexsmobs:spawn_egg_jerboa",
            nameKey: "Spot a jerboa",
            observeKey: "alexsmobs:jerboa"
          },
          {
            iconKey: "alexsmobs:spawn_egg_roadrunner",
            nameKey: "Spot a roadrunner",
            observeKey: "alexsmobs:roadrunner"
          },
          {
            iconKey: "exoticbirds:roadrunner_spawn_egg",
            nameKey: "Spot a Roadrunner",
            observeKey: "exoticbirds:roadrunner"
          },
          {
            iconKey: "exoticbirds:ostrich_spawn_egg",
            nameKey: "Spot an Ostrich",
            observeKey: "exoticbirds:ostrich"
          }
        ]
      },
      { # Forest
        nameKey: 'Forest Completion',
        iconKey: 'minecraft:oak_sapling',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:wolf_spawn_egg",
            nameKey: "Spot a wolf",
            observeKey: "minecraft:wolf"
          },
          {
            iconKey: "alexsmobs:spawn_egg_skunk",
            nameKey: "Spot a skunk",
            observeKey: "alexsmobs:skunk"
          },
          {
            iconKey: "alexsmobs:spawn_egg_tasmanian_devil",
            nameKey: "Spot a tasmanian devil",
            observeKey: "alexsmobs:tasmanian_devil"
          },
          {
            iconKey: "alexsmobs:spawn_egg_potoo",
            nameKey: "Spot a potoo",
            observeKey: "alexsmobs:potoo"
          },
          {
            iconKey: "exoticbirds:bluejay_spawn_egg",
            nameKey: "Spot a Blue Jay",
            observeKey: "exoticbirds:bluejay"
          },
          {
            iconKey: "alexsmobs:spawn_egg_blue_jay",
            nameKey: "Spot a blue jay",
            observeKey: "alexsmobs:blue_jay"
          },
          {
            iconKey: "alexsmobs:spawn_egg_banana_slug",
            nameKey: "Spot a banana slug",
            observeKey: "alexsmobs:banana_slug"
          },
          {
            iconKey: "alexsmobs:spawn_egg_sugar_glider",
            nameKey: "Spot a sugar glider",
            observeKey: "alexsmobs:sugar_glider"
          },
          {
            iconKey: "alexsmobs:spawn_egg_bald_eagle",
            nameKey: "Spot a bald eagle",
            observeKey: "alexsmobs:bald_eagle"
          },
          {
            iconKey: "exoticbirds:kiwi_spawn_egg",
            nameKey: "Spot a Kiwi",
            observeKey: "exoticbirds:kiwi"
          },
          {
            iconKey: "exoticbirds:owl_spawn_egg",
            nameKey: "Spot an Owl",
            observeKey: "exoticbirds:owl"
          },
          {
            iconKey: "exoticbirds:cardinal_spawn_egg",
            nameKey: "Spot a Cardinal",
            observeKey: "exoticbirds:cardinal"
          },
          {
            iconKey: "exoticbirds:cassowary_spawn_egg",
            nameKey: "Spot a Cassowary",
            observeKey: "exoticbirds:cassowary"
          },
          {
            iconKey: "exoticbirds:magpie_spawn_egg",
            nameKey: "Spot a Magpie",
            observeKey: "exoticbirds:magpie"
          },
          {
            iconKey: "exoticbirds:lyrebird_spawn_egg",
            nameKey: "Spot a Lyrebird",
            observeKey: "exoticbirds:lyrebird"
          },
          {
            iconKey: "exoticbirds:robin_spawn_egg",
            nameKey: "Spot a Robin",
            observeKey: "exoticbirds:robin"
          },
          {
            iconKey: "exoticbirds:kookaburra_spawn_egg",
            nameKey: "Spot a Kookaburra",
            observeKey: "exoticbirds:kookaburra"
          }

        ]
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:panda_spawn_egg",
            nameKey: "Spot a panda",
            observeKey: "minecraft:panda"
          },
          {
            iconKey: "minecraft:parrot_spawn_egg",
            nameKey: "Spot a parrot",
            observeKey: "minecraft:parrot"
          },
          {
            iconKey: "alexsmobs:spawn_egg_leafcutter_ant",
            nameKey: "Spot a leafcutter ant",
            observeKey: "alexsmobs:leafcutter_ant"
          },
          {
            iconKey: "alexsmobs:spawn_egg_gorilla",
            nameKey: "Spot a gorilla",
            observeKey: "alexsmobs:gorilla"
          },
          {
            iconKey: "alexsmobs:spawn_egg_toucan",
            nameKey: "Spot a toucan",
            observeKey: "alexsmobs:toucan"
          },
          {
            iconKey: "minecraft:ocelot_spawn_egg",
            nameKey: "Spot an ocelot",
            observeKey: "minecraft:ocelot"
          },
          {
            iconKey: "alexsmobs:spawn_egg_capuchin_monkey",
            nameKey: "Spot a capuchin monkey",
            observeKey: "alexsmobs:capuchin_monkey"
          },
          {
            iconKey: "alexsmobs:spawn_egg_anteater",
            nameKey: "Spot an anteater",
            observeKey: "alexsmobs:anteater"
          },
          {
            iconKey: "exoticbirds:hummingbird_spawn_egg",
            nameKey: "Spot a Hummingbird",
            observeKey: "exoticbirds:hummingbird"
          },
          {
            iconKey: "alexsmobs:spawn_egg_hummingbird",
            nameKey: "Spot a hummingbird",
            observeKey: "alexsmobs:hummingbird"
          },
          {
            iconKey: "exoticbirds:macaw_spawn_egg",
            nameKey: "Spot a Macaw",
            observeKey: "exoticbirds:macaw"
          },
          {
            iconKey: "exoticbirds:toucan_spawn_egg",
            nameKey: "Spot a Toucan",
            observeKey: "exoticbirds:toucan"
          }
        ]
      },
      { # Mountain
        nameKey: 'Mountain Completion',
        iconKey: 'minecraft:goat_horn',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:goat_spawn_egg",
            nameKey: "Spot a Goat",
            observeKey: "minecraft:goat"
          }
        ]
      },
      { # Special
        nameKey: 'Special Completion',
        iconKey: 'minecraft:nether_star',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_sunbird",
            nameKey: "Spot a sunbird",
            observeKey: "alexsmobs:sunbird"
          },
          {
            iconKey: "minecraft:bee_spawn_egg",
            nameKey: "Spot a bee",
            observeKey: "minecraft:bee"
          },
          {
            iconKey: "alexsmobs:spawn_egg_devils_hole_pupfish",
            nameKey: "Spot a devils hole pupfish",
            observeKey: "alexsmobs:devils_hole_pupfish"
          },
          {
            iconKey: "minecraft:allay_spawn_egg",
            nameKey: "Spot an allay",
            observeKey: "minecraft:allay"
          },
          {
            iconKey: "minecraft:cat_spawn_egg",
            nameKey: "Spot a cat",
            observeKey: "minecraft:cat"
          }
        ]
      },
      { # Savanna
        nameKey: 'Savanna Completion',
        iconKey: 'minecraft:acacia_sapling',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_emu",
            nameKey: "Spot an emu",
            observeKey: "alexsmobs:emu"
          },
          {
            iconKey: "minecraft:llama_spawn_egg",
            nameKey: "Spot a llama",
            observeKey: "minecraft:llama"
          },
          {
            iconKey: "alexsmobs:spawn_egg_kangaroo",
            nameKey: "Spot a kangaroo",
            observeKey: "alexsmobs:kangaroo"
          },
          {
            iconKey: "alexsmobs:spawn_egg_gazelle",
            nameKey: "Spot a gazelle",
            observeKey: "alexsmobs:gazelle"
          },
          {
            iconKey: "alexsmobs:spawn_egg_maned_wolf",
            nameKey: "Spot a maned wolf",
            observeKey: "alexsmobs:maned_wolf"
          },
          {
            iconKey: "alexsmobs:spawn_egg_elephant",
            nameKey: "Spot an elephant",
            observeKey: "alexsmobs:elephant"
          },
          {
            iconKey: "alexsmobs:spawn_egg_rhinoceros",
            nameKey: "Spot a rhinoceros",
            observeKey: "alexsmobs:rhinoceros"
          },
          {
            iconKey: "exoticbirds:gouldianfinch_spawn_egg",
            nameKey: "Spot a Gouldian Finch",
            observeKey: "exoticbirds:gouldianfinch"
          },
          {
            iconKey: "exoticbirds:budgerigar_spawn_egg",
            nameKey: "Spot a Budgerigar",
            observeKey: "exoticbirds:budgerigar"
          },
          {
            iconKey: "exoticbirds:cockatoo_spawn_egg",
            nameKey: "Spot a Cockatoo",
            observeKey: "exoticbirds:cockatoo"
          },
          {
            iconKey: "exoticbirds:woodpecker_spawn_egg",
            nameKey: "Spot a Woodpecker",
            observeKey: "exoticbirds:woodpecker"
          }
        ]
      },
      { # Plains
        nameKey: 'Plains Completion',
        iconKey: 'minecraft:poppy',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:horse_spawn_egg",
            nameKey: "Spot a horse",
            observeKey: "minecraft:horse"
          },
          {
            iconKey: "alexsmobs:spawn_egg_crow",
            nameKey: "Spot a crow",
            observeKey: "alexsmobs:crow"
          },
          {
            iconKey: "alexsmobs:spawn_egg_bison",
            nameKey: "Spot a bison",
            observeKey: "alexsmobs:bison"
          },
          {
            iconKey: "minecraft:donkey_spawn_egg",
            nameKey: "Spot a donkey",
            observeKey: "minecraft:donkey"
          },
          {
            iconKey: "alexsmobs:spawn_egg_raccoon",
            nameKey: "Spot a raccoon",
            observeKey: "alexsmobs:raccoon"
          },
          {
            iconKey: "alexsmobs:spawn_egg_gelada_monkey",
            nameKey: "Spot a gelada monkey",
            observeKey: "alexsmobs:gelada_monkey"
          },
          {
            iconKey: "exoticbirds:peafowl_spawn_egg",
            nameKey: "Spot a Peafowl",
            observeKey: "exoticbirds:peafowl"
          },
          {
            iconKey: "meadow:brown_bear_spawn_egg",
            nameKey: "Spot a Brown Bear",
            observeKey: "meadow:brown_bear"
          },
          {
            iconKey: "meadow:wooly_cow_spawn_egg",
            nameKey: "Spot a Wooly Cow",
            observeKey: "meadow:wooly_cow"
          },
          {
            iconKey: "meadow:water_buffalo_spawn_egg",
            nameKey: "Spot a Water Buffalo",
            observeKey: "meadow:water_buffalo"
          }
        ]
      },
      { # Grass
        nameKey: 'Grass Completion',
        iconKey: 'minecraft:grass_block',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_fly",
            nameKey: "Spot a fly",
            observeKey: "alexsmobs:fly"
          },
          {
            iconKey: "minecraft:pig_spawn_egg",
            nameKey: "Spot a pig",
            observeKey: "minecraft:pig"
          },
          {
            iconKey: "minecraft:chicken_spawn_egg",
            nameKey: "Spot a chicken",
            observeKey: "minecraft:chicken"
          },
          {
            iconKey: "minecraft:rabbit_spawn_egg",
            nameKey: "Spot a rabbit",
            observeKey: "minecraft:rabbit"
          },
          {
            iconKey: "exoticbirds:pigeon_spawn_egg",
            nameKey: "Spot a Pigeon",
            observeKey: "exoticbirds:pigeon"
          },
          {
            iconKey: "minecraft:sheep_spawn_egg",
            nameKey: "Spot a sheep",
            observeKey: "minecraft:sheep"
          },
          {
            iconKey: "minecraft:cow_spawn_egg",
            nameKey: "Spot a cow",
            observeKey: "minecraft:cow"
          }
        ]
      },
      { # Caves
        nameKey: 'Caves Completion',
        iconKey: 'minecraft:stone',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:bat_spawn_egg",
            nameKey: "Spot a bat",
            observeKey: "minecraft:bat"
          },
          {
            iconKey: "minecraft:glow_squid_spawn_egg",
            nameKey: "Spot a glow squid",
            observeKey: "minecraft:glow_squid"
          },
          {
            iconKey: "alexsmobs:spawn_egg_flutter",
            nameKey: "Spot a flutter",
            observeKey: "alexsmobs:flutter"
          },
          {
            iconKey: "alexsmobs:spawn_egg_cockroach",
            nameKey: "Spot a cockroach",
            observeKey: "alexsmobs:cockroach"
          },
          {
            iconKey: "minecraft:axolotl_spawn_egg",
            nameKey: "Spot an axolotl",
            observeKey: "minecraft:axolotl"
          }
        ]
      },
      { # Snowy
        nameKey: 'Snowy Completion',
        iconKey: 'minecraft:snowball',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "minecraft:polar_bear_spawn_egg",
            nameKey: "Spot a polar bear",
            observeKey: "minecraft:polar_bear"
          },
          {
            iconKey: "alexsmobs:spawn_egg_moose",
            nameKey: "Spot a moose",
            observeKey: "alexsmobs:moose"
          },
          {
            iconKey: "alexsmobs:spawn_egg_snow_leopard",
            nameKey: "Spot a snow leopard",
            observeKey: "alexsmobs:snow_leopard"
          },
          {
            iconKey: "minecraft:fox_spawn_egg",
            nameKey: "Spot a fox",
            observeKey: "minecraft:fox"
          }
        ]
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'biomesoplenty:willow_sapling',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_shoebill",
            nameKey: "Spot a shoebill",
            observeKey: "alexsmobs:shoebill"
          },
          {
            iconKey: "alexsmobs:spawn_egg_catfish",
            nameKey: "Spot a catfish",
            observeKey: "alexsmobs:catfish"
          },
          {
            iconKey: "minecraft:frog_spawn_egg",
            nameKey: "Spot a frog",
            observeKey: "minecraft:frog"
          },
          {
            iconKey: "minecraft:tadpole_spawn_egg",
            nameKey: "Spot a tadpole",
            observeKey: "minecraft:tadpole"
          },
          {
            iconKey: "alexsmobs:spawn_egg_caiman",
            nameKey: "Spot a Caiman",
            observeKey: "alexsmobs:caiman"
          },
          {
            iconKey: "alexsmobs:spawn_egg_mudskipper",
            nameKey: "Spot a mudskipper",
            observeKey: "alexsmobs:mudskipper"
          }
        ]
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '2D62FBEF18E6ABF6', # Spotting animals
        tasksKey: [
          {
            iconKey: "alexsmobs:spawn_egg_bunfungus",
            nameKey: "Spot a bunfungus",
            observeKey: "alexsmobs:bunfungus"
          },
          {
            iconKey: "alexsmobs:spawn_egg_mungus",
            nameKey: "Spot a mungus",
            observeKey: "alexsmobs:mungus"
          },
          {
            iconKey: "minecraft:mooshroom_spawn_egg",
            nameKey: "Spot a mooshroom",
            observeKey: "minecraft:mooshroom"
          },
        ]
      }
    ]

  },
  { # Aquarium
    filenameKey: 'aquarium',
    nameKey: 'Aquarium',
    iconKey: 'aquaculture:atlantic_herring',
    collectionNotificationKey: 'New fish caught!',
    increaseRateKey: 0.03,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla
        nameKey: 'Vanilla Completion',
        iconKey: 'minecraft:grass_block',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "minecraft:cod",
          "minecraft:salmon",
          "minecraft:tropical_fish",
          "minecraft:pufferfish"
        ]
      },
      { # Freshwater
        nameKey: 'Freshwater Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:smallmouth_bass",
          "aquaculture:bluegill",
          "aquaculture:brown_trout",
          "aquaculture:carp",
          "aquaculture:catfish",
          "aquaculture:gar",
          "aquaculture:minnow",
          "aquaculture:muskellunge",
          "aquaculture:perch"
        ]
      },
      { # Arid
        nameKey: 'Arid Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:bayad",
          "aquaculture:boulti",
          "aquaculture:capitaine",
          "aquaculture:synodontis"
        ]
      },
      { # Artic
        nameKey: 'Artic Completion',
        iconKey: 'minecraft:packed_ice',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:atlantic_cod",
          "aquaculture:blackfish",
          "aquaculture:pacific_halibut",
          "aquaculture:atlantic_halibut",
          "aquaculture:atlantic_herring",
          "aquaculture:pink_salmon",
          "aquaculture:pollock",
          "aquaculture:rainbow_trout"
        ]
      },
      { # Saltwater
        nameKey: 'Saltwater Completion',
        iconKey: 'biomesoplenty:dried_salt',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:jellyfish",
          "aquaculture:red_grouper",
          "aquaculture:tuna"
        ]
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'biomesoplenty:willow_sapling',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:box_turtle",
          "aquaculture:leech",
          "aquaculture:goldfish"
        ]
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:brown_shrooma",
          "aquaculture:red_shrooma"
        ]
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: [
          "aquaculture:arapaima",
          "aquaculture:piranha",
          "aquaculture:tambaqui",
          "aquaculture:arrau_turtle"
        ]
      }
    ]
  },
  { # Cooking collection
    filenameKey: 'cooking_collection',
    nameKey: 'Cooking Collection',
    iconKey: 'bakery:strawberry_cupcake',
    collectionNotificationKey: 'New dish cooked!',
    increaseRateKey: 0.04,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      ## Lets Do Foods
      { # Oven
        nameKey: 'Oven Recipes Completion',
        iconKey: 'bakery:brick_stove',
        dependencyIdKey: '57BAA8B414FF1F4F', # seed
        tasksKey: [
          'bakery:croissant',
          'bakery:crusty_bread',
          'bakery:bread',
          'bakery:baguette',
          'bakery:toast',
          'bakery:braided_bread',
          'bakery:bun',
          'bakery:vegetable_sandwich',
          'bakery:sandwich',
          'bakery:bread_crate',
          'bakery:linzer_tart',
          'bakery:apple_pie',
          'bakery:glowberry_tart',
          'bakery:chocolate_tart',
          'bakery:bundt_cake',
          'bakery:waffle'
        ]
      },
      { # Small Cooking Pot
        nameKey: 'Small Cooking Pot Recipes Completion',
        iconKey: 'bakery:small_cooking_pot',
        dependencyIdKey: '13B67DDBCF1019AB', # bread
        tasksKey: [
          'bakery:strawberry_jam',
          'bakery:sweetberry_jam',
          'bakery:glowberry_jam',
          'bakery:apple_jam',
          'bakery:chocolate_jam',
          'bakery:chocolate_truffle',
          'bakery:pudding',
          'bakery:jam_roll'
        ]
      },
      { # Baker Station
        nameKey: 'Baking Station Recipes Completion',
        iconKey: 'bakery:baker_station',
        dependencyIdKey: '5E93B9E15372F454', # jar
        tasksKey: [
          'bakery:strawberry_cupcake',
          'bakery:sweetberry_cupcake',
          'bakery:apple_cupcake',
          'bakery:strawberry_glazed_cookie',
          'bakery:sweetberry_glazed_cookie',
          'bakery:chocolate_glazed_cookie',
          'bakery:strawberry_cake',
          'bakery:sweetberry_cake',
          'bakery:chocolate_cake'
        ]
      },
      { # Grapevine Pot
        nameKey: 'Grapevine Pot Recipes Completion',
        iconKey: 'vinery:grapevine_pot',
        dependencyIdKey: '45CAACDFDC15E734', # cake
        tasksKey: [
          'vinery:red_grapejuice_wine_bottle',
          'vinery:white_grapejuice_wine_bottle',
          'vinery:taiga_red_grapejuice_bottle',
          'vinery:taiga_white_grapejuice_bottle',
          'vinery:jungle_red_grapejuice_bottle',
          'vinery:jungle_white_grapejuice_bottle',
          'vinery:savanna_red_grapejuice_bottle',
          'vinery:savanna_white_grapejuice_bottle'
        ]
      },
      { # Aging Barrel
        nameKey: 'Aging Barrel Recipes Completion',
        iconKey: 'vinery:fermentation_barrel',
        additionalRewardsKey: [
          'vinery:straw_hat',
          'vinery:vinemaker_apron',
          'vinery:vinemaker_leggings',
          'vinery:vinemaker_boots'
        ],
        dependencyIdKey: '45CAACDFDC15E734', # cake
        tasksKey: [
          'vinery:apple_juice',
          'vinery:apple_wine',
          'vinery:cherry_wine',
          'vinery:magnetic_wine',
          'vinery:noir_wine',
          'vinery:king_danis_wine',
          'vinery:mellohi_wine',
          'vinery:stal_wine',
          'vinery:strad_wine',
          'vinery:solaris_wine',
          'vinery:chorus_wine',
          'vinery:aegis_wine',
          'vinery:clark_wine',
          'vinery:bolvar_wine',
          'vinery:kelp_cider',
          'vinery:chenet_wine',
          'vinery:apple_cider',
          'vinery:jellie_wine',
          'vinery:red_wine',
          'vinery:praetorian_wine',
          'vinery:jo_special_mixture',
          'vinery:cristel_wine',
          'vinery:creepers_crush',
          'vinery:villagers_fright',
          'vinery:glowing_wine',
          'vinery:mead',
          'vinery:bottle_mojang_noir',
          'vinery:eiswein'
        ]
      },
      { # Cheese Press
        nameKey: 'Cheese Press Recipes Completion',
        iconKey: 'meadow:cheese_form',
        additionalRewardsKey: [
          'meadow:fur_helmet',
          'meadow:fur_chestplate',
          'meadow:fur_leggings',
          'meadow:fur_boots'
        ],
        dependencyIdKey: '65B28F78A7DDBD06', # wine
        tasksKey: [
          'meadow:cheese_block',
          'meadow:sheep_cheese_block',
          'meadow:grain_cheese_block',
          'meadow:amethyst_cheese_block',
          'meadow:buffalo_cheese_block',
          'meadow:goat_cheese_block',
          'meadow:cheese_sandwich',
          'meadow:cheese_roll',
          'meadow:cheesecake',
          'meadow:cheese_tart'
        ]
      },
      { # Cooking Pot
        nameKey: 'Cooking Pot Recipes Completion',
        iconKey: 'candlelight:cooking_pot',
        dependencyIdKey: '57889789985B323E', # cheese stick
        tasksKey: [
          'candlelight:tomato_soup',
          'candlelight:mushroom_soup',
          'candlelight:pasta',
          'candlelight:chicken_teriyaki',
          'candlelight:chocolate',
          'candlelight:lasagne',
          'candlelight:chicken',
          'candlelight:pork_ribs',
          'candlelight:salmon_wine'
        ]
      },
      { # Cooking Pan
        nameKey: 'Cooking Pan Recipes Completion',
        iconKey: 'candlelight:cooking_pan',
        additionalRewardsKey: [
          'candlelight:cooking_hat',
          'candlelight:chefs_jacket',
          'candlelight:chefs_pants',
          'candlelight:chefs_boots'
        ],
        dependencyIdKey: '48C7E0AF4C9A3C3E', # mushroom soup
        tasksKey: [
          'candlelight:pancake',
          'candlelight:fricasse',
          'candlelight:roastbeef_carrots',
          'candlelight:beef_wellington',
          'candlelight:pizza',
          'candlelight:cooked_beef',
          'candlelight:bolognese',
          'candlelight:chicken_alfredo',
          'candlelight:lettuce_beef',
          'candlelight:pasta_bolognese',
          'candlelight:pasta_lettuce'
        ]
      },
      { # Crafting table
        nameKey: 'Regular Crafting Recipes Completion',
        iconKey: 'minecraft:crafting_table',
        dependencyIdKey: '57889789985B323E', # cheese stick
        tasksKey: [
          'candlelight:tomato_mozzarella_salad',
          'candlelight:veggie_plate',
          'candlelight:lettuce_tomato',
          'candlelight:lettuce_salad',
          'candlelight:beef_tartare',
          'candlelight:beetroot_salad'
        ]
      },
      { # Mini Fridge
        nameKey: 'Mini Fridge Recipes Completion',
        iconKey: 'beachparty:mini_fridge',
        dependencyIdKey: '56C6F1D87FA09C24', # pizza
        tasksKey: [
          'beachparty:sweetberry_icecream',
          'beachparty:coconut_icecream',
          'beachparty:chocolate_icecream',
          'beachparty:icecream_chocolate',
          'beachparty:icecream_coconut',
          'beachparty:icecream_cactus',
          'beachparty:icecream_melon',
          'beachparty:icecream_sweetberries',
        ]
      },
      { # Tiki Bar
        nameKey: 'Tiki Bar Recipes Completion',
        iconKey: 'beachparty:tiki_bar',
        additionalRewardsKey: [
          'beachparty:beach_hat',
          'beachparty:swim_wings',
          'beachparty:trunks',
          'beachparty:crocs'
        ],
        dependencyIdKey: '2D0063702FDE9B52', # ice cream coconut
        tasksKey: [
          'beachparty:chocolate_milkshake',
          'beachparty:coconut_milkshake',
          'beachparty:sweetberry_milkshake',
          'beachparty:honey_cocktail',
          'beachparty:melon_cocktail',
          'beachparty:pumpkin_cocktail',
          'beachparty:cocoa_cocktail',
          'beachparty:sweetberries_cocktail',
          'beachparty:coconut_cocktail'
        ]
      },
      ## Farmers Delight Suite Recipes
      { # Delightful
        nameKey: 'Delightful Cooking Pot Recipes Completion',
        iconKey: 'delightful:sinigang',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: [
          'delightful:animal_oil_bottle',
          'delightful:ender_nectar',
          'delightful:glow_jelly_bottle',
          'delightful:jelly_bottle',
          'delightful:lavender_tea',
          'delightful:matcha',
          'delightful:nut_butter_bottle',
          'delightful:rock_candy',
          'delightful:salmonberry_gummy',
          'delightful:sinigang',
        ]
      },
      { # Alex Delight
        nameKey: "Alex's Delight Cooking Pot Recipes Completion",
        iconKey: 'alexsdelight:acacia_blossom_soup',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: [
          'alexsdelight:acacia_blossom_soup',
          'alexsdelight:kangaroo_pasta',
          'alexsdelight:kangaroo_stew',
          'alexsdelight:lobster_pasta'
        ]
      },
      { # Aquaculture Delight
        nameKey: 'Aquaculture Delight Cooking Pot Recipes Completion',
        iconKey: 'aquaculturedelight:halibut_with_tartar_sauce',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: [
          'aquaculture:turtle_soup',
          'aquaculturedelight:baked_pollock_with_carrots',
          'aquaculturedelight:bass_stew',
          'aquaculturedelight:buckling',
          'aquaculturedelight:halaszle',
          'aquaculturedelight:halibut_with_tartar_sauce',
          'aquaculturedelight:jellyfish_jelly',
          'aquaculturedelight:poor_fisher_chowder',
          'aquaculturedelight:rollmops',
          'aquaculturedelight:tuna_spaghetti',
          'aquaculturedelight:unusual_fish_soup'
        ]
      },
      { # Farmer's Delight
        nameKey: 'Farmers Delight Cooking Pot Recipes Completion',
        iconKey: 'farmersdelight:pasta_with_meatballs',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: [
          'farmersdelight:apple_cider',
          'farmersdelight:baked_cod_stew',
          'farmersdelight:beef_stew',
          'farmersdelight:bone_broth',
          'farmersdelight:cabbage_rolls',
          'farmersdelight:chicken_soup',
          'farmersdelight:cooked_rice',
          'farmersdelight:dog_food',
          'farmersdelight:dumplings',
          'farmersdelight:fish_stew',
          'farmersdelight:fried_rice',
          'farmersdelight:glow_berry_custard',
          'farmersdelight:hot_cocoa',
          'farmersdelight:mushroom_rice',
          'farmersdelight:noodle_soup',
          'farmersdelight:pasta_with_meatballs',
          'farmersdelight:pasta_with_mutton_chop',
          'farmersdelight:pumpkin_soup',
          'farmersdelight:ratatouille',
          'farmersdelight:squid_ink_pasta',
          'farmersdelight:stuffed_pumpkin_block',
          'farmersdelight:tomato_sauce',
          'farmersdelight:vegetable_noodles',
          'farmersdelight:vegetable_soup'
        ]
      },
      { # Cuisine Delight
        nameKey: 'Cuisine Delight Recipes Completion',
        iconKey: 'cuisinedelight:cuisine_skillet',
        dependencyIdKey: '29F10804B90D8DA8', # cabbage rolls
        tasksKey: [
          'cuisinedelight:ham_fried_rice',
          'cuisinedelight:fried_rice',
          'cuisinedelight:mixed_fried_rice',
          'cuisinedelight:meat_with_seafood',
          'cuisinedelight:meat_with_vegetables',
          'cuisinedelight:seafood_with_vegetables',
          'cuisinedelight:fried_pasta',
          'cuisinedelight:mixed_pasta',
          'cuisinedelight:meat_fried_rice',
          'cuisinedelight:meat_pasta',
          'cuisinedelight:scrambled_egg_and_tomato',
          'cuisinedelight:fried_meat_and_melon',
          'cuisinedelight:meat_platter',
          'cuisinedelight:seafood_fried_rice',
          'cuisinedelight:seafood_pasta',
          'cuisinedelight:vegetable_fried_rice',
          'cuisinedelight:vegetable_pasta',
          'cuisinedelight:seafood_platter',
          'cuisinedelight:vegetable_platter',
          'cuisinedelight:fried_mushroom'
        ]
      }
    ]
  },
  { # Flora collection
    filenameKey: 'flora_compendium',
    nameKey: 'Flora Compendium',
    iconKey: 'meadow:alpine_poppy',
    collectionNotificationKey: 'New flora collected!',
    increaseRateKey: 0.02,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla Foods
        nameKey: 'Vanilla Foods Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:apple",
          "minecraft:bamboo",
          "minecraft:beetroot_seeds",
          "minecraft:brown_mushroom",
          "minecraft:cactus",
          "minecraft:carrot",
          "minecraft:cocoa_beans",
          "minecraft:glow_berries",
          "minecraft:kelp",
          "minecraft:melon_slice",
          "minecraft:potato",
          "minecraft:pumpkin_seeds",
          "minecraft:pumpkin",
          "minecraft:red_mushroom",
          "minecraft:sugar_cane",
          "minecraft:sweet_berries",
          "minecraft:wheat_seeds"
        ]
      },
      { # Misc Foods
        nameKey: 'Moded Foods Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "alexsmobs:banana",
          "bakery:oat_seeds",
          "bakery:strawberry_seeds",
          "beachparty:coconut",
          "candlelight:lettuce_seeds",
          "candlelight:tomato_seeds",
          "delightful:cantaloupe_slice",
          "delightful:salmonberries",
          "farmersdelight:cabbage_seeds",
          "farmersdelight:onion",
          "farmersdelight:rice",
          "farmersdelight:tomato_seeds",
          "supplementaries:flax_seeds",
          "vinery:jungle_grape_seeds_red",
          "vinery:jungle_grape_seeds_white",
          "vinery:red_grape_seeds",
          "vinery:savanna_grape_seeds_red",
          "vinery:savanna_grape_seeds_white",
          "vinery:taiga_grape_seeds_red",
          "vinery:taiga_grape_seeds_white",
          "vinery:white_grape_seeds"
        ]
      },
      { # Vanilla Flower
        nameKey: 'Vanilla Flower Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:allium",
          "minecraft:azure_bluet",
          "minecraft:blue_orchid",
          "minecraft:cornflower",
          "minecraft:dandelion",
          "minecraft:lilac",
          "minecraft:lily_of_the_valley",
          "minecraft:orange_tulip",
          "minecraft:oxeye_daisy",
          "minecraft:peony",
          "minecraft:pink_tulip",
          "minecraft:poppy",
          "minecraft:red_tulip",
          "minecraft:rose_bush",
          "minecraft:sunflower",
          "minecraft:white_tulip",
          "minecraft:wither_rose",
          "minecraft:torchflower_seeds"
        ]
      },
      { # Biomes o Plenty
        nameKey: 'Biomes o Plenty Flowers Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomesoplenty:blue_hydrangea",
          "biomesoplenty:burning_blossom",
          "biomesoplenty:cattail",
          "biomesoplenty:glowflower",
          "biomesoplenty:goldenrod",
          "biomesoplenty:icy_iris",
          "biomesoplenty:lavender",
          "biomesoplenty:orange_cosmos",
          "biomesoplenty:pink_daffodil",
          "biomesoplenty:pink_hibiscus",
          "biomesoplenty:rose",
          "biomesoplenty:tall_lavender",
          "biomesoplenty:violet",
          "biomesoplenty:waterlily",
          "biomesoplenty:white_petals",
          "biomesoplenty:wildflower",
          "biomesoplenty:wilted_lily"
        ]
      },
      { # Misc Flowers
        nameKey: 'Misc Flower Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "alexsmobs:acacia_blossom",
          "candlelight:rose",
          "meadow:alpine_poppy",
          "meadow:delphinium",
          "meadow:enzian",
          "meadow:eriophorum_tall",
          "meadow:eriophorum",
          "meadow:fire_lily",
          "meadow:saxifrage"
        ]
      },
      { # Vanilla Sapling
        nameKey: 'Vanilla Sapling Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "minecraft:acacia_sapling",
          "minecraft:azalea",
          "minecraft:birch_sapling",
          "minecraft:cherry_sapling",
          "minecraft:dark_oak_sapling",
          "minecraft:jungle_sapling",
          "minecraft:oak_sapling",
          "minecraft:spruce_sapling"
        ]
      },
      { # Modded Saplings
        nameKey: 'Modded Sapling Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomesoplenty:dead_sapling",
          "biomesoplenty:fir_sapling",
          "biomesoplenty:flowering_oak_sapling",
          "biomesoplenty:jacaranda_sapling",
          "biomesoplenty:magic_sapling",
          "biomesoplenty:mahogany_sapling",
          "biomesoplenty:maple_sapling",
          "biomesoplenty:orange_autumn_sapling",
          "biomesoplenty:origin_sapling",
          "biomesoplenty:palm_sapling",
          "biomesoplenty:rainbow_birch_sapling",
          "biomesoplenty:redwood_sapling",
          "biomesoplenty:snowblossom_sapling",
          "biomesoplenty:willow_sapling",
          "biomesoplenty:yellow_autumn_sapling",
          "beachparty:palm_sapling",
          "meadow:pine_sapling",
          "vinery:cherry_sapling",
          "vinery:apple_tree_sapling"
        ]
      },
      { # Misc Flora
        nameKey: 'Misc Flora Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: [
          "biomesoplenty:toadstool",
          "biomesoplenty:glowshroom",
          "minecraft:flowering_azalea",
          "minecraft:moss_block",
          "minecraft:moss_carpet",
          "minecraft:pink_petals",
          "minecraft:spore_blossom",
          "minecraft:big_dripleaf",
          "minecraft:sea_pickle",
          "minecraft:lily_pad",
          "biomesoplenty:huge_lily_pad",
          "biomesoplenty:glowing_moss_block",
          "biomesoplenty:glowing_moss_carpet"
        ]
      }
    ]
  },
  { # Mineral Museum
    filenameKey: 'mineral_museum',
    nameKey: 'Mineral Museum',
    iconKey: 'minecraft:raw_gold',
    collectionNotificationKey: 'New mineral mined!',
    increaseRateKey: 0.03,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Vanilla Blocks
        nameKey: 'Vanilla Blocks Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.01,
        tasksKey: [
          "minecraft:cobblestone",
          "minecraft:mossy_cobblestone",
          "minecraft:cobbled_deepslate",
          "minecraft:diorite",
          "minecraft:granite",
          "minecraft:andesite",
          "minecraft:sandstone",
          "minecraft:red_sandstone",
          "minecraft:calcite",
          "minecraft:dripstone_block",
          "minecraft:pointed_dripstone",
          "minecraft:smooth_basalt",
          "minecraft:tuff",
          "minecraft:obsidian"
        ]
      },
      { # Modded Blocks
        nameKey: 'Modded Blocks Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.01,
        tasksKey: [
          "create:crimsite",
          "create:asurine",
          "create:veridium",
          "create:ochrum",
          "create:scoria",
          "create:limestone",
          "meadow:mossy_cobbled_limestone",
          "meadow:cobbled_limestone",
          "biomesoplenty:white_sandstone",
          "biomesoplenty:orange_sandstone",
          "biomesoplenty:black_sandstone",
          "biomesoplenty:dried_salt"
        ]
      },
      { # Ore
        nameKey: 'Ore Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.03,
        tasksKey: [
          "minecraft:coal",
          "minecraft:raw_copper",
          "minecraft:raw_iron",
          "minecraft:amethyst_shard",
          "minecraft:raw_gold",
          "create:raw_zinc",
          "minecraft:redstone",
          "minecraft:lapis_lazuli"
        ]
      },
      { # Rare Gems
        nameKey: 'Rare Gems Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.15,
        tasksKey: [
          "minecraft:diamond",
          "gemsnjewels:dusk_emerald",
          "gemsnjewels:opal",
          "gemsnjewels:pale_diamond",
          "gemsnjewels:ruby",
          "gemsnjewels:sable_amethyst",
          "gemsnjewels:sapphire"
        ]
      },
      { # Common Gems
        nameKey: 'Common Gems Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.07,
        tasksKey: [
          "gemsnjewels:garnet",
          "gemsnjewels:topaz",
          "gemsnjewels:peridot",
          "gemsnjewels:aquamarine",
          "gemsnjewels:zircon",
          "gemsnjewels:alexandrite",
          "gemsnjewels:tanzanite",
          "gemsnjewels:tourmaline",
          "gemsnjewels:spinel",
          "gemsnjewels:black_opal",
          "gemsnjewels:citrine",
          "gemsnjewels:morganite",
          "gemsnjewels:ametrine",
          "gemsnjewels:iolite",
          "gemsnjewels:kunzite",
          "gemsnjewels:jade"
        ]
      }
    ]

  }
]