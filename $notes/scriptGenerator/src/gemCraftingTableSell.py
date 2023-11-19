from lib import craftingTableSell
from input import gemPrices

def genGemCraftingTableSell():
	craftingTableSell.generateCraftingSellRecipes(gemPrices.gemPrices, 2, 'gem', 's')
