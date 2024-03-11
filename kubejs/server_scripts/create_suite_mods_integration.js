ServerEvents.recipes(event => {
  event.shapeless(
    'createaddition:zinc_sheet', ['createdeco:zinc_sheet']
  )
  event.shapeless(
    'createdeco:zinc_sheet', ['createaddition:zinc_sheet']
  )
})

ServerEvents.tags('item', event => {
  event.add('forge:plates/zinc', 'createdeco:zinc_sheet')
  event.add('createdeco:internal/plates/zinc_plates', 'createaddition:zinc_sheet')
})