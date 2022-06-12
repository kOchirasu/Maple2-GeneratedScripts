using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001630: Vasara Chen
/// </summary>
public class _11001630 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0516130207006132$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0531170907006286$
                // - What is it now?
                switch (selection) {
                    // $script:0531170907006287$
                    // - Did you know about $npcName:11001629[gender:0]$'s plan?
                    case 0:
                        return 30;
                }
                return -1;
            case (30, 0):
                // $script:0531170907006288$
                // - Not that I think you'll believe me, but no, I didn't. Even if I did know, so what? It's not my job to stop him.
                switch (selection) {
                    // $script:0531170907006289$
                    // - Then you're no better than $npcName:11001629[gender:0]$.
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0531170907006290$
                // - Listen. My old man and I don't always see eye to eye, but he built Blackstar from the ground up. You gotta be ruthless to succeed in this town, and he's earned my respect.
                switch (selection) {
                    // $script:0531170907006291$
                    // - Old man... You're $npcName:11001629[gender:0]$'s son?!
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:0531170907006292$
                // - I didn't tell you? Must've slipped my mind. $npcName:11001630[gender:0]$, son of $npcName:11001629[gender:0]$, at your service.
                switch (selection) {
                    // $script:0531170907006293$
                    // - Slipped your mind. Sure.
                    case 0:
                        return 60;
                }
                return -1;
            case (60, 0):
                // $script:0531170907006294$
                // - Hey, where's it written that I have to tell every idiot who stumbles in here who my dad is? Now, get out of my face before I get mad.
                switch (selection) {
                    // $script:0531170907006295$
                    // - I'm not done with you.
                    case 0:
                        return 70;
                }
                return -1;
            case (70, 0):
                // $script:0531170907006296$
                // - Me neither. I got a feeling we'll be fighting again real soon. And next time, I'll beat you fair and square. No tricks.
                switch (selection) {
                    // $script:0531170907006297$
                    // - I'll see you in the ring.
                    case 0:
                        return 80;
                }
                return -1;
            case (80, 0):
                // $script:0531170907006298$
                // - Count on it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (80, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
