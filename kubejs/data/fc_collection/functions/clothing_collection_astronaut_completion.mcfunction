scoreboard players add @p clothing_collection_astronaut_completion 1
tellraw @p ["", {"text":"Astronaut Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_astronaut_completion"}}, {"text":"/4)"}]
tellraw @p [""]
