using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001652: Suspicious Man
/// </summary>
public class _11001652 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0519143707006208$
    // - ... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0630142807006512$
                // - What's taking him so long...? Huh? What do you want?!
                switch (selection) {
                    // $script:0630142807006513$
                    // - What are you up to?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0630142807006514$
                // - Wh-what do you think? I'm sorting junk, that's what!
                switch (selection) {
                    // $script:0630142807006515$
                    // - (Stare at him.)
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0630142807006516$
                // - I-I'm not up to anything bad. Really. I'm just...
                return 32;
            case (32, 1):
                // $script:0630142807006517$
                // - Wait. You're...
                switch (selection) {
                    // $script:0630142807006518$
                    // - You know me?
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0630142807006519$
                // - You're the Gray Wolf! I was there when you took down those Blackstar goons in $map:02000138$.
                switch (selection) {
                    // $script:0630142807006520$
                    // - You're thinking of someone else.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0630142807006521$
                // - No, I'm not. You trying to stay off the radar? I would, too, if I had as many enemies as you. But your face has been burned into my brain ever since that day.
                switch (selection) {
                    // $script:0630142807006522$
                    // - ...
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:0630142807006523$
                // - Anyway, what are you doing here?
                switch (selection) {
                    // $script:0630142807006524$
                    // - I have business here.
                    case 0:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:0630142807006525$
                // - Here? You and the Blackstars are mortal enemies now, right? Wait... you didn't come here to take them on at their headquarters, did you?
                switch (selection) {
                    // $script:0630142807006526$
                    // - Things... got a little out of control.
                    case 0:
                        return 37;
                }
                return -1;
            case (37, 0):
                // $script:0630142807006527$
                // - Y-you really are the terror of $map:02000138$! The equal of a hundred warriors! Y'know, I used to think you were just another thug... Since you're here, maybe there's a question you can answer for me. 
                return 37;
            case (37, 1):
                // $script:0630142807006528$
                // - I have a, uh, "friend" who went inside their headquarters. He should have been able to sneak out while you kept the gangsters busy, but he's still missing. You didn't see anyone... suspicious when you were there, did you?
                switch (selection) {
                    // $script:0630142807006529$
                    // - Everyone in there looked suspicious.
                    case 0:
                        return 38;
                }
                return -1;
            case (38, 0):
                // $script:0630142807006530$
                // - Yeah, yeah, good point. Ha, I almost feel sorry for the Blackstars, having an enemy like you. Hahaha!
                switch (selection) {
                    // $script:0630142807006531$
                    // - (Say nothing.)
                    case 0:
                        return 39;
                }
                return -1;
            case (39, 0):
                // $script:0630142807006532$
                // - Ha... Ha ha... Ahem. You're a pretty intense $male:guy,female:gal$, you know that? I hope we meet again.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.SelectableDistractor,
            (37, 0) => NpcTalkButton.Next,
            (37, 1) => NpcTalkButton.SelectableDistractor,
            (38, 0) => NpcTalkButton.SelectableDistractor,
            (39, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
