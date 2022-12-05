# Python 3.11, I think
from typing import Any
from typing import cast
from typing import Optional

# so the way this works is
# the mods kind of manage themselves as a data structure
# and I'll just output a document later

class SomeCollectible:
    def __init__(self, id:str, aliases:set[str]):
        self.id:str = id
        self.aliases:set[str] = aliases
        self.aliases.add(self.id)
    def answersTo(self, name:str):
        return name in self.aliases
    def addAlias(self, name:str):
        self.aliases.add(name)
    def canonize(self, name:str):
        return self.id

class SomeCollection:
    def __init__(self):
        self.contents:list[SomeCollectible] = []
    def add(self, collectible:SomeCollectible):
        self.contents.append(collectible)
    def get(self, name:str) -> Optional[SomeCollectible]:
        ret:Optional[SomeCollectible] = None
        found:bool                    = False
        
        for item in self.contents:
            if (not found):
                if item.answersTo(name):
                    found = True
                    ret = item
        
        return ret
    # I'm lazy, let's write a pair of operators for id lookup
    
    # conditional "in" support
    def __contains__(self, name:str) -> bool:
        ret:bool = False
        
        for item in self.contents:
            if (not ret):
                if item.answersTo(name):
                    ret = True
        
        return ret
    
    # dict key accessor - well, if you contain something, you can access it
    # via key
    def __getitem__(self, key:str):
        return self.get(key)

class User(SomeCollectible):
    # I've collected the entire class O.o
    pass

class UserList(SomeCollection):
    def get(self, name:str) -> Optional[User]:
        # literally the only change is a casting
        return cast(User,super().get(name))

class Vote(SomeCollectible):
    def __init__(self, user:User, vote:bool, notes:list[str]=[], reason:str=""):
        super().__init__(user.id, set())
        self.user:User = user
        self.notes:list[str] = notes
        self.vote:bool = vote
        self.reason:str = reason

class VoteCollection(SomeCollection):
    def get(self, userName:str) -> Optional[Vote]:
        # literally the only change is a casting
        return cast(Vote,super().get(userName))

class Status:
    def __init__(self, included:bool, reason:str=""):
        self.included = included
        self.reason = reason

class Version(SomeCollectible):
    def __init__(self, id:str):
        super().__init__(id, set())
        self.votes = VoteCollection()
    def addVote(self, vote:Vote):
        self.votes.add(vote)

class VersionCollection(SomeCollection):
    # oops, I did it again
    pass

class Mod(SomeCollectible):
    def __init__(self, name:str, curseId:str):
        super().__init__(name, set())
        self.curseId:str = curseId

class ModCollection(SomeCollection):
    pass

class FeatureSet(SomeCollection):
    def __init__(self, name:str):
        super().__init__()
        self.name = name



################################################################################
# FINALLY ACTUALLY DO STUFF                                                    #
################################################################################

# init
# ------------------------------------------------------------------------------

mods:ModCollection = ModCollection()

# mods
# ------------------------------------------------------------------------------

