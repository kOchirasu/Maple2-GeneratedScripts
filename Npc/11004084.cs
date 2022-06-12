using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004084: Torchy
/// </summary>
public class _11004084 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0622133907010284$
    // - Shh! You'll wake up the other fireflies. No loud noises allowed.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0622133907010285$
                // - Shh! You'll wake up the other fireflies. No loud noises allowed.
                return 10;
            case (10, 1):
                // $script:0622133907010286$
                // - Quietly, now... You're here looking for a quiet place to rest, aren't you?
                switch (selection) {
                    // $script:0622133907010287$
                    // - What makes you think that?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0622133907010288$
                // - Humans always come here when something's on their mind. Our pretty light helps them feel better! I figured you might be the same.
                return 31;
            case (31, 1):
                // $script:0622133907010289$
                // - I can't do a danged thing to actually help you. But hey, if staring at our sparkly heinies brings you peace, then stare away!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
