using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001377: Locault
/// </summary>
public class _11001377 : NpcScript {
    internal _11001377(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005365$ 
                // - Hm...
                return true;
            case 30:
                // $script:1217144507005368$ 
                // - What, you think a woman can't be a fight manager? Just watch. I'm going to turn Boh and every other one of my clients into world champions.
                return true;
            default:
                return true;
        }
    }
}
