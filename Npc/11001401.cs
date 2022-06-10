using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001401: Montino
/// </summary>
public class _11001401 : NpcScript {
    internal _11001401(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005401$ 
                // - Th-this is too high up...
                return true;
            case 30:
                // $script:1228164407005741$ 
                // - I need to climb down sooner or later, but I'm worried that <i>they</i> are still down there.
                switch (selection) {
                    // $script:1228164407005742$
                    // - Who's they?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1228164407005743$ 
                // - Those robots! They were supposed to help us develop the desert, but they all went crazy!
                return true;
            default:
                return true;
        }
    }
}
