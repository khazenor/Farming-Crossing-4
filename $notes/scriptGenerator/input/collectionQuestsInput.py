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
additionalRewardsKey = 'additionalRewards'

startingQuestlineIdx = 2
questlines = [
  { # Cooking collection
    filenameKey: 'cooking_collection_2',
    nameKey: 'Cooking Collection',
    iconKey: 'bakery:strawberry_cupcake',
    collectionNotificationKey: 'New dish cooked!',
    increaseRateKey: 0.04,
    questGroupsKey: [
      ## Lets Do Foods
      { # Oven
        nameKey: 'Oven Recipes Completion',
        iconKey: 'bakery:brick_stove',
        dependencyIdKey: '57BAA8B414FF1F4F', # seed
        typeKey: itemQuestTypeConst,
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
        typeKey: itemQuestTypeConst,
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
        typeKey: itemQuestTypeConst,
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
        typeKey: itemQuestTypeConst,
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
        typeKey: itemQuestTypeConst,
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
  }
  # { # Flora collection
  #   filenameKey: 'flora_compendium',
  #   nameKey: 'Flora Compendium',
  #   iconKey: 'meadow:alpine_poppy',
  #   questGroupsKey: [
  #     { # Vanilla Foods
  #       nameKey: 'Vanilla Foods',
  #       iconKey: 'minecraft:apple',
  #       dependencyIdKey: '0EABDA42EA87C46C',
  #       tasksKey: [
  #         "minecraft:apple",
  #         "minecraft:bamboo",
  #         "minecraft:beetroot_seeds",
  #         "minecraft:brown_mushroom",
  #         "minecraft:cactus",
  #         "minecraft:carrot",
  #         "minecraft:cocoa_beans",
  #         "minecraft:glow_berries",
  #         "minecraft:kelp",
  #         "minecraft:melon_slice",
  #         "minecraft:potato",
  #         "minecraft:pumpkin_seeds",
  #         "minecraft:pumpkin",
  #         "minecraft:red_mushroom",
  #         "minecraft:sugar_cane",
  #         "minecraft:sweet_berries",
  #         "minecraft:torchflower_seeds",
  #         "minecraft:wheat_seeds"
  #       ]
  #     },
  #     { # Misc Foods
  #       nameKey: 'Misc Foods',
  #       iconKey: 'alexsmobs:banana',
  #       dependencyIdKey: '0EABDA42EA87C46C',
  #       tasksKey: [
  #         "alexsmobs:banana",
  #         "bakery:oat_seeds",
  #         "bakery:strawberry_seeds",
  #         "beachparty:coconut",
  #         "candlelight:lettuce_seeds",
  #         "candlelight:tomato_seeds",
  #         "delightful:cantaloupe_slice",
  #         "delightful:salmonberries",
  #         "farmersdelight:cabbage_seeds",
  #         "farmersdelight:onion",
  #         "farmersdelight:rice",
  #         "farmersdelight:tomato_seeds",
  #         "supplementaries:flax_seeds",
  #         "vinery:jungle_grape_seeds_red",
  #         "vinery:jungle_grape_seeds_white",
  #         "vinery:red_grape_seeds",
  #         "vinery:savanna_grape_seeds_red",
  #         "vinery:savanna_grape_seeds_white",
  #         "vinery:taiga_grape_seeds_red",
  #         "vinery:taiga_grape_seeds_white",
  #         "vinery:white_grape_seeds"
  #       ]
  #     }
  #   ]
  # }
]