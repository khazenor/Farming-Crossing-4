

StartupEvents.registry("block", (event) => {
  const textureAvailable = [
    "Elna's Shop",
    "Bernina's Shop",
    "Bakery Customer Table",
  ]
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
    let modelJson
    let blockId = stringToName(blockName)
    if (textureAvailable.includes(blockName)) {
      modelJson = {
        "parent": "minecraft:block/cube",
        "textures": {
          "up": `kubejs:block/${blockId}_top`,
          "down": `kubejs:block/${blockId}_bottom`,
          "north": `kubejs:block/${blockId}_side2`,
          "south": `kubejs:block/${blockId}_side2`,
          "east": `kubejs:block/${blockId}_side1`,
          "west": `kubejs:block/${blockId}_side1`,
          "particle": `kubejs:block/${blockId}_side1`
        }
      }
    } else {
      modelJson = {
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
    console.log(modelJson)
    event.create(blockId, "cardinal")
      .displayName(blockName)
      .material("wood") // Set a material (affects the sounds and some properties)
      .hardness(1.0) // Set hardness (affects mining time)
      .tagBlock("mineable/axe") //can be mined faster with an axe
      .modelJson = modelJson
  }
})