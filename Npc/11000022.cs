using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000022: Harry
/// </summary>
public class _11000022 : NpcScript {
    internal _11000022(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000111$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000114$ 
                // - Are you heading to $map:02000001$. You know that the way is blocked, right?
                switch (selection) {
                    // $script:0831180407000115$
                    // - Yeah, I heard.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000116$
                    // - No, I didn't. Really?
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000117$ 
                // - Good, I don't have to explain it to you. So... if you can't get to $map:02000001$, what are you going to do?
                switch (selection) {
                    // $script:0831180407000118$
                    // - I'll find another way!
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0831180407000119$
                    // - Beats me.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407000120$ 
                // - What are you gonna do, fly? The road is gone! It has ceased to be! You need to be realistic about this.
                // $script:0831180407000121$ 
                // - Seriously, have a look at $map:02000115$. Let me know what you think of the terrible, yawning chasm of doom in your way. I'll wait.
                return true;
            case 33:
                // $script:0831180407000122$ 
                // - That's understandable. $map:02000001$ has it all, and all we've got is... fish. Might as well head home once you've got your fill of fish, huh?
                return true;
            case 34:
                // $script:0831180407000123$ 
                // - It sure is. The Royal Road is the main route from this harbor to $map:02000001$, and it was cracked open by the earthquake that happened the other day. Now no one can get to $map:02000001$.
                // $script:0831180407000124$ 
                // - If you don't believe me, go to $map:02000115$ and see for yourself.
                return true;
            default:
                return true;
        }
    }
}
