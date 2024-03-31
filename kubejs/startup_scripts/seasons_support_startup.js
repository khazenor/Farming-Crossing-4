const SeasonHelper = Java.loadClass("sereneseasons.api.season.SeasonHelper")
const Season = Java.loadClass("sereneseasons.api.season.Season")
const villagers = [
  'andre',
  'laly',
  'pamela',
  'ren',
  'sam',
  'yukkie'
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
let season

ForgeEvents.onEvent('sereneseasons.api.season.SeasonChangedEvent', event => {
  const seasonObj = event.getNewSeason()
  if (!isDryWet(seasonObj)) {
    season = seasonName(seasonObj.getSeason())
    event.getLevel().tell(`The season is now ${season}`)
    for (const player of event.getLevel().players) {
      updateVillagerAroundPlayer(player)
    }
  }
})

const updateVillagerAroundPlayer = (player) => {
  for (const villager of villagers) {
    player.getServer().runCommandSilent(
      `execute at @p run function fc_villagers:${villager}_update_trades_${season}`
    )
  }
} 