ServerEvents.recipes(event => {
  event.remove({output: 'vinery:cherry_boat'})
  event.shaped('minecraft:mangrove_boat',[
    'P P',
    'PPP'
  ], {
    P: 'vinery:cherry_planks'
  })
})