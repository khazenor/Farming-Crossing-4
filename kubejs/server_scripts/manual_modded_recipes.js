ServerEvents.recipes(event => {
  
  event.remove({ output: 'farmingforblockheads:market' })
  event.shapeless(
    Item.of('farmingforblockheads:market', 1),
    [
      'kubejs:miles_ticket', 'kubejs:miles_ticket',
      'kubejs:miles_ticket', 'kubejs:miles_ticket'
    ]
  )

  event.shaped('refinedstorage:1k_storage_disk', [
    'X',
    'X'
  ], {
    X: 'kubejs:1k_storage_disk_ticket'
  })
  event.shaped('refinedstorage:4k_storage_disk', [
    'X',
    'X'
  ], {
    X: 'kubejs:4k_storage_disk_ticket'
  })
  event.shaped('refinedstorage:16k_storage_disk', [
    'X',
    'X'
  ], {
    X: 'kubejs:16k_storage_disk_ticket'
  })
  event.shaped('refinedstorage:64k_storage_disk', [
    'X',
    'X'
  ], {
    X: 'kubejs:64k_storage_disk_ticket'
  })

  event.remove({output: 'non_wandering_trader:travellers_table'})
  event.remove({id: 'constructionwand:core_destruction'})

  event.shapeless('exoticbirds:eggshell', [
    "#forge:eggs",
    "#forge:eggs",
    "#forge:eggs",
    "#forge:eggs"
  ])
})
