scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p plains_completion 1
tellraw @p ["", {"text":"Plains Completion ("}, {"score":{"name":"@p","objective":"plains_completion"}}, {"text":"/10)"}]
tellraw @p [""]
