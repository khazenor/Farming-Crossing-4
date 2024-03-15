from lib import commands

nitwitVillagerData = ',VillagerData: { profession: "minecraft:nitwit", level: 5, type: "minecraft:plains" }'

villagerItemKey = 'villagerItemKey'
villagerQtyKey = 'villagerQtyKey'
playerGiveKey = 'playerGiveKey'
playerQtyKey = 'playerQtyKey'

def summonNpcCommand(texture, name, offers, hasTradesDefined):
	entityData = f'{{texture_name:"{texture}"'
	entityData += f',CustomName:"{commands.textJsonEscaped(name)}"'
	if len(offers) > 0:
		entityData += f',Offers: {offerString(offers)}'
	if hasTradesDefined:
		entityData += nitwitVillagerData
	entityData += '}\n'
	return commands.summonEntity('ssls_npc_maker_mod:npc', entityData=entityData)

def updateNpcCommand(name, offers):
	command = 'data modify entity '
	command += f'@e[type=ssls_npc_maker_mod:npc, name={name}, sort=nearest, limit=1]'
	command += f' Offers set value {offerString(offers)}'
	command += '\n'
	return command

def highlightNpcCommand(name):
	command = 'execute at @p'
	command += f' if entity @e[type=ssls_npc_maker_mod:npc, name={name}, sort=nearest, limit=1]'
	command += f' run effect give @e[type=ssls_npc_maker_mod:npc, name={name}, sort=nearest, limit=1]'
	command += ' minecraft:glowing 30 1 true'
	command += '\n'
	return command

def offerString(offers):
	return f"{{Recipes: [{offerRecipeString(offers)}]}}"

# offer: {villagerItem, villagerQty, playerGive, playerQty}
def offerRecipeString(offers):
	offerRecipeStringOut = ""
	for i, offer in enumerate(offers):
		offerRecipeStringOut += '{'
		offerRecipeStringOut += f'buy: {{id: "{offer[playerGiveKey]}", Count: {offer[playerQtyKey]}}}'
		offerRecipeStringOut += f',sell: {{id: "{offer[villagerItemKey]}", Count: {offer[villagerQtyKey]}}}'
		offerRecipeStringOut += ',maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0'
		offerRecipeStringOut += ', demand: 0, rewardExp: 0'
		offerRecipeStringOut += '}'
		if i < len(offers) - 1:
			offerRecipeStringOut += ', '
	return offerRecipeStringOut
