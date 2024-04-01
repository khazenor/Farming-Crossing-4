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
let season

const getSeasonFromLevel = (level) => {
  return seasonName(SeasonHelper.getSeasonState(level).getSeason())
}

ItemEvents.rightClicked('sereneseasons:calendar', event => {
  event.player.tell(`Trades for nearby farming crossing villagers are now updated for ${season}`)
  updateVillagerAroundPlayer(event.player)
})

PlayerEvents.loggedIn(event => {
  const level = event.player.level
  season = getSeasonFromLevel(level)
  event.player.tell(`The season is now ${season}`)
  updateVillagerAroundPlayer(event.player)
})

const updateVillagerAroundPlayer = (player) => {
  for (const villager of villagers) {
    player.getServer().runCommandSilent(
      `execute at @p run function fc_villagers:${villager}_update_trades_${season}`
    )
  }
} 