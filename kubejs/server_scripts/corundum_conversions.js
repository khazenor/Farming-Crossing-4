ServerEvents.recipes(event => {
  var colorPairs = {
    black: 'black',
    blue: 'light_blue',
    green: 'green',
    indigo: 'blue',
    orange: 'orange',
    red: 'red',
    violet: 'magenta',
    white: 'white',
    yellow: 'yellow',
  }

  for (let quarkColor in colorPairs) {
    let minecraftColor = colorPairs[quarkColor]

    let minecraftDyeId = `minecraft:${minecraftColor}_dye`
    let corundumId = `quark:${quarkColor}_corundum`
    let clusterId = `quark:${quarkColor}_corundum_cluster`

    event.shapeless(`32x ${minecraftDyeId}`, [clusterId, clusterId])
    event.shapeless(`64x ${minecraftDyeId}`, [corundumId, corundumId])
    event.shapeless('2x minecraft:quartz', [clusterId])
    event.shapeless('8x minecraft:quartz', [corundumId])
  }
})