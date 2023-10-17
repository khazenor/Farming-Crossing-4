
def categoryStore(entries, category, categoryName, categoryItem):
	return {
		"customCategories": {
			category: {
				"name": categoryName,
				"icon": {
					"item": categoryItem
				}
			}
		},
		"customEntries": entries
	}

def entry(item, itemCount, payment, paymentCount, category):
	return {
		"output": { "item": item, "count": itemCount },
		"payment": { "item": payment, "count": paymentCount },
		"category": category
	}

def entryNBT(item, itemCount, payment, paymentCount, category, itemNBT):
	return {
		"output": { "item": item, "count": itemCount, 'nbt': itemNBT},
		"payment": { "item": payment, "count": paymentCount },
		"category": category
	}