StartupEvents.registry('sound_event', event => {
  event.create("farming_crossing_records:oneul_autumn_breeze")

})

StartupEvents.registry('item', event => {
  event.create("kubejs:oneul_autumn_breeze", "music_disc")
    .song("farming_crossing_records:oneul_autumn_breeze", 112)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_autumn_breeze")
    .displayName("Oneul - Autumn Breeze")

})