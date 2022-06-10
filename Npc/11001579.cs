using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001579: Landevian
/// </summary>
public class _11001579 : NpcScript {
    internal _11001579(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006067$ 
                // - Ah, $MyPCName$! 
                return true;
            case 10:
                // $script:0515180307006121$ 
                // - This is not going to be easy.  
                return true;
            case 20:
                // $script:0524142307006215$ 
                // - This is not going to be easy.  
                return true;
            default:
                return true;
        }
    }
}
