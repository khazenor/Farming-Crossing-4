const SeasonHelper = Java.loadClass("sereneseasons.api.season.SeasonHelper")
const Season = Java.loadClass("sereneseasons.api.season.Season")

global.fc4Villagers = [
  { id: 'andre', name: 'Andre' },
  { id: 'laly', name: 'Laly' },
  { id: 'pamela', name: 'Pamela' },
  { id: 'ren', name: 'Ren' },
  { id: 'sam', name: 'Sam' },
  { id: 'yukkie', name: 'Yukkie' }
]
const seasonName = (seasonObj) => {
  if (seasonObj == Season.SPRING) {
    return 'spring'
  } else if (seasonObj == Season.SUMMER) {
    return 'summer'
  } else if (seasonObj == Season.AUTUMN) {
    return 'fall'
  } else {
    return 'winter'
  }
} 
const isDryWet = (seasonObj) => {
  if (
    seasonObj == Season.TropicalSeason.EARLY_DRY ||
    seasonObj == Season.TropicalSeason.MID_DRY ||
    seasonObj == Season.TropicalSeason.LATE_DRY ||
    seasonObj == Season.TropicalSeason.EARLY_WET ||
    seasonObj == Season.TropicalSeason.MID_WET ||
    seasonObj == Season.TropicalSeason.LATE_WET
  ) {
    return true
  } else {
    return false
  }
}

ForgeEvents.onEvent('sereneseasons.api.season.SeasonChangedEvent', event => {
  let seasonObj = event.getNewSeason()
  let server = event.getLevel().server
  updateAllVillagerTrades(server, seasonObj)
})

const updateAllVillagerTrades = (server, seasonObj) => {
  if (!isDryWet(seasonObj)) {
    let season = seasonName(seasonObj.getSeason())
    for (let villager of global.fc4Villagers) {
      server.runCommandSilent(
        global.updateVillagerCommand('e', villager.name, villager, season)
      )
    }
    for (let player of server.players) {
      player.tell(`The season is now ${season}`)
    }
  }
}

global.updateVillagerCommand = (targetSelector, name, villager, season) => {
  return `execute at @${targetSelector}[name=${name}] run function fc_villagers:${villager.id}_update_trades_${season}`
}

global.getSeasonFromLevel = (level) => {
  return seasonName(SeasonHelper.getSeasonState(level).getSeason())
}
