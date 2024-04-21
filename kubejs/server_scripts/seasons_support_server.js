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

ItemEvents.rightClicked('sereneseasons:calendar', event => {
  updateVillagerAroundPlayer(
    'Trades for nearby farming crossing villagers are now updated for',
    event.player
  )
})

PlayerEvents.loggedIn(event => {
  updateVillagerAroundPlayer('The season is now', event.player)
})

const updateVillagerAroundPlayer = (noticeMsg, player) => {
  const level = player.level
  const season = global.getSeasonFromLevel(level)
  player.tell(`${noticeMsg} ${season}`)
  for (const villager of villagers) {
    player.getServer().runCommandSilent(
      `execute at @p run function fc_villagers:${villager}_update_trades_${season}`
    )
  }
} 