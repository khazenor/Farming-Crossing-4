const drawers = [
  'storagedrawers:acacia_full_drawers_1',
  'storagedrawers:acacia_full_drawers_2',
  'storagedrawers:acacia_full_drawers_4',
  'storagedrawers:acacia_half_drawers_1',
  'storagedrawers:acacia_half_drawers_2',
  'storagedrawers:acacia_half_drawers_4',
  'storagedrawers:birch_full_drawers_1',
  'storagedrawers:birch_full_drawers_2',
  'storagedrawers:birch_full_drawers_4',
  'storagedrawers:birch_half_drawers_1',
  'storagedrawers:birch_half_drawers_2',
  'storagedrawers:birch_half_drawers_4',
  'storagedrawers:compacting_drawers_3',
  'storagedrawers:crimson_full_drawers_1',
  'storagedrawers:crimson_full_drawers_2',
  'storagedrawers:crimson_full_drawers_4',
  'storagedrawers:crimson_half_drawers_1',
  'storagedrawers:crimson_half_drawers_2',
  'storagedrawers:crimson_half_drawers_4',
  'storagedrawers:dark_oak_full_drawers_1',
  'storagedrawers:dark_oak_full_drawers_2',
  'storagedrawers:dark_oak_full_drawers_4',
  'storagedrawers:dark_oak_half_drawers_1',
  'storagedrawers:dark_oak_half_drawers_2',
  'storagedrawers:dark_oak_half_drawers_4',
  'storagedrawers:drawer_key',
  'storagedrawers:jungle_full_drawers_1',
  'storagedrawers:jungle_full_drawers_2',
  'storagedrawers:jungle_full_drawers_4',
  'storagedrawers:jungle_half_drawers_1',
  'storagedrawers:jungle_half_drawers_2',
  'storagedrawers:jungle_half_drawers_4',
  'storagedrawers:oak_full_drawers_1',
  'storagedrawers:oak_full_drawers_2',
  'storagedrawers:oak_full_drawers_4',
  'storagedrawers:oak_half_drawers_1',
  'storagedrawers:oak_half_drawers_2',
  'storagedrawers:oak_half_drawers_4',
  'storagedrawers:spruce_full_drawers_1',
  'storagedrawers:spruce_full_drawers_2',
  'storagedrawers:spruce_full_drawers_4',
  'storagedrawers:spruce_half_drawers_1',
  'storagedrawers:spruce_half_drawers_2',
  'storagedrawers:spruce_half_drawers_4',
  'storagedrawers:warped_full_drawers_1',
  'storagedrawers:warped_full_drawers_2',
  'storagedrawers:warped_full_drawers_4',
  'storagedrawers:warped_half_drawers_1',
  'storagedrawers:warped_half_drawers_2',
  'storagedrawers:warped_half_drawers_4'
]

BlockEvents.rightClicked(event => {
  console.log('block:', event.getBlock().id)
  if (
    (event.getItem().getId() === 'easy_mob_farm:netherite_lasso') &&
    (drawers.indexOf(event.getBlock().id) !== -1)
  ){
    event.getEntity().tell("Please do not store netherite lassos in drawers.  It causes a client crash.")
  }
})