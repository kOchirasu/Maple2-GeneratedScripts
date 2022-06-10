using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004159: Beatrice
/// </summary>
public class _11004159 : NpcScript {
    internal _11004159(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010543$ 
                // - I pray everyone is safe... 
                return true;
            case 10:
                // $script:0730132107010544$ 
                // - Please don't overexert yourself. 
                return true;
            default:
                return true;
        }
    }
}
