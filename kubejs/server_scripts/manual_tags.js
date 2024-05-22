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
    'meadow:wooden_water_bucket'
  ])
  event.add('meadow:water_bottles', 'pamhc2foodcore:freshwateritem')
  event.add('candlelight:water_bottles', 'pamhc2foodcore:freshwateritem')
  
  event.add('diet:vegetables', [
    'candlelight:tomato',
    'candlelight:lettuce'
  ])

  // event.add('diet:proteins', [
  // ])

  event.add('diet:fruits', [
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

  // event.add('diet:sugars', [
  // ])

  event.add('diet:grains', [
    'bakery:oat',
    'bakery:dough',
    'bakery:sweet_dough',
    'candlelight:dough',
    'create:dough',
    'bakery:blank_cake'
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

  event.add('forge:tea_leaves/green', [
    'herbalbrews:green_tea_leaf',
    'pamhc2crops:tealeafitem'
  ])

  event.add('forge:egg', [
    'exoticbirds:bluejay_egg',
    'exoticbirds:booby_egg',
    'exoticbirds:budgerigar_egg',
    'exoticbirds:cardinal_egg',
    'exoticbirds:cassowary_egg',
    'exoticbirds:cloud_phoenix_egg',
    'exoticbirds:cockatoo_egg',
    'exoticbirds:crane_egg',
    'exoticbirds:desert_phoenix_egg',
    'exoticbirds:duck_egg',
    'exoticbirds:ender_phoenix_egg',
    'exoticbirds:fire_phoenix_egg',
    'exoticbirds:flamingo_egg',
    'exoticbirds:gouldianfinch_egg',
    'exoticbirds:gull_egg',
    'exoticbirds:heron_egg',
    'exoticbirds:hummingbird_egg',
    'exoticbirds:kingfisher_egg',
    'exoticbirds:kiwi_egg',
    'exoticbirds:kookaburra_egg',
    'exoticbirds:lyrebird_egg',
    'exoticbirds:macaw_egg',
    'exoticbirds:magpie_egg',
    'exoticbirds:mystery_egg',
    'exoticbirds:nether_phoenix_egg',
    'exoticbirds:ostrich_egg',
    'exoticbirds:owl_egg',
    'exoticbirds:peafowl_egg',
    'exoticbirds:pelican_egg',
    'exoticbirds:penguin_egg',
    'exoticbirds:phoenix_egg',
    'exoticbirds:pigeon_egg',
    'exoticbirds:roadrunner_egg',
    'exoticbirds:robin_egg',
    'exoticbirds:skeleton_phoenix_egg',
    'exoticbirds:snowy_phoenix_egg',
    'exoticbirds:swan_egg',
    'exoticbirds:toucan_egg',
    'exoticbirds:twilight_phoenix_egg',
    'exoticbirds:water_phoenix_egg',
    'exoticbirds:woodpecker_egg'
  ])
})