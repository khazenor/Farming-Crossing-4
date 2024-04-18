let woodTypes = [
  'beachparty:palm',
  'biomesoplenty:dead',
  'biomesoplenty:fir',
  'biomesoplenty:hellbark',
  'biomesoplenty:jacaranda',
  'biomesoplenty:magic',
  'biomesoplenty:mahogany',
  'biomesoplenty:palm',
  'biomesoplenty:redwood',
  'biomesoplenty:umbran',
  'biomesoplenty:willow',
  'bloomingnature:aspen',
  'bloomingnature:baobab',
  'bloomingnature:chestnut',
  'bloomingnature:ebony',
  'bloomingnature:fir',
  'bloomingnature:larch',
  'bloomingnature:palm',
  'bloomingnature:swamp_cypress',
  'bloomingnature:swamp_oak',
  'botania:dreamwood',
  'botania:livingwood',
  'luphieclutteredmod:luphie_flowering_pink',
  'luphieclutteredmod:luphie_flowering_purple',
  'luphieclutteredmod:luphie_flowering_yellow',
  'luphieclutteredmod:luphie_glow',
  'luphieclutteredmod:luphie_green',
  'luphieclutteredmod:luphie_pink',
  'luphieclutteredmod:luphie_purple',
  'luphieclutteredmod:luphie_yellow',
  'meadow:alpine_birch',
  'meadow:alpine_oak',
  'meadow:pine',
  'quark:ancient',
  'quark:azalea',
  'quark:blossom',
  'vinery:apple',
  'vinery:cherry'
]
ServerEvents.recipes(event => {
  for (let woodType of woodTypes) {
    let split = woodType.split(':')
    let modName = split[0]
    let woodName = split[1]

    let log = woodType + "_log"
    let strippedLog = `${modName}:stripped_${woodName}_log`

    let wood = woodType + "_wood"
    let strippedWood = `${modName}:stripped_${woodName}_wood`

    event.custom({
      "type": "farmersdelight:cutting",
      "ingredients": [
        {
          "item": log
        }
      ],
      "result": [
        {
          "item": strippedLog
        },
        {
          "item": "farmersdelight:tree_bark"
        }
      ],
      "sound": "minecraft:item.axe.strip",
      "tool": {
        "type": "farmersdelight:tool_action",
        "action": "axe_strip"
      }
    })
    
    event.custom({
      "type": "farmersdelight:cutting",
      "ingredients": [
        {
          "item": wood
        }
      ],
      "result": [
        {
          "item": strippedWood
        },
        {
          "item": "farmersdelight:tree_bark"
        }
      ],
      "sound": "minecraft:item.axe.strip",
      "tool": {
        "type": "farmersdelight:tool_action",
        "action": "axe_strip"
      }
    })
  }
})