using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000180: Konus
/// </summary>
public class _11000180 : NpcScript {
    internal _11000180(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000743$ 
                // - What? 
                return true;
            case 30:
                // $script:0831180407000746$ 
                // - That stuff you're carrying don't look like junk. Are you going to toss it? People nowadays throw out just any old thing. New, old, doesn't matter. I found boxes of stuff like that.  
                switch (selection) {
                    // $script:0831180407000747$
                    // - What kinds of things did you find?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000748$ 
                // - Ha! Everything, my friend. Sometimes little baubles, sometimes official palace weapons. Found a lot of those lately, ever since the empress's court was canceled. 
                // $script:0831180407000749$ 
                // - A lot of time and effort went into making those weapons. Why not stockpile them? They'd be more useful than melting them down, surely. 
                return true;
            default:
                return true;
        }
    }
}
