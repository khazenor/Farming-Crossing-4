ServerEvents.recipes(event => {
  event.remove({id: 'bakery:crafting_bowl/cake_dough'})
  event.remove({id: 'bakery:crafting_bowl/dough'})
  event.remove({id: 'bakery:crafting_bowl/sweet_dough'})
  event.remove({id: 'bakery:crafting_bowl'})

  event.shapeless('4x bakery:cake_dough', [
    '#forge:egg',
    'minecraft:sugar',
    '#candlelight:wheat',
    '#forge:milk'
  ])

  event.shapeless('4x bakery:dough',[
    "#bakery:wheat",
    "bakery:yeast",
    "#forge:water",
    "minecraft:sugar"
  ])
  
  event.shapeless('4x bakery:sweet_dough',[
    "#bakery:wheat",
    "minecraft:sugar",
    "minecraft:sugar",
    "#forge:water"
  ])
})