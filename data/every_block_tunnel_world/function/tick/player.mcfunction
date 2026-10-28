execute if predicate {type:"minecraft:location_check",predicate:{position:{y:{min:319}}}} run function every_block_tunnel_world:player_spawn

scoreboard players enable @s block_count
execute if score @s block_count matches 1 run function every_block_tunnel_world:player/block_count
execute if score @s block_count matches 2.. run title @s actionbar ""
execute if score @s block_count matches 2.. run scoreboard players reset @s block_count