using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003439: Jorge
/// </summary>
public class _11003439 : NpcScript {
    internal _11003439(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008687$ 
                // - It's a tad noisy here for my tastes. 
                return true;
            case 10:
                // $script:0721142007008705$ 
                // - It's a tad noisy here for my tastes. 
                return true;
            default:
                return true;
        }
    }
}
