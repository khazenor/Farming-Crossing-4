const dungeonChestLoots = [
  'minecraft:chests/abandoned_mineshaft',
  'minecraft:chests/ancient_city',
  'minecraft:chests/ancient_city_ice_box',
  'minecraft:chests/bastion_bridge',
  'minecraft:chests/bastion_hoglin_stable',
  'minecraft:chests/bastion_other',
  'minecraft:chests/bastion_treasure',
  'minecraft:chests/buried_treasure',
  'minecraft:chests/desert_pyramid',
  'minecraft:chests/end_city_treasure',
  'minecraft:chests/igloo_chest',
  'minecraft:chests/jungle_temple',
  'minecraft:chests/jungle_temple_dispenser',
  'minecraft:chests/nether_bridge',
  'minecraft:chests/pillager_outpost',
  'minecraft:chests/ruined_portal',
  'minecraft:chests/shipwreck_map',
  'minecraft:chests/shipwreck_supply',
  'minecraft:chests/shipwreck_treasure',
  'minecraft:chests/simple_dungeon',
  'minecraft:chests/spawn_bonus_chest',
  'minecraft:chests/stronghold_corridor',
  'minecraft:chests/stronghold_crossing',
  'minecraft:chests/stronghold_library',
  'minecraft:chests/underwater_ruin_big',
  'minecraft:chests/underwater_ruin_small',
  'minecraft:chests/woodland_mansion'
]

const villageChestLoots = [
  'minecraft:chests/village/village_armorer',
  'minecraft:chests/village/village_butcher',
  'minecraft:chests/village/village_cartographer',
  'minecraft:chests/village/village_desert_house',
  'minecraft:chests/village/village_fisher',
  'minecraft:chests/village/village_fletcher',
  'minecraft:chests/village/village_mason',
  'minecraft:chests/village/village_plains_house',
  'minecraft:chests/village/village_savanna_house',
  'minecraft:chests/village/village_shepherd',
  'minecraft:chests/village/village_snowy_house',
  'minecraft:chests/village/village_taiga_house',
  'minecraft:chests/village/village_tannery',
  'minecraft:chests/village/village_temple',
  'minecraft:chests/village/village_toolsmith',
  'minecraft:chests/village/village_weaponsmith'
]

const summonDungeonItemId = 'kubejs:spawn_lootr_dungeon_chest'
const summonVillageItemId = 'kubejs:spawn_lootr_village_chest'

ItemEvents.rightClicked(summonDungeonItemId, event => {
  spawnChest(event, dungeonChestLoots)
})
ItemEvents.rightClicked(summonVillageItemId, event => {
  spawnChest(event, villageChestLoots)
})

const spawnChest = (itemEvent, lootTable) => {
  itemEvent.server.runCommand(
    `execute at @p run lootr chest ${randomElm(lootTable)}`
  )
  itemEvent.item.count--
}

const randomElm = (arr) => (arr[Math.floor(Math.random() * arr.length)])
