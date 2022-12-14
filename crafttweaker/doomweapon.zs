# small handful of doomweapons we don't like much
import crafttweaker.api.item.IItemStack;

# list of all the items we want to remove, as an array.
var itemsToRemove = [
    <item:doom:argent_axe>,
    <item:doom:argent_bolt>,
    <item:doom:argent_hoe>,
    <item:doom:argent_paxel>,
    <item:doom:argent_pickaxe>,
    <item:doom:argent_shovel>,
    <item:doom:argent_sword>,
    <item:doom:axe_marauder_closed>,
    <item:doom:axe_marauder_open>,
    <item:doom:ballista>,
    <item:doom:bfg_eternal>,
    <item:doom:chainsaw64>,
    <item:doom:chainsaweternal>,
    <item:doom:cruciblesword>,
    <item:doom:cruciblesword_closed>,
    <item:doom:daisy>,
    <item:doom:heavycannon>,
    <item:doom:unmaykr>,
    <item:doom:unmaykr_bolt>
] as IItemStack[];

# defined in grey.zs
gRemoveAndHideList(itemsToRemove);

# Items to hide, for various reasons
var itemsToHide = [
    # wait, nothing here?
] as IItemStack[];

# defined in grey.zs
gHideList(itemsToHide);