ServerEvents.recipes(event => {
  event.shapeless('refinedstorage:creative_portable_grid', [
    'refinedstorage:portable_grid',
    'kubejs:creative_upgrade'
  ])
  event.shapeless('refinedstorage:creative_wireless_fluid_grid', [
    'refinedstorage:wireless_fluid_grid',
    'kubejs:creative_upgrade'
  ])
  event.shapeless('refinedstorage:creative_wireless_grid', [
    'refinedstorage:creative_wireless_grid',
    'kubejs:creative_upgrade'
  ])
  event.shapeless('refinedstorageaddons:creative_wireless_crafting_grid', [
    'refinedstorageaddons:wireless_crafting_grid',
    'kubejs:creative_upgrade'
  ])
})