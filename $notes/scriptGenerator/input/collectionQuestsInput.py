from list import collectionQuests as cqlist

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
questStartAtCenterKey = 'questStartAtCenter'

questlineGroupId = '5326E5A8132593FA'

itemSeedStrs = {
  "vinery:knulp_wine": "vinery:king_danis_wine",
  "vinery:lilitu_wine": "vinery:praetorian_wine"
}
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
        iconKey: 'artifacts:umbrella',
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
            iconKey: "quark:crab_spawn_egg",
            nameKey: "Spot a Crab",
            observeKey: "quark:crab"
          },
          {
            observeKey: 'bloomingnature:pelican',
            nameKey: 'Spot a pelican',
            iconKey: 'bloomingnature:pelican_spawn_egg'
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
            iconKey: "minecraft:camel_spawn_egg",
            nameKey: "Spot a camel",
            observeKey: "minecraft:camel"
          },
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
          },
          {
            observeKey: 'bloomingnature:deer',
            nameKey: 'Spot a deer',
            iconKey: 'bloomingnature:deer_spawn_egg'
          },
          {
            observeKey: 'bloomingnature:turkey',
            nameKey: 'Spot a turkey',
            iconKey: 'bloomingnature:turkey_spawn_egg'
          },
          {
            observeKey: 'bloomingnature:owl',
            nameKey: 'Spot a owl',
            iconKey: 'bloomingnature:owl_spawn_egg'
          },
          {
            observeKey: 'bloomingnature:boar',
            nameKey: 'Spot a boar',
            iconKey: 'bloomingnature:boar_spawn_egg'
          },
          {
            observeKey: 'bloomingnature:red_wolf',
            nameKey: 'Spot a red wolf',
            iconKey: 'bloomingnature:red_wolf_spawn_egg'
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
          },
          {
            iconKey: "quark:shiba_spawn_egg",
            nameKey: "Spot a Shiba",
            observeKey: "quark:shiba"
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
          },
          {
            observeKey: 'bloomingnature:bison',
            nameKey: 'Spot a bison',
            iconKey: 'bloomingnature:bison_spawn_egg'
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
          },
          {
            observeKey: 'bloomingnature:raccoon',
            nameKey: 'Spot a raccoon',
            iconKey: 'bloomingnature:raccoon_spawn_egg'
          },
          {
            observeKey: 'bloomingnature:squirrel',
            nameKey: 'Spot a squirrel',
            iconKey: 'bloomingnature:squirrel_spawn_egg'
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
          },
          {
            iconKey: "quark:stoneling_spawn_egg",
            nameKey: "Spot a Stoneling",
            observeKey: "quark:stoneling"
          },
          {
            iconKey: "quark:toretoise_spawn_egg",
            nameKey: "Spot a Toretoise",
            observeKey: "quark:toretoise"
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
          },
          {
            observeKey: 'bloomingnature:mossy_sheep',
            nameKey: 'Spot a mossy sheep',
            iconKey: 'bloomingnature:mossy_sheep_spawn_egg'
          },
          {
            observeKey: 'bloomingnature:muddy_pig',
            nameKey: 'Spot a muddy pig',
            iconKey: 'bloomingnature:muddy_pig_spawn_egg'
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
        tasksKey: cqlist.fishVanilla
      },
      { # Freshwater
        nameKey: 'Freshwater Completion',
        iconKey: 'minecraft:water_bucket',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishFreshWater
      },
      { # Arid
        nameKey: 'Arid Completion',
        iconKey: 'minecraft:dead_bush',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishArid
      },
      { # Artic
        nameKey: 'Artic Completion',
        iconKey: 'minecraft:packed_ice',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishArtic
      },
      { # Saltwater
        nameKey: 'Saltwater Completion',
        iconKey: 'biomesoplenty:dried_salt',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishSaltWater
      },
      { # Swamp
        nameKey: 'Swamp Completion',
        iconKey: 'biomesoplenty:willow_sapling',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishSwamp
      },
      { # Mushroom
        nameKey: 'Mushroom Completion',
        iconKey: 'minecraft:red_mushroom',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishMushroom
      },
      { # Jungle
        nameKey: 'Jungle Completion',
        iconKey: 'minecraft:jungle_sapling',
        dependencyIdKey: '51AC164BB0124EBA', # Catching Fishes
        tasksKey: cqlist.fishJungle
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
    questStartAtCenterKey: True,
    questGroupsKey: [
      ## Lets Do Foods
      { # Oven
        nameKey: 'Oven Recipes Completion',
        iconKey: 'bakery:brick_stove',
        dependencyIdKey: '57BAA8B414FF1F4F', # seed
        tasksKey: cqlist.foodOven
      },
      { # Small Cooking Pot
        nameKey: 'Small Cooking Pot Recipes Completion',
        iconKey: 'bakery:small_cooking_pot',
        dependencyIdKey: '13B67DDBCF1019AB', # bread
        tasksKey: cqlist.foodSmallCookingPot
      },
      { # Baker Station
        nameKey: 'Baking Station Recipes Completion',
        iconKey: 'bakery:baker_station',
        dependencyIdKey: '5E93B9E15372F454', # jar
        tasksKey: cqlist.foodBakerStation
      },
      { # Grapevine Pot
        nameKey: 'Grapevine Pot Recipes Completion',
        iconKey: 'vinery:grapevine_pot',
        dependencyIdKey: '45CAACDFDC15E734', # cake
        tasksKey: cqlist.foodGrapevinePot
      },
      { # Aging Barrel
        nameKey: 'Aging Barrel Recipes Completion',
        iconKey: 'vinery:fermentation_barrel',
        dependencyIdKey: '45CAACDFDC15E734', # cake
        tasksKey: cqlist.foodAgingBarrel
      },
      { # Cheese Press
        nameKey: 'Cheese Press Recipes Completion',
        iconKey: 'meadow:cheese_form',
        dependencyIdKey: '65B28F78A7DDBD06', # wine
        tasksKey: cqlist.foodCheesePress
      },
      { # Cooking Pot
        nameKey: 'Cooking Pot Recipes Completion',
        iconKey: 'candlelight:cooking_pot',
        dependencyIdKey: '57889789985B323E', # cheese stick
        tasksKey: cqlist.foodCookingPot
      },
      { # Cooking Pan
        nameKey: 'Cooking Pan Recipes Completion',
        iconKey: 'candlelight:cooking_pan',
        dependencyIdKey: '48C7E0AF4C9A3C3E', # mushroom soup
        tasksKey: cqlist.foodCookingPan
      },
      { # Crafting table
        nameKey: 'Regular Crafting Recipes Completion',
        iconKey: 'minecraft:crafting_table',
        dependencyIdKey: '57889789985B323E', # cheese stick
        tasksKey: cqlist.foodCraftingTable
      },
      { # Mini Fridge
        nameKey: 'Mini Fridge Recipes Completion',
        iconKey: 'beachparty:mini_fridge',
        dependencyIdKey: '56C6F1D87FA09C24', # pizza
        tasksKey: cqlist.foodMiniFridge
      },
      { # Tiki Bar
        nameKey: 'Tiki Bar Recipes Completion',
        iconKey: 'beachparty:tiki_bar',
        dependencyIdKey: '2D0063702FDE9B52', # ice cream coconut
        tasksKey: cqlist.foodTikiBar
      },
      { # Tea kettle
        nameKey: 'Tea Kettle Recipes Completion',
        iconKey: 'herbalbrews:tea_kettle',
        dependencyIdKey: '524F06C306C3B675', # green tea leaf
        tasksKey: cqlist.foodTeaKettle
      },
      { # Brewing Cauldron
        nameKey: 'Brewing Cauldron Recipes Completion',
        iconKey: 'herbalbrews:cauldron',
        dependencyIdKey: '55EF5DFF6C8B14A1', # green tea
        tasksKey: cqlist.foodCauldron
      },
      { # Brewing Station
        nameKey: 'Wooden Brewing Station Recipes Completion',
        iconKey: 'brewery:wooden_brewingstation',
        dependencyIdKey: '451FA11444C0ADC0', # dried barley
        tasksKey: cqlist.foodBrewingWood
      },
      {
        nameKey: 'Copper Brewing Station Recipes Completion',
        iconKey: 'brewery:copper_brewingstation',
        dependencyIdKey: '5864CE9EC333F521', # barley beer
        tasksKey: cqlist.foodBrewingCopper
      },
      ## Farmers Delight Suite Recipes
      { # Delightful
        nameKey: 'Delightful Cooking Pot Recipes Completion',
        iconKey: 'delightful:sinigang',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: cqlist.foodDelightful
      },
      { # Alex Delight
        nameKey: "Alex's Delight Cooking Pot Recipes Completion",
        iconKey: 'alexsdelight:acacia_blossom_soup',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: cqlist.foodAlex
      },
      { # Aquaculture Delight
        nameKey: 'Aquaculture Delight Cooking Pot Recipes Completion',
        iconKey: 'aquaculturedelight:halibut_with_tartar_sauce',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: cqlist.foodAquaculture
      },
      { # Farmer's Delight
        nameKey: 'Farmers Delight Cooking Pot Recipes Completion',
        iconKey: 'farmersdelight:pasta_with_meatballs',
        dependencyIdKey: '277E14B2EF5D2F6A', # cabbage leaf
        tasksKey: cqlist.foodFarmersDelight
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
        tasksKey: cqlist.floraFoodVanilla
      },
      { # Misc Foods
        nameKey: 'Moded Foods Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraMiscFood
      },
      { # Vanilla Flower
        nameKey: 'Vanilla Flower Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraFlowerVanilla
      },
      { # Biomes o Plenty
        nameKey: 'Biomes o Plenty Flowers Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraFlowerBiomesoPlenty
      },
      { # Blooming Nature Flowers
        nameKey: 'Blooming Nature Flowers Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraFlowerBloomingNature
      },
      { # Botania Flowers
        nameKey: 'Botania Flowers Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraFlowerBotania
      },
      { # Botania Shrooms
        nameKey: 'Botania Mushrooms Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraShroomBotania
      },
      { # Misc Flowers
        nameKey: 'Misc Flower Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraFlowerMisc
      },
      { # Vanilla Sapling
        nameKey: 'Vanilla Sapling Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraSaplingVanilla
      },
      { # Modded Saplings
        nameKey: 'Modded Sapling Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraSaplingModded
      },
      { # Misc Flora
        nameKey: 'Misc Flora Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '0EABDA42EA87C46C',
        tasksKey: cqlist.floraMisc
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
        tasksKey: cqlist.mineralVanilla
      },
      { # Modded Blocks
        nameKey: 'Modded Blocks Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.01,
        tasksKey: cqlist.mineralModded
      },
      { # Ore
        nameKey: 'Ore Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.03,
        tasksKey: cqlist.mineralOre
      },
      {
        nameKey: 'Corundums Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.03,
        tasksKey: cqlist.mineralCorundum
      },
      { # Rare Gems
        nameKey: 'Rare Gems Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.15,
        tasksKey: cqlist.mineralGemRare
      },
      { # Common Gems
        nameKey: 'Common Gems Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '44DB551B93AA28F9',
        increaseRateKey: 0.07,
        tasksKey: cqlist.mineralGemCommon
      }
    ]
  },
  { # Common Decorations
    filenameKey: 'common_decorations',
    nameKey: 'Common Decorations',
    iconKey: 'moa_decor_art:martilloycincel',
    collectionNotificationKey: 'New Common Decoration Collected!',
    increaseRateKey: 0.06,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Handheld Instruments
        nameKey: 'Handheld Instruments Completion',
        iconKey: 'moa_decor_art:guitarra',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonHandheldInstruments
      },
      { # Trophies
        nameKey: 'Trophies Completion',
        iconKey: 'handcrafted:bear_trophy',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonTrophies
      },
      { # Snare
        nameKey: 'Snare Completion',
        iconKey: 'moa_decor_art:tamborrojo',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonSnare
      },
      { # Mariachi
        nameKey: 'Mariachi Completion',
        iconKey: 'moa_decor_holidays:mariachiguitarra',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonMariachi
      },
      { # Graveyard
        nameKey: 'Graveyard Completion',
        iconKey: 'moa_decor_holidays:lapida',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonGraveyard
      },
      { # Bathroom
        nameKey: 'Bathroom Completion',
        iconKey: 'moa_decor_bath:inodoro',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonBathroom
      },
      { # Arts
        nameKey: 'Arts Completion',
        iconKey: 'moa_decor_art:paletadepintura',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonArts
      },
      { # Film
        nameKey: 'Film Completion',
        iconKey: 'moa_decor_art:claqueta',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonFilm
      },
      { # Festive
        nameKey: 'Festive Completion',
        iconKey: 'moa_decor_holidays:corona_navidena',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonFestive
      },
      { # Books and Exploration
        nameKey: 'Books and Exploration Completion',
        iconKey: 'moa_decor_science:globoterraqueo',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonBooksExploration
      },
      { # Lab
        nameKey: 'Lab Completion',
        iconKey: 'moa_decor_science:microscopio',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonLab
      },
      { # Sheep Plushes
        nameKey: 'Sheep Plushes Completion',
        iconKey: 'moa_decor_toys:ovejarosa',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushSheep
      },
      { # Horse Plushes
        nameKey: 'Horse Plushes Completion',
        iconKey: 'moa_decor_toys:caballocafe',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushHorse
      },
      { # Home Animal Plushes
        nameKey: 'Home Animal Plushes Completion',
        iconKey: 'moa_decor_toys:gallina',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushHomeAnimal
      },
      { # Rabbit Plushes
        nameKey: 'Rabbit Plushes Completion',
        iconKey: 'moa_decor_toys:conejocastano',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushRabbit
      },
      { # Cat Plushes
        nameKey: 'Cat Plushes Completion',
        iconKey: 'moa_decor_toys:gatojellie',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushCat
      },
      { # Parrot Plushes
        nameKey: 'Parrot Plushes Completion',
        iconKey: 'moa_decor_toys:loroazul',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushParrot
      },
      { # Frog Plushes
        nameKey: 'Frog Plushes Completion',
        iconKey: 'moa_decor_toys:ranahelada',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushFrog
      },
      { # Llama Plushes
        nameKey: 'Llama Plushes Completion',
        iconKey: 'moa_decor_toys:llamagris',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushLlama
      },
      { # Wild Animal Plushes
        nameKey: 'Wild Animal Plushes Completion',
        iconKey: 'moa_decor_toys:zorro',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushWildAnimal
      },
      { # Axolotl Plushes
        nameKey: 'Axolotl Plushes Completion',
        iconKey: 'moa_decor_toys:ajoloterosa',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushAxolotl
      },
      { # Water Animal Plushes
        nameKey: 'Water Animal Plushes Completion',
        iconKey: 'moa_decor_toys:delfin',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushWaterAnimal
      },
      { # Village Plushes
        nameKey: 'Village Plushes Completion',
        iconKey: 'moa_decor_toys:aldeano',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushVillage
      },
      { # Nether Plushes
        nameKey: 'Nether Plushes Completion',
        iconKey: 'moa_decor_toys:blaze',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushNether
      },
      { # Zombie Plushes
        nameKey: 'Zombie Plushes Completion',
        iconKey: 'moa_decor_toys:zombie',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushZombie
      },
      { # Raid Plushes
        nameKey: 'Raid Plushes Completion',
        iconKey: 'moa_decor_toys:invocador',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushRaid
      },
      { # Hostile Plushes
        nameKey: 'Hostile Plushes Completion',
        iconKey: 'moa_decor_toys:creeper',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushHostileMob
      },
      { # Boss Plushes
        nameKey: 'Boss Plushes Completion',
        iconKey: 'moa_decor_toys:dragondelender',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonPlushBoss
      },
      { # Toys
        nameKey: 'Toys Completion',
        iconKey: 'playdate:rocking_horse',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.commonToy
      },
      { # Flower Shelf
        nameKey: 'Flower Shelf Completion',
        iconKey: 'luphieclutteredmod:yellow_flower_shelf',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonFlowerShelf
      },
      { # Bicycles
        nameKey: 'Bicycles Completion',
        iconKey: 'luphieclutteredmod:cute_yellow_bicycle',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonBicycles
      },
      { # Record Players
        nameKey: 'Record Players Completion',
        iconKey: 'luphieclutteredmod:luphie_brown_record_player',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonRecordPlayers
      },
      { # Fridges
        nameKey: 'Fridges Completion',
        iconKey: 'luphieclutteredmod:luphie_retro_black_fridge',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonFridges
      },
      { # Birdhouse
        nameKey: 'Birdhouse Completion',
        iconKey: 'luphieclutteredmod:unpainted_birdhouse',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonBirdhouse
      },
      { # Wall Decorations
        nameKey: 'Wall Decorations Completion',
        iconKey: 'luphieclutteredmod:luphie_polaroids_c',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonWallDecs
      },
      { # Lamps
        nameKey: 'Lamps Completion',
        iconKey: 'luphieclutteredmod:stainedglasslamp',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonLamps
      },
      { # Zelda
        nameKey: 'Zelda Completion',
        iconKey: 'luphieclutteredmod:red_sand_seal_plush',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonZelda
      },
      { # Rubiks Cube
        nameKey: 'Rubiks Cube Completion',
        iconKey: 'luphieclutteredmod:scrambled_pastel_rubiks_cube',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonRubiksCube
      },
      { # Sims
        nameKey: 'Sims Completion',
        iconKey: 'luphieclutteredmod:luphie_wedding_arch',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonSims
      },
      { # Starbound
        nameKey: 'Starbound Completion',
        iconKey: 'luphieclutteredmod:luphie_pastel_wardrobe',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonStarbound
      },
      { # Animal Crossing
        nameKey: 'Animal Crossing Completion',
        iconKey: 'luphieclutteredmod:luphie_apple_chair',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonAnimalCrossing
      },
      { # Overwatch
        nameKey: 'Overwatch Completion',
        iconKey: 'luphieclutteredmod:cluttered_purple_cabinet',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonOverwatch
      },
      { # Table and Desks
        nameKey: 'Table and Desks Completion',
        iconKey: 'luphieclutteredmod:luphie_imperial_table',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonTableAndDesks
      },
      { # Cluttered Mod Misc
        nameKey: 'Cluttered Mod Misc Completion',
        iconKey: 'luphieclutteredmod:luphie_polaroid_camera',
        dependencyIdKey: '7DA124C26F220448',
        tasksKey: cqlist.commonClutterModMisc
      }
    ]
  },
  { # Rare Decorations
    filenameKey: 'rare_decorations',
    nameKey: 'Rare Decorations',
    iconKey: 'moa_decor_art:premiooscar',
    collectionNotificationKey: 'New Rare Decoration Collected!',
    increaseRateKey: 0.1,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Statues
        nameKey: 'Statues Completion',
        iconKey: 'moa_decor_art:esculturaelpensador',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rareStatues
      },
      { # Mob Trophies
        nameKey: 'Mob Trophies Completion',
        iconKey: 'handcrafted:creeper_trophy',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rareMobTrophies
      },
      { # Paintings
        nameKey: 'Paintings Completion',
        iconKey: 'moa_decor_art:plamonalisa',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rarePaintings
      },
      { # Misc
        nameKey: 'Misc Completion',
        iconKey: 'moa_decor_art:maquinadediscos',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rareMisc
      },
      { # Oneul Food Music Disc
        nameKey: 'Oneul Food Music Discs Completion',
        iconKey: 'kubejs:oneul_melon_bread',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rareOneulFood
      },
      { # Oneul Pink Bear Music Disc
        nameKey: 'Oneul Pink Bear Music Disc Completion',
        iconKey: 'kubejs:oneul_around_midnight',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rareOneulPinkBear
      },
      { # Oneul Misc Music Disc
        nameKey: 'Oneul Misc Music Disc Completion',
        iconKey: 'kubejs:oneul_april_daisy',
        dependencyIdKey: '7DA124C26F220448', # buy first decoration
        tasksKey: cqlist.rareOneulMisc
      }
    ]
  },
  { # Hats
    filenameKey: 'hat_collection',
    nameKey: 'Hat Collection',
    iconKey: 'simplehats:haticon',
    collectionNotificationKey: 'New hat obtained!',
    increaseRateKey: 0.05,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Flat Hats
        nameKey: 'Flat Hats Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatFlat
      },
      { # Medium Hats
        nameKey: 'Medium Hats Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatMedium
      },
      { # Tall Hats
        nameKey: 'Tall Hats Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatTall
      },
      { # Face Overings
        nameKey: 'Face Overings Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatFaceCovering
      },
      { # Head Toppers
        nameKey: 'Head Toppers Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatHeadTopper
      },
      { # Disguise
        nameKey: 'Disguise Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatDisguise
      },
      { # Animal Hats
        nameKey: 'Animal Hats Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatAnimal
      },
      { # Eyewear
        nameKey: 'Eyewear Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatEyewear
      },
      { # Around the Head
        nameKey: 'Around the Head Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatAroundHead
      },
      { # Animated Details
        nameKey: 'Animated Details Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatAnimatedDetail
      },
      { # Accessories
        nameKey: 'Accessories Completion',
        iconKey: 'kubejs:miles_ticket',
        dependencyIdKey: '4D5EC74BAEAA9C3A', # Buy a hat
        tasksKey: cqlist.hatAccesories
      }
    ]
  },
  { # Clothing
    filenameKey: 'clothing_collection',
    nameKey: 'Clothing Collection',
    iconKey: 'cosmeticarmoursmod:royal_tunic_light_blue_chestplate',
    collectionNotificationKey: 'New clothing item obtained!',
    increaseRateKey: 0.06,
    typeKey: itemQuestTypeConst,
    questGroupsKey: [
      { # Royal Outfit
        nameKey: 'Royal Outfit Completion',
        iconKey: 'cosmeticarmoursmod:royal_tunic_light_blue_chestplate',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmRoyalOutfit
      },
      { # Steampunkers
        nameKey: 'Steampunkers Completion',
        iconKey: 'cosmeticarmoursmod:steampunkers_goggles_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmSteampunkers
      },
      { # Winter Survivalist
        nameKey: 'Winter Survivalist Completion',
        iconKey: 'cosmeticarmoursmod:brown_ushanka_hat_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmWinterSurvivalist
      },
      { # Astronaut
        nameKey: 'Astronaut Completion',
        iconKey: 'cosmeticarmoursmod:astronaut_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmAstronaut
      },
      { # Centurion
        nameKey: 'Centurion Completion',
        iconKey: 'cosmeticarmoursmod:centurions_helmet_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmCenturion
      },
      { # Farmer
        nameKey: 'Farmer Completion',
        iconKey: 'cosmeticarmoursmod:straw_hat_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmFarmer
      },
      { # Fisherman
        nameKey: 'Fisherman Completion',
        iconKey: 'cosmeticarmoursmod:fishermans_bucket_hat_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmFisherman
      },
      { # Ghillie Suit
        nameKey: 'Ghillie Suit Completion',
        iconKey: 'cosmeticarmoursmod:ghillie_suit_chestplate',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmGhillieSuit
      },
      { # Mobster
        nameKey: 'Mobster Completion',
        iconKey: 'cosmeticarmoursmod:mobster_chestplate',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmMobster
      },
      { # Beach Outfit
        nameKey: 'Beach Outfit Completion',
        iconKey: 'beachparty:beach_hat',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.outfitBeach
      },
      { # Chef Outfit
        nameKey: 'Chef Outfit Completion',
        iconKey: 'candlelight:cooking_hat',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.outfitChef
      },
      { # Fur Outfit
        nameKey: 'Fur Outfit Completion',
        iconKey: 'meadow:fur_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.outfitFur
      },
      { # Vinemaker's Outfit
        nameKey: "Vinemaker's Outfit Completion",
        iconKey: 'vinery:straw_hat',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.outfitVinemaker
      },
      { # Brewfest Outfit
        nameKey: 'Brewfest Outfit Completion',
        iconKey: 'brewery:brewfest_hat',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.outfitBrewfest
      },
      { # Tops
        nameKey: 'Tops Completion',
        iconKey: 'cosmeticarmoursmod:pink_skirt_chestplate',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmTops
      },
      { # Skirts and Boots
        nameKey: 'Skirts and Boots Completion',
        iconKey: 'cosmeticarmoursmod:orange_plaid_skirt_boots',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmSkirtBoots
      },
      { # Thigh High Socks
        nameKey: 'Thigh High Socks Completion',
        iconKey: 'cosmeticarmoursmod:orange_plaid_skirt_leggings',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmThighHighSocks
      },
      { # Knight Armor
        nameKey: 'Knight Armor Completion',
        iconKey: 'cosmeticarmoursmod:red_knight_helmet_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmKnightArmors
      },
      { # Archer
        nameKey: 'Archer Completion',
        iconKey: 'cosmeticarmoursmod:red_archers_attire_chestplate',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmArchersAttire
      },
      { # Christmas
        nameKey: 'Christmas Completion',
        iconKey: 'cosmeticarmoursmod:santa_hat_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmChristmas
      },
      { # Christmas Elves
        nameKey: 'Christmas Elves Completion',
        iconKey: 'cosmeticarmoursmod:christmas_elf_hat_green_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmElves
      },
      { # Crowns
        nameKey: 'Crowns Completion',
        iconKey: 'cosmeticarmoursmod:crown_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmCrowns
      },
      { # Cat Ears
        nameKey: 'Cat Ears Completion',
        iconKey: 'cosmeticarmoursmod:cat_ears_white_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmCatEars
      },
      { # Masks
        nameKey: 'Masks Completion',
        iconKey: 'cosmeticarmoursmod:axolotl_mask_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmMasks
      },
      { # Halo
        nameKey: 'Halo Completion',
        iconKey: 'cosmeticarmoursmod:gold_halo_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmHalos
      },
      { # Bunny Outfit
        nameKey: 'Bunny Outfit Completion',
        iconKey: 'cosmeticarmoursmod:bunny_ears_white_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmBunny
      },
      { # Misc Hats
        nameKey: 'Misc Hats Completion',
        iconKey: 'cosmeticarmoursmod:frankenstein_bolts_helmet',
        dependencyIdKey: '3EEF31508FB57A05', # Buy a cloths
        tasksKey: cqlist.cosmMiscHats
      }
    ]
  }
]