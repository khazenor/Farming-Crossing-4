fcCategoryKey = 'fc'
floraCategoryKey = 'flora'
farmCategoryKey = 'farm'
miningCategoryKey = 'mining'

nameKey = 'name'
iconKey = 'icon'
entryGroupsKey = 'entryGroups'
itemsKey = 'items'
priceKey = 'price'
priceItemKey = 'priceItem'
productNumKey = 'productNum'
nbtKey = 'nbt'

categories = {
  fcCategoryKey: {
    nameKey: "Farming Crossing Shop",
    iconKey: "lootbags:loot_bag",
    entryGroupsKey: [
      {
        priceKey: 16,
        itemsKey: ["minecraft:villager_spawn_egg"]
      }, {
        priceKey: 32,
        itemsKey: ["minecraft:wandering_trader_spawn_egg"]
      }, {
        priceKey: 8,
        itemsKey: ["minecraft:bundle"]
      }, {
        priceKey: 4,
        itemsKey: ["minecraft:white_bed"]
      }, { # furniture
        priceKey: 8,
        itemsKey: ["lootbags:loot_bag"],
        nbtKey: {
          "Color": 13882323,
          "Loot":"lootbags:furniture/loot_furniture",
          "Name":"Furniture Kit",
          "Type":"COMMON"
        }
      }, { # Neighborly
        priceKey: 16,
        itemsKey: ["lootbags:loot_bag"],
        nbtKey: {
          "Type": "RARE",
          "Loot": "lootbags:furniture/loot_neighborly",
          "Color": 13882323,
          "Name": "Neighborly Villager Move In Kit"
        }
      }, { # Storage
        priceKey: 16,
        productNumKey: 2,
        itemsKey: ["kubejs:1k_storage_disk_ticket"]
      }, {
        priceKey: 72,
        productNumKey: 2,
        itemsKey: ["kubejs:4k_storage_disk_ticket"]
      }, {
        priceKey: 297,
        productNumKey: 2,
        itemsKey: ["kubejs:16k_storage_disk_ticket"]
      }, {
        priceKey: 1215,
        productNumKey: 2,
        itemsKey: ["kubejs:64k_storage_disk_ticket"]
      }, { # storage items
        priceKey: 32,
        itemsKey: [
          "refinedstorage:disk_drive",
          "refinedstorage:crafting_grid",
          "refinedstorage:controller",
          "createaddition:alternator"
        ]
      }, { # handcrafted
        productNumKey: 2,
        itemsKey: [
          "handcrafted:black_sheet",
          "handcrafted:blue_sheet",
          "handcrafted:brown_sheet",
          "handcrafted:cyan_sheet",
          "handcrafted:gray_sheet",
          "handcrafted:green_sheet",
          "handcrafted:light_blue_sheet",
          "handcrafted:light_gray_sheet",
          "handcrafted:lime_sheet",
          "handcrafted:magenta_sheet",
          "handcrafted:orange_sheet",
          "handcrafted:pink_sheet",
          "handcrafted:purple_sheet",
          "handcrafted:red_sheet",
          "handcrafted:white_sheet",
          "handcrafted:yellow_sheet",
          "handcrafted:black_cushion",
          "handcrafted:blue_cushion",
          "handcrafted:brown_cushion",
          "handcrafted:cyan_cushion",
          "handcrafted:gray_cushion",
          "handcrafted:green_cushion",
          "handcrafted:light_blue_cushion",
          "handcrafted:light_gray_cushion",
          "handcrafted:lime_cushion",
          "handcrafted:magenta_cushion",
          "handcrafted:orange_cushion",
          "handcrafted:pink_cushion",
          "handcrafted:purple_cushion",
          "handcrafted:red_cushion",
          "handcrafted:white_cushion",
          "handcrafted:yellow_cushion" 
        ]
      }
    ]
  },
  floraCategoryKey: {
    nameKey: "Garden Stand",
    iconKey: "minecraft:poppy",
    entryGroupsKey: [
      {
        priceKey: 8,
        itemsKey: ["minecraft:chorus_fruit"]
      }, { # dyes
        priceKey: 4,
        productNumKey: 8,
        itemsKey: [
          "minecraft:black_dye",
          "minecraft:blue_dye",
          "minecraft:brown_dye",
          "minecraft:cyan_dye",
          "minecraft:gray_dye",
          "minecraft:green_dye",
          "minecraft:light_blue_dye",
          "minecraft:light_gray_dye",
          "minecraft:lime_dye",
          "minecraft:magenta_dye",
          "minecraft:orange_dye",
          "minecraft:pink_dye",
          "minecraft:purple_dye",
          "minecraft:red_dye",
          "minecraft:white_dye",
          "minecraft:yellow_dye"
        ]
      }, { # seeds
        priceKey: 32,
        productNumKey: 4,
        itemsKey: [
          "minecraft:beetroot_seeds",
          "minecraft:melon_seeds",
          "minecraft:pumpkin_seeds",
          "minecraft:wheat_seeds",
          "minecraft:carrot",
          "minecraft:potato",
          "minecraft:sugar_cane",
          "minecraft:sweet_berries",
          "minecraft:brown_mushroom",
          "minecraft:red_mushroom",
          "minecraft:crimson_fungus",
          "minecraft:warped_fungus",
          "minecraft:cactus",
          "minecraft:kelp",
          "minecraft:glow_berries",
          "bakery:oat_seeds",
          "bakery:strawberry_seeds",
          "candlelight:lettuce_seeds",
          "candlelight:tomato_seeds",
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
      }, { # saplings
        priceKey: 32,
        productNumKey: 2,
        itemsKey: [
          "beachparty:palm_sapling",
          "biomesoplenty:dead_sapling",
          "biomesoplenty:fir_sapling",
          "biomesoplenty:flowering_oak_sapling",
          "biomesoplenty:hellbark_sapling",
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
          "biomesoplenty:umbran_sapling",
          "biomesoplenty:willow_sapling",
          "biomesoplenty:yellow_autumn_sapling",
          "meadow:pine_sapling",
          "minecraft:acacia_sapling",
          "minecraft:birch_sapling",
          "minecraft:cherry_sapling",
          "minecraft:dark_oak_sapling",
          "minecraft:jungle_sapling",
          "minecraft:oak_sapling",
          "minecraft:spruce_sapling",
          "vinery:apple_tree_sapling",
          "vinery:cherry_sapling"
        ]
      }, { # flowers
        priceKey: 32,
        productNumKey: 4,
        itemsKey: [
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
          "minecraft:sunflower",
          "minecraft:white_tulip",
          "minecraft:rose_bush",
          "biomesoplenty:rose",
          "biomesoplenty:violet",
          "biomesoplenty:lavender",
          "biomesoplenty:tall_lavender",
          "biomesoplenty:blue_hydrangea",
          "biomesoplenty:wildflower",
          "biomesoplenty:goldenrod",
          "biomesoplenty:orange_cosmos",
          "biomesoplenty:pink_daffodil",
          "biomesoplenty:pink_hibiscus",
          "biomesoplenty:waterlily",
          "biomesoplenty:white_petals",
          "biomesoplenty:icy_iris",
          "biomesoplenty:glowflower",
          "biomesoplenty:wilted_lily",
          "biomesoplenty:burning_blossom",
          "biomesoplenty:cattail",
          "meadow:enzian",
          "meadow:fire_lily",
          "meadow:eriophorum",
          "meadow:eriophorum_tall",
          "meadow:alpine_poppy",
          "meadow:delphinium",
          "meadow:saxifrage"

        ]
      }
    ]
  },
  farmCategoryKey: {
    nameKey: "Animal Range",
    iconKey: "minecraft:leather",
    entryGroupsKey: [
      {
        priceKey: 32,
        itemsKey: [
          "create:blaze_burner",
          "alexsmobs:pupfish_locator",
          "alexsmobs:unsettling_kimono",
          "alexsmobs:squid_grapple",
          "alexsmobs:straddleboard"
        ]
      }, { # meats
        priceKey: 2,
        productNumKey: 8,
        itemsKey: [
          "minecraft:beef",
          "minecraft:chicken",
          "minecraft:cod",
          "minecraft:mutton",
          "minecraft:porkchop",
          "minecraft:rabbit",
          "minecraft:salmon",
          "alexsmobs:kangaroo_meat",
          "alexsmobs:moose_ribs",
          "alexsmobs:raw_catfish",
          "alexsmobs:lobster_tail",
          "alexsmobs:maggot",
          "alexsmobs:centipede_leg",
          "beachparty:raw_mussel_meat",
          "meadow:raw_bear_meat",
          "exoticbirds:raw_birdmeat",
          "alexsmobs:raw_catfish",
          "aquaculture:fish_fillet_raw",
          "beachparty:raw_pelican"
        ]
      }, {
        productNumKey: 4,
        itemsKey: ["minecraft:arrow"]
      }, {
        priceKey: 2,
        itemsKey: [
          "minecraft:feather",
          "minecraft:string"
        ]
      }, {
        priceKey: 4,
        itemsKey: [
          "minecraft:rotten_flesh",
          "minecraft:leather",
          "minecraft:rabbit_hide",
          "alexsmobs:kangaroo_hide",
          "minecraft:bone",
          "minecraft:slime_ball",
          "minecraft:bow"
        ]
      }, {
        priceKey: 8,
        itemsKey: [
          "minecraft:spider_eye",
          "minecraft:gunpowder",
          "minecraft:prismarine_shard",
          "minecraft:prismarine_crystals"
        ]
      }, {
        priceKey: 24,
        itemsKey: [
          "minecraft:ender_pearl",
          "minecraft:blaze_rod"
        ]
      }, { # alexmobs items
        itemsKey: [
          "alexsmobs:fish_bones",
          "alexsmobs:ambergris",
          "alexsmobs:cachalot_whale_tooth",
          "alexsmobs:tarantula_hawk_wing_fragment"
        ]
      }, {
        priceKey: 16,
        itemsKey: ["alexsmobs:skreecher_soul"]
      }, {
        priceKey: 4,
        itemsKey: ["alexsmobs:bone_serpent_tooth"]
      }, { # spawn eggs
        priceKey: 64,
        productNumKey: 1,
        itemsKey: [
          "alexsmobs:spawn_egg_alligator_snapping_turtle",
          "alexsmobs:spawn_egg_anaconda",
          "alexsmobs:spawn_egg_anteater",
          "alexsmobs:spawn_egg_bald_eagle",
          "alexsmobs:spawn_egg_banana_slug",
          "alexsmobs:spawn_egg_bison",
          "alexsmobs:spawn_egg_blobfish",
          "alexsmobs:spawn_egg_blue_jay",
          "alexsmobs:spawn_egg_bone_serpent",
          "alexsmobs:spawn_egg_bunfungus",
          "alexsmobs:spawn_egg_cachalot_whale",
          "alexsmobs:spawn_egg_caiman",
          "alexsmobs:spawn_egg_capuchin_monkey",
          "alexsmobs:spawn_egg_catfish",
          "alexsmobs:spawn_egg_centipede",
          "alexsmobs:spawn_egg_cockroach",
          "alexsmobs:spawn_egg_comb_jelly",
          "alexsmobs:spawn_egg_cosmaw",
          "alexsmobs:spawn_egg_cosmic_cod",
          "alexsmobs:spawn_egg_crimson_mosquito",
          "alexsmobs:spawn_egg_crocodile",
          "alexsmobs:spawn_egg_crow",
          "alexsmobs:spawn_egg_devils_hole_pupfish",
          "alexsmobs:spawn_egg_dropbear",
          "alexsmobs:spawn_egg_elephant",
          "alexsmobs:spawn_egg_emu",
          "alexsmobs:spawn_egg_endergrade",
          "alexsmobs:spawn_egg_enderiophage",
          "alexsmobs:spawn_egg_farseer",
          "alexsmobs:spawn_egg_flutter",
          "alexsmobs:spawn_egg_fly",
          "alexsmobs:spawn_egg_flying_fish",
          "alexsmobs:spawn_egg_frilled_shark",
          "alexsmobs:spawn_egg_froststalker",
          "alexsmobs:spawn_egg_gazelle",
          "alexsmobs:spawn_egg_gelada_monkey",
          "alexsmobs:spawn_egg_giant_squid",
          "alexsmobs:spawn_egg_gorilla",
          "alexsmobs:spawn_egg_grizzly_bear",
          "alexsmobs:spawn_egg_guster",
          "alexsmobs:spawn_egg_hammerhead_shark",
          "alexsmobs:spawn_egg_hummingbird",
          "alexsmobs:spawn_egg_jerboa",
          "alexsmobs:spawn_egg_kangaroo",
          "alexsmobs:spawn_egg_komodo_dragon",
          "alexsmobs:spawn_egg_laviathan",
          "alexsmobs:spawn_egg_leafcutter_ant",
          "alexsmobs:spawn_egg_lobster",
          "alexsmobs:spawn_egg_maned_wolf",
          "alexsmobs:spawn_egg_mantis_shrimp",
          "alexsmobs:spawn_egg_mimic_octopus",
          "alexsmobs:spawn_egg_mimicube",
          "alexsmobs:spawn_egg_moose",
          "alexsmobs:spawn_egg_mudskipper",
          "alexsmobs:spawn_egg_mungus",
          "alexsmobs:spawn_egg_murmur",
          "alexsmobs:spawn_egg_orca",
          "alexsmobs:spawn_egg_platypus",
          "alexsmobs:spawn_egg_potoo",
          "alexsmobs:spawn_egg_raccoon",
          "alexsmobs:spawn_egg_rain_frog",
          "alexsmobs:spawn_egg_rattlesnake",
          "alexsmobs:spawn_egg_rhinoceros",
          "alexsmobs:spawn_egg_roadrunner",
          "alexsmobs:spawn_egg_rocky_roller",
          "alexsmobs:spawn_egg_seagull",
          "alexsmobs:spawn_egg_seal",
          "alexsmobs:spawn_egg_shoebill",
          "alexsmobs:spawn_egg_skelewag",
          "alexsmobs:spawn_egg_skreecher",
          "alexsmobs:spawn_egg_skunk",
          "alexsmobs:spawn_egg_snow_leopard",
          "alexsmobs:spawn_egg_soul_vulture",
          "alexsmobs:spawn_egg_spectre",
          "alexsmobs:spawn_egg_straddler",
          "alexsmobs:spawn_egg_stradpole",
          "alexsmobs:spawn_egg_sugar_glider",
          "alexsmobs:spawn_egg_sunbird",
          "alexsmobs:spawn_egg_tarantula_hawk",
          "alexsmobs:spawn_egg_tasmanian_devil",
          "alexsmobs:spawn_egg_terrapin",
          "alexsmobs:spawn_egg_tiger",
          "alexsmobs:spawn_egg_toucan",
          "alexsmobs:spawn_egg_triops",
          "alexsmobs:spawn_egg_tusklin",
          "alexsmobs:spawn_egg_underminer",
          "alexsmobs:spawn_egg_void_worm",
          "alexsmobs:spawn_egg_warped_mosco",
          "alexsmobs:spawn_egg_warped_toad",
          "aquaculture:arrau_turtle_spawn_egg",
          "aquaculture:box_turtle_spawn_egg",
          "aquaculture:starshell_turtle_spawn_egg",
          "artifacts:mimic_spawn_egg",
          "bakery:wandering_baker_spawn_egg",
          "beachparty:pelican_spawn_egg",
          "meadow:brown_bear_spawn_egg",
          "meadow:water_buffalo_spawn_egg",
          "meadow:wooly_cow_spawn_egg",
          "minecraft:allay_spawn_egg",
          "minecraft:axolotl_spawn_egg",
          "minecraft:bat_spawn_egg",
          "minecraft:bee_spawn_egg",
          "minecraft:blaze_spawn_egg",
          "minecraft:camel_spawn_egg",
          "minecraft:cat_spawn_egg",
          "minecraft:cave_spider_spawn_egg",
          "minecraft:chicken_spawn_egg",
          "minecraft:cod_spawn_egg",
          "minecraft:cow_spawn_egg",
          "minecraft:creeper_spawn_egg",
          "minecraft:dolphin_spawn_egg",
          "minecraft:donkey_spawn_egg",
          "minecraft:drowned_spawn_egg",
          "minecraft:elder_guardian_spawn_egg",
          "minecraft:ender_dragon_spawn_egg",
          "minecraft:enderman_spawn_egg",
          "minecraft:endermite_spawn_egg",
          "minecraft:evoker_spawn_egg",
          "minecraft:fox_spawn_egg",
          "minecraft:frog_spawn_egg",
          "minecraft:ghast_spawn_egg",
          "minecraft:glow_squid_spawn_egg",
          "minecraft:goat_spawn_egg",
          "minecraft:guardian_spawn_egg",
          "minecraft:hoglin_spawn_egg",
          "minecraft:horse_spawn_egg",
          "minecraft:husk_spawn_egg",
          "minecraft:iron_golem_spawn_egg",
          "minecraft:llama_spawn_egg",
          "minecraft:magma_cube_spawn_egg",
          "minecraft:mooshroom_spawn_egg",
          "minecraft:mule_spawn_egg",
          "minecraft:ocelot_spawn_egg",
          "minecraft:panda_spawn_egg",
          "minecraft:parrot_spawn_egg",
          "minecraft:phantom_spawn_egg",
          "minecraft:pig_spawn_egg",
          "minecraft:piglin_brute_spawn_egg",
          "minecraft:piglin_spawn_egg",
          "minecraft:pillager_spawn_egg",
          "minecraft:polar_bear_spawn_egg",
          "minecraft:pufferfish_spawn_egg",
          "minecraft:rabbit_spawn_egg",
          "minecraft:ravager_spawn_egg",
          "minecraft:salmon_spawn_egg",
          "minecraft:sheep_spawn_egg",
          "minecraft:shulker_spawn_egg",
          "minecraft:silverfish_spawn_egg",
          "minecraft:skeleton_horse_spawn_egg",
          "minecraft:skeleton_spawn_egg",
          "minecraft:slime_spawn_egg",
          "minecraft:sniffer_spawn_egg",
          "minecraft:snow_golem_spawn_egg",
          "minecraft:spider_spawn_egg",
          "minecraft:squid_spawn_egg",
          "minecraft:stray_spawn_egg",
          "minecraft:strider_spawn_egg",
          "minecraft:tadpole_spawn_egg",
          "minecraft:trader_llama_spawn_egg",
          "minecraft:tropical_fish_spawn_egg",
          "minecraft:turtle_spawn_egg",
          "minecraft:vex_spawn_egg",
          "minecraft:villager_spawn_egg",
          "minecraft:vindicator_spawn_egg",
          "minecraft:wandering_trader_spawn_egg",
          "minecraft:witch_spawn_egg",
          "minecraft:wither_skeleton_spawn_egg",
          "minecraft:wolf_spawn_egg",
          "minecraft:zoglin_spawn_egg",
          "minecraft:zombie_horse_spawn_egg",
          "minecraft:zombie_spawn_egg",
          "minecraft:zombie_villager_spawn_egg",
          "minecraft:zombified_piglin_spawn_egg",
          "supplementaries:red_merchant_spawn_egg",
          "vinery:mule_spawn_egg",
          "vinery:wandering_winemaker_spawn_egg",
          "exoticbirds:bluejay_spawn_egg",
          "exoticbirds:booby_spawn_egg",
          "exoticbirds:budgerigar_spawn_egg",
          "exoticbirds:cardinal_spawn_egg",
          "exoticbirds:cassowary_spawn_egg",
          "exoticbirds:cockatoo_spawn_egg",
          "exoticbirds:crane_spawn_egg",
          "exoticbirds:duck_spawn_egg",
          "exoticbirds:flamingo_spawn_egg",
          "exoticbirds:gouldianfinch_spawn_egg",
          "exoticbirds:gull_spawn_egg",
          "exoticbirds:heron_spawn_egg",
          "exoticbirds:hummingbird_spawn_egg",
          "exoticbirds:kingfisher_spawn_egg",
          "exoticbirds:kiwi_spawn_egg",
          "exoticbirds:kookaburra_spawn_egg",
          "exoticbirds:lyrebird_spawn_egg",
          "exoticbirds:macaw_spawn_egg",
          "exoticbirds:magpie_spawn_egg",
          "exoticbirds:ostrich_spawn_egg",
          "exoticbirds:owl_spawn_egg",
          "exoticbirds:peafowl_spawn_egg",
          "exoticbirds:pelican_spawn_egg",
          "exoticbirds:penguin_spawn_egg",
          "exoticbirds:pigeon_spawn_egg",
          "exoticbirds:roadrunner_spawn_egg",
          "exoticbirds:robin_spawn_egg",
          "exoticbirds:swan_spawn_egg",
          "exoticbirds:toucan_spawn_egg",
          "exoticbirds:woodpecker_spawn_egg",
          "exoticbirds:cloud_phoenix_spawn_egg",
          "exoticbirds:desert_phoenix_spawn_egg",
          "exoticbirds:ender_phoenix_spawn_egg",
          "exoticbirds:fire_phoenix_spawn_egg",
          "exoticbirds:nether_phoenix_spawn_egg",
          "exoticbirds:skeleton_phoenix_spawn_egg",
          "exoticbirds:snowy_phoenix_spawn_egg",
          "exoticbirds:twilight_phoenix_spawn_egg",
          "exoticbirds:water_phoenix_spawn_egg"
        ]
      }
    ]
  },
  miningCategoryKey: {
    nameKey: "Mineral Museum",
    iconKey: "minecraft:glowstone_dust",
    entryGroupsKey: [
      {
        productNumKey: 4,
        itemsKey: [
          "minecraft:emerald",
          "create:experience_nugget"
        ]
      }, {
        priceKey: 4,
        itemsKey: ["minecraft:quartz"]
      }, {
        priceKey: 6,
        itemsKey: ["minecraft:glowstone_dust"]
      }, { # blocks
        priceKey: 32,
        itemsKey: [
          "minecraft:ice",
          "minecraft:blackstone"
        ]
      }
    ]
  }
}

enchantments = {
  "alexsmobs:board_return": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "alexsmobs:lavawax": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "alexsmobs:serpentfriend": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "alexsmobs:straddle_jump": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "create:capacity": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "create:potato_recovery": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:aqua_affinity": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:bane_of_arthropods": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:binding_curse": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:blast_protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:channeling": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:depth_strider": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:efficiency": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:feather_falling": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:fire_aspect": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:fire_protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:flame": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:fortune": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:frost_walker": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:impaling": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:infinity": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:knockback": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:looting": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:loyalty": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:luck_of_the_sea": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:lure": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:mending": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:multishot": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:piercing": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:power": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:projectile_protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:protection": {
    "maxLvCost": 32,
    "maxLv": 4
  },
  "minecraft:punch": {
    "maxLvCost": 32,
    "maxLv": 2
  },
  "minecraft:quick_charge": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:respiration": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:riptide": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:sharpness": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:silk_touch": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "minecraft:smite": {
    "maxLvCost": 32,
    "maxLv": 5
  },
  "minecraft:soul_speed": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:sweeping": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:swift_sneak": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:thorns": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:unbreaking": {
    "maxLvCost": 32,
    "maxLv": 3
  },
  "minecraft:vanishing_curse": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "supplementaries:stasis": {
    "maxLvCost": 32,
    "maxLv": 1
  },
  "utilitix:bell_range": {
    "maxLvCost": 32,
    "maxLv": 3
  }
}
