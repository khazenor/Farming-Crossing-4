// Listen to item registry event
StartupEvents.registry('item', event => {
  // The texture for this item has to be placed in kubejs/assets/kubejs/textures/item/test_item.png
  // If you want a custom item model, you can create one in Blockbench and put it in kubejs/assets/kubejs/models/item/test_item.json
  event.create('kubejs:miles_ticket').displayName('Miles Ticket').maxStackSize(10000)
	event.create('kubejs:voucher_decoration_common').displayName("Common Decoration Collection Voucher").maxStackSize(10000)
	event.create('kubejs:voucher_decoration_rare').displayName("Rare Decoration Collection Voucher").maxStackSize(10000)
	event.create('kubejs:voucher_hat').displayName("Hat Collection Voucher").maxStackSize(10000)
	event.create('kubejs:cooking_certificate').displayName('Chef Certificate')
	event.create('kubejs:animal_certificate').displayName('Animal Certificate')
	event.create('kubejs:fishing_certificate').displayName('Aquarium Certificate')
	event.create('kubejs:housing_certificate').displayName('Housing Certificate')
	event.create('kubejs:mining_certificate').displayName('Museum Certificate')
	event.create('kubejs:sapling_certificate').displayName('Orchard Certificate')
	event.create('kubejs:flower_certificate').displayName('Garden Certificate')
	event.create('kubejs:tellme').displayName('TellMe Debug Item')
	event.create('kubejs:1k_storage_disk_ticket').displayName('1k storage disk ticket')
	event.create('kubejs:4k_storage_disk_ticket').displayName('4k storage disk ticket (72 Miles Tickets)')
	event.create('kubejs:16k_storage_disk_ticket').displayName('16k storage disk ticket (297 Miles Tickets)')
	event.create('kubejs:64k_storage_disk_ticket').displayName('64k storage disk ticket (1215 Miles Tickets)')
	event.create('kubejs:fresh_water').displayName('Fresh Water')
})