StartupEvents.registry('sound_event', event => {
  event.create("farming_crossing_records:oneul_april_daisy")
  event.create("farming_crossing_records:oneul_around_midnight")
  event.create("farming_crossing_records:oneul_autumn_blessing")
  event.create("farming_crossing_records:oneul_autumn_breeze")
  event.create("farming_crossing_records:oneul_brunch")
  event.create("farming_crossing_records:oneul_bubble")
  event.create("farming_crossing_records:oneul_byesummer")
  event.create("farming_crossing_records:oneul_canele")
  event.create("farming_crossing_records:oneul_cheeseburger")
  event.create("farming_crossing_records:oneul_chestnut_latte")
  event.create("farming_crossing_records:oneul_chocolate_world")
  event.create("farming_crossing_records:oneul_chuseok")
  event.create("farming_crossing_records:oneul_cloudy_rain")
  event.create("farming_crossing_records:oneul_cookie_tree")
  event.create("farming_crossing_records:oneul_dreamy")
  event.create("farming_crossing_records:oneul_flamingo")
  event.create("farming_crossing_records:oneul_floating_marshmallow")
  event.create("farming_crossing_records:oneul_full_moon")
  event.create("farming_crossing_records:oneul_get_up")
  event.create("farming_crossing_records:oneul_gift")
  event.create("farming_crossing_records:oneul_happy_reindeer")
  event.create("farming_crossing_records:oneul_joy")
  event.create("farming_crossing_records:oneul_melon_bread")
  event.create("farming_crossing_records:oneul_miracle_morning")
  event.create("farming_crossing_records:oneul_mistletoe")
  event.create("farming_crossing_records:oneul_moonlight")
  event.create("farming_crossing_records:oneul_morning_peppermint")
  event.create("farming_crossing_records:oneul_painting")
  event.create("farming_crossing_records:oneul_pajama")
  event.create("farming_crossing_records:oneul_raindrops")
  event.create("farming_crossing_records:oneul_roommate")
  event.create("farming_crossing_records:oneul_sandwich")
  event.create("farming_crossing_records:oneul_smile_peach")
  event.create("farming_crossing_records:oneul_snow_dance")
  event.create("farming_crossing_records:oneul_story")
  event.create("farming_crossing_records:oneul_strawberry_dance")
  event.create("farming_crossing_records:oneul_summer_vacation")
  event.create("farming_crossing_records:oneul_surf")
  event.create("farming_crossing_records:oneul_tiramisu")
  event.create("farming_crossing_records:oneul_umbrella")
  event.create("farming_crossing_records:oneul_vanilla_milkshake")
  event.create("farming_crossing_records:oneul_watermelon_fizz")
  event.create("farming_crossing_records:oneul_weekend_blanket")
  event.create("farming_crossing_records:oneul_winter_glow")
})

