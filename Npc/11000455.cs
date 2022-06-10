using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000455: Pason
/// </summary>
public class _11000455 : NpcScript {
    internal _11000455(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002014$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407002017$ 
                // - Everyone's all freaked out about the storm and the earthquake, but so what? We need some excitement around here! 
                return true;
            default:
                return true;
        }
    }
}
