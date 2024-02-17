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
	event.create('kubejs:cert_ani_diamond').displayName('Animal Collection Certificate')
	event.create('kubejs:cert_decocom_diamond').displayName('Common Deco Collection Certificate')
	event.create('kubejs:cert_decorare_diamond').displayName('Rare Deco Collection Certificate')
	event.create('kubejs:cert_fish_diamond').displayName('Fishing Collection Certificate')
	event.create('kubejs:cert_hat_diamond').displayName('Hat Collection Certificate')
	event.create('kubejs:cert_cook_diamond').displayName('Chef Certificate')
	event.create('kubejs:cert_flora_diamond').displayName('Flora Compendium Certificate')
	event.create('kubejs:cert_mining_diamond').displayName('Mineral Museum Certificate')
	event.create('kubejs:cert_clothes_diamond').displayName('Clothing Collection Certificate')
})