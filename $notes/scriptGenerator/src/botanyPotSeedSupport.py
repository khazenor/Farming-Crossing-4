from lib import botanyBots

seedKey = 'seed'
cropKey = 'crop'
blockKey = 'block'

seedSupports = [
	{
		seedKey: 'candlelight:lettuce_seeds',
		cropKey: 'candlelight:lettuce',
		blockKey: 'candlelight:lettuce_crop'
	},
	{
		seedKey: 'bakery:oat_seeds',
		cropKey: 'bakery:oat',
		blockKey: 'bakery:oat_crop'
	},
	{
		seedKey: 'bakery:strawberry_seeds',
		cropKey: 'bakery:strawberry',
		blockKey: 'bakery:strawberry_crop'
	},
	{
		seedKey: 'candlelight:tomato_seeds',
		cropKey: 'candlelight:tomato',
		blockKey: 'candlelight:tomato_crop'
	},
	{
		seedKey: 'delightful:cantaloupe_seeds',
		cropKey: 'delightful:cantaloupe',
		blockKey: 'delightful:cantaloupe'
	},
	{
		seedKey: 'nethervinery:crimson_grape_seeds',
		cropKey: 'nethervinery:crimson_grape',
		blockKey: 'nethervinery:crimson_grape_bush'
	},
	{
		seedKey: 'nethervinery:warped_grape_seeds',
		cropKey: 'nethervinery:warped_grape',
		blockKey: 'nethervinery:warped_grape_bush'
	},
	{
		seedKey: 'vinery:jungle_grape_seeds_red',
		cropKey: 'vinery:jungle_grapes_red',
		blockKey: 'vinery:jungle_grape_bush_red'
	},
	{
		seedKey: 'vinery:jungle_grape_seeds_white',
		cropKey: 'vinery:jungle_grapes_white',
		blockKey: 'vinery:jungle_grape_bush_white'
	},
	{
		seedKey: 'vinery:red_grape_seeds',
		cropKey: 'vinery:red_grape',
		blockKey: 'vinery:red_grape_bush'
	},
	{
		seedKey: 'vinery:savanna_grape_seeds_red',
		cropKey: 'vinery:savanna_grapes_red',
		blockKey: 'vinery:savanna_grape_bush_red'
	},
	{
		seedKey: 'vinery:savanna_grape_seeds_white',
		cropKey: 'vinery:savanna_grapes_white',
		blockKey: 'vinery:savanna_grape_bush_white'
	},
	{
		seedKey: 'vinery:taiga_grape_seeds_red',
		cropKey: 'vinery:taiga_grapes_red',
		blockKey: 'vinery:taiga_grape_bush_red'
	},
	{
		seedKey: 'vinery:taiga_grape_seeds_white',
		cropKey: 'vinery:taiga_grapes_white',
		blockKey: 'vinery:taiga_grape_bush_white'
	},
	{
		seedKey: 'vinery:white_grape_seeds',
		cropKey: 'vinery:white_grape',
		blockKey: 'vinery:white_grape_bush'
	}
]

