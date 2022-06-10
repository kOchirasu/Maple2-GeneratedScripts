using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000740: Pia
/// </summary>
public class _11000740 : NpcScript {
    internal _11000740(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002877$ 
                // - Hm...
                return true;
            case 40:
                // $script:0831180407002881$ 
                // - Err? Are you a traveler? You look... cool. 
                // $script:0831180407002882$ 
                // - I'm cooler, though. Hee hee!
                return true;
            default:
                return true;
        }
    }
}
