const playerFullFoodLevel = 20
const cravingThreshold = 2
const potionEffectTime = 24000 // 20*20*60
const potionAmplifier = 2
const hasEatenFirstFoodKey = 'hasEatenFirstFoodKey'
const foodCravingCacheKey = 'foodCravingCacheKey'
const disableFoodCravingNotificationKey = 'disableFoodCravingNotificationKey'

const potionEffects = [
  {
    id: 'minecraft:speed',
    name: 'Speed'
  }, {
    id: 'minecraft:haste',
    name: 'Haste'
  }, {
    id: 'minecraft:strength',
    name: 'Strength'
  }, {
    id: 'minecraft:regeneration',
    name: 'Regeneration'
  }, {
    id: 'minecraft:resistance',
    name: 'Resistance'
  }, {
    id: 'minecraft:absorption',
    name: 'Absorption'
  }, {
    id: 'minecraft:luck',
    name: 'Luck'
  }
]

ItemEvents.foodEaten(event => {
  const cravings = playerFoodCravings(event.player)
  const cravingScore = getCravingScore(event.item.id, cravings)
  if (cravingScore === 0 && event.player.foodLevel < playerFullFoodLevel) {
    autoNotifyPlayerCravings(event.player, cravings)
  }
  if (cravingScore > 0) {
    rewardPlayerWithPotionEffects(event.player, cravingScore)
  } else {
    updatePlayerFoodTallies(event.item, event.player)
    givePlayerCheckItemIfFirstTimeEating(event.player)
  }
})

PlayerEvents.tick(event => {
  const foodLevel = event.player.foodLevel
  const playerData = event.player.persistentData
  if (foodLevel === playerFullFoodLevel && !playerData.wasFull) {
    playerData.wasFull = true
  } else if (foodLevel < playerFullFoodLevel && playerData.wasFull) {
    playerData.wasFull = false
    const cravings = playerFoodCravings(event.player)
    autoNotifyPlayerCravings(event.player, cravings)
  }
})

ItemEvents.rightClicked('kubejs:check_food_cravings', event => {
  const player = event.player
  if (player.shiftKeyDown) {
    let newDoDisable
    if (player.persistentData[disableFoodCravingNotificationKey]) {
      newDoDisable = !player.persistentData[disableFoodCravingNotificationKey]
    } else {
      newDoDisable = true
    }
    player.persistentData[disableFoodCravingNotificationKey] = newDoDisable
    const onOff = newDoDisable ? 'off': 'on'
    player.tell(`Craving notification is now turned ${onOff}`)
  } else {
    player.tell('')
    displayFoodTallies(player)
    const cravings = playerFoodCravings(player)
    if (cravings.length > 0) {
      notifyPlayerOfCravings(player, cravings)
    } else {
      player.tell('You are currently not craving any types of food.')
    }

    if (player.persistentData[disableFoodCravingNotificationKey]) {
      player.tell('You currently have craving notifications turned off')
    }
  }
})

const givePlayerCheckItemIfFirstTimeEating = (player) => {
  const playerData = player.persistentData
  if (!playerData[hasEatenFirstFoodKey]) {
    player.give('kubejs:check_food_cravings')
    playerData[hasEatenFirstFoodKey] = true
  }
}

const getCravingScore = (itemId, cravings) => {
  let cravingScore = 0
  for (let craving of cravings) {
    if (global.foodClassifications[craving].includes(itemId)) {
      cravingScore++
    }
  }
  return cravingScore
}

const rewardPlayerWithPotionEffects = (player, cravingScore) => {
  const effects = randomSelectFromArr(potionEffects, cravingScore)
  if (cravingScore === 1) {
    player.tell('That was tasty!')
  } else if (cravingScore === 2) {
    player.tell('That was delicious!')
  } else {
    player.tell('That was out of this world!')
  }

  let message = 'The food has given you '

  player.potionEffects.clear()
  for (let i = 0; i<effects.length; i++) {
    let effect = effects[i]
    player.potionEffects.add(
      effect.id,
      potionEffectTime,
      potionAmplifier,
      false,
      false
    )

    if (i > 0 && effects.length > 2) {
      message += ","
    }
    if (i > 0) {
      message += " "
    }
    if (i > 0 && i === effects.length - 1) {
      message += "and "
    }
    message += effect.name
  }
  player.tell(message)

  resetTallies(player)
}

