// prints all foods in the pack

ItemEvents.modification(event => {
  event.modify(/.*/, item => {
    if (item.foodProperties) {
      console.log(item.id)
    }
  })
})