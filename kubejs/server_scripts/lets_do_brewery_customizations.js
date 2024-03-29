ServerEvents.recipes(event => {
  event.remove({id: 'brewery:pretzel'})
  event.custom({
    "type": "bakery:stove",
    "ingredients": [
      { "tag": "forge:water" },
      { "tag": "meadow:salt" },
      { "tag": "forge:dough" }
    ],
    "item": "brewery:pretzel",
    "count": 6,
    "experience": 0.3
  })
  event.remove({id: 'brewery:gingerbread'})
  event.custom({
    "type": "bakery:stove",
    "ingredients": [
      { "item": "bakery:sweet_dough" },
      { "item": "minecraft:white_dye" },
      { "item": "minecraft:cyan_dye" }
    ],
    "item": "brewery:gingerbread",
    "count": 2,
    "experience": 0.3
  })
})