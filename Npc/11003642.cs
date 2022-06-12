using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003642: Jacqueline
/// </summary>
public class _11003642 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009134$
    // - I feel like a diamond in a toilet...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009135$
                // - Who are you?
                switch (selection) {
                    // $script:1109121007009136$
                    // - Um... What are you doing up here?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009137$
                // - Yes, yes, I know. A beauty like mine doesn't belong in a disgusting place like this.
                switch (selection) {
                    // $script:1109121007009138$
                    // - That's not quite what I meant...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009139$
                // - Still, I have a job to do. Tell the boss that I said, "Twinkle, twinkle, little star."
                switch (selection) {
                    // $script:1109121007009140$
                    // - Oh, you're one of ours?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009141$
                // - I understand why you're so confused. I'm way too gorgeous for this kind of work! I should've become a model or an actress. Even waitressing would be better than this.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
