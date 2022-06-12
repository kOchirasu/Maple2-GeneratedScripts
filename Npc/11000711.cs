using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000711: Mint
/// </summary>
public class _11000711 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30;40
    }

    // Select 0:
    // $script:0831180407002847$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002848$
                // - Woo-hoo! Have a great day today!
                return -1;
            case (20, 0):
                // $script:0831180407002849$
                // - Yoo-hoo! Yet another beautiful day has dawned. Isn't it great?
                switch (selection) {
                    // $script:0831180407002850$
                    // - Yep!
                    case 0:
                        return 21;
                    // $script:0831180407002851$
                    // - It's not worth it.
                    case 1:
                        return 22;
                }
                return -1;
            case (21, 0):
                // $script:0831180407002852$
                // - Since I became a Bunny Gal, every day has been like a dream. I never thought my life could be this fun!
                return -1;
            case (22, 0):
                // $script:0831180407002853$
                // - Oh, you don't think so? Why not? It's all a matter of perspective. You should try to think positive. Like me! Hee hee hee!
                return -1;
            case (30, 0):
                // $script:0831180407002854$
                // - Hm? Where are you staring at?
                switch (selection) {
                    // $script:0831180407002855$
                    // - I can't help it... you're so pretty!
                    case 0:
                        return 31;
                    // $script:0831180407002856$
                    // - I... wasn't staring at you!
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002857$
                // - Oh, really? Do you think I'm pretty? I wasn't always so pretty, you know. Hee hee hee! I'd like it if you'd come visit me more often. I think I like you!
                return -1;
            case (32, 0):
                // $script:0831180407002858$
                // - Oh, y-you weren't? Hmph, for a moment I thought you had the hots for me.
                return 32;
            case (32, 1):
                // $script:0831180407002859$
                // - But... are you SURE you weren't staring at me?
                switch (selection) {
                    // $script:0831180407002860$
                    // - Nope!
                    case 0:
                        return 33;
                    // $script:0831180407002861$
                    // - Okay... you caught me.
                    case 1:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:0831180407002862$
                // - No? Well... All right then. If you say you weren't, then you weren't. Oh well!
                return -1;
            case (34, 0):
                // $script:0831180407002863$
                // - You were, right? I knew it. Hee hee! Don't be embarrassed. You aren't the only one who likes to stare at me.
                return -1;
            case (40, 0):
                // $script:0831180407002864$
                // - Wow, $MyPCName$, don't you just love the weather today? Back when I had to stay inside, I could hardly tell what the weather was.
                switch (selection) {
                    // $script:0831180407002865$
                    // - What happened to you back then?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002866$
                // - Huh? W-well... I don't... I don't want to talk about my past. 
                return 41;
            case (41, 1):
                // $script:0831180407002867$
                // - Let's talk about something else, shall we? Keep your head in the present, I always say! Eyes on the prize!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
