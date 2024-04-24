// prints all foods in the pack

ItemEvents.modification(event => {
  event.modify(/.*/, item => {
    if (item.foodProperties) {
      if (item.foodProperties.saturationModifier < .7) {
        console.log(`Light: ${item.id}`)
      } else if (item.foodProperties.saturationModifier > 1.2) {
        console.log(`Heavy: ${item.id}`)
      }
    }
  })
})