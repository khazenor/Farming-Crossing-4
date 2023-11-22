ItemEvents.tooltip(event => {
  event.add(
    [
      "aquaculture:iron_hook",
      "aquaculture:gold_hook",
      "aquaculture:diamond_hook",
      "aquaculture:light_hook",
      "aquaculture:heavy_hook",
      "aquaculture:double_hook",
      "aquaculture:redstone_hook",
      "aquaculture:note_hook",
      "aquaculture:nether_star_hook",
      "refinedstorage:crafting_grid",
      "refinedstorage:1k_storage_disk",
      "refinedstorage:4k_storage_disk",
      "refinedstorage:16k_storage_disk",
      "refinedstorage:64k_storage_disk",
      "immersive_aircraft:airship",
      "immersive_aircraft:cargo_airship",
      "immersive_aircraft:biplane",
      "immersive_aircraft:gyrodyne",
      "immersive_aircraft:quadrocopter"
    ],
    [
      "Unlock the crafting recipe for this item",
      "by completing quests in the quest book."
    ])
  
  event.add([
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
  ], [
    "You can reroll this villager spawn egg by",
    "putting two of these eggs in the crafting table"
  ])

  event.add([
    'gemsnjewels:dusk_emerald',
    'gemsnjewels:opal',
    'gemsnjewels:pale_diamond',
    'gemsnjewels:ruby',
    'gemsnjewels:sable_amethyst',
    'gemsnjewels:sapphire'
  ], [
    '', "Laly will buy this gem at a higher rate."
  ])

  event.add([
    'aquaculture:catfish',
    'aquaculture:capitaine',
    'aquaculture:tuna',
    'aquaculture:arrau_turtle',
    'aquaculture:starshell_turtle'
  ], [
    '', 'Sam will buy this fish at a higher rate.'
  ])
})