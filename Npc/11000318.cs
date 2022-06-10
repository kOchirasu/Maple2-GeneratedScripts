using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000318: Lionel
/// </summary>
public class _11000318 : NpcScript {
    internal _11000318(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001215$ 
                // - What is it?
                return true;
            case 60:
                // $script:0831180407001221$ 
                // - I don't recognize you. What do you want?
                switch (selection) {
                    // $script:0831180407001222$
                    // - I need directions.
                    case 0:
                        Id = 61;
                        return false;
                    // $script:0831180407001223$
                    // - Nothing in particular.
                    case 1:
                        Id = 63;
                        return false;
                }
                return true;
            case 61:
                // $script:0831180407001224$ 
                // - You must be new to $map:02000001$, huh? Boy, I'd love to prank you, but you look like you're here to shop. Okay, I'll let you off... THIS time!
                // $script:0831180407001225$ 
                // - Follow that big road straight ahead.
                switch (selection) {
                    // $script:0831180407001226$
                    // - What's along the road?
                    case 0:
                        Id = 62;
                        return false;
                }
                return true;
            case 62:
                // $script:0831180407001227$ 
                // - Oh, I ran out of patience for you a while ago. Stop bothering me and move on.
                return true;
            case 63:
                // $script:0831180407001228$ 
                // - Is that so? Strange... You really don't look familiar to me, and there's no way I can forget someone so ugly. Ha ha ha!
                switch (selection) {
                    // $script:0831180407001229$
                    // - Yeah, well... you're uglier!
                    case 0:
                        Id = 64;
                        return false;
                    // $script:0831180407001230$
                    // - Uhh, pot to kettle...
                    case 1:
                        Id = 65;
                        return false;
                }
                return true;
            case 64:
                // $script:0831180407001231$ 
                // - Heh. You've never seen a handsome man before, have you?
                switch (selection) {
                    // $script:0831180407001232$
                    // - This is ridiculous. I'm just going to leave.
                    case 0:
                        Id = 67;
                        return false;
                }
                return true;
            case 65:
                // $script:0831180407001233$ 
                // - I can't hear you. 
                switch (selection) {
                    // $script:0831180407001234$
                    // - Takes one to know one, Buddy!
                    case 0:
                        Id = 66;
                        return false;
                }
                return true;
            case 66:
                // $script:0831180407001235$ 
                // - I said, I can't hear you. 
                switch (selection) {
                    // $script:0831180407001236$
                    // - Right, that's about enough. Time to leave.
                    case 0:
                        Id = 67;
                        return false;
                }
                return true;
            case 67:
                // $script:0831180407001237$ 
                // - Oh, come on, are you just going to leave?
                return true;
            default:
                return true;
        }
    }
}
