execute at @p if entity @e[type=ssls_npc_maker_mod:npc, name=Sam, sort=nearest, limit=1] run effect give @e[type=ssls_npc_maker_mod:npc, name=Sam, sort=nearest, limit=1] minecraft:glowing 30 1 true
data modify entity @e[type=ssls_npc_maker_mod:npc, name=Sam, sort=nearest, limit=1] Offers set value {Recipes: [{buy: {id: "aquaculture:catfish", Count: 1},sell: {id: "kubejs:miles_ticket", Count: 20},maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0, demand: 0, rewardExp: 0}, {buy: {id: "aquaculture:capitaine", Count: 1},sell: {id: "kubejs:miles_ticket", Count: 20},maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0, demand: 0, rewardExp: 0}, {buy: {id: "aquaculture:tuna", Count: 1},sell: {id: "kubejs:miles_ticket", Count: 20},maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0, demand: 0, rewardExp: 0}, {buy: {id: "aquaculture:arrau_turtle", Count: 1},sell: {id: "kubejs:miles_ticket", Count: 20},maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0, demand: 0, rewardExp: 0}, {buy: {id: "aquaculture:starshell_turtle", Count: 1},sell: {id: "kubejs:miles_ticket", Count: 20},maxUses: 2147483647, xp: 0, uses: 0, priceMultiplier: 0.0, specialPrice: 0, demand: 0, rewardExp: 0}]}
