using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001690: Jayce
/// </summary>
public class _11001690 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006497$
    // - The sooner we get out of this dusty hole, the better.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0708220807006684$
                // - Was there something you wanted to ask me?
                switch (selection) {
                    // $script:0708220807006685$
                    // - What do you make of my arrangement with $npcName:11001629[gender:0]$?
                    case 0:
                        return 40;
                    // $script:0708220807006686$
                    // - What happened to the vagrants Blackstar took hostage?
                    case 1:
                        return 50;
                    // $script:0712221207006745$
                    // - Tell me about $npcName:11001547[gender:0]$.
                    case 2:
                        return 60;
                }
                return -1;
            case (40, 0):
                // $script:0708220807006687$
                // - To be honest, I don't know why that man—I mean, the boss—keeps you around. The things he's asked you to do... 
                switch (selection) {
                    // $script:0708220807006688$
                    // - ...could be done by anyone.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0708220807006689$
                // - Yes. Easily. And you don't even like him. So why does he have you do it?
                switch (selection) {
                    // $script:0708220807006690$
                    // - I think I know the answer to that.
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0708220807006691$
                // - Oh?
                switch (selection) {
                    // $script:0708220807006692$
                    // - He's trying to tame me.
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:0708220807006693$
                // - Maybe, but <i>can</i> you be tamed? My peers may think you're harmless, but I see a wolf that's taken care to hide $male:his,female:her$ fangs and claws.
                switch (selection) {
                    // $script:0708225907006705$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (50, 0):
                // $script:0708220807006694$
                // - If you're worried about their safety, well, that all depends on your cooperation.
                return 50;
            case (50, 1):
                // $script:0708220807006695$
                // - I don't understand why you allow the boss to walk all over you. You have no obligation to him. Blackstar is big, but you...
                switch (selection) {
                    // $script:0708220807006696$
                    // - I lost the match. I'm honor bound to work with him.
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0708220807006697$
                // - You say that, even knowing that the fight was fixed? Incredible. You're the most loyal, honorable, and... frustratingly righteous person I've ever met.
                switch (selection) {
                    // $script:0708225907006706$
                    // - I've learned a new lesson from $npcName:11001629[gender:0]$.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:0629000607006499$
                // - If that's what you think, then I won't ask any further.
                return 52;
            case (52, 1):
                // $script:0630002207006511$
                // - If you need anything, you can try asking $npcName:11001674[gender:0]$ or $npcName:11001682[gender:0]$. I can't guarantee that they'll be very helpful, though.
                switch (selection) {
                    // $script:0708225907006707$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
            case (60, 0):
                // $script:0712221207006746$
                // - $npcName:11001547[gender:0]$ is truly a magnificent beast. It's not just that he's strong—he is completely and utterly fearless.
                switch (selection) {
                    // $script:0712221207006747$
                    // - What does he have to fear? His dad is the boss!
                    case 0:
                        return 61;
                }
                return -1;
            case (61, 0):
                // $script:0712221207006748$
                // - Of course you would assume that $npcName:11001547[gender:0]$ gets special treatment because of his father. But, in truth, it's $npcName:11001618[gender:0]$ who is lucky to have $npcName:11001547[gender:0]$ for a son.
                return 61;
            case (61, 1):
                // $script:0712221207006749$
                // - When Blackstar was first started, it had many enemies. Hardly a day passed when someone didn't try to take the boss's life. But $npcName:11001547[gender:0]$ watched over $map:02000100$ like a hawk, keeping his father safe and eliminating our enemies one at a time.
                return 61;
            case (61, 2):
                // $script:0712221207006750$
                // - He won't take credit for it, but there would be no Blackstar without him. And yet, some people still grumble that he acts too cocky for a brat who merely happened to be <i>adopted</i> by the boss.
                switch (selection) {
                    // $script:0712221207006751$
                    // - Wait, $npcName:11001547[gender:0]$ was adopted?
                    case 0:
                        return 62;
                }
                return -1;
            case (62, 0):
                // $script:0712221207006752$
                // - I don't know the details. All I know is that the boss brought home this ten-year-old boy one day and treated him as a son. He couldn't possibly be the boss's real child.
                return 62;
            case (62, 1):
                // $script:0712221207006753$
                // - Whatever their story is, $npcName:11001547[gender:0]$ doesn't seem to care about his birth or his position in Blackstar. Most of us respect and admire him, and those who don't are too cowardly to speak up.
                switch (selection) {
                    // $script:0712221207006754$
                    // - Let's talk about something else.
                    case 0:
                        return 30;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Next,
            (61, 1) => NpcTalkButton.Next,
            (61, 2) => NpcTalkButton.SelectableDistractor,
            (62, 0) => NpcTalkButton.Next,
            (62, 1) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
