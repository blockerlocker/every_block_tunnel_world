import os, sys, urllib.request
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