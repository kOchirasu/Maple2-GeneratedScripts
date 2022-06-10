using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004457: Evian
/// </summary>
public class _11004457 : NpcScript {
    internal _11004457(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0109134107012662$ 
                // - Our first steps in a new world. I should be excited, but all I feel is nervous... 
                return true;
            case 10:
                // $script:0109134107012663$ 
                // - Our first steps in a new world. I should be excited, but all I feel is nervous... 
                return true;
            default:
                return true;
        }
    }
}
