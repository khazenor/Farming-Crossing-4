// Listen to item registry event
StartupEvents.registry('item', event => {
  // The texture for this item has to be placed in kubejs/assets/kubejs/textures/item/test_item.png
  // If you want a custom item model, you can create one in Blockbench and put it in kubejs/assets/kubejs/models/item/test_item.json
  event.create('kubejs:miles_ticket').displayName('Miles Ticket').maxStackSize(10000)
	event.create('kubejs:tellme').displayName('TellMe Debug Item')
	event.create('kubejs:1k_storage_disk_ticket').displayName('1k storage disk ticket')
	event.create('kubejs:4k_storage_disk_ticket').displayName('4k storage disk ticket (72 Miles Tickets)')
	event.create('kubejs:16k_storage_disk_ticket').displayName('16k storage disk ticket (297 Miles Tickets)')
	event.create('kubejs:64k_storage_disk_ticket').displayName('64k storage disk ticket (1215 Miles Tickets)')
	event.create('kubejs:cert_ani_diamond').displayName('Diamond Animal Collection Certificate')
	event.create('kubejs:cert_ani_gold').displayName('Golden Animal Collection Certificate')
	event.create('kubejs:cert_ani_iron').displayName('Iron Animal Collection Certificate')
	event.create('kubejs:cert_ani_stone').displayName('Stone Animal Collection Certificate')
	event.create('kubejs:cert_ani_wood').displayName('Wooden Animal Collection Certificate')
	event.create('kubejs:cert_decocom_diamond').displayName('Diamond Common Deco Collection Certificate')
	event.create('kubejs:cert_decocom_gold').displayName('Golden Common Deco Collection Certificate')
	event.create('kubejs:cert_decocom_iron').displayName('Iron Common Deco Collection Certificate')
	event.create('kubejs:cert_decocom_stone').displayName('Stone Common Deco Collection Certificate')
	event.create('kubejs:cert_decocom_wood').displayName('Wooden Common Deco Collection Certificate')
	event.create('kubejs:cert_decorare_diamond').displayName('Diamond Rare Deco Collection Certificate')
	event.create('kubejs:cert_decorare_gold').displayName('Golden Rare Deco Collection Certificate')
	event.create('kubejs:cert_decorare_iron').displayName('Iron Rare Deco Collection Certificate')
	event.create('kubejs:cert_decorare_stone').displayName('Stone Rare Deco Collection Certificate')
	event.create('kubejs:cert_decorare_wood').displayName('Wooden Rare Deco Collection Certificate')
	event.create('kubejs:cert_fish_diamond').displayName('Diamond Fishing Collection Certificate')
	event.create('kubejs:cert_fish_gold').displayName('Golden Fishing Collection Certificate')
	event.create('kubejs:cert_fish_iron').displayName('Iron Fishing Collection Certificate')
	event.create('kubejs:cert_fish_stone').displayName('Stone Fishing Collection Certificate')
	event.create('kubejs:cert_fish_wood').displayName('Wooden Fishing Collection Certificate')
	event.create('kubejs:cert_hat_diamond').displayName('Diamond Hat Collection Certificate')
	event.create('kubejs:cert_hat_gold').displayName('Golden Hat Collection Certificate')
	event.create('kubejs:cert_hat_iron').displayName('Iron Hat Collection Certificate')
	event.create('kubejs:cert_hat_stone').displayName('Stone Hat Collection Certificate')
	event.create('kubejs:cert_hat_wood').displayName('Wooden Hat Collection Certificate')
	event.create('kubejs:cert_cook_diamond').displayName('Diamond Chef Certificate')
	event.create('kubejs:cert_cook_gold').displayName('Golden Chef Certificate')
	event.create('kubejs:cert_cook_iron').displayName('Iron Chef Certificate')
	event.create('kubejs:cert_cook_stone').displayName('Stone Chef Certificate')
	event.create('kubejs:cert_cook_wood').displayName('Wooden Chef Certificate')
	event.create('kubejs:cert_flora_diamond').displayName('Diamond Flora Compendium Certificate')
	event.create('kubejs:cert_flora_gold').displayName('Golden Flora Compendium Certificate')
	event.create('kubejs:cert_flora_iron').displayName('Iron Flora Compendium Certificate')
	event.create('kubejs:cert_flora_stone').displayName('Stone Flora Compendium Certificate')
	event.create('kubejs:cert_flora_wood').displayName('Wooden Flora Compendium Certificate')
	event.create('kubejs:cert_mining_diamond').displayName('Diamond Mineral Museum Certificate')
	event.create('kubejs:cert_mining_gold').displayName('Golden Mineral Museum Certificate')
	event.create('kubejs:cert_mining_iron').displayName('Iron Mineral Museum Certificate')
	event.create('kubejs:cert_mining_stone').displayName('Stone Mineral Museum Certificate')
	event.create('kubejs:cert_mining_wood').displayName('Wooden Mineral Museum Certificate')
})