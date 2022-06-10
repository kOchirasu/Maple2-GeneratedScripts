using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003788: Nairin
/// </summary>
public class _11003788 : NpcScript {
    internal _11003788(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009646$ 
                // - All systems are operational! 
                return true;
            case 10:
                // $script:1213192607009647$ 
                // - How may I help you today, $male:Sir,female:Ma'am$? 
                return true;
            default:
                return true;
        }
    }
}
