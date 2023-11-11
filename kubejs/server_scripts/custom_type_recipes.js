ServerEvents.recipes(event => {
  event.custom({
    "type": "meadow:cooking",
    "ingredients": [
      {
        "tag": "forge:water"
      }
    ],
    "result": {
      "item":  "meadow:alpine_salt"
    }
  }
  )
  event.custom({
    "type": "minecraft:crafting_shaped",
    "pattern": [
      " B ",
      "W W",
      " S "
    ],
    "key": {
      "S": {
        "tag": "bakery:wheat"
      },
      "W": {
        "item": "minecraft:sugar"
      },
      "B": {
        "tag": "forge:water"
      }
    },
    "result": {
      "item": "bakery:sweet_dough",
      "count": 4
    }
  })
  event.custom({
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
      {
        "tag": "forge:water"
      },
      {
        "item": "minecraft:sugar"
      },
      {
        "item": "minecraft:brown_mushroom"
      }
    ],
    "result": {
      "item": "bakery:yeast",
      "count": 12
    }
  })
  event.custom({
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
      {
        "tag": "aquaculture:turtle"
      },
      {
        "tag": "forge:water"
      },
      {
        "item": "minecraft:bowl"
      }
    ],
    "result": {
      "item": "aquaculture:turtle_soup"
    }
  })
})