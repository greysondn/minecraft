import crafttweaker.api.block.material.MCMaterial;
import crafttweaker.api.blocks.MCBlock;
import crafttweaker.api.blocks.MCBlockState;
import crafttweaker.api.entity.MCEntityType;
import crafttweaker.api.fluid.MCFluid;
import crafttweaker.api.game.MCGame;
import crafttweaker.api.item.IItemStack;
import crafttweaker.api.mods.ModInfo;
import crafttweaker.api.mods.Mods;
import crafttweaker.api.util.MCResourceLocation;
import crafttweaker.api.tag.MCTag;
import crafttweaker.api.tool.ToolType;

##
# lists the loaded blocks
function gdn_listBlocks() as void
{
    # indents, so I don't have to keep typing longer and longer lines.
    var _i0 = "";
    var _i1 = "    ";
    var _i2 = _i1 + _i1;
    var _i3 = _i2 + _i1;
    var _i4 = _i3 + _i1;
    var _i5 = _i4 + _i1;
    var _i6 = _i5 + _i1;
    var _i7 = _i6 + _i1;
    var _i8 = _i7 + _i1;
    var _i9 = _i8 + _i1;

    print("blocks:");
    
    for _block in game.blocks
    {
        println(_i0 + "-");
        println(_i1 + "registryName:          " + _block.registryName.toString());
        println(_i1 + "translationKey:        " + _block.translationKey);
        println(_i1 + "commandString:         " + _block.commandString);
        println(_i1 + "blastResistance:       " + _block.blastResistance);
        println(_i1 + "canCollide:            " + _block.canCollide);
        println(_i1 + "harvestLevel:          " + _block.harvestLevel); # of the default blockstate
        if (_block.harvestTool != null)
        {
            println(_i1 + "harvestTool:           " + _block.harvestTool.name); # of the default blockstate
        }
        println(_i1 + "jumpFactor:            " + _block.jumpFactor);
        println(_i1 + "lootTable:             " + _block.lootTable);
        println(_i1 + "slipperiness:          " + _block.slipperiness);
        println(_i1 + "speedFactor:           " + _block.speedFactor);
        println(_i1 + "variableOpacity:       " + _block.variableOpacity);
        println(_i1 + "material:              " + _block.material.commandString);
        println(_i1 + "defaultState:          " + _block.defaultState.commandString);

        # validstates
        # we only need the ids - other places can do extensive data
        var _swplist1 = _block.validStates;
        
        if (!_swplist1.isEmpty)
        {
            println(_i1 + "validStates:");
            
            for _swp1 in _swplist1
            {
                println(_i2 + "- " + _swp1.commandString);
            }
        }

        # tags
        # we only need the ids - other places can do extensive data
        var _swplist2 = _block.tags;

        println(_i1 + "tags:");
        
        for _swp2 in _swplist2
        {
            println(_i2 + "- " + _swp2.id.toString());
        }

    }
}



































# blockstates
# directionaxises
# effects
# enchantments
# entityClassifications
# entityTypes
# fluids
# formattings
# items
# potions
# recipeTypes
# villagerProfessions






































##
# check is by
# loadedMods.isModLoaded(modid_as_string)
function gdn_listMods() as void
{
    # indents, so I don't have to keep typing longer and longer lines.
    var _i0 = "";
    var _i1 = "    ";
    var _i2 = _i1 + _i1;
    var _i3 = _i2 + _i1;
    var _i4 = _i3 + _i1;
    var _i5 = _i4 + _i1;
    var _i6 = _i5 + _i1;
    var _i7 = _i6 + _i1;
    var _i8 = _i7 + _i1;
    var _i9 = _i8 + _i1;

    var _modslist = loadedMods.mods;

    if (!_modslist.isEmpty)
    {
        print("mods:");
        
        for _mod in _modslist
        {
            println(_i0 + "-");
            println(_i1 + "modid:       " + _mod.modid);
            println(_i1 + "displayname: " + _mod.displayName);
            println(_i1 + "modid:       " + _mod.namespace);
            println(_i1 + "version:     " + _mod.version);
            
            # blocks
            # we only need the ids - other places can do extensive data
            var _swplist1 = _mod.blocks;
            
            if (!_swplist1.isEmpty)
            {
                println(_i1 + "blocks:");
                
                for _swp1 in _swplist1
                {
                    println(_i2 + "- " + _swp1.registryName.toString());
                }
            }

            # entitytypes
            # we only need the ids - other places can do extensive data
            var _swplist2 = _mod.entitytypes;
            
            if (!_swplist2.isEmpty)
            {
                println(_i1 + "entitytypes:");
                
                for _swp2 in _swplist2
                {
                    println(_i2 + "- " + _swp2.registryName.toString());
                }
            }
            
            # items
            # we only need the ids - other places can do extensive data
            var _swplist3 = _mod.items;
            
            if (!_swplist3.isEmpty)
            {
                println(_i1 + "items:");
                
                for _swp3 in _swplist3
                {
                    println(_i2 + "- " + _swp3.registryName.toString());
                }
            }
            
            #fluids
            # we only need the ids - other places can do extensive data
            var _swplist4 = _mod.items;
            
            if (!_swplist4.isEmpty)
            {
                println(_i1 + "fluids:");
                
                for _swp4 in _swplist4
                {
                    println(_i2 + "- " + _swp4.registryName.toString());
                }
            }
        }
    }
}

println("====================================================================");
println("");

# blocks
gdn_listBlocks();

# mods
gdn_listMods();

println("");
println("===================================================================="); 