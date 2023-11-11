ServerEvents.recipes(event => {
  event.remove({ output: 'villagersplus:acacia_horticulturist_table' })
  event.shapeless('villagersplus:acacia_horticulturist_table', [
    "minecraft:stripped_acacia_log",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:bamboo_horticulturist_table' })
  event.shapeless('villagersplus:bamboo_horticulturist_table', [
    "minecraft:bamboo_block",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:birch_horticulturist_table' })
  event.shapeless('villagersplus:birch_horticulturist_table', [
    "#minecraft:logs",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:cherry_horticulturist_table' })
  event.shapeless('villagersplus:cherry_horticulturist_table', [
    "minecraft:stripped_cherry_log",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:crimson_horticulturist_table' })
  event.shapeless('villagersplus:crimson_horticulturist_table', [
    "minecraft:stripped_crimson_stem",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:dark_oak_horticulturist_table' })
  event.shapeless('villagersplus:dark_oak_horticulturist_table', [
    "minecraft:stripped_dark_oak_log",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:jungle_horticulturist_table' })
  event.shapeless('villagersplus:jungle_horticulturist_table', [
    "minecraft:stripped_jungle_log",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:mangrove_horticulturist_table' })
  event.shapeless('villagersplus:mangrove_horticulturist_table', [
    "minecraft:stripped_mangrove_log",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:oak_horticulturist_table' })
  // event.shapeless('villagersplus:oak_horticulturist_table', [
  //   "minecraft:stripped_oak_log",
  //   'minecraft:paper'
  // ])
  event.remove({ output: 'villagersplus:spruce_horticulturist_table' })
  event.shapeless('villagersplus:spruce_horticulturist_table', [
    "minecraft:stripped_spruce_log",
    'minecraft:paper'
  ])
  event.remove({ output: 'villagersplus:warped_horticulturist_table' })
  event.shapeless('villagersplus:warped_horticulturist_table', [
    "minecraft:stripped_warped_stem",
    'minecraft:paper'
  ])
})