mods.add(Mod("", ""))
mods.add(Mod("AFK Manager", "406231")) # AFK Notification - this is a good
mods.add(Mod("Anger Management", "305211"))
mods.add(Mod("Anvil Data", "377327"))
mods.add(Mod("Anvil Recipes", "396185"))
mods.add(Mod("Anvil Tweaks", "331921"))
mods.add(Mod("Auto Attack", "358906")) # omniswing
mods.add(Mod("AutoLoot Bow Enchantment", "407528")) # is looting already in the game? craft tweak?
mods.add(Mod("Banjo-Kazooie Mod", "345227"))
mods.add(Mod("Banknotes", "411359")) # currency mod I might jack
mods.add(Mod("Banner Capes", "376768"))
mods.add(Mod("Batteries", "425605")) # I want to not need it
mods.add(Mod("Bedrock Blocks", "410982")) # modpack utilities
mods.add(Mod("Behgameon RPG Additions", "353478"))
mods.add(Mod("Better FPS Graph-Vanilla Profiler", "416139")) # debugging
mods.add(Mod("Better Mod Button", "386293")) # Half function, half eye candy
mods.add(Mod("Better Model Properties", "407660")) # eye candy?
mods.add(Mod("Better Sprinting", "227409")) # prefer better controls, no 1.16.5
mods.add(Mod("Blast Processing Forge", "392147"))   # CraftTweak?
mods.add(Mod("Blockshifter [Forge]", "405572")) # just use create?
mods.add(Mod("Blood Particles", "336320"))
mods.add(Mod("Boost Boots", "407575")) # double jump
mods.add(Mod("Builder's Backpacks", "419564"))
mods.add(Mod("Campfire Torches", "333389")) # crafttweaker?
mods.add(Mod("ClearView", "379020"))
mods.add(Mod("Clockout", "357108")) # logic
mods.add(Mod("Coal Nugget", "314663"))      # CraftTweak? Fabric.
mods.add(Mod("Coffee mod", "381715")) # COFFEE COFFEE COFFEE
mods.add(Mod("Color Unchained", "391781")) # social
mods.add(Mod("Colorful Campfire", "403083")) # eye candy
mods.add(Mod("Cotton Resources", "321104")) # modpack tools
mods.add(Mod("Crazy Generators", "409861")) # alternative FE generation
mods.add(Mod("CreeperFix", "341131")) # antigrief
mods.add(Mod("Cr³stal", "393992")) # April fool's! ... resource packs?
mods.add(Mod("Custom Selection Box", "308792")) # fabric? Sad eye candy noises
mods.add(Mod("Dark Tribute", "360591"))
mods.add(Mod("Darker Loading Screen", "385783")) # eye candy
mods.add(Mod("De-Extinction Mod", "301016")) # clever girl
mods.add(Mod("Deadly End Phantoms", "374034")) # move phantoms to the end
mods.add(Mod("Deborder",            "368466"))      # Fabric
mods.add(Mod("Demagnetize", "301356"))
mods.add(Mod("Diamond In The Rough", "348203")) # Craft tweaker?
mods.add(Mod("Dig", "252707")) # modpack tooling
mods.add(Mod("Dimensional Bridge Builder", "392480"))
mods.add(Mod("DontPushMe", "391724"))
mods.add(Mod("Dragon-Free Tipped Arrows", "407358")) # Craft tweaker?
mods.add(Mod("Earth2Java [FORGE]", "387396"))
mods.add(Mod("Effect Pads", "415173")) # course work?
mods.add(Mod("Equivalence [FABRIC]", "384762"))     # Fabric
mods.add(Mod("FallingBlocks", "411662")) # modpack utilities
mods.add(Mod("Fast Furnace minus Replacement", "389989"))
mods.add(Mod("Fence Hopper",        "364368"))      # Fabric
mods.add(Mod("Filters Reborn", "397288")) # MrCrayfish vs Creative Tab bloat
mods.add(Mod("Finite Water & Infinite Lava", "353794"))
mods.add(Mod("Fire Smelting", "377009")) # yes plz
mods.add(Mod("Flaming Arrows", "360140"))
mods.add(Mod("Flowing Background", "380476")) # vendor fancy
mods.add(Mod("Food Tweaks", "364926")) # modpack utilities
mods.add(Mod("Gestus", "401707"))   # social
mods.add(Mod("Glass mod",           "386451"))      # CraftTweak?
mods.add(Mod("Gulliver Reloaded",   "371246"))
mods.add(Mod("Hanami", "399717")) # Abnormals sakura forest
mods.add(Mod("Heroic Death", "403054")) # custom death messages
mods.add(Mod("Hidden Items", "398679")) # craft tweaker?
mods.add(Mod("Howling Wolves", "400360"))
mods.add(Mod("Hwyla", "253449"))    # discontinued :(
mods.add(Mod("Improved Stations (Forge)", "361348"))
mods.add(Mod("Infinity Works With All Arrows", "363710"))
mods.add(Mod("InfinityMendingBow", "409176"))
mods.add(Mod("Inventory Overlay", "298073")) # QOL
mods.add(Mod("Inventory Profiles", "347463"))
mods.add(Mod("Inventory Tweaks Renewed", "383070"))
mods.add(Mod("JsonifyCraft", "349863")) # Modpack tools +1!
mods.add(Mod("Just Enough Beacons", "352622")) # JEI ... rewrite into patchouli?
mods.add(Mod("Just Sword Blocking", "406495"))
mods.add(Mod("Komodo Dragon Mod", "409076"))
mods.add(Mod("Last Stand", "409803")) # and PMMO?
mods.add(Mod("Lava Smelting", "371543"))
mods.add(Mod("Lil' Beaver", "417492"))
mods.add(Mod("Login Toast", "408383"))
mods.add(Mod("Looting Bow Enchantment", "409430")) # is looting already in the game? craft tweak?
mods.add(Mod("MC-144761 Fix", "399720")) # still broken as of 1.18.2
mods.add(Mod("MC-5169 Fix", "405963")) # sadly still broken in 1.19
mods.add(Mod("Mechanized Steam Power", "373653"))
mods.add(Mod("Mine Factory", "411094")) # a factorio future?
mods.add(Mod("Missing Structure Fix", "414261")) # nuther bug
mods.add(Mod("Mod Blocker [FORGE]", "383434")) # yeah, we should
mods.add(Mod("Modpack Addons", "404322")) # modpack authoring
mods.add(Mod("Mosquitoes!", "407216"))
mods.add(Mod("MrCrayfish's Vehicle Mod", "286660"))
mods.add(Mod("Neon Craft 2 Mod", "566953"))
mods.add(Mod("Neon Craft Mod", "399802"))
mods.add(Mod("No Potion Offset (Fabric/Forge)", "361550")) # yet another bug fix
mods.add(Mod("No Soliciting", "354425")) # denies wandering trader spawns
mods.add(Mod("NonZero Farming",     "366925"))      # unnecessary past 20w12a
mods.add(Mod("OpLock", "397381"))
mods.add(Mod("PMMO and NBT Compat", "470136"))
mods.add(Mod("Pacifist Mobs", "412929"))
mods.add(Mod("Pandoras Creatures", "342804"))
mods.add(Mod("Paranoia", "414417")) # who needs sanity?
mods.add(Mod("Pehkui", "319596"))
mods.add(Mod("PersistentChatHistory", "390878")) # social
mods.add(Mod("Pick Pick", "398082"))
mods.add(Mod("Player Skull Drops", "392452"))
mods.add(Mod("Portal Tags", "399075"))
mods.add(Mod("Programmer's Chest", "415632")) # Reimplement in computercraft?!?
mods.add(Mod("Project MMO and Cooking for Blockheads Compat", "431915"))
mods.add(Mod("Project MMO", "353935")) # Uh?
mods.add(Mod("Project Table", "325309")) # modpack tools
mods.add(Mod("Pumice", "391594")) # Fabric, but can we craft tweak it?
mods.add(Mod("Pumpkin Spice Everything", "410697"))
mods.add(Mod("Pumpkin Spice Latte", "276907"))
mods.add(Mod("Recently Used", "404472")) # creative QOL
mods.add(Mod("RedLogic", "420245")) # logic gates
mods.add(Mod("Redstone Lantern (Forge)", "408777"))
mods.add(Mod("Redstone Pixels", "410621"))
mods.add(Mod("Redstone Quit", "393112")) # idle qol
mods.add(Mod("Repairable Anvils", "393742")) # Fabric... probably.
mods.add(Mod("Replacement Finder", "379873")) # debugging
mods.add(Mod("Resource Pack Organizer", "246231")) # eye candy
mods.add(Mod("Rock Candy", "221743"))
mods.add(Mod("Ropes Mod!", "358557")) # terrariaesque rope
mods.add(Mod("SCP: Obscurity", "368964")) # N/A
mods.add(Mod("Sculk Sensor", "412691")) # earlty sculk sensor
mods.add(Mod("SetPlayerData", "362577")) # fabric
mods.add(Mod("Shared Health", "414333"))
mods.add(Mod("ShouldCraft", "403741")) # crafttweaker?
mods.add(Mod("Shulker's Super Simple Structure System", "401397")) # mod pack tooling
mods.add(Mod("Shut Up Console", "396776"))
mods.add(Mod("Shutup Experimental Settings!", "407174"))
mods.add(Mod("SignEdit", "278701"))
mods.add(Mod("Simple Colored Blocks", "324192"))
mods.add(Mod("SimpleHarvest", "240783"))
mods.add(Mod("SimplySamples", "418493")) # modpack tooling
mods.add(Mod("Skyblock Enchantments", "391364"))
mods.add(Mod("Slabs to Blocks", "413834")) # crafttweaker?
mods.add(Mod("Smarter HUD", "394281")) # eye candy
mods.add(Mod("Smooth Chunks", "415285")) # eye candy
mods.add(Mod("Smooth Scrolling Everywhere (Forge)", "327056")) # eye candy
mods.add(Mod("Sneak Through Berries", "324945")) # QOL
mods.add(Mod("Sockets", "363481"))
mods.add(Mod("Sound Filters", "222789")) # ear candy
mods.add(Mod("Spiders 2.0", "410497")) # more intimidating spiders
mods.add(Mod("Stuff A Sock In It", "262137"))
mods.add(Mod("Switcheroo", "396505")) # equipment autoswapping
mods.add(Mod("TIS-3D-Additions", "416105"))
mods.add(Mod("Table Tweaks", "402861"))
mods.add(Mod("Tabula – Minecraft Modeler", "229092"))
mods.add(Mod("Taffy - Shield", "381069")) # QOL
mods.add(Mod("Tag, You're It!", "419415"))
mods.add(Mod("TapeMouse", "223065")) # ban it
mods.add(Mod("Telekinesis", "389704"))
mods.add(Mod("Text Coloriser Plugin", "366398"))
mods.add(Mod("Text Damage Indicators", "407673")) # Eye candy/data
mods.add(Mod("The Birdwatching Mod", "316581"))
mods.add(Mod("Thresher", "382011"))
mods.add(Mod("Through The Looking Glass", "398027")) # og pleaseeeee
mods.add(Mod("Tiered Magnets", "326998")) # item magnetism
mods.add(Mod("Tiled Floor Mod", "415592"))
mods.add(Mod("Towers Of The Wild", "386415"))
mods.add(Mod("Tux", "403923"))
mods.add(Mod("UnderwaterGrass", "410824")) # crafttweak?
mods.add(Mod("Unicornia (Zoey's Mod)", "407847")) # yes please
mods.add(Mod("Unifix", "384713")) # item unification, can we craft tweak?
mods.add(Mod("WTBW Core", "357092")) # ???
mods.add(Mod("WTBW Machines", "357095"))
mods.add(Mod("WTBW Tools", "357092")) # greenhouse?
mods.add(Mod("Wasted Death", "393044")) # memetic
mods.add(Mod("Water Strainer", "246939"))
mods.add(Mod("WorldEdit",           "225608"))      # FAWE instead?
mods.add(Mod("WorldWands", "404989")) # worldedit QOL
mods.add(Mod("Your Options Shall Be Respected (YOSBR)", "374274"))
mods.add(Mod("animalium", "263442")) # rats bruh
mods.add(Mod("better-fps-graph", "399699")) # debugging
mods.add(Mod("lost-and-found", "427349")) # this plus void bag = item obtain frequency?
mods.add(Mod("monopoly", "404223")) # unification of items... Crafttweak?
mods.add(Mod("narrator off", "412000")) # QOL
mods.add(Mod("prone", "392471"))
mods.add(Mod("superbackpacks", "395965")) # no, there are better ones
mods.add(Mod("varied mob textures", "399578")) # Mob eye candy

