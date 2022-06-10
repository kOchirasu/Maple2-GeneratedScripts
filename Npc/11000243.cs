using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000243: Laura
/// </summary>
public class _11000243 : NpcScript {
    internal _11000243(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001028$ 
                // - Oh, can I help you?
                return true;
            case 20:
                // $script:0831180407001031$ 
                // - I don't know what to do... I think he's interested in me!
                switch (selection) {
                    // $script:0831180407001032$
                    // - I'm not really interested in you, sorry.
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0831180407001033$
                    // - Who are you talking about?
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407001034$ 
                // - Well... good! I'm not interested in you either, $MyPCName$.
                return true;
            case 22:
                // $script:0831180407001035$ 
                // - That guy over there, the tired one... Do you know that feeling you get when you make eye contact with someone special?
                // $script:0831180407001036$ 
                // - Eeeee! What do I do?
                return true;
            default:
                return true;
        }
    }
}
