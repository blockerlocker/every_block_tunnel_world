forceload add 0 0 15 15
fill 0 0 0 15 15 15 air strict
fill 7 0 7 8 0 8 torch strict
setworldspawn 7 0 7
gamerule respawn_radius 0

function every_block_tunnel_world:build_tunnel

data modify storage every_block_tunnel_world:state initialized set value true