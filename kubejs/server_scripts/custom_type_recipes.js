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
  event.custom({
    "type": "minecraft:crafting_shapeless",
    'ingredients': [
      {"tag": "forge:neighborly_spawn_eggs"},
      {"tag": "forge:neighborly_spawn_eggs"}
    ],
    "result": {
      "item": 'lootbags:loot_bag',
      "count": 1,
      "nbt": {
        "Type": "RARE",
        "Loot": "lootbags:furniture/loot_neighborly",
        "Color": 13882323,
        "Name": "Neighborly Villager Move In Kit"
      }
    }
  })

  event.custom({
    "result": {
      "item": "waystones:warp_plate"
    },
    "type": "minecraft:crafting_shaped",
    "pattern": [
      "SOS",
      "OOO",
      "SOS"
    ],
    "key": {
      "O": {
        "item": "minecraft:obsidian"
      },
      "S": {
        "item": "minecraft:stone_bricks"
      }
    }
  }
  )
})