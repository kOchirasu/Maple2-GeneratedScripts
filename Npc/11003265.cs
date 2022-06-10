using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003265: Abandoned Notebook
/// </summary>
public class _11003265 : NpcScript {
    internal _11003265(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008210$ 
                // - <font color="#909090">(This log was tucked away in an inconspicuous corner.)</font> 
                return true;
            case 30:
                // $script:0403155707008211$ 
                // - <font color="#909090">(It looks like this was abandoned, and yet it's suspiciously free of dust.)</font> 
                return true;
            default:
                return true;
        }
    }
}
