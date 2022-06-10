using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000416: Eisley
/// </summary>
public class _11000416 : NpcScript {
    internal _11000416(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000835$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000836$ 
                // - I shall reclaim my empire! 
                return true;
            default:
                return true;
        }
    }
}
