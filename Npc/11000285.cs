using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000285: Torhara
/// </summary>
public class _11000285 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001114$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001117$
                // - Is there someone you love?
                switch (selection) {
                    // $script:0831180407001118$
                    // - Yes.
                    case 0:
                        return 31;
                    // $script:0831180407001119$
                    // - No.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407001120$
                // - Good for you. Cherish them while you can. Have you ever lost someone you love?
                switch (selection) {
                    // $script:0831180407001121$
                    // - Yes.
                    case 0:
                        return 33;
                    // $script:0831180407001122$
                    // - No.
                    case 1:
                        return 34;
                }
                return -1;
            case (32, 0):
                // $script:0831180407001123$
                // - I see. Sometimes love begets tragedy, but it's worth more than the pain. 
                return -1;
            case (33, 0):
                // $script:0831180407001124$
                // - I see. I daresay I understand your pain. 
                return -1;
            case (34, 0):
                // $script:0831180407001125$
                // - I see. Let me give you some advice. Never take the ones you love for granted. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
