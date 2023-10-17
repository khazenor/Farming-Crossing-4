MoreJSEvents.wandererTrades((event) => {
	event.removeVanillaTrades(1)
	event.removeVanillaTrades(2)
	event.removeModdedTrades(1)
	event.removeModdedTrades(2)
})

MoreJSEvents.villagerTrades((event) => {
	event.removeModdedTrades(["morevillagers:florist"], 1)
	event.removeModdedTrades(["morevillagers:florist"], 2)
	event.removeModdedTrades(["morevillagers:florist"], 3)
	event.removeModdedTrades(["morevillagers:florist"], 4)
	event.removeModdedTrades(["morevillagers:florist"], 5)
	event.removeVanillaTrades(["morevillagers:florist"], 1)
	event.removeVanillaTrades(["morevillagers:florist"], 2)
	event.removeVanillaTrades(["morevillagers:florist"], 3)
	event.removeVanillaTrades(["morevillagers:florist"], 4)
	event.removeVanillaTrades(["morevillagers:florist"], 5)
})