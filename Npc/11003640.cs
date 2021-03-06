using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003640: Heidi
/// </summary>
public class _11003640 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009114$
    // - When she asked if I like it hot, I had no idea she meant THIS...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009115$
                // - How can people <i>live</i> like this! At least they could turn on the AC... Are you on vacation here, too?
                switch (selection) {
                    // $script:1109121007009116$
                    // - That's right.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009117$
                // - You liar. You've got $npcName:11003535[gender:1]$'s fingerprints all over you.
                switch (selection) {
                    // $script:1109121007009118$
                    // - <i>All</i> over me?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009119$
                // - Don't look so surprised. Any trained Dark Wind agent knows the signs. Anyway, I'm guessing you're here for my message?
                switch (selection) {
                    // $script:1109121007009120$
                    // - You guessed right.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009121$
                // - Listen closely. "Jeans. Air conditioner! Poker?"
                switch (selection) {
                    // $script:1109121007009122$
                    // - Is that really the message?
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009123$
                // - Oh, please. Anyway, I need some space, so shoo. This heat is killing me...
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
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
