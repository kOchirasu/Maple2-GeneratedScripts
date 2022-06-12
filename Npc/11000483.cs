using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000483: Bunny Gal
/// </summary>
public class _11000483 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;60
    }

    // Select 0:
    // $script:0831180407002119$
    // - Welcome, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002124$
                // - You're amazing!
                return -1;
            case (60, 0):
                // $script:0831180407002125$
                // - You did it! Good job!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
