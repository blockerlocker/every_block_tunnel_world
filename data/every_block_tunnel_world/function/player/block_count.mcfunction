execute summon marker run function every_block_tunnel_world:player/get_z

scoreboard players operation #current_z every_block_tunnel_distance -= #offset every_block_tunnel_distance

execute unless score #current_z every_block_tunnel_distance <= @s every_block_tunnel_distance unless score #current_z every_block_tunnel_distance > #block_count every_block_tunnel_distance run scoreboard players operation @s every_block_tunnel_distance = #current_z every_block_tunnel_distance

title @s actionbar [{score:{objective:"every_block_tunnel_distance",name:"*"},color:green},{text:"/",color:aqua},{score:{objective:"every_block_tunnel_distance",name:"#block_count"},color:green},{text:" blocks",color:yellow}]