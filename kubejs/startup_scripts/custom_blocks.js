

StartupEvents.registry("block", (event) => {
  const createBlock = (id, name, topTexture, sideTexture) => {
    event.create(id, "cardinal")
    .displayName(name)
    .material("wood") // Set a material (affects the sounds and some properties)
    .hardness(1.0) // Set hardness (affects mining time)
    .tagBlock("mineable/axe") //can be mined faster with an axe
    .modelJson = {
      "parent": "minecraft:block/cube",
      "textures": {
        "north": "kubejs:block/side",
        "south": "kubejs:block/side",
        "east": `kubejs:block/${sideTexture}`,
        "west": `kubejs:block/${sideTexture}`,
        "up": `kubejs:block/${topTexture}`,
        "down": "kubejs:block/bottom",
        "particle": "kubejs:block/side"
      }
    }
  }
  createBlock('berninas_shop', "Bernina's Shop", 'berninas_shop', 'shop_side')
  createBlock('elnas_shop', "Elna's Shop", 'elnas_shop', 'shop_side')
  createBlock(
    'bakery_customer_table',
    "Bakery Customer Table",
    'bakery_customer',
    'customer_side'
  )
  createBlock(
    'beach_customer_table',
    "Beach Customer Table",
    'beach_customer',
    'customer_side'
  )
  createBlock(
    'candlelight_customer_table',
    "Candlelight Customer Table",
    'candlelight_customer',
    'customer_side'
  )
  createBlock(
    'drink_customer_table',
    "Drink Customer Table",
    'drink_customer',
    'customer_side'
  )
  createBlock(
    'farmers_delight_customer_table',
    "Farmer's Delight Customer Table",
    'farmers_delight_customer',
    'customer_side'
  )
})