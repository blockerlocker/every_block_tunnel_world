For Minecraft 26.4

This data pack is meant to be installed when creating a new world, and creates a world where you spawn at one end of a giant tunnel, filled with every single block in the game in alphabetical order. Can you make it to the other side?

If you have any issues, be sure to create a help thread in my Discord server: https://discord.blocker.locker

## Installing
When creating the world, in the 'World' tab, be sure that 'World Type' is just set to 'Default', and 'Generate Structures' is set to 'OFF'. Then go over to the 'More' tab, hit 'Data Packs', 'Open Pack Folder', paste `every_block_tunnel_world.zip` from the [Releases page](https://github.com/blockerlocker/every_block_tunnel_world/releases) into the folder that pops up, and then back in the game click on the pack so that it is in the 'Selected' list on the right side of the screen. Hit 'Done', then hit 'Create New World', and after a few seconds of generating, you should spawn at the beginning of the tunnel!

## Block Counter
There is an optional block counter display that you can toggle with `/trigger block_count`, which shows you your progress in the tunnel.

## Script Generation
The pack is generated with `generate_tunnel_function.py`, and if you change `latest-snapshot` on line 9 to a specific version, you can re-generate the pack for future versions of the game.

## Upgrading Your World
The way this data pack works is that it generates the entire tunnel the moment the world is created. This means that if you try to update the data pack to a newer version of the game, the tunnel itself will not change, but the numbers used to control the block counter will, making it inaccurate. It is not recommended to try and upgrade your world to a newer version, but if you have to, I suggest using MCA selector to delete all chunks besides the ones you have already been in, generating a completely new world with the updated data pack, and the importing the chunks from the new world into the old world without overwriting the existing chunks. Then be sure to put the newer version of the data pack in the old world so the block count is accurate.

Again, I really don't recommend doing this, and problems could still potentially arise. I will not be able to provide help if you are trying to upgrade your world, it is best that you keep the version of the data pack installed that you created the world with.