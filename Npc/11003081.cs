using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003081: Seaside Cabin
/// </summary>
public class _11003081 : NpcScript {
    internal _11003081(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0113143107007762$ 
                // - <font color="#909090">(You see a wooden cabin weathered by wind and sea.)</font> 
                return true;
            case 30:
                // $script:0113143107007763$ 
                // - <font color="#909090">(Is someone inside this cabin? You can hear voices.)</font> 
                return true;
            default:
                return true;
        }
    }
}
