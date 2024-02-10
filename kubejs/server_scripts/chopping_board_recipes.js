ServerEvents.recipes(event => {
  event.custom({
    type: 'farmersdelight:cutting',
    ingredients: [ { item: "minecraft:pumpkin" } ],
    tool: { tag: 'forge:shears', },
    result: [
      { item: "minecraft:carved_pumpkin" },
      {
        item: "minecraft:pumpkin_seeds",
        count: 4
      }
    ]
  })
})