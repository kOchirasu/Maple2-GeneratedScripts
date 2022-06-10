using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001568: Ishura
/// </summary>
public class _11001568 : NpcScript {
    internal _11001568(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006056$ 
                // - Ah, $MyPCName$!
                return true;
            case 10:
                // $script:0515180307006111$ 
                // - We can't give up yet. There's still so much to do!
                return true;
            case 20:
                // $script:0524142307006212$ 
                // - We can't give up yet. There's still too much to do!
                return true;
            default:
                return true;
        }
    }
}