StartupEvents.registry('item', event => {
  event.create("kubejs:oneul_april_daisy", "music_disc")
    .song("farming_crossing_records:oneul_april_daisy", 151)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_april_daisy")
    .displayName("Music Disc: Oneul - April Daisy")
    .maxStackSize(64)
  event.create("kubejs:oneul_around_midnight", "music_disc")
    .song("farming_crossing_records:oneul_around_midnight", 107)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_around_midnight")
    .displayName("Music Disc: Oneul - Around Midnight")
    .maxStackSize(64)
  event.create("kubejs:oneul_autumn_blessing", "music_disc")
    .song("farming_crossing_records:oneul_autumn_blessing", 111)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_autumn_blessing")
    .displayName("Music Disc: Oneul - Autumn Blessing")
    .maxStackSize(64)
  event.create("kubejs:oneul_autumn_breeze", "music_disc")
    .song("farming_crossing_records:oneul_autumn_breeze", 112)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_autumn_breeze")
    .displayName("Music Disc: Oneul - Autumn Breeze")
    .maxStackSize(64)
  event.create("kubejs:oneul_brunch", "music_disc")
    .song("farming_crossing_records:oneul_brunch", 111)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_brunch")
    .displayName("Music Disc: Oneul - Brunch")
    .maxStackSize(64)
  event.create("kubejs:oneul_bubble", "music_disc")
    .song("farming_crossing_records:oneul_bubble", 142)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_bubble")
    .displayName("Music Disc: Oneul - Bubble")
    .maxStackSize(64)
  event.create("kubejs:oneul_byesummer", "music_disc")
    .song("farming_crossing_records:oneul_byesummer", 99)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_byesummer")
    .displayName("Music Disc: Oneul - Bye,Summer!")
    .maxStackSize(64)
  event.create("kubejs:oneul_canele", "music_disc")
    .song("farming_crossing_records:oneul_canele", 104)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_canele")
    .displayName("Music Disc: Oneul - Canelé")
    .maxStackSize(64)
  event.create("kubejs:oneul_cheeseburger", "music_disc")
    .song("farming_crossing_records:oneul_cheeseburger", 102)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_cheeseburger")
    .displayName("Music Disc: Oneul - Cheeseburger")
    .maxStackSize(64)
  event.create("kubejs:oneul_chestnut_latte", "music_disc")
    .song("farming_crossing_records:oneul_chestnut_latte", 86)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_chestnut_latte")
    .displayName("Music Disc: Oneul - Chestnut Latte")
    .maxStackSize(64)
  event.create("kubejs:oneul_chocolate_world", "music_disc")
    .song("farming_crossing_records:oneul_chocolate_world", 122)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_chocolate_world")
    .displayName("Music Disc: Oneul - Chocolate World")
    .maxStackSize(64)
  event.create("kubejs:oneul_chuseok", "music_disc")
    .song("farming_crossing_records:oneul_chuseok", 97)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_chuseok")
    .displayName("Music Disc: Oneul - Chuseok")
    .maxStackSize(64)
  event.create("kubejs:oneul_cloudy_rain", "music_disc")
    .song("farming_crossing_records:oneul_cloudy_rain", 126)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_cloudy_rain")
    .displayName("Music Disc: Oneul - Cloudy Rain")
    .maxStackSize(64)
  event.create("kubejs:oneul_cookie_tree", "music_disc")
    .song("farming_crossing_records:oneul_cookie_tree", 121)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_cookie_tree")
    .displayName("Music Disc: Oneul - Cookie Tree")
    .maxStackSize(64)
  event.create("kubejs:oneul_dreamy", "music_disc")
    .song("farming_crossing_records:oneul_dreamy", 134)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_dreamy")
    .displayName("Music Disc: Oneul - Dreamy")
    .maxStackSize(64)
  event.create("kubejs:oneul_flamingo", "music_disc")
    .song("farming_crossing_records:oneul_flamingo", 129)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_flamingo")
    .displayName("Music Disc: Oneul - Flamingo")
    .maxStackSize(64)
  event.create("kubejs:oneul_floating_marshmallow", "music_disc")
    .song("farming_crossing_records:oneul_floating_marshmallow", 93)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_floating_marshmallow")
    .displayName("Music Disc: Oneul - Floating Marshmallow")
    .maxStackSize(64)
  event.create("kubejs:oneul_full_moon", "music_disc")
    .song("farming_crossing_records:oneul_full_moon", 130)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_full_moon")
    .displayName("Music Disc: Oneul - Full Moon")
    .maxStackSize(64)
  event.create("kubejs:oneul_get_up", "music_disc")
    .song("farming_crossing_records:oneul_get_up", 107)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_get_up")
    .displayName("Music Disc: Oneul - Get up")
    .maxStackSize(64)
  event.create("kubejs:oneul_gift", "music_disc")
    .song("farming_crossing_records:oneul_gift", 104)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_gift")
    .displayName("Music Disc: Oneul - Gift")
    .maxStackSize(64)
  event.create("kubejs:oneul_happy_reindeer", "music_disc")
    .song("farming_crossing_records:oneul_happy_reindeer", 84)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_happy_reindeer")
    .displayName("Music Disc: Oneul - Happy Reindeer")
    .maxStackSize(64)
  event.create("kubejs:oneul_joy", "music_disc")
    .song("farming_crossing_records:oneul_joy", 109)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_joy")
    .displayName("Music Disc: Oneul - Joy")
    .maxStackSize(64)
  event.create("kubejs:oneul_melon_bread", "music_disc")
    .song("farming_crossing_records:oneul_melon_bread", 91)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_melon_bread")
    .displayName("Music Disc: Oneul - Melon Bread")
    .maxStackSize(64)
  event.create("kubejs:oneul_miracle_morning", "music_disc")
    .song("farming_crossing_records:oneul_miracle_morning", 81)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_miracle_morning")
    .displayName("Music Disc: Oneul - Miracle Morning")
    .maxStackSize(64)
  event.create("kubejs:oneul_mistletoe", "music_disc")
    .song("farming_crossing_records:oneul_mistletoe", 86)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_mistletoe")
    .displayName("Music Disc: Oneul - Mistletoe")
    .maxStackSize(64)
  event.create("kubejs:oneul_moonlight", "music_disc")
    .song("farming_crossing_records:oneul_moonlight", 148)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_moonlight")
    .displayName("Music Disc: Oneul - Moonlight")
    .maxStackSize(64)
  event.create("kubejs:oneul_morning_peppermint", "music_disc")
    .song("farming_crossing_records:oneul_morning_peppermint", 116)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_morning_peppermint")
    .displayName("Music Disc: Oneul - Morning Peppermint")
    .maxStackSize(64)
  event.create("kubejs:oneul_painting", "music_disc")
    .song("farming_crossing_records:oneul_painting", 107)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_painting")
    .displayName("Music Disc: Oneul - Painting")
    .maxStackSize(64)
  event.create("kubejs:oneul_pajama", "music_disc")
    .song("farming_crossing_records:oneul_pajama", 81)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_pajama")
    .displayName("Music Disc: Oneul - Pajama")
    .maxStackSize(64)
  event.create("kubejs:oneul_raindrops", "music_disc")
    .song("farming_crossing_records:oneul_raindrops", 101)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_raindrops")
    .displayName("Music Disc: Oneul - Raindrops")
    .maxStackSize(64)
  event.create("kubejs:oneul_roommate", "music_disc")
    .song("farming_crossing_records:oneul_roommate", 139)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_roommate")
    .displayName("Music Disc: Oneul - Roommate")
    .maxStackSize(64)
  event.create("kubejs:oneul_sandwich", "music_disc")
    .song("farming_crossing_records:oneul_sandwich", 314)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_sandwich")
    .displayName("Music Disc: Oneul - Sandwich")
    .maxStackSize(64)
  event.create("kubejs:oneul_smile_peach", "music_disc")
    .song("farming_crossing_records:oneul_smile_peach", 94)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_smile_peach")
    .displayName("Music Disc: Oneul - Smile Peach")
    .maxStackSize(64)
  event.create("kubejs:oneul_snow_dance", "music_disc")
    .song("farming_crossing_records:oneul_snow_dance", 148)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_snow_dance")
    .displayName("Music Disc: Oneul - Snow Dance")
    .maxStackSize(64)
  event.create("kubejs:oneul_story", "music_disc")
    .song("farming_crossing_records:oneul_story", 114)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_story")
    .displayName("Music Disc: Oneul - Story")
    .maxStackSize(64)
  event.create("kubejs:oneul_strawberry_dance", "music_disc")
    .song("farming_crossing_records:oneul_strawberry_dance", 82)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_strawberry_dance")
    .displayName("Music Disc: Oneul - Strawberry Dance")
    .maxStackSize(64)
  event.create("kubejs:oneul_summer_vacation", "music_disc")
    .song("farming_crossing_records:oneul_summer_vacation", 109)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_summer_vacation")
    .displayName("Music Disc: Oneul - Summer Vacation")
    .maxStackSize(64)
  event.create("kubejs:oneul_surf", "music_disc")
    .song("farming_crossing_records:oneul_surf", 112)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_surf")
    .displayName("Music Disc: Oneul - Surf")
    .maxStackSize(64)
  event.create("kubejs:oneul_tiramisu", "music_disc")
    .song("farming_crossing_records:oneul_tiramisu", 99)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_tiramisu")
    .displayName("Music Disc: Oneul - Tiramisu")
    .maxStackSize(64)
  event.create("kubejs:oneul_umbrella", "music_disc")
    .song("farming_crossing_records:oneul_umbrella", 77)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_umbrella")
    .displayName("Music Disc: Oneul - Umbrella")
    .maxStackSize(64)
  event.create("kubejs:oneul_vanilla_milkshake", "music_disc")
    .song("farming_crossing_records:oneul_vanilla_milkshake", 90)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_vanilla_milkshake")
    .displayName("Music Disc: Oneul - Vanilla Milkshake")
    .maxStackSize(64)
  event.create("kubejs:oneul_watermelon_fizz", "music_disc")
    .song("farming_crossing_records:oneul_watermelon_fizz", 75)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_watermelon_fizz")
    .displayName("Music Disc: Oneul - Watermelon Fizz")
    .maxStackSize(64)
  event.create("kubejs:oneul_weekend_blanket", "music_disc")
    .song("farming_crossing_records:oneul_weekend_blanket", 123)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_weekend_blanket")
    .displayName("Music Disc: Oneul - Weekend Blanket")
    .maxStackSize(64)
  event.create("kubejs:oneul_winter_glow", "music_disc")
    .song("farming_crossing_records:oneul_winter_glow", 83)
    .analogOutput(1)
    .texture("farming_crossing_records:item/oneul_winter_glow")
    .displayName("Music Disc: Oneul - Winter Glow")
    .maxStackSize(64)
})