ServerEvents.recipes(event => {
  event.shapeless("kubejs:bakery_customer_table", [
    "bakery:bread",
    '#minecraft:logs'
  ])
  event.shapeless("kubejs:drink_customer_table", [
    "vinery:red_grapejuice_wine_bottle",
    '#minecraft:logs'
  ])
  event.shapeless("kubejs:candlelight_customer_table", [
    "candlelight:mushroom_soup",
    '#minecraft:logs'
  ])
  event.shapeless("kubejs:beach_customer_table", [
    "beachparty:icecream_coconut",
    '#minecraft:logs'
  ])
  event.shapeless("kubejs:farmers_delight_customer_table", [
    "farmersdelight:cabbage_rolls",
    '#minecraft:logs'
  ])
})