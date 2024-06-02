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
  let season = global.getSeasonFromLevel(level)
  player.tell(`${noticeMsg} ${season}`)
  for (const villager of global.fc4Villagers) {
    player.getServer().runCommandSilent(
      global.updateVillagerCommand(`@p[name=${player.username}]`, villager, season)
    )
  }
} 