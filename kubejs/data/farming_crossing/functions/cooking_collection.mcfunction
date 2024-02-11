scoreboard players add @p cooking_collection 1
tellraw @p ["",{"text":"New dish cooked! ("},{"score":{"name":"@p","objective":"cooking_collection"}},{"text":"/191)"}]
