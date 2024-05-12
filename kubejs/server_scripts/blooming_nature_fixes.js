const logs = [
  "aspen_log",
  "baobab_log",
  "chestnut_log",
  "ebony_log",
  "fir_log",
  "larch_log",
  "palm_log",
  "swamp_cypress_log",
  "swamp_oak_log"
]

for (const log of logs) {
  let logId = `bloomingnature:${log}`
  let strippedLogId = `bloomingnature:stripped_${log}`

  ServerEvents.recipes(event => {
    event.custom({
      "type": "create:cutting",
      "ingredients": [
        {
          "item": logId
        }
      ],
      "processingTime": 50,
      "results": [
        {
          "item": strippedLogId
        }
      ]
    })
    event.smelting('minecraft:charcoal', logId)
    event.smelting('minecraft:charcoal', strippedLogId)
  })

  ServerEvents.tags('item', event => {
    event.add('minecraft:logs_that_burn', logId)
    event.add('minecraft:logs_that_burn', strippedLogId)
    event.add('forge:stripped_logs', strippedLogId)
  })
}
