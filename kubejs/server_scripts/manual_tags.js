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
})