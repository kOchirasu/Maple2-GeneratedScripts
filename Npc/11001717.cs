using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001717: Junta
/// </summary>
public class _11001717 : NpcScript {
    internal _11001717(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006968$ 
                // - You'd better have a good reason for interrupting my training. 
                return true;
            case 30:
                // $script:0805021607007093$ 
                // - I've given it some thought, but I still don't understand why some of us would leave the master's guidance to live in human cities like $map:02000001$. $MyPCName$, do you like this place? 
                switch (selection) {
                    // $script:0805021607007094$
                    // - It's not too bad. 
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0805021607007095$
                    // - It's too loud for me!
                    case 1:
                        Id = 40;
                        return false;
                }
                return true;
            case 31:
                // $script:0805021607007096$ 
                // - Hmph. If you have time to enjoy the sights, then you have time to train! 
                switch (selection) {
                    // $script:0805021607007097$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 40:
                // $script:0805021607007098$ 
                // - Yes... Yes, it is, isn't it? It hasn't escaped my notice that you've been training hard lately. Don't strain yourself. 
                switch (selection) {
                    // $script:0805021607007099$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
