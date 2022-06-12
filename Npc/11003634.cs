using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003634: Becker
/// </summary>
public class _11003634 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009034$
    // - I'm a man on a mission.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009035$
                // - Let's get to business.
                switch (selection) {
                    // $script:1109121007009036$
                    // - $npcName:11003535[gender:1]$ sent me.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009037$
                // - Yeah, likely story. How do I know I can trust you?
                switch (selection) {
                    // $script:1109121007009038$
                    // - There's got to be a way to prove myself.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009039$
                // - If $npcName:11003535[gender:1]$ really sent you, then you should know Dark Wind's motto.
                switch (selection) {
                    // $script:1109121007009040$
                    // - All hail $npcName:11000006[gender:0]$!
                    case 0:
                        return 13;
                    // $script:1109121007009041$
                    // - All hail $npcName:11000044[gender:0]$!
                    case 1:
                        return 14;
                    // $script:1109121007009042$
                    // - (Say nothing.)
                    case 2:
                        return 15;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009043$
                // - You are a fool.
                switch (selection) {
                    // $script:1109121007009044$
                    // - Give me another chance!
                    case 0:
                        return 16;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009045$
                // - You think I'm stupid? There's no way $npcName:11003535[gender:1]$ would send an idiot like you.
                switch (selection) {
                    // $script:1109121007009046$
                    // - Give me another chance!
                    case 0:
                        return 16;
                }
                return -1;
            case (15, 0):
                // $script:1109121007009047$
                // - Ah, so $npcName:11003535[gender:1]$ did send you, after all. Good. Tell her, "Ducky. Purple slime. Cerbe."
                switch (selection) {
                    // $script:1109121007009048$
                    // - Really?
                    case 0:
                        return 17;
                }
                return -1;
            case (16, 0):
                // $script:1109121007009049$
                // - What's Dark Wind's slogan?
                switch (selection) {
                    // $script:1109121007009050$
                    // - All hail $npcName:11000006[gender:0]$!
                    case 0:
                        return 13;
                    // $script:1109121007009051$
                    // - All hail $npcName:11000044[gender:0]$!
                    case 1:
                        return 14;
                    // $script:1109121007009052$
                    // - (Say nothing.)
                    case 2:
                        return 15;
                }
                return -1;
            case (17, 0):
                // $script:1109121007009053$
                // - Don't leave anything out! Tell her <i>exactly</i> what I said!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.SelectableDistractor,
            (16, 0) => NpcTalkButton.SelectableDistractor,
            (17, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
