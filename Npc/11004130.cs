using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004130: Eupheria
/// </summary>
public class _11004130 : NpcScript {
    internal _11004130(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720143007010503$ 
                // - My head hurts...
                return true;
            case 10:
                // $script:0720143007010504$ 
                // - Just what did we see in the darkness...?
                return true;
            default:
                return true;
        }
    }
}