const resetTallies = (player) => {
  for (let foodCategory in global.foodClassifications) {
    player.persistentData[foodCategory] = 0
  }
  player.persistentData[foodCravingCacheKey] = ""
}

const randomSelectFromArr = (arr, numSelect) => {
  const randomElms = []
  for (let i = 0; i<numSelect; i++) {
    let randomElm = arr[Math.floor(Math.random() * arr.length)]
    while (randomElms.includes(randomElm)) {
      randomElm = arr[Math.floor(Math.random() * arr.length)]
    }
    randomElms.push(randomElm)
  }
  return randomElms
}

const autoNotifyPlayerCravings = (player, cravings) => {
  if (!player.persistentData[disableFoodCravingNotificationKey] && cravings.length > 0) {
    cravings.sort()
    const cravingKey = concatArrVals(cravings)
    if (player.persistentData[foodCravingCacheKey] !== cravingKey) {
      player.persistentData[foodCravingCacheKey] = cravingKey
      notifyPlayerOfCravings(player, cravings)
    }
  }
}

const notifyPlayerOfCravings = (player, cravings) => {
  let message = "You are currently craving something that is "
  for (let i = 0; i<cravings.length; i++) {
    let craving = cravings[i]
    if (i > 0 && cravings.length > 2) {
      message += ","
    }
    if (i > 0) {
      message += " "
    }
    if (i > 0 && i === cravings.length - 1) {
      message += "or "
    }
    message += global.foodClassificationNames[craving]
  }
  player.tell(message)
}

const playerFoodCravings = (player) => {
  const playerData = player.persistentData
  const cravings = []
  addCraving(global.sweet, global.savory, playerData, cravings)
  addCraving(global.light, global.heavy, playerData, cravings)
  addCraving(global.hot, global.cold, playerData, cravings)
  addCraving(global.wet, global.dry, playerData, cravings)
  return cravings
}

const addCraving = (categoryYing, categoryYang, playerData, cravings) => {
  const yingVal = playerData[categoryYing] ? playerData[categoryYing] : 0
  const yangVal = playerData[categoryYang] ? playerData[categoryYang] : 0
  if (yingVal >= cravingThreshold && yingVal > yangVal) {
    cravings.push(categoryYang)
  } else if (yangVal >= cravingThreshold && yangVal > yingVal) {
    cravings.push(categoryYing)
  }
}

const updatePlayerFoodTallies = (item, player) => {
  const playerData = player.persistentData
  updateTalliesBasedOnCategories(item.id, playerData)
  updateTalliesBasedOnSeason(player, playerData)
}

const displayFoodTallies = (player) => {
  const sweet = playerTally('sweet', player)
  const savory = playerTally('savory', player)
  const light = playerTally('light', player)
  const heavy = playerTally('heavy', player)
  const hot = playerTally('hot', player)
  const cold = playerTally('cold', player)
  const wet = playerTally('wet', player)
  const dry = playerTally('dry', player)
  player.tell('====== CRAVING SCORES ======')
  player.tell(`  Sweet: ${sweet},   Savory: ${savory}`)
  player.tell(`  Light: ${light},   Heavy: ${heavy}`)
  player.tell(`  Hot: ${hot},   Cold: ${cold}`)
  player.tell(`  Wet: ${wet},   Dry: ${dry}`)
  player.tell('============================')
}

const playerTally = (tallySortName, player) => {
  const playerData = player.persistentData
  return defaultToZero(playerData[global[tallySortName]])
}

const defaultToZero = (value) => {
  return value ? value : 0
}

const concatArrVals = (array) => {
  let strVals = ""
  for (let val of array) {
    strVals += val
  }
  return strVals
}

const updateTalliesBasedOnCategories = (itemId, playerData) => {
  for (let foodCategory in global.foodClassifications) {
    if (global.foodClassifications[foodCategory].includes(itemId)) {
      incrementPlayerData(foodCategory, playerData)
    }
  }
}

const updateTalliesBasedOnSeason = (player, playerData) => {
  const season = global.getSeasonFromLevel(player.level)
  if (season === 'summer') {
    incrementPlayerData(global.hot, playerData)
  } else if (season === 'winter') {
    incrementPlayerData(global.cold, playerData)
  }
}

const incrementPlayerData = (propertyName, playerData) => {
  if (playerData[propertyName] > 0) {
    playerData[propertyName] ++
  } else {
    playerData[propertyName] = 1
  }
}