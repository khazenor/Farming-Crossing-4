MoreJSEvents.wandererTrades((event) => {
	event.removeVanillaTrades(1)
	event.removeVanillaTrades(2)
	event.removeModdedTrades(1)
	event.removeModdedTrades(2)
})

MoreJSEvents.villagerTrades((event) => {
	event.removeModdedTrades(["villagersplus:horticulturist"], 1)
	event.removeModdedTrades(["villagersplus:horticulturist"], 2)
	event.removeModdedTrades(["villagersplus:horticulturist"], 3)
	event.removeModdedTrades(["villagersplus:horticulturist"], 4)
	event.removeModdedTrades(["villagersplus:horticulturist"], 5)
	event.removeVanillaTrades(["villagersplus:horticulturist"], 1)
	event.removeVanillaTrades(["villagersplus:horticulturist"], 2)
	event.removeVanillaTrades(["villagersplus:horticulturist"], 3)
	event.removeVanillaTrades(["villagersplus:horticulturist"], 4)
	event.removeVanillaTrades(["villagersplus:horticulturist"], 5)
})