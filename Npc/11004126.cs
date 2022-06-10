using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004126: Fledgling Guard
/// </summary>
public class _11004126 : NpcScript {
    internal _11004126(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720130407010495$ 
                // - ...N-nothing to report! 
                return true;
            case 10:
                // $script:0720130407010496$ 
                // - Y-you're talking to me? 
                return true;
            default:
                return true;
        }
    }
}
