using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004542: Keian
/// </summary>
public class _11004542 : NpcScript {
    internal _11004542(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0110183907012678$ 
                // - I can't believe my luck...
                return true;
            case 10:
                // $script:0110183907012679$ 
                // - I can't believe my luck...
                // $script:0110183907012680$ 
                // - This place is <i>amazing</i>! Just this morning alone, I discovered three new molecules and a new kind of superconductor!
                return true;
            default:
                return true;
        }
    }
}
