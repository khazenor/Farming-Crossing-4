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
})