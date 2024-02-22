MoreJSEvents.wandererTrades((event) => {
	event.removeVanillaTrades(1)
	event.removeVanillaTrades(2)
	event.removeModdedTrades(1)
	event.removeModdedTrades(2)
})

MoreJSEvents.villagerTrades((event) => {
	event.removeModdedTrades(["non_wandering_trader:traveller"], 1)
	event.removeModdedTrades(["non_wandering_trader:traveller"], 2)
	event.removeModdedTrades(["non_wandering_trader:traveller"], 3)
	event.removeModdedTrades(["non_wandering_trader:traveller"], 4)
	event.removeModdedTrades(["non_wandering_trader:traveller"], 5)
	event.removeVanillaTrades(["non_wandering_trader:traveller"], 1)
	event.removeVanillaTrades(["non_wandering_trader:traveller"], 2)
	event.removeVanillaTrades(["non_wandering_trader:traveller"], 3)
	event.removeVanillaTrades(["non_wandering_trader:traveller"], 4)
	event.removeVanillaTrades(["non_wandering_trader:traveller"], 5)
})