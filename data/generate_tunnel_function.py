import os, sys, urllib.request, json
from pathlib import Path


if len(sys.argv) > 1:
    MCVERSION = sys.argv[1]
else:
#### SET MINECRAFT VERSION MANUALLY HERE ####
    MCVERSION = "latest-snapshot"


os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not Path.cwd().name == "data":
    print(f"Working directory not named 'data'! Instead got '{Path.cwd().name}'. bldp generation scripts must be stored within the 'data' folder of your pack to generate correctly!")
    input("Press Enter to exit program...")
    sys.exit()

if not Path("bldp.py").is_file():
    with open("bldp.py", "w", encoding="utf-8") as bldp_main:
        bldp_main.write(urllib.request.urlopen("https://raw.githubusercontent.com/blockerlocker/bldp/main/data/bldp.py").read().decode('utf-8'))

import bldp

MCVERSION = bldp.get_version(MCVERSION)

bldp.remove_path("every_block_tunnel_world/function/build_tunnel.mcfunction")
bldp.remove_path("every_block_tunnel_world/function/load.mcfunction")
bldp.remove_path("../pack.mcmeta")

block_list = bldp.get_registry_data(MCVERSION,"block")

build_tunnel_function = []
z_coordinate = 15

for block in block_list:
    z_coordinate += 1
    build_tunnel_function.append(f"fill 0 0 {z_coordinate} 15 15 {z_coordinate} {block} strict") 

z_coordinate += 1
build_tunnel_function.append(f"fill 0 0 {z_coordinate} 15 15 {z_coordinate+15} light strict") 

build_tunnel_function.insert(0,f"forceload add 0 16 15 {z_coordinate+15}")
build_tunnel_function.append(f"forceload remove all")

bldp.string_to_file("\n".join(build_tunnel_function),"every_block_tunnel_world/function","build_tunnel.mcfunction")

load_function = [
    "execute unless data storage every_block_tunnel_world:state {initialized:true} run function every_block_tunnel_world:initialize",
    "scoreboard objectives add every_block_tunnel_distance dummy",
    "scoreboard players set #offset every_block_tunnel_distance 15",
    f"scoreboard players set #block_count every_block_tunnel_distance {len(block_list)}",
    "scoreboard objectives add block_count trigger"
]

bldp.string_to_file("\n".join(load_function),"every_block_tunnel_world/function","load.mcfunction")

data_pack_format = bldp.get_version_data(MCVERSION)["data_pack_version"]

pack = {
    "pack": {
        "description": "Creates a world that is just a tunnel made up of every block.",
        "min_format": data_pack_format,
        "max_format": data_pack_format
    }
}

bldp.string_to_file(json.dumps(pack, indent=4),"../","pack.mcmeta")