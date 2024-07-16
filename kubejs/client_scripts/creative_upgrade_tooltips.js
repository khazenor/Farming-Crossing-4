ItemEvents.tooltip(event => {
  event.add([
    'refinedstorage:creative_portable_grid',
    'refinedstorage:creative_wireless_fluid_grid',
    'refinedstorage:creative_wireless_grid',
    'refinedstorageaddons:creative_wireless_crafting_grid'
  ], [
    'Can be obtained using the',
    'Creative Upgrade available in the Market'
  ])

  event.add([
    'refinedstorage:portable_grid',
    'refinedstorage:wireless_fluid_grid',
    'refinedstorage:creative_wireless_grid',
    'refinedstorageaddons:wireless_crafting_grid'
  ], [
    'Can be upgraded to a creative version with the',
    'Creative Upgrade available in the market'
  ])
})
