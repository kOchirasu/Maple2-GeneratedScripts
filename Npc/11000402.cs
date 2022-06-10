using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000402: Kiru
/// </summary>
public class _11000402 : NpcScript {
    internal _11000402(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001627$ 
                // - Uuugh...  
                return true;
            case 20:
                // $script:0831180407001629$ 
                // - I need $item:20000060$ from $npcName:21000078$... to cleanse myself... 
                return true;
            case 30:
                // $script:0831180407001630$ 
                // - This toxin... stronger than I thought...  
                return true;
            default:
                return true;
        }
    }
}
