
global.sweet = 'fcSweetFoodsEatenCount'
global.savory = 'fcSavoryFoodsEatenCount'
global.light = 'fcLightFoodsEatenCount'
global.heavy = 'fcHeavyFoodsEatenCount'
global.hot = 'fcHotFoodsEatenCount'
global.cold = 'fcColdFoodsEatenCount'
global.foodClassificationNames = {
  fcSweetFoodsEatenCount: 'Sweet',
  fcSavoryFoodsEatenCount: 'Savory',
  fcLightFoodsEatenCount: 'Light',
  fcHeavyFoodsEatenCount: 'Heavy',
  fcHotFoodsEatenCount: 'Hot',
  fcColdFoodsEatenCount: 'Cold'
}
global.foodClassifications = {
  fcSweetFoodsEatenCount: [
    'minecraft:apple'
  ],
  fcSavoryFoodsEatenCount: [
    'minecraft:cooked_beef',
    'pamhc2foodcore:friedchickenitem'
  ],
  fcLightFoodsEatenCount: [
    'pamhc2foodcore:chorusjuiceitem'
  ],
  fcHeavyFoodsEatenCount: [
    'pamhc2foodextended:blackberrycobbleritem',
    'pamhc2foodcore:friedchickenitem'
  ],
  fcHotFoodsEatenCount: [
    'herbalbrews:green_tea'
  ],
  fcColdFoodsEatenCount: [
    'pamhc2foodcore:icecreamitem'
  ]
}


global.getSeasonFromLevel = (level) => {
  return seasonName(SeasonHelper.getSeasonState(level).getSeason())
}

global.seasonName = (seasonObj) => {
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