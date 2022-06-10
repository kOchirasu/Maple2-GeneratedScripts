using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004127: Veteran Guard
/// </summary>
public class _11004127 : NpcScript {
    internal _11004127(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720130407010497$ 
                // - Hmph... To think I'd be stationed in a place like this in my twilight years... 
                return true;
            case 10:
                // $script:0720130407010498$ 
                // - So... tired... When's the next shift change? 
                return true;
            default:
                return true;
        }
    }
}
