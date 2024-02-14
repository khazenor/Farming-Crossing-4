scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p animal_watching_snowy_completion 1
tellraw @p ["", {"text":"Snowy Completion ("}, {"score":{"name":"@p","objective":"animal_watching_snowy_completion"}}, {"text":"/4)"}]
tellraw @p [""]
