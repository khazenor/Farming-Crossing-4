

StartupEvents.registry("block", (event) => {
  const blockNames = [
    "Elna's Shop",
    "Bernina's Shop",
    "Bakery Customer Table",
    "Drink Customer Table",
    "Candlelight Customer Table",
    "Beach Customer Table",
    "Farmer's Delight Customer Table"
  ]
  
  const stringToName = (name) => {
    return name.replace(/'/g, "").replace(/ /g, '_').toLowerCase()
  }

  for (let blockName of blockNames) {
    console.log(blockName, stringToName(blockName))
    event.create(stringToName(blockName), "cardinal")
      .displayName(blockName)
      .material("wood") // Set a material (affects the sounds and some properties)
      .hardness(1.0) // Set hardness (affects mining time)
      .tagBlock("mineable/axe") //can be mined faster with an axe
      .modelJson = {
        "parent": "minecraft:block/cube",
        "textures": {
          "down": "kubejs:block/bottom",
          "east": "kubejs:block/side",
          "north": "kubejs:block/side",
          "particle": "kubejs:block/side",
          "south": "kubejs:block/side",
          "up": "kubejs:block/top",
          "west": "kubejs:block/side"
        }
      }
  }
})