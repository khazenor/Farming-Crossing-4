ServerEvents.recipes(event => {
  event.shaped("waystones:warp_stone", [
    "OOO",
    "O O",
    "OOO"
  ], {
    O: "minecraft:obsidian"
  })

  event.shaped("waystones:warp_plate",[
    "SOS",
    "OOO",
    "SOS"
  ], {
    O: "minecraft:obsidian",
    S: "minecraft:stone_bricks"
  })

  event.shapeless("2x waystones:warp_plate", [
    "#waystones:waystones"
  ])
})