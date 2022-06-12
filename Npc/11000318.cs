using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000318: Lionel
/// </summary>
public class _11000318 : NpcScript {
    protected override int First() {
        return 60;
    }

    // Select 0:
    // $script:0831180407001215$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:0831180407001221$
                // - I don't recognize you. What do you want?
                switch (selection) {
                    // $script:0831180407001222$
                    // - I need directions.
                    case 0:
                        return 61;
                    // $script:0831180407001223$
                    // - Nothing in particular.
                    case 1:
                        return 63;
                }
                return -1;
            case (61, 0):
                // $script:0831180407001224$
                // - You must be new to $map:02000001$, huh? Boy, I'd love to prank you, but you look like you're here to shop. Okay, I'll let you off... THIS time!
                return 61;
            case (61, 1):
                // $script:0831180407001225$
                // - Follow that big road straight ahead.
                switch (selection) {
                    // $script:0831180407001226$
                    // - What's along the road?
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:0831180407001227$
                // - Oh, I ran out of patience for you a while ago. Stop bothering me and move on.
                return -1;
            case (63, 0):
                // $script:0831180407001228$
                // - Is that so? Strange... You really don't look familiar to me, and there's no way I can forget someone so ugly. Ha ha ha!
                switch (selection) {
                    // $script:0831180407001229$
                    // - Yeah, well... you're uglier!
                    case 0:
                        return 64;
                    // $script:0831180407001230$
                    // - Uhh, pot to kettle...
                    case 1:
                        return 65;
                }
                return -1;
            case (64, 0):
                // $script:0831180407001231$
                // - Heh. You've never seen a handsome man before, have you?
                switch (selection) {
                    // $script:0831180407001232$
                    // - This is ridiculous. I'm just going to leave.
                    case 0:
                        return 67;
                }
                return -1;
            case (65, 0):
                // $script:0831180407001233$
                // - I can't hear you. 
                switch (selection) {
                    // $script:0831180407001234$
                    // - Takes one to know one, Buddy!
                    case 0:
                        return 66;
                }
                return -1;
            case (66, 0):
                // $script:0831180407001235$
                // - I said, I can't hear you. 
                switch (selection) {
                    // $script:0831180407001236$
                    // - Right, that's about enough. Time to leave.
                    case 0:
                        return 67;
                }
                return -1;
            case (67, 0):
                // $script:0831180407001237$
                // - Oh, come on, are you just going to leave?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Next,
            (61, 1) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.Close,
            (63, 0) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.SelectableDistractor,
            (65, 0) => NpcTalkButton.SelectableDistractor,
            (66, 0) => NpcTalkButton.SelectableDistractor,
            (67, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
