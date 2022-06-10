using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004134: Ishura
/// </summary>
public class _11004134 : NpcScript {
    internal _11004134(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010529$ 
                // - ...
                return true;
            case 10:
                // $script:0730132107010530$ 
                // - Huh?
                return true;
            case 100:
                // $script:0730132107010531$ 
                // - Huh?
                switch (selection) {
                    // $script:0730132107010532$
                    // - I was worried about you. Let's get out of here.
                    case 0:
                        Id = 101;
                        return false;
                }
                return true;
            case 101:
                // $script:0730132107010533$ 
                // - Nonsense.
                // $script:0730132107010534$ 
                // - There's nothing more to talk about.
                return true;
            default:
                return true;
        }
    }
}
