using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000372: Dr. Mikhail
/// </summary>
public class _11000372 : NpcScript {
    internal _11000372(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001526$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407001529$ 
                // - As scientists, we must always look toward the future. We must not abandon our research because we aren't happy with the immediate results, or out of fear of perceived consequences. Science requires persistence and dedication!
                return true;
            default:
                return true;
        }
    }
}
