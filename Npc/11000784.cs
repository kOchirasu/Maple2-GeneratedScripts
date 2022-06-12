using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000784: Carrie
/// </summary>
public class _11000784 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002956$
    // - Who are you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002959$
                // - Strange... I see cake everywhere, but I smell nothing.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
