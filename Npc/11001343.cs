using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001343: Vex
/// </summary>
public class _11001343 : NpcScript {
    internal _11001343(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005292$ 
                // - I'm busy! Get to the point.
                return true;
            case 30:
                // $script:1217012607005295$ 
                // - Sigh... I can't ever let my guard down at work. Accidents happen all the time, you know.
                switch (selection) {
                    // $script:1217012607005296$
                    // - How old are you?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1217012607005297$ 
                // - Ahem! Why do you care? I'm old enough, thank you very much.
                return true;
            default:
                return true;
        }
    }
}
