scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/127)"}]
scoreboard players add @p flora_compendium_misc_flora_completion 1
tellraw @p ["", {"text":"Misc Flora Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_misc_flora_completion"}}, {"text":"/13)"}]
tellraw @p [""]
