using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004116: Royal Guard
/// </summary>
public class _11004116 : NpcScript {
    internal _11004116(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010475$ 
                // - All's well! 
                return true;
            case 10:
                // $script:0720125407010476$ 
                // - All's well! 
                return true;
            default:
                return true;
        }
    }
}