hcFruits = [
  {
    cropKey: 'pamhc2trees:acornitem',
    seedKey: 'pamhc2trees:acorn_sapling',
    blockKey: 'pamhc2trees:acorn_sapling'
  },
  {
    cropKey: 'pamhc2trees:almonditem',
    seedKey: 'pamhc2trees:almond_sapling',
    blockKey: 'pamhc2trees:almond_sapling'
  },
  {
    cropKey: 'minecraft:apple',
    seedKey: 'pamhc2trees:apple_sapling',
    blockKey: 'pamhc2trees:apple_sapling'
  },
  {
    cropKey: 'pamhc2trees:apricotitem',
    seedKey: 'pamhc2trees:apricot_sapling',
    blockKey: 'pamhc2trees:apricot_sapling'
  },
  {
    cropKey: 'pamhc2trees:avocadoitem',
    seedKey: 'pamhc2trees:avocado_sapling',
    blockKey: 'pamhc2trees:avocado_sapling'
  },
  {
    cropKey: 'pamhc2trees:bananaitem',
    seedKey: 'pamhc2trees:banana_sapling',
    blockKey: 'pamhc2trees:banana_sapling'
  },
  {
    cropKey: 'pamhc2trees:breadfruititem',
    seedKey: 'pamhc2trees:breadfruit_sapling',
    blockKey: 'pamhc2trees:breadfruit_sapling'
  },
  {
    cropKey: 'pamhc2trees:candlenutitem',
    seedKey: 'pamhc2trees:candlenut_sapling',
    blockKey: 'pamhc2trees:candlenut_sapling'
  },
  {
    cropKey: 'pamhc2trees:cashewitem',
    seedKey: 'pamhc2trees:cashew_sapling',
    blockKey: 'pamhc2trees:cashew_sapling'
  },
  {
    cropKey: 'pamhc2trees:cherryitem',
    seedKey: 'pamhc2trees:cherry_sapling',
    blockKey: 'pamhc2trees:cherry_sapling'
  },
  {
    cropKey: 'pamhc2trees:chestnutitem',
    seedKey: 'pamhc2trees:chestnut_sapling',
    blockKey: 'pamhc2trees:chestnut_sapling'
  },
  {
    cropKey: 'pamhc2trees:cinnamonitem',
    seedKey: 'pamhc2trees:cinnamon_sapling',
    blockKey: 'pamhc2trees:cinnamon_sapling'
  },
  {
    cropKey: 'pamhc2trees:coconutitem',
    seedKey: 'pamhc2trees:coconut_sapling',
    blockKey: 'pamhc2trees:coconut_sapling'
  },
  {
    cropKey: 'pamhc2trees:dateitem',
    seedKey: 'pamhc2trees:date_sapling',
    blockKey: 'pamhc2trees:date_sapling'
  },
  {
    cropKey: 'pamhc2trees:dragonfruititem',
    seedKey: 'pamhc2trees:dragonfruit_sapling',
    blockKey: 'pamhc2trees:dragonfruit_sapling'
  },
  {
    cropKey: 'pamhc2trees:durianitem',
    seedKey: 'pamhc2trees:durian_sapling',
    blockKey: 'pamhc2trees:durian_sapling'
  },
  {
    cropKey: 'pamhc2trees:figitem',
    seedKey: 'pamhc2trees:fig_sapling',
    blockKey: 'pamhc2trees:fig_sapling'
  },
  {
    cropKey: 'pamhc2trees:gooseberryitem',
    seedKey: 'pamhc2trees:gooseberry_sapling',
    blockKey: 'pamhc2trees:gooseberry_sapling'
  },
  {
    cropKey: 'pamhc2trees:grapefruititem',
    seedKey: 'pamhc2trees:grapefruit_sapling',
    blockKey: 'pamhc2trees:grapefruit_sapling'
  },
  {
    cropKey: 'pamhc2trees:guavaitem',
    seedKey: 'pamhc2trees:guava_sapling',
    blockKey: 'pamhc2trees:guava_sapling'
  },
  {
    cropKey: 'pamhc2trees:hazelnutitem',
    seedKey: 'pamhc2trees:hazelnut_sapling',
    blockKey: 'pamhc2trees:hazelnut_sapling'
  },
  {
    cropKey: 'pamhc2trees:jackfruititem',
    seedKey: 'pamhc2trees:jackfruit_sapling',
    blockKey: 'pamhc2trees:jackfruit_sapling'
  },
  {
    cropKey: 'pamhc2trees:lemonitem',
    seedKey: 'pamhc2trees:lemon_sapling',
    blockKey: 'pamhc2trees:lemon_sapling'
  },
  {
    cropKey: 'pamhc2trees:limeitem',
    seedKey: 'pamhc2trees:lime_sapling',
    blockKey: 'pamhc2trees:lime_sapling'
  },
  {
    cropKey: 'pamhc2trees:lycheeitem',
    seedKey: 'pamhc2trees:lychee_sapling',
    blockKey: 'pamhc2trees:lychee_sapling'
  },
  {
    cropKey: 'pamhc2trees:mangoitem',
    seedKey: 'pamhc2trees:mango_sapling',
    blockKey: 'pamhc2trees:mango_sapling'
  },
  {
    cropKey: 'pamhc2trees:maplesyrupitem',
    seedKey: 'pamhc2trees:maple_sapling',
    blockKey: 'pamhc2trees:maple_sapling'
  },
  {
    cropKey: 'pamhc2trees:nutmegitem',
    seedKey: 'pamhc2trees:nutmeg_sapling',
    blockKey: 'pamhc2trees:nutmeg_sapling'
  },
  {
    cropKey: 'pamhc2trees:oliveitem',
    seedKey: 'pamhc2trees:olive_sapling',
    blockKey: 'pamhc2trees:olive_sapling'
  },
  {
    cropKey: 'pamhc2trees:orangeitem',
    seedKey: 'pamhc2trees:orange_sapling',
    blockKey: 'pamhc2trees:orange_sapling'
  },
  {
    cropKey: 'pamhc2trees:papayaitem',
    seedKey: 'pamhc2trees:papaya_sapling',
    blockKey: 'pamhc2trees:papaya_sapling'
  },
  {
    cropKey: 'minecraft:paper',
    seedKey: 'pamhc2trees:paperbark_sapling',
    blockKey: 'pamhc2trees:paperbark_sapling'
  },
  {
    cropKey: 'pamhc2trees:passionfruititem',
    seedKey: 'pamhc2trees:passionfruit_sapling',
    blockKey: 'pamhc2trees:passionfruit_sapling'
  },
  {
    cropKey: 'pamhc2trees:pawpawitem',
    seedKey: 'pamhc2trees:pawpaw_sapling',
    blockKey: 'pamhc2trees:pawpaw_sapling'
  },
  {
    cropKey: 'pamhc2trees:peachitem',
    seedKey: 'pamhc2trees:peach_sapling',
    blockKey: 'pamhc2trees:peach_sapling'
  },
  {
    cropKey: 'pamhc2trees:pearitem',
    seedKey: 'pamhc2trees:pear_sapling',
    blockKey: 'pamhc2trees:pear_sapling'
  },
  {
    cropKey: 'pamhc2trees:pecanitem',
    seedKey: 'pamhc2trees:pecan_sapling',
    blockKey: 'pamhc2trees:pecan_sapling'
  },
  {
    cropKey: 'pamhc2trees:peppercornitem',
    seedKey: 'pamhc2trees:peppercorn_sapling',
    blockKey: 'pamhc2trees:peppercorn_sapling'
  },
  {
    cropKey: 'pamhc2trees:persimmonitem',
    seedKey: 'pamhc2trees:persimmon_sapling',
    blockKey: 'pamhc2trees:persimmon_sapling'
  },
  {
    cropKey: 'pamhc2trees:pinenutitem',
    seedKey: 'pamhc2trees:pinenut_sapling',
    blockKey: 'pamhc2trees:pinenut_sapling'
  },
  {
    cropKey: 'pamhc2trees:pistachioitem',
    seedKey: 'pamhc2trees:pistachio_sapling',
    blockKey: 'pamhc2trees:pistachio_sapling'
  },
  {
    cropKey: 'pamhc2trees:plumitem',
    seedKey: 'pamhc2trees:plum_sapling',
    blockKey: 'pamhc2trees:plum_sapling'
  },
  {
    cropKey: 'pamhc2trees:pomegranateitem',
    seedKey: 'pamhc2trees:pomegranate_sapling',
    blockKey: 'pamhc2trees:pomegranate_sapling'
  },
  {
    cropKey: 'pamhc2trees:rambutanitem',
    seedKey: 'pamhc2trees:rambutan_sapling',
    blockKey: 'pamhc2trees:rambutan_sapling'
  },
  {
    cropKey: 'pamhc2trees:soursopitem',
    seedKey: 'pamhc2trees:soursop_sapling',
    blockKey: 'pamhc2trees:soursop_sapling'
  },
  {
    cropKey: 'minecraft:string',
    seedKey: 'pamhc2trees:spiderweb_sapling',
    blockKey: 'pamhc2trees:spiderweb_sapling'
  },
  {
    cropKey: 'pamhc2trees:starfruititem',
    seedKey: 'pamhc2trees:starfruit_sapling',
    blockKey: 'pamhc2trees:starfruit_sapling'
  },
  {
    cropKey: 'pamhc2trees:tamarinditem',
    seedKey: 'pamhc2trees:tamarind_sapling',
    blockKey: 'pamhc2trees:tamarind_sapling'
  },
  {
    cropKey: 'pamhc2trees:vanillabeanitem',
    seedKey: 'pamhc2trees:vanillabean_sapling',
    blockKey: 'pamhc2trees:vanillabean_sapling'
  },
  {
    cropKey: 'pamhc2trees:walnutitem',
    seedKey: 'pamhc2trees:walnut_sapling',
    blockKey: 'pamhc2trees:walnut_sapling'
  }
]

