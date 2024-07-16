ServerEvents.recipes(event => {
  const creativeUpgrades = {
    'refinedstorage:creative_portable_grid': 'refinedstorage:portable_grid',
    'refinedstorage:creative_wireless_fluid_grid': 'refinedstorage:wireless_fluid_grid',
    'refinedstorage:creative_wireless_grid': 'refinedstorage:wireless_grid',
    'refinedstorageaddons:creative_wireless_crafting_grid': 'refinedstorageaddons:wireless_crafting_grid',
    'refinedstorage:creative_controller': 'refinedstorage:controller'
  }

  for (let creativeId in creativeUpgrades) {
    event.shapeless(creativeId, [
      creativeUpgrades[creativeId],
      'kubejs:creative_upgrade'
    ])
  }
})