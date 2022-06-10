using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000212: David
/// </summary>
public class _11000212 : NpcScript {
    internal _11000212(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000900$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000902$ 
                // - You look like you're still wet behind the ears. Stay out of trouble until you learn the ropes.
                return true;
            case 40:
                // $script:0831180407000903$ 
                // - When you get out of here, move ten cells southeast, and then ten more cells northeast. You'll arrive at a small iron gate. That gate leads to $map:02000156$, where the godfather of Blackstar, $npcName:11000251[gender:0]$, resides.
                return true;
            default:
                return true;
        }
    }
}
