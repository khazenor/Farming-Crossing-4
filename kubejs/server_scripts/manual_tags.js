ServerEvents.tags('item', event => {
  event.add('forge:aqua_rods', [
    "aquaculture:diamond_fishing_rod",
    "aquaculture:gold_fishing_rod",
    "aquaculture:iron_fishing_rod",
    "aquaculture:neptunium_fishing_rod"
  ])

  event.add('forge:raw_fishes', 'aquaculture:fish_fillet_raw')
  event.add('forge:fishes', 'aquaculture:fish_fillet_raw')
  event.add('forge:cooked_fishes', 'aquaculture:fish_fillet_cooked')
  event.add('forge:fishes', 'aquaculture:fish_fillet_cooked')

  event.remove('artifacts:artifacts', ['artifacts:villager_hat'])

  event.add('forge:waystones_and_obsidian', [
    "waystones:mossy_waystone",
    "waystones:sandy_waystone",
    "waystones:waystone",
    "minecraft:obsidian"
  ])

  event.add('forge:water', [
    'minecraft:water_bucket',
    'meadow:wooden_water_bucket',
    'kubejs:fresh_water'
  ])
  event.add('meadow:water_bottles', 'kubejs:fresh_water')
  event.add('candlelight:water_bottles', 'kubejs:fresh_water')

  event.add('forge:customer_tables',[
    "villagersplus:acacia_horticulturist_table",
    "villagersplus:bamboo_horticulturist_table",
    "villagersplus:birch_horticulturist_table",
    "villagersplus:cherry_horticulturist_table",
    "villagersplus:crimson_horticulturist_table",
    "villagersplus:dark_oak_horticulturist_table",
    "villagersplus:jungle_horticulturist_table",
    "villagersplus:mangrove_horticulturist_table",
    "villagersplus:oak_horticulturist_table",
    "villagersplus:spruce_horticulturist_table",
    "villagersplus:warped_horticulturist_table"
  ])

  event.add('forge:minerals',[
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
    "minecraft:blackstone",
    "minecraft:smooth_basalt",
    "minecraft:tuff",
    "minecraft:obsidian",
    "minecraft:raw_copper",
    "minecraft:raw_gold",
    "minecraft:raw_iron",
    "minecraft:redstone",
    "minecraft:diamond",
    "create:crimsite",
    "create:asurine",
    "create:veridium",
    "create:ochrum",
    "create:scoria",
    "create:limestone",
    "create:scorchia",
    "create:raw_zinc",
    "minecraft:amethyst_shard",
    "meadow:mossy_cobbled_limestone",
    "meadow:cobbled_limestone",
    "biomesoplenty:white_sandstone",
    "biomesoplenty:orange_sandstone",
    "biomesoplenty:black_sandstone",
    "biomesoplenty:dried_salt"
  ])

  
  // event.add('forge:nutrients/vegetables', [
  // ])

  // event.add('forge:nutrients/proteins', [
  // ])

  event.add('forge:nutrients/fruits', [
    "vinery:jungle_grapes_red",
    "vinery:jungle_grapes_white",
    "vinery:savanna_grapes_red",
    "vinery:savanna_grapes_white",
    "vinery:taiga_grapes_red",
    "vinery:taiga_grapes_white",
    "vinery:cherry",
    "vinery:apple_juice",
    "vinery:jungle_red_grapejuice_bottle",
    "vinery:jungle_white_grapejuice_bottle",
    "vinery:red_grapejuice_wine_bottle",
    "vinery:savanna_red_grapejuice_bottle",
    "vinery:savanna_white_grapejuice_bottle",
    "vinery:taiga_red_grapejuice_bottle",
    "vinery:taiga_white_grapejuice_bottle",
    "vinery:white_grapejuice_wine_bottle"
  ])

  // event.add('forge:nutrients/sugars', [
  // ])

  event.add('forge:nutrients/carbs', [
    'bakery:oat',
    'bakery:dough',
    'bakery:sweet_dough',
    'candlelight:dough',
    'create:dough'
  ])

  event.add('forge:neighborly_spawn_eggs', [
    'neighborly:barrybear_spawn_egg',
    'neighborly:chloe_cat_spawn_egg',
    'neighborly:duckley_spawn_egg',
    'neighborly:duncan_spawn_egg',
    'neighborly:jammer_cat_spawn_egg',
    'neighborly:jasper_spawn_egg',
    'neighborly:roxy_imp_spawn_egg',
    'neighborly:sapphire_penguin_spawn_egg',
    'neighborly:shroomer_spawn_egg',
    'neighborly:sigma_spawn_egg',
    'neighborly:sparkle_spawn_egg',
    'neighborly:thompson_frog_spawn_egg'
  ])
})