otherCrops = [
	{
		seedKey: "vinery:cherry_sapling",
		cropKey: "vinery:cherry",
		blockKey: "vinery:cherry_sapling"
  },
	{
		seedKey: "vinery:apple_tree_sapling",
		cropKey: "minecraft:apple",
		blockKey: "vinery:apple_tree_sapling"
  },
	{
		seedKey: "pamhc2trees:apple_sapling",
		cropKey: "minecraft:apple",
		blockKey: "pamhc2trees:apple_sapling"
  },
	{
		seedKey: "beachparty:palm_sapling",
		cropKey: "beachparty:coconut",
		blockKey: "beachparty:palm_sapling"
  },
	{
    seedKey: "brewery:hops_seeds",
    cropKey: "brewery:hops",
		blockKey: "brewery:hops_crop"
  },
	{
    seedKey: "brewery:barley_seeds",
    cropKey: "brewery:barley",
		blockKey: "brewery:barley_crop"
  },
	{
    seedKey: "brewery:corn_seeds",
    cropKey: "brewery:corn",
		blockKey: "brewery:corn_crop"
  },
	{
		seedKey: "herbalbrews:tea_blossom",
		cropKey: "herbalbrews:green_tea_leaf",
		blockKey: "herbalbrews:tea_plant"
  },
	{
		seedKey: "herbalbrews:yerba_mate_leaf",
		cropKey: "herbalbrews:yerba_mate_leaf",
		blockKey: "herbalbrews:yerba_mate_plant"
  },
	{
		seedKey: "herbalbrews:rooibos_leaf",
		cropKey: "herbalbrews:rooibos_leaf",
		blockKey: "herbalbrews:rooibos_plant"
  },
	{
		seedKey: "herbalbrews:coffee_beans",
		cropKey: "herbalbrews:coffee_beans",
		blockKey: "herbalbrews:coffee_plant"
  },
	{
		seedKey: 'minecraft:vine',
		cropKey: 'minecraft:vine',
		blockKey: 'minecraft:vine'
  },
	{
		seedKey: 'minecraft:weeping_vines',
		cropKey: 'minecraft:weeping_vines',
		blockKey: 'minecraft:weeping_vines_plant'
  },
	{
		seedKey: 'minecraft:twisting_vines',
		cropKey: 'minecraft:twisting_vines',
		blockKey: 'minecraft:twisting_vines_plant'
  },
	{
		seedKey: 'biomesoplenty:willow_vine',
		cropKey: 'biomesoplenty:willow_vine',
		blockKey: 'biomesoplenty:willow_vine'
  }
]

def genBotanySeedSupport():
	for seedList in [seedSupports, hcFruits, otherCrops]:
		for seedSupport in seedList:
			botanyBots.writeSeedJson(
				seedSupport[seedKey],
				seedSupport[cropKey],
				seedSupport[blockKey]
			)