# Armor Toughness Bar - ui goodness
# Images - from the web!
# Interactio - In-World Crafting with Datapacks! - modpack tool
# Lumens - solr panels
# Naughty Or Nice
# SorceryCraft - balanced magic?!!

'''
absolutely
----------
https://www.curseforge.com/minecraft/mc-mods/advanced-chimneys
https://www.curseforge.com/minecraft/mc-mods/advanced-peripherals
https://www.curseforge.com/minecraft/mc-mods/ageing-spawners
https://www.curseforge.com/minecraft/mc-mods/aquaculture
https://www.curseforge.com/minecraft/mc-mods/arrows-info
https://www.curseforge.com/minecraft/mc-mods/bad-wither-no-cookie-reloaded
https://www.curseforge.com/minecraft/mc-mods/baubley-heart-canisters
https://www.curseforge.com/minecraft/mc-mods/better-muffling
https://www.curseforge.com/minecraft/mc-mods/botania
https://www.curseforge.com/minecraft/mc-mods/cc-tweaked
https://www.curseforge.com/minecraft/mc-mods/colds-magic-mirror-forge
https://www.curseforge.com/minecraft/mc-mods/color-me-outlines
https://www.curseforge.com/minecraft/mc-mods/cultures
https://www.curseforge.com/minecraft/mc-mods/custom-skyboxes
https://www.curseforge.com/minecraft/mc-mods/dimension-stacking-rifts           dimension stacking
https://www.curseforge.com/minecraft/mc-mods/discernment
https://www.curseforge.com/minecraft/mc-mods/dont-run-with-scissors
https://www.curseforge.com/minecraft/mc-mods/dynamiclights-reforged
https://www.curseforge.com/minecraft/mc-mods/dynamictrees
https://www.curseforge.com/minecraft/mc-mods/elemental-combat
https://www.curseforge.com/minecraft/mc-mods/elenai-dodge-2
https://www.curseforge.com/minecraft/mc-mods/everyday-commands
https://www.curseforge.com/minecraft/mc-mods/firework-rocket-duration
https://www.curseforge.com/minecraft/mc-mods/flux-networks
https://www.curseforge.com/minecraft/mc-mods/hardcore-torches-forge
https://www.curseforge.com/minecraft/mc-mods/in-control
https://www.curseforge.com/minecraft/mc-mods/infinite-pollution-filter
https://www.curseforge.com/minecraft/mc-mods/itemphysic
https://www.curseforge.com/minecraft/mc-mods/jei-integration
https://www.curseforge.com/minecraft/mc-mods/kobolds
https://www.curseforge.com/minecraft/mc-mods/krypton-reforged
https://www.curseforge.com/minecraft/mc-mods/langsplit
https://www.curseforge.com/minecraft/mc-mods/linkingbooks
https://www.curseforge.com/minecraft/mc-mods/mambience
https://www.curseforge.com/minecraft/mc-mods/noluck                             who needs luck anyway
https://www.curseforge.com/minecraft/mc-mods/open-loader                        forcefully loaded resource pack shipping
https://www.curseforge.com/minecraft/mc-mods/paragliders
https://www.curseforge.com/minecraft/mc-mods/pehkui
https://www.curseforge.com/minecraft/mc-mods/pollutant-pump
https://www.curseforge.com/minecraft/mc-mods/pollutant-pump
https://www.curseforge.com/minecraft/mc-mods/pollution-of-the-realms
https://www.curseforge.com/minecraft/mc-mods/quickstack
https://www.curseforge.com/minecraft/mc-mods/radon
https://www.curseforge.com/minecraft/mc-mods/rpg-parties
https://www.curseforge.com/minecraft/mc-mods/spare-parts                        modpack useless pieces
https://www.curseforge.com/minecraft/mc-mods/tax-free-levels
https://www.curseforge.com/minecraft/mc-mods/textrues-rubidium-options
https://www.curseforge.com/minecraft/mc-mods/total-darkness
https://www.curseforge.com/minecraft/mc-mods/worm-industries
https://www.curseforge.com/minecraft/mc-mods/you-cant-see-me-forge              100% clear glass, like oldschool zawa exhibit glass

baubles et al
-------------


bugfix - bug
------------
https://www.curseforge.com/minecraft/mc-mods/advancements-debug
https://www.curseforge.com/minecraft/mc-mods/chunk-saving-fix
https://www.curseforge.com/minecraft/mc-mods/client-side-noteblocks
https://www.curseforge.com/minecraft/mc-mods/dispenser-crash-fix
https://www.curseforge.com/minecraft/mc-mods/dupe-fixes
https://www.curseforge.com/minecraft/mc-mods/erroring-entity-remover
https://www.curseforge.com/minecraft/mc-mods/fastopenlinksandfolders
https://www.curseforge.com/minecraft/mc-mods/fix-selected-item-text
https://www.curseforge.com/minecraft/mc-mods/flyspeedpatch
https://www.curseforge.com/minecraft/mc-mods/keepheadnames
https://www.curseforge.com/minecraft/mc-mods/raised
https://www.curseforge.com/minecraft/mc-mods/randompatches-forge
https://www.curseforge.com/minecraft/mc-mods/recipebuffers
https://www.curseforge.com/minecraft/mc-mods/semitranslucency-fix
https://www.curseforge.com/minecraft/mc-mods/smoothcoasters
https://www.curseforge.com/minecraft/mc-mods/spoorn-extras
https://www.curseforge.com/minecraft/mc-mods/storage-drawers-crash-fix
https://www.curseforge.com/minecraft/mc-mods/thread-safety
https://www.curseforge.com/minecraft/mc-mods/too-fast

bugfix - sanity
---------------
https://www.curseforge.com/minecraft/mc-mods/loginshield
https://www.curseforge.com/minecraft/mc-mods/hot-or-not                         burn players for carrying hot liquids
https://www.curseforge.com/minecraft/mc-mods/jukefix                            Sound emits from center of jukebox
https://www.curseforge.com/minecraft/mc-mods/real-sleep                         ticks process when you sleep
https://www.curseforge.com/minecraft/mc-mods/slipperywalls                      Spiders can't climb ice
https://www.curseforge.com/minecraft/mc-mods/splash-water                       bottled Water extinguishes fire
https://www.curseforge.com/minecraft/mc-mods/towelette                          universalize waterlogging
https://www.curseforge.com/minecraft/mc-mods/more-sound-config                  switch sound device at runtime
https://www.curseforge.com/minecraft/mc-mods/villagerfollow                     villagers follow you if you have an emerald in your hand

building
--------
https://www.curseforge.com/minecraft/mc-mods/angel-block
https://www.curseforge.com/minecraft/mc-mods/buildercraft                       C&B compatible
https://www.curseforge.com/minecraft/mc-mods/chisel                             chisel proper
https://www.curseforge.com/minecraft/mc-mods/chunkborders                       better chunkborders visualization
https://www.curseforge.com/minecraft/mc-mods/colourplate
https://www.curseforge.com/minecraft/mc-mods/dungeon-based-spawners
https://www.curseforge.com/minecraft/mc-mods/icu
https://www.curseforge.com/minecraft/mc-mods/misc-tab
https://www.curseforge.com/minecraft/mc-mods/obj-importer
https://www.curseforge.com/minecraft/mc-mods/simple-chimney                     Actual chimney
https://www.curseforge.com/minecraft/mc-mods/versatile-portals
https://www.curseforge.com/minecraft/mc-mods/essential-modern-construction-block-32px-edition
https://www.curseforge.com/minecraft/mc-mods/lantern-colors
https://www.curseforge.com/minecraft/mc-mods/delicate-and-dainty


building - light blocks
-----------------------
https://www.curseforge.com/minecraft/mc-mods/light-blocks-for-java-1-14-4
https://www.curseforge.com/minecraft/mc-mods/light-block-forge
https://www.curseforge.com/minecraft/mc-mods/light-it-up
https://www.curseforge.com/minecraft/mc-mods/light-blocks-from-1-17

building - sound
----------------
https://www.curseforge.com/minecraft/mc-mods/clef

changes - alarming to most players
----------------------------------
https://www.curseforge.com/minecraft/mc-mods/antiportals                        disable end and nether portals

commands
--------
https://www.curseforge.com/minecraft/mc-mods/more-mc-commands

config
------
https://www.curseforge.com/minecraft/mc-mods/start-script

curious
-------
https://www.curseforge.com/minecraft/mc-mods/block-log
https://www.curseforge.com/minecraft/mc-mods/cartographer
https://www.curseforge.com/minecraft/mc-mods/composing
https://www.curseforge.com/minecraft/mc-mods/dummy-players                      how far did it go? Can I message them?
https://www.curseforge.com/minecraft/mc-mods/dynamic-difficulty
https://www.curseforge.com/minecraft/mc-mods/fantasy-mounts
https://www.curseforge.com/minecraft/mc-mods/game-of-life-3d-forge
https://www.curseforge.com/minecraft/mc-mods/glimmering-potions
https://www.curseforge.com/minecraft/mc-mods/illumination
https://www.curseforge.com/minecraft/mc-mods/linfox-dimension-stack
https://www.curseforge.com/minecraft/mc-mods/magic-mirrors-forge
https://www.curseforge.com/minecraft/mc-mods/mo-structures-forge
https://www.curseforge.com/minecraft/mc-mods/modifiers
https://www.curseforge.com/minecraft/mc-mods/more-death-messages
https://www.curseforge.com/minecraft/mc-mods/potion-snowballs
https://www.curseforge.com/minecraft/mc-mods/proxies
https://www.curseforge.com/minecraft/mc-mods/quiver-redux                       better than my favorite?
https://www.curseforge.com/minecraft/mc-mods/risingtides                        mostly animals
https://www.curseforge.com/minecraft/mc-mods/simplified-commands
https://www.curseforge.com/minecraft/mc-mods/traverse-reforged
https://www.curseforge.com/minecraft/mc-mods/virus-disease-mod                  covid-19 as a mod?
https://www.curseforge.com/minecraft/mc-mods/wesleys-roguelike-dungeons
https://www.curseforge.com/minecraft/mc-mods/feudal-weaponry-forge

debug
-----
https://www.curseforge.com/minecraft/mc-mods/chunk-profiler
https://www.curseforge.com/minecraft/mc-mods/craftdumper                        it's kind of like tellme, just not the same.
https://www.curseforge.com/minecraft/mc-mods/packet-logger
https://www.curseforge.com/minecraft/mc-mods/worldgeneration-profiler
https://www.curseforge.com/minecraft/mc-mods/blame

enchantments
------------
https://www.curseforge.com/minecraft/mc-mods/curse
https://www.curseforge.com/minecraft/mc-mods/time-to-die                        Quite unique
https://www.curseforge.com/minecraft/mc-mods/enchantable                        Enchantments by Mr. Crayfish

extensions - AE2
----------------
https://www.curseforge.com/minecraft/mc-mods/mass-inscriber                     put whole stacks of inputs into inscriber

extensions - computer mods
--------------------------
https://www.curseforge.com/minecraft/mc-mods/bperipherals
https://www.curseforge.com/minecraft/mc-mods/storage-for-computercraft          integrate AE2

extensions - create
-------------------
https://www.curseforge.com/minecraft/mc-mods/create-addon                       Balance for armor and drill addons
https://www.curseforge.com/minecraft/mc-mods/cogwheel-tweaker                   tweak cogwheels

extensions - farmer's delight
-----------------------------
https://www.curseforge.com/minecraft/mc-mods/the-irregular-chef                 integration. Environmental, Neapolitan, upgrae aquatic, atmospheric, and so on mods I never install.

eye candy
---------
https://www.curseforge.com/minecraft/mc-mods/soul-sand-grabbing-effect
https://www.curseforge.com/minecraft/mc-mods/hyper-lighting-colored-light-core

fabric
------
https://www.curseforge.com/minecraft/mc-mods/damage-threshold
https://www.curseforge.com/minecraft/mc-mods/dihydrogen-monoxide-reloaded
https://www.curseforge.com/minecraft/mc-mods/mechanix
https://www.curseforge.com/minecraft/mc-mods/mubble                             but it's mit licensed
https://www.curseforge.com/minecraft/mc-mods/quadz
https://www.curseforge.com/minecraft/mc-mods/attach-leads-to-logs               fabric - tie off animal leads to logs
https://www.curseforge.com/minecraft/mc-mods/bow-tie                            write datapacks in non-json formats

holiday
-------
https://www.curseforge.com/minecraft/mc-mods/linden-files                       halloween
https://www.curseforge.com/minecraft/mc-mods/snowed-in                          christmas

holiday - halloween
-------------------
https://www.curseforge.com/minecraft/mc-mods/projectfrightmod

imports - 1.17
--------------
https://www.curseforge.com/minecraft/mc-mods/lush-caves-and-axolotls            axolotls
https://www.curseforge.com/minecraft/mc-mods/deepslate                          deepslate
https://www.curseforge.com/minecraft/mc-mods/axolotl-and-axolotl-in-a-bucket    axolotls

imports - factorio
------------------
https://www.curseforge.com/minecraft/mc-mods/transport                          trains?
https://www.curseforge.com/minecraft/mc-mods/simplerail                         trains?
https://www.curseforge.com/minecraft/mc-mods/factoriores                        drills? conveyor belts? pickers?

imports - the legend of zelda
-----------------------------
https://www.curseforge.com/minecraft/mc-mods/heart-container-mod                actual heart containers as upgrading hp

imports - luigi's mansion
-------------------------
https://www.curseforge.com/minecraft/mc-mods/scootys-luigis-mansion-mod

imports - portal
----------------
https://www.curseforge.com/minecraft/mc-mods/portal-blocks-remake
https://www.curseforge.com/minecraft/mc-mods/portal-gels

imports - risk of rain
----------------------
https://www.curseforge.com/minecraft/mc-mods/risk-of-rain-mod

imports - scp
-------------
https://www.curseforge.com/minecraft/mc-mods/scp-555                            scp 00555 "corpse magnet"

imports - Steven Universe
-------------------------
https://www.curseforge.com/minecraft/mc-mods/crystal-universe                   steven universe

just computer craft it
----------------------
https://www.curseforge.com/minecraft/mc-mods/communication                      chat box
https://www.curseforge.com/minecraft/mc-mods/smart-observer                     observer, but for specific blocks
https://www.curseforge.com/minecraft/mc-mods/universal-power-monitor-upm        little harder but sure it's doable

just craft tweak it
-------------------
https://www.curseforge.com/minecraft/mc-mods/more-baked-foods
https://www.curseforge.com/minecraft/mc-mods/spill
https://www.curseforge.com/minecraft/mc-mods/craftable-bell
https://www.curseforge.com/minecraft/mc-mods/craftable-nametags
https://www.curseforge.com/minecraft/mc-mods/crafteos
https://www.curseforge.com/minecraft/mc-mods/crafting-glitches
https://www.curseforge.com/minecraft/mc-mods/dungeon-discs
https://www.curseforge.com/minecraft/mc-mods/easypaths
https://www.curseforge.com/minecraft/mc-mods/gudunify
https://www.curseforge.com/minecraft/mc-mods/instant-unify
https://www.curseforge.com/minecraft/mc-mods/make-trident
https://www.curseforge.com/minecraft/mc-mods/mo-recipes-a-mod-by-skittlq
https://www.curseforge.com/minecraft/mc-mods/pheonixs-craftable-nametags
https://www.curseforge.com/minecraft/mc-mods/turtle-shell-drop
https://www.curseforge.com/minecraft/mc-mods/unified-resources
https://www.curseforge.com/minecraft/mc-mods/wool-to-string
https://www.curseforge.com/minecraft/mc-mods/apple-pie-ported

just patchouli it
-----------------
https://www.curseforge.com/minecraft/mc-mods/farmers-delight-cookbook-addon
https://www.curseforge.com/minecraft/mc-mods/jei-professions
https://www.curseforge.com/minecraft/mc-mods/just-enough-vehicles
https://www.curseforge.com/minecraft/mc-mods/minecraftwikimod                   ARR, but you can't copyright pure facts
https://www.curseforge.com/minecraft/mc-mods/patchouli-jam

just reimplement it somehow
---------------------------
https://www.curseforge.com/minecraft/mc-mods/enderio-alloys                     Literally metal alloys
https://www.curseforge.com/minecraft/mc-mods/soul-blaze
https://www.curseforge.com/minecraft/mc-mods/xp-coins

maybe should
------------
https://www.curseforge.com/minecraft/mc-mods/architects-palette
https://www.curseforge.com/minecraft/mc-mods/auto-look
https://www.curseforge.com/minecraft/mc-mods/better-advancements
https://www.curseforge.com/minecraft/mc-mods/better-combat-by-daedelus
https://www.curseforge.com/minecraft/mc-mods/better-drowning                    breathing, drowning, "And more"
https://www.curseforge.com/minecraft/mc-mods/bobacraft
https://www.curseforge.com/minecraft/mc-mods/callable-horses
https://www.curseforge.com/minecraft/mc-mods/coffee-break                       coffee.
https://www.curseforge.com/minecraft/mc-mods/datafixerslayer
https://www.curseforge.com/minecraft/mc-mods/extra-progressions                 storm
https://www.curseforge.com/minecraft/mc-mods/fat-experience-orbs
https://www.curseforge.com/minecraft/mc-mods/ffs-fancy-fluid-storage
https://www.curseforge.com/minecraft/mc-mods/grieflogger
https://www.curseforge.com/minecraft/mc-mods/inventorio-forge
https://www.curseforge.com/minecraft/mc-mods/kaupenjoes-all-consuming-grey-goo
https://www.curseforge.com/minecraft/mc-mods/lootr
https://www.curseforge.com/minecraft/mc-mods/mine-and-slash-reloaded
https://www.curseforge.com/minecraft/mc-mods/minecoprocessors
https://www.curseforge.com/minecraft/mc-mods/mobs-attempt-parkour
https://www.curseforge.com/minecraft/mc-mods/modern-elevators-and-escalators
https://www.curseforge.com/minecraft/mc-mods/modifiers
https://www.curseforge.com/minecraft/mc-mods/nbt-peripheral
https://www.curseforge.com/minecraft/mc-mods/nosleep
https://www.curseforge.com/minecraft/mc-mods/overworld-two-forge
https://www.curseforge.com/minecraft/mc-mods/pet-revival
https://www.curseforge.com/minecraft/mc-mods/pipez
https://www.curseforge.com/minecraft/mc-mods/pistorder
https://www.curseforge.com/minecraft/mc-mods/pixelmon
https://www.curseforge.com/minecraft/mc-mods/projecte-integration               "but why?"
https://www.curseforge.com/minecraft/mc-mods/rawore
https://www.curseforge.com/minecraft/mc-mods/rereskillable                      lock using crap behind skills
https://www.curseforge.com/minecraft/mc-mods/sbm-fluid-gun                      literally just a liquid gun
https://www.curseforge.com/minecraft/mc-mods/simple-fried-egg-forge
https://www.curseforge.com/minecraft/mc-mods/thirsty-water-forrge
https://www.curseforge.com/minecraft/mc-mods/trashcans-reborn
https://www.curseforge.com/minecraft/mc-mods/triumph
https://www.curseforge.com/minecraft/mc-mods/vanilla-biomes
https://www.curseforge.com/minecraft/mc-mods/waystones2waypoints

mobs
----
https://www.curseforge.com/minecraft/mc-mods/mobswhynot
https://www.curseforge.com/minecraft/mc-mods/mobtastic

mobs - animals
--------------
https://www.curseforge.com/minecraft/mc-mods/deer-mod                           deer
https://www.curseforge.com/minecraft/mc-mods/colds-ostriches-forge              ostritch
https://www.curseforge.com/minecraft/mc-mods/morris-animal-mod
https://curseforge.com/minecraft/mc-mods/wizards-animals
https://www.curseforge.com/minecraft/mc-mods/ancient-animals
https://www.curseforge.com/minecraft/mc-mods/better-wilderness

mobs - behaviors
----------------
https://www.curseforge.com/minecraft/mc-mods/progressive-aggressivity           scaling aggressive behavior
https://www.curseforge.com/minecraft/mc-mods/fishy-bears                        polar bears go fishing
https://www.curseforge.com/minecraft/mc-mods/herd-mentality                     animals react as a herd

mobs - hostile
--------------
https://www.curseforge.com/minecraft/mc-mods/direbats-forge                     dire bats
https://www.curseforge.com/minecraft/mc-mods/trap-chest                         Mimic

modpack util
------------
https://www.curseforge.com/minecraft/mc-mods/bigger-structures                  remove structure block limit
https://www.curseforge.com/minecraft/mc-mods/block-renderer                     create reference png of block on demand
https://www.curseforge.com/minecraft/mc-mods/block-swap
https://www.curseforge.com/minecraft/mc-mods/blockcarpentry
https://www.curseforge.com/minecraft/mc-mods/build-guide
https://www.curseforge.com/minecraft/mc-mods/carve-this                         tell worldcarver to carve material
https://www.curseforge.com/minecraft/mc-mods/cauldron-recipes                   datapack cauldron recipes
https://www.curseforge.com/minecraft/mc-mods/colormatic
https://www.curseforge.com/minecraft/mc-mods/creative-tweaker
https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-cem
https://www.curseforge.com/minecraft/mc-mods/custom-machinery
https://www.curseforge.com/minecraft/mc-mods/datapackrecipemaker                make recipes via datapack
https://www.curseforge.com/minecraft/mc-mods/default-servers                    ship servers via datapack
https://www.curseforge.com/minecraft/mc-mods/devside-tools
https://www.curseforge.com/minecraft/mc-mods/dimensional-paintings
https://www.curseforge.com/minecraft/mc-mods/essential-features                 modpack lightning smelting
https://www.curseforge.com/minecraft/mc-mods/fast-projectile-fix
https://www.curseforge.com/minecraft/mc-mods/framedblocks
https://www.curseforge.com/minecraft/mc-mods/ftb-quests-forge
https://www.curseforge.com/minecraft/mc-mods/game-stages-conditions
https://www.curseforge.com/minecraft/mc-mods/harmful-stonecutters               stonecutters and "others" actually hurt player for standing on
https://www.curseforge.com/minecraft/mc-mods/infinity-item-editor
https://www.curseforge.com/minecraft/mc-mods/jsmacros                           programmable mods
https://www.curseforge.com/minecraft/mc-mods/just-enough-effects                data on status effects
https://www.curseforge.com/minecraft/mc-mods/kaleido
https://www.curseforge.com/minecraft/mc-mods/kubejs                             programmable mods
https://www.curseforge.com/minecraft/mc-mods/legendary-tooltips
https://www.curseforge.com/minecraft/mc-mods/mcdj                               add songs as oggs
https://www.curseforge.com/minecraft/mc-mods/mob-heads                          datapack mobheads
https://www.curseforge.com/minecraft/mc-mods/mobifier
https://www.curseforge.com/minecraft/mc-mods/mobserve                           includes a "looking at" trigger
https://www.curseforge.com/minecraft/mc-mods/modern-flat-colored-blocks
https://www.curseforge.com/minecraft/mc-mods/multiblocked
https://www.curseforge.com/minecraft/mc-mods/music-triggers
https://www.curseforge.com/minecraft/mc-mods/nbt-ingredient-predicate           recipe partial predicate matching
https://www.curseforge.com/minecraft/mc-mods/ob-tooltips
https://www.curseforge.com/minecraft/mc-mods/potion-stacker                     configurable potion stacking
https://www.curseforge.com/minecraft/mc-mods/quests-additions
https://www.curseforge.com/minecraft/mc-mods/rarities
https://www.curseforge.com/minecraft/mc-mods/resourceful-bees
https://www.curseforge.com/minecraft/mc-mods/set-my-name
https://www.curseforge.com/minecraft/mc-mods/simple-machinery                   dead machinery
https://www.curseforge.com/minecraft/mc-mods/simple-museum                      resource packed museum displays
https://www.curseforge.com/minecraft/mc-mods/suffocate                          ???
https://www.curseforge.com/minecraft/mc-mods/terra-world-generator              data driven world generation
https://www.curseforge.com/minecraft/mc-mods/time-stages
https://www.curseforge.com/minecraft/mc-mods/tips
https://www.curseforge.com/minecraft/mc-mods/vault-research                     research-based locking system for mods

modpack util - branding
-----------------------
https://www.curseforge.com/minecraft/mc-mods/better-game-menu
https://www.curseforge.com/minecraft/mc-mods/betterpanoramas                    change title panorama
https://www.curseforge.com/minecraft/mc-mods/modern-loading-screen
https://www.curseforge.com/minecraft/mc-mods/random-title                       random title bar
https://www.curseforge.com/minecraft/mc-mods/custom-start-screen
https://www.curseforge.com/minecraft/mc-mods/spiffy-hud-forge

no, but alternates to stuff we do use
-------------------------------------
https://www.curseforge.com/minecraft/mc-mods/blockrunner                        happy trails
https://www.curseforge.com/minecraft/mc-mods/chunknogobyebye                    chickenchunk
https://www.curseforge.com/minecraft/mc-mods/cryness-double-slabs               kleeslabs?
https://www.curseforge.com/minecraft/mc-mods/fast-redstone-utilities            projectred
https://www.curseforge.com/minecraft/mc-mods/forcefield                         securitycraft?
https://www.curseforge.com/minecraft/mc-mods/travellers-map                     xaero
https://www.curseforge.com/minecraft/mc-mods/vanilladeathchest-forge            corail
https://www.curseforge.com/minecraft/mc-mods/voxelmap                           Xaero
https://www.curseforge.com/minecraft/mc-mods/colds-block-detector               the one scanner storm never uses

qol
---
https://www.curseforge.com/minecraft/mc-mods/abacus
https://www.curseforge.com/minecraft/mc-mods/cauldron-riptide
https://www.curseforge.com/minecraft/mc-mods/silencer
https://www.curseforge.com/minecraft/mc-mods/smooth-boot-forge

qol - basic mechanics
----------------------
https://www.curseforge.com/minecraft/mc-mods/better-jumping                     hold velocity through a jump
https://www.curseforge.com/minecraft/mc-mods/coyotelib-double-jump
https://www.curseforge.com/minecraft/mc-mods/better-minecart-rotation-forge
https://www.curseforge.com/minecraft/mc-mods/sbm-punt-animal                    push animals around

qol - data exposure
-------------------
https://www.curseforge.com/minecraft/mc-mods/actual-attack-speed                better dps calc in inventory
https://www.curseforge.com/minecraft/mc-mods/hitmarker-forge
https://www.curseforge.com/minecraft/mc-mods/nbt-advanced-tooltips
https://www.curseforge.com/minecraft/mc-mods/startup-qol
https://www.curseforge.com/minecraft/mc-mods/torch-optimizer                    light levels

qol - loot
----------
https://www.curseforge.com/minecraft/mc-mods/pillagers                          you get villager loot by murdering pillagers

qol - rf et al
--------------
https://www.curseforge.com/minecraft/mc-mods/odd-power                          unusual generators
https://www.curseforge.com/minecraft/mc-mods/pigawatts-reloaded                 I'm wondering if we can do this with Create?
https://www.curseforge.com/minecraft/mc-mods/powah

qol - worldgen
--------------
https://www.curseforge.com/minecraft/mc-mods/save-my-stronghold
https://www.curseforge.com/minecraft/mc-mods/no-bedrock                         destroys bedrock layer entirely
https://www.curseforge.com/minecraft/mc-mods/ore-recursion-forge                (vanilla) ore can also gen inside sand, gravel, dirt
qol - worldedit
---------------
https://www.curseforge.com/minecraft/mc-mods/world-edit-axe-recipe              worldedit wand

single object
-------------
https://www.curseforge.com/minecraft/mc-mods/postlamp                           lamp light to slap anywhere

social
------
https://www.curseforge.com/minecraft/mc-mods/chat-embeds
https://www.curseforge.com/minecraft/mc-mods/door-knocker-forge
https://www.curseforge.com/minecraft/mc-mods/forge-survival-spectator
https://www.curseforge.com/minecraft/mc-mods/kirara

social - death
--------------
https://www.curseforge.com/minecraft/mc-mods/deathquotes-death-quotes

Veganism
https://www.curseforge.com/minecraft/mc-mods/no-breeding
https://www.curseforge.com/minecraft/mc-mods/spare-the-animals

worldgen - biomes (vanilla)
---------------------------
https://www.curseforge.com/minecraft/mc-mods/voyage

unsorted
--------
https://www.curseforge.com/minecraft/mc-mods/a-man-with-plushies
https://www.curseforge.com/minecraft/mc-mods/aardvarks-better-bovines
https://www.curseforge.com/minecraft/mc-mods/aardvarks-retro-party-stuff
https://www.curseforge.com/minecraft/mc-mods/abyssal-depths
https://www.curseforge.com/minecraft/mc-mods/aggressive-furries
https://www.curseforge.com/minecraft/mc-mods/apophis
https://www.curseforge.com/minecraft/mc-mods/arrowheads
https://www.curseforge.com/minecraft/mc-mods/atlantis
https://www.curseforge.com/minecraft/mc-mods/back-tools
https://www.curseforge.com/minecraft/mc-mods/banneradditions                    modpack
https://www.curseforge.com/minecraft/mc-mods/blueflame
https://www.curseforge.com/minecraft/mc-mods/bobby-forge
https://www.curseforge.com/minecraft/mc-mods/book-display
https://www.curseforge.com/minecraft/mc-mods/borkler
https://www.curseforge.com/minecraft/mc-mods/chain-suspension-forge
https://www.curseforge.com/minecraft/mc-mods/charm-reforged
https://www.curseforge.com/minecraft/mc-mods/charmonium-reforged
https://www.curseforge.com/minecraft/mc-mods/chest-locator
https://www.curseforge.com/minecraft/mc-mods/classes                            pmmo
https://www.curseforge.com/minecraft/mc-mods/coffee-plus
https://www.curseforge.com/minecraft/mc-mods/colwater
https://www.curseforge.com/minecraft/mc-mods/command-alias-creator
https://www.curseforge.com/minecraft/mc-mods/cozy-coniferous
https://www.curseforge.com/minecraft/mc-mods/custom-entity-models-kaimyentity-reborn
https://www.curseforge.com/minecraft/mc-mods/detailedhp
https://www.curseforge.com/minecraft/mc-mods/dndmc
https://www.curseforge.com/minecraft/mc-mods/drill
https://www.curseforge.com/minecraft/mc-mods/effect-enchantments
https://www.curseforge.com/minecraft/mc-mods/electrona
https://www.curseforge.com/minecraft/mc-mods/enhanced-block-entities
https://www.curseforge.com/minecraft/mc-mods/entitled
https://www.curseforge.com/minecraft/mc-mods/evolved-rpg
https://www.curseforge.com/minecraft/mc-mods/fakeblocks                         no collision
https://www.curseforge.com/minecraft/mc-mods/full-turtle-armor
https://www.curseforge.com/minecraft/mc-mods/grapple-hooks
https://www.curseforge.com/minecraft/mc-mods/gun-mode-mod
https://www.curseforge.com/minecraft/mc-mods/hardcore-battle-towers
https://www.curseforge.com/minecraft/mc-mods/heads-down-display
https://www.curseforge.com/minecraft/mc-mods/helpful-commands
https://www.curseforge.com/minecraft/mc-mods/hwylafastfix
https://www.curseforge.com/minecraft/mc-mods/ibe-editor
https://www.curseforge.com/minecraft/mc-mods/infinite-anvil
https://www.curseforge.com/minecraft/mc-mods/instantlava
https://www.curseforge.com/minecraft/mc-mods/isometric-renders
https://www.curseforge.com/minecraft/mc-mods/lil-critters
https://www.curseforge.com/minecraft/mc-mods/lost-trinkets
https://www.curseforge.com/minecraft/mc-mods/modular-powersuits
https://www.curseforge.com/minecraft/mc-mods/more-red                           we don't use it
https://www.curseforge.com/minecraft/mc-mods/more-red-computercraft-integration we don't use more red
https://www.curseforge.com/minecraft/mc-mods/more-wires
https://www.curseforge.com/minecraft/mc-mods/old-elysium/screenshots
https://www.curseforge.com/minecraft/mc-mods/once-upon-a-stroll
https://www.curseforge.com/minecraft/mc-mods/painting-cycle
https://www.curseforge.com/minecraft/mc-mods/parkour-recorder                   does it work on a server?
https://www.curseforge.com/minecraft/mc-mods/particlegenerator
https://www.curseforge.com/minecraft/mc-mods/path-under-gates
https://www.curseforge.com/minecraft/mc-mods/pew-pew-towers-forge-edition
https://www.curseforge.com/minecraft/mc-mods/platos-transporters
https://www.curseforge.com/minecraft/mc-mods/prp
https://www.curseforge.com/minecraft/mc-mods/raidmeter
https://www.curseforge.com/minecraft/mc-mods/rats
https://www.curseforge.com/minecraft/mc-mods/redstone-bits
https://www.curseforge.com/minecraft/mc-mods/refined-pipes
https://www.curseforge.com/minecraft/mc-mods/rope-bridge
https://www.curseforge.com/minecraft/mc-mods/scuffys-pvz-mod
https://www.curseforge.com/minecraft/mc-mods/shatter
https://www.curseforge.com/minecraft/mc-mods/shelf
https://www.curseforge.com/minecraft/mc-mods/shfa-same-hitboxes-for-all
https://www.curseforge.com/minecraft/mc-mods/silent-gear
https://www.curseforge.com/minecraft/mc-mods/silents-mechanisms
https://www.curseforge.com/minecraft/mc-mods/simply-improved-terrain
https://www.curseforge.com/minecraft/mc-mods/simply-tea
https://www.curseforge.com/minecraft/mc-mods/slapmap
https://www.curseforge.com/minecraft/mc-mods/splatcraft
https://www.curseforge.com/minecraft/mc-mods/sticks-debugged
https://www.curseforge.com/minecraft/mc-mods/stumble-upon-campsites
https://www.curseforge.com/minecraft/mc-mods/stupendous-travels                 happy trails
https://www.curseforge.com/minecraft/mc-mods/superslegend
https://www.curseforge.com/minecraft/mc-mods/taterzens-forge
https://www.curseforge.com/minecraft/mc-mods/tbplugin
https://www.curseforge.com/minecraft/mc-mods/theatrical
https://www.curseforge.com/minecraft/mc-mods/time-to-live
https://www.curseforge.com/minecraft/mc-mods/total-darkness
https://www.curseforge.com/minecraft/mc-mods/towers-of-the-wild
https://www.curseforge.com/minecraft/mc-mods/travelers-titles
https://www.curseforge.com/minecraft/mc-mods/traversal
https://www.curseforge.com/minecraft/mc-mods/trevor-creatures-reborn
https://www.curseforge.com/minecraft/mc-mods/two-players-one-horse
https://www.curseforge.com/minecraft/mc-mods/useful-axolotl
https://www.curseforge.com/minecraft/mc-mods/useful-bat
https://www.curseforge.com/minecraft/mc-mods/useful-polar-bears
https://www.curseforge.com/minecraft/mc-mods/variant16x-biomesyougo
https://www.curseforge.com/minecraft/mc-mods/waila-harvestability
https://www.curseforge.com/minecraft/mc-mods/walking-canes
https://www.curseforge.com/minecraft/mc-mods/water-erosion
https://www.curseforge.com/minecraft/mc-mods/wiki-zoomer
https://www.curseforge.com/minecraft/mc-mods/witherutils-actor
https://www.curseforge.com/minecraft/mc-mods/yungs-better-caves
https://www.curseforge.com/minecraft/mc-mods/zawa-evolved
'''