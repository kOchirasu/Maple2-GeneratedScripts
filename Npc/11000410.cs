using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000410: Venus
/// </summary>
public class _11000410 : NpcScript {
    internal _11000410(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001731$ 
                // - $MyPCName$, nice to meet you! 
                // $script:0831180407001732$ 
                // - I hope we can clean up this forest trail once more...  
                return true;
            case 10:
                // $script:0831180407001733$ 
                // - This forest trail is the only path connecting us to $npcName:11000407[gender:0]$, and the monsters are making it unusable. $npcName:11000409[gender:0]$ and I are working to clear them out. 
                return true;
            default:
                return true;
        }
    }
}
