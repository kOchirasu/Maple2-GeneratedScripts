using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001430: Miel
/// </summary>
public class _11001430 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:1217205907005427$
    // - Many things shine, not all of them valuable.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005509$
                // - It's so close, but I can't reach it. It comes to me in the night and vanishes at dawn.
                return 40;
            case (40, 1):
                // $script:1222203907005510$
                // - The more I lean into the sunlight, the more I hide in the moonlight. But then, it all drifts apart. I can't continue this way... 
                switch (selection) {
                    // $script:1222203907005511$
                    // - What on earth are you talking about?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1222203907005512$
                // - Huh...? Shoo! You wouldn't understand.
                return -1;
            case (50, 0):
                // $script:0610174107006339$
                // - Hello.
                switch (selection) {
                    // $script:0610174107006340$
                    // - Did you miss your best friend?
                    case 0:
                        return 56;
                    // $script:0610174107006341$
                    // - How are you doing?
                    case 1:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0610174107006342$
                // - The desert is always the same—beautiful and desolate. $MyPCName$, how have you been?
                switch (selection) {
                    // $script:0610174107006343$
                    // - I came running all this way to see you.
                    case 0:
                        return 52;
                    // $script:0610174107006344$
                    // - Things have been nice and quiet without you to bother me.
                    case 1:
                        return 55;
                }
                return -1;
            case (52, 0):
                // $script:0610174107006345$
                // - Ha... I see. I thought I saw a bright light coming from afar... It lifted my spirits.
                switch (selection) {
                    // $script:0610174107006346$
                    // - Do you miss me?
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:0610174107006347$
                // - Are you feeling all right? When I mentioned a bright light from afar, I meant the moon. The moon! Not you.
                switch (selection) {
                    // $script:0610174107006348$
                    // - I'll be sure to visit more often.
                    case 0:
                        return 54;
                }
                return -1;
            case (54, 0):
                // $script:0610174107006349$
                // - Sure, you do that. Who knows? Maybe next time I'll even be waiting for you.
                //   <font color="#909090">(In spite of his cool words, there's a warm smile on his lips.)</font> 
                return -1;
            case (55, 0):
                // $script:0610174107006350$
                // - How nice for you. Leave in peace, then.
                //   <font color="#909090">(He sighs and looks away.)</font>
                return -1;
            case (56, 0):
                // $script:0610174107006351$
                // - My friend? Who? 
                switch (selection) {
                    // $script:0610174107006352$
                    // - Have you forgotten our friendship?
                    case 0:
                        return 57;
                    // $script:0610174107006353$
                    // - Are you feeling okay?
                    case 1:
                        return 58;
                }
                return -1;
            case (57, 0):
                // $script:0610174107006354$
                // - Ah, of course I remember! You and I are friends now. It was just a little joke. 
                switch (selection) {
                    // $script:0610174107006355$
                    // - Keep these jokes up, and I'll stop visiting.
                    case 0:
                        return 59;
                }
                return -1;
            case (58, 0):
                // $script:0610174107006356$
                // - I feel fine. Thank you for your concern, but... I was just playing a little joke on you. Maybe you're too naive for such play...
                switch (selection) {
                    // $script:0610174107006357$
                    // - Keep these jokes up, and I'll stop visiting.
                    case 0:
                        return 59;
                }
                return -1;
            case (59, 0):
                // $script:0610174107006358$
                // - I thought this was what friends do! Now you're making <i>me</i> confused. If visiting me is such a bother, then you don't have to do it, you know. 
                switch (selection) {
                    // $script:0610174107006359$
                    // - I'll visit you again soon.
                    case 0:
                        return 54;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.SelectableDistractor,
            (54, 0) => NpcTalkButton.Close,
            (55, 0) => NpcTalkButton.Close,
            (56, 0) => NpcTalkButton.SelectableDistractor,
            (57, 0) => NpcTalkButton.SelectableDistractor,
            (58, 0) => NpcTalkButton.SelectableDistractor,
            (59, